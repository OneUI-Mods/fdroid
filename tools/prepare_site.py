#!/usr/bin/env python3
"""Validate signed F-Droid indexes and stage public files without private signing state."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import os

from fdroidserver import common, index

FINGERPRINT = "A12CF1059CEDFBECBD883F5F653A9228EEFD0227EC5DA4BDFB805337A97AC8B2"


def validate(work):
    repo = work / "repo"
    java = Path(os.environ["JAVA_HOME"]) / "bin" / "jarsigner"
    common.config = {"jarsigner": str(java)}
    entry, _, _ = index.get_index_from_jar(str(repo / "entry.jar"), FINGERPRINT)
    data = (repo / "index-v2.json").read_bytes()
    if (
        len(data) != entry["index"]["size"]
        or hashlib.sha256(data).hexdigest() != entry["index"]["sha256"]
    ):
        raise ValueError("Index does not match its signed entry")
    catalog = json.loads(data)
    manifest = json.loads((work / "verified-releases.json").read_text())
    expected = {row["app"]["packageName"]: row for row in manifest}
    if set(expected) != set(catalog["packages"]):
        raise ValueError("Indexed app set differs from the verified catalog")
    expected_apks = {}
    for package, record in expected.items():
        declared = {v["sha256"]: v for v in record["versions"]}
        versions = catalog["packages"][package]["versions"]
        if set(versions) != set(declared):
            raise ValueError("Indexed versions differ from verified releases")
        for digest, version in versions.items():
            apk = repo / declared[digest]["filename"]
            if version["file"]["name"] != "/" + apk.name:
                raise ValueError("Unexpected indexed APK path")
            if hashlib.sha256(apk.read_bytes()).hexdigest() != digest:
                raise ValueError("Indexed APK changed after signature verification")
            expected_apks[apk.name] = digest
    if {p.name for p in repo.glob("*.apk")} != set(expected_apks):
        raise ValueError("Unverified APKs are present; remove them before publication")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = validate(args.work)
    if args.output.exists():
        if any(args.output.iterdir()):
            raise ValueError("Output must be empty to avoid publishing stale files")
    args.output.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        args.work / "repo",
        args.output / "repo",
        ignore=shutil.ignore_patterns("status"),
    )
    forbidden = {"config.yml", "credentials.txt", "repository.p12", "keystore.p12"}
    for file in args.output.rglob("*"):
        if (
            file.is_symlink()
            or file.name in forbidden
            or file.suffix in {".keystore", ".p12", ".jks"}
        ):
            raise ValueError("Private state in public output")
    (args.output / ".nojekyll").touch()
    (args.output / "verified-releases.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    source = Path(__file__).resolve().parent.parent / "docs" / "index.html"
    shutil.copyfile(source, args.output / "index.html")
    print(f"Validated signed index and staged {len(manifest)} apps for publication.")


if __name__ == "__main__":
    main()
