#!/usr/bin/env python3
"""Generate public release metadata from a signed APK, without reading signing keys."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent


def write_metadata(apk, output, tools, catalog=ROOT / "catalog/apps.json"):
    badging = subprocess.run(
        [str(tools / "aapt2"), "dump", "badging", str(apk)],
        capture_output=True, text=True, check=True,
    ).stdout
    package = re.search(r"^package: name='([^']+)' versionCode='([0-9]+)' versionName='([^']*)'", badging, re.M)
    if not package or "application-debuggable" in badging:
        raise ValueError("A release APK is required")
    pkg, code, version = package.groups()
    major = re.search(r"versionCodeMajor='([0-9]+)'", badging)
    code = int(code) | ((int(major.group(1)) if major else 0) << 32)
    if code <= 0 or not version:
        raise ValueError("Missing APK version")
    app = next((a for a in json.loads(catalog.read_text(encoding="utf-8"))["apps"] if a["packageName"] == pkg), None)
    if app is None:
        raise ValueError("APK package is not in the app catalog")
    verified = subprocess.run(
        [str(tools / "apksigner"), "verify", "--print-certs", str(apk)],
        capture_output=True, text=True, check=True,
    ).stdout
    certs = re.findall(r"certificate SHA-256 digest: ([0-9a-f]+)", verified)
    if len(certs) != 1 or certs[0] not in app["certificates"]:
        raise ValueError("APK signing certificate is not trusted")
    metadata = {"schema": 1, "packageName": pkg, "versionCode": code,
                "versionName": version, "apk": apk.name,
                "sha256": hashlib.sha256(apk.read_bytes()).hexdigest()}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apk", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    sdk = Path(os.environ.get("ANDROID_HOME", Path.home() / "Library/Android/sdk"))
    parser.add_argument("--tools", type=Path, default=sdk / "build-tools/37.0.0")
    args = parser.parse_args()
    write_metadata(args.apk, args.output, args.tools)
    print("Public metadata generated from verified release APK")


if __name__ == "__main__":
    main()
