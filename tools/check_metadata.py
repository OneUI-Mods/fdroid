#!/usr/bin/env python3
"""Validate public package records without reading private repository configuration."""

import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parent.parent


def main():
    rows = json.loads((ROOT / "submissions/requests.json").read_text())
    packages = {r["packageName"] for r in rows}
    if len(packages) != len(rows):
        raise ValueError("Duplicate package records")
    if packages != {p.stem for p in (ROOT / "metadata").glob("*.yml")}:
        raise ValueError("Public metadata does not match the submission records")
    for row in rows:
        name = row["packageName"] + ".yml"
        info = yaml.safe_load((ROOT / "metadata" / name).read_text())
        draft = yaml.safe_load((ROOT / "packaging/drafts" / name).read_text())
        if not info["SourceCode"].startswith("https://github.com/OneUI-Mods/"):
            raise ValueError("Unexpected source repository")
        if not info["AllowedAPKSigningKeys"] or any(
            not re.fullmatch(r"[0-9a-f]{64}", key)
            for key in info["AllowedAPKSigningKeys"]
        ):
            raise ValueError("Missing public certificate pin")
        if draft["Builds"][0]["commit"] != row["sourceCommit"]:
            raise ValueError("Draft source commit mismatch")
        if not re.fullmatch(r"[0-9a-f]{40}", row["sourceCommit"]):
            raise ValueError("Source revision must be immutable")
        if row.get("url") and not re.fullmatch(
            r"https://gitlab.com/fdroid/rfp/-/work_items/[0-9]+", row["url"]
        ):
            raise ValueError("Unexpected official request URL")
    print(f"Public metadata and official request records verified: {len(rows)} apps")


if __name__ == "__main__":
    main()
