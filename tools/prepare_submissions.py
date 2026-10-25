#!/usr/bin/env python3
"""Prepare honest source-build drafts and individual official F-Droid packaging requests."""

import argparse
import base64
import re
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import yaml

ROOT = Path(__file__).resolve().parent.parent


def prepare(record, notes):
    app = record["app"]
    repo = "OneUI-Mods/" + app["repo"]
    version = next(
        (v for v in record["versions"] if not v["preview"]), record["versions"][0]
    )
    commit = json.loads(
        subprocess.check_output(
            ["gh", "api", f'repos/{repo}/commits/{version["tag"]}'], text=True
        )
    )["sha"]
    listing = json.loads(
        subprocess.check_output(
            ["gh", "api", f"repos/{repo}/contents/app?ref={commit}"], text=True
        )
    )
    build_file = next(
        f for f in listing if f["name"] in ["build.gradle", "build.gradle.kts"]
    )
    source = json.loads(
        subprocess.check_output(["gh", "api", build_file["url"]], text=True)
    )
    build_text = base64.b64decode(source["content"]).decode()
    sdk_match = re.search(r"compileSdk(?:Version)?\s*=?\s*([0-9]+)", build_text)
    sdk = int(sdk_match[1]) if sdk_match else None
    row = notes.get(
        app["repo"], {"summary": app["description"], "details": app["description"]}
    )
    metadata = yaml.safe_load(
        (ROOT / "metadata" / (app["packageName"] + ".yml")).read_text()
    )
    metadata.update(
        {
            "RepoType": "git",
            "Repo": f"https://github.com/{repo}.git",
            "MaintainerNotes": "Source build recipe draft. Not yet built with the F-Droid build server or verified reproducible. Please retain the developer signature only after a successful reproducibility check.",
            "Builds": [
                {
                    "versionName": version["versionName"],
                    "versionCode": version["versionCode"],
                    "commit": commit,
                    "subdir": "app",
                    "gradle": ["yes"],
                }
            ],
            "AutoUpdateMode": "None",
            "UpdateCheckMode": "Tags",
        }
    )
    if app["repo"] == "tail-adb":
        metadata["Builds"][0]["ndk"] = "28.2.13676358"
    filename = app["packageName"] + ".yml"
    (ROOT / "packaging/drafts" / filename).write_text(
        yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False)
    )
    concerns = (
        f"The requested release tag uses compileSdk {sdk}; newer source branches must be reviewed separately. "
        if sdk
        else "The requested source tag's SDK configuration needs manual review. "
    )
    concerns += "The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established."
    if app["repo"] == "tail-adb":
        concerns += " Native helper code is included as source and built with Android NDK 28.2.13676358. It uses the device's system adbd rather than bundling a proprietary daemon."
    if app["repo"] in ["OneUIModsManager", "galaxy-shutter-mute-manager"]:
        concerns += " The app offers explicit user-initiated APK downloads from GitHub. Please review the downloader consent flow against the executable-download policy before inclusion; a dedicated consent clarification or build flavor may be needed."
    if app["repo"] == "galaxy-shutter-mute":
        concerns += " Its deliberately old Android compatibility settings are required for the Samsung setting it changes. Installation on recent Android releases is normally performed through its separate Shizuku manager."
    body = f"""* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/{repo}

### Link to app in another app store:
{version["releaseUrl"]}

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`{app["packageName"]}`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
{row["summary"]}

### Description:
{row["details"]}

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **{version["versionName"]}** (`{version["versionCode"]}`); {"experimental release" if version["preview"] else "stable release"}.
- Immutable source commit: `{commit}`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/{filename}
- Developer certificate SHA-256: `{app["certificates"][0]}`.
- APK SHA-256: `{version["sha256"]}`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: {", ".join(row.get("antiFeatures", [])) or "none declared"}.

{concerns}

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
"""
    (ROOT / "submissions" / (app["packageName"] + ".md")).write_text(body)
    return {
        "repo": app["repo"],
        "packageName": app["packageName"],
        "title": app["title"],
        "requestTitle": app["title"],
        "body": body,
        "versionName": version["versionName"],
        "versionCode": version["versionCode"],
        "sourceCommit": commit,
        "status": "prepared",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    previous = ROOT / "submissions/requests.json"
    if previous.exists() and any(
        row.get("url") for row in json.loads(previous.read_text())
    ):
        raise ValueError(
            "Submitted records already exist; update them in place instead of overwriting request history"
        )
    records = json.loads(args.manifest.read_text())
    notes = json.loads((ROOT / "catalog-notes.json").read_text())
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda record: prepare(record, notes), records))
    (ROOT / "submissions/requests.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n"
    )
    print(f"Prepared {len(results)} independent requests and source-build drafts.")


if __name__ == "__main__":
    main()
