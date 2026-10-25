#!/usr/bin/env python3
"""Render the original APK launcher vectors as store artwork; never modifies APKs."""

import argparse
import base64
from io import BytesIO
import json
import os
from pathlib import Path
import re
from xml.etree import ElementTree as ET

from androguard.core.apk import APK
from androguard.core.axml import AXMLPrinter
import cairosvg
from loguru import logger
from PIL import Image

ANDROID = "{http://schemas.android.com/apk/res/android}"


def render(apk_path, destination):
    apk = APK(str(apk_path))
    resources = apk.get_android_resources()
    sdk = Path(os.environ["ANDROID_HOME"]) / "platforms/android-37.0/data/res/values"
    colors = {
        e.get("name"): e.text
        for e in ET.parse(sdk / "colors.xml").getroot()
        if e.tag == "color"
    }
    framework = {
        int(e.get("id"), 16): colors.get(e.get("name"))
        for e in ET.parse(sdk / "public-final.xml").getroot()
        if e.tag == "public" and e.get("type") == "color"
    }

    def value(text):
        if text and text.startswith("@android:"):
            result = framework.get(int(text.split(":", 1)[1], 16))
            if result is None:
                raise ValueError("Framework color is not available in the selected SDK")
            return result
        if text and text.startswith("@"):
            choices = resources.get_resolved_res_configs(int(text[1:], 16))
            return choices[0][1]
        return text

    def color(text):
        text = value(text) or "#00000000"
        if text.startswith("#") and len(text) == 9:
            return "#" + text[3:] + text[1:3]
        return text

    def attr(node, name, default=None):
        return node.get(ANDROID + name, default)

    def children(node):
        output = []
        for child in node:
            if child.tag == "path":
                props = {
                    "d": attr(child, "pathData"),
                    "fill": color(attr(child, "fillColor")),
                }
                for source, target in [
                    ("fillAlpha", "fill-opacity"),
                    ("strokeAlpha", "stroke-opacity"),
                    ("strokeWidth", "stroke-width"),
                    ("strokeLineCap", "stroke-linecap"),
                    ("strokeLineJoin", "stroke-linejoin"),
                ]:
                    if attr(child, source) is not None:
                        props[target] = attr(child, source)
                if attr(child, "strokeColor"):
                    props["stroke"] = color(attr(child, "strokeColor"))
                if attr(child, "fillType") == "1":
                    props["fill-rule"] = "evenodd"
                if any(
                    attr(child, key) is not None
                    for key in ["trimPathStart", "trimPathEnd"]
                ):
                    raise ValueError("Trimmed vector needs an explicit artwork export")
                output.append(ET.Element("path", props))
            elif child.tag == "group":
                px, py = attr(child, "pivotX", "0"), attr(child, "pivotY", "0")
                transform = (
                    f'translate({attr(child,"translateX","0")} {attr(child,"translateY","0")}) '
                    f'rotate({attr(child,"rotation","0")} {px} {py}) '
                    f'translate({px} {py}) scale({attr(child,"scaleX","1")} {attr(child,"scaleY","1")}) '
                    f"translate({-float(px)} {-float(py)})"
                )
                group = ET.Element("g", {"transform": transform})
                group.extend(children(child))
                output.append(group)
            else:
                raise ValueError("Unsupported vector node: " + child.tag)
        return output

    def drawable(reference, depth=0):
        if depth > 8:
            raise ValueError("Drawable recursion limit")
        reference = value(reference)
        if reference.startswith("#"):
            return ET.Element(
                "rect", {"width": "108", "height": "108", "fill": color(reference)}
            )
        data = apk.get_file(reference)
        if not reference.endswith(".xml"):
            return ET.Element(
                "image",
                {
                    "width": "108",
                    "height": "108",
                    "href": "data:image/png;base64," + base64.b64encode(data).decode(),
                },
            )
        root = AXMLPrinter(data).get_xml_obj()
        if root.tag == "vector":
            svg = ET.Element(
                "svg",
                {
                    "width": "108",
                    "height": "108",
                    "viewBox": f'0 0 {attr(root,"viewportWidth")} {attr(root,"viewportHeight")}',
                },
            )
            svg.extend(children(root))
            return svg
        if root.tag == "adaptive-icon":
            group = ET.Element("g")
            for item in root:
                if item.tag in ["background", "foreground"]:
                    group.append(drawable(attr(item, "drawable"), depth + 1))
            return group
        if root.tag == "inset":
            return drawable(attr(root, "drawable"), depth + 1)
        raise ValueError("Unsupported launcher drawable: " + root.tag)

    icon = apk.get_app_icon()
    if icon is None:
        return False  # Keep the client's default when the original app declares no artwork.
    root = (
        AXMLPrinter(apk.get_file(icon)).get_xml_obj() if icon.endswith(".xml") else None
    )
    adaptive = root is not None and root.tag == "adaptive-icon"
    svg = ET.Element(
        "svg",
        {
            "xmlns": "http://www.w3.org/2000/svg",
            "width": "512",
            "height": "512",
            "viewBox": "18 18 72 72" if adaptive else "0 0 108 108",
        },
    )
    svg.append(drawable(icon))
    png = cairosvg.svg2png(bytestring=ET.tostring(svg))
    destination.parent.mkdir(parents=True, exist_ok=True)
    Image.open(BytesIO(png)).convert("RGBA").save(destination)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work", type=Path, required=True)
    args = parser.parse_args()
    logger.remove()
    records = json.loads((args.work / "verified-releases.json").read_text())
    for record in records:
        version = max(record["versions"], key=lambda v: v["versionCode"])
        destination = (
            args.work
            / "metadata"
            / record["app"]["packageName"]
            / "en-US/images/icon.png"
        )
        rendered = render(args.work / "repo" / version["filename"], destination)
        print(
            record["app"]["title"]
            + (
                ": original artwork rendered"
                if rendered
                else ": Android default icon retained"
            )
        )


if __name__ == "__main__":
    main()
