#!/usr/bin/env python3
"""Mirror catalog-pinned public release APKs into a private F-Droid working directory."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import urllib.request

import yaml
from verify_apk import write_metadata

CATALOG_URL = "https://raw.githubusercontent.com/OneUI-Mods/OneUIModsManager/main/catalog/apps.json"


def gh(*args):
    return subprocess.check_output(["gh", *args], text=True)


def sync_app(app, work, catalog, tools):
    repo = "OneUI-Mods/" + app["repo"]
    releases = json.loads(gh("api", f"repos/{repo}/releases?per_page=100"))
    published = [r for r in releases if not r["draft"]]
    candidates = []
    for preview in [False, True]:
        release = next((r for r in published if r["prerelease"] == preview), None)
        if release is not None:
            candidates.append(release)
    if not candidates:
        raise ValueError(f"{repo}: no published releases")
    versions = []
    for release in candidates:
        assets = [
            a
            for a in release["assets"]
            if a["name"].lower().endswith(".apk")
            and not any(v in a["name"].lower() for v in ["debug", "unsigned"])
        ]
        if len(assets) != 1:
            raise ValueError(f"{repo}: release APK is ambiguous")
        asset = assets[0]
        if Path(asset["name"]).name != asset["name"] or any(
            c in asset["name"] for c in "*?[]\\"
        ):
            raise ValueError("Unsafe APK filename")
        with tempfile.TemporaryDirectory(prefix="oneui-fdroid-") as directory:
            folder = Path(directory)
            gh(
                "release",
                "download",
                release["tag_name"],
                "--repo",
                repo,
                "--pattern",
                asset["name"],
                "--dir",
                directory,
            )
            apk = folder / asset["name"]
            info = write_metadata(apk, folder / "verified.json", tools, catalog)
            if info["packageName"] != app["packageName"]:
                raise ValueError(f"{repo}: wrong package")
            if asset.get("digest") != "sha256:" + info["sha256"]:
                raise ValueError(f"{repo}: missing or mismatched GitHub SHA-256")
            filename = f'{info["packageName"]}_{info["versionCode"]}.apk'
            target = work / "repo" / filename
            if (
                target.exists()
                and hashlib.sha256(target.read_bytes()).hexdigest() != info["sha256"]
            ):
                raise ValueError(f"{repo}: existing version has different contents")
            shutil.copyfile(apk, target)
            versions.append(
                {
                    **info,
                    "filename": filename,
                    "tag": release["tag_name"],
                    "releaseUrl": release["html_url"],
                    "apkUrl": asset["browser_download_url"],
                    "preview": release["prerelease"],
                }
            )
    preferred = next((v for v in versions if not v["preview"]), versions[0])
    previous_manifest = work / "verified-releases.json"
    if previous_manifest.exists():
        previous = next(
            (
                row
                for row in json.loads(previous_manifest.read_text())
                if row["app"]["packageName"] == app["packageName"]
            ),
            None,
        )
        current = {v["versionCode"]: v for v in versions}
        for old in previous["versions"] if previous else []:
            existing = current.get(old["versionCode"])
            if existing is not None:
                if existing["sha256"] != old["sha256"]:
                    raise ValueError(f"{repo}: published version contents changed")
                continue
            expected_name = f'{app["packageName"]}_{old["versionCode"]}.apk'
            if old["filename"] != expected_name:
                raise ValueError("Unexpected cached APK filename")
            # Keep already-published APKs available to clients holding an older signed index.
            with tempfile.TemporaryDirectory(
                prefix="oneui-fdroid-history-"
            ) as directory:
                verified = write_metadata(
                    work / "repo" / expected_name,
                    Path(directory) / "verified.json",
                    tools,
                    catalog,
                )
            if any(
                verified[key] != old[key]
                for key in ["packageName", "versionCode", "versionName", "sha256"]
            ):
                raise ValueError(
                    f"{repo}: previous APK no longer matches its verified record"
                )
            versions.append(old)

    notes = json.loads(
        (Path(__file__).resolve().parent.parent / "catalog-notes.json").read_text()
    ).get(
        app["repo"],
        {
            "summary": app["description"],
            "details": app["description"]
            + ". See the source README for supported devices and setup.",
        },
    )
    description = "<p>" + notes["details"] + "</p>"
    metadata = {
        "Categories": ["System"],
        "License": "MIT",
        "AuthorName": "ryuya0124",
        "AuthorWebSite": "https://github.com/ryuya0124",
        "WebSite": f"https://github.com/{repo}",
        "SourceCode": f"https://github.com/{repo}",
        "IssueTracker": f"https://github.com/{repo}/issues",
        "Name": app["title"],
        "Summary": notes["summary"],
        "Description": description,
        "AllowedAPKSigningKeys": app["certificates"],
        "CurrentVersion": preferred["versionName"],
        "CurrentVersionCode": preferred["versionCode"],
    }
    if notes.get("root"):
        metadata["RequiresRoot"] = True
    if notes.get("antiFeatures"):
        metadata["AntiFeatures"] = notes["antiFeatures"]
    (work / "metadata" / (app["packageName"] + ".yml")).write_text(
        yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    print(f"{repo}: {len(versions)} signed release APK(s) verified", flush=True)
    return {"app": app, "versions": versions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--work", type=Path, required=True, help="Private fdroid init directory"
    )
    parser.add_argument(
        "--tools", type=Path, required=True, help="Android Build Tools directory"
    )
    args = parser.parse_args()
    args.work.mkdir(parents=True, exist_ok=True)
    for name in ["repo", "metadata"]:
        (args.work / name).mkdir(exist_ok=True)
    with urllib.request.urlopen(CATALOG_URL, timeout=30) as response:
        raw = response.read(1024 * 1024 + 1)
    if len(raw) > 1024 * 1024:
        raise ValueError("Catalog too large")
    data = json.loads(raw)
    apps = data["apps"]
    if (
        data["schema"] != 1
        or not apps
        or len({a["packageName"] for a in apps}) != len(apps)
    ):
        raise ValueError("Invalid catalog")
    # APK verification also validates every package against this exact catalog snapshot.
    catalog = args.work / "catalog.json"
    catalog.write_bytes(raw)
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(
            pool.map(lambda app: sync_app(app, args.work, catalog, args.tools), apps)
        )
    (args.work / "verified-releases.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Verified {len(results)} apps; run fdroid update before publishing.")


if __name__ == "__main__":
    main()
