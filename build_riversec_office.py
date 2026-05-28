"""Build a larger River-Security-branded office from the WorkAdventure starter map.

Steps:
1. Duplicate the starter office horizontally and extend the garden downward to make a
   roughly 2x larger map (61x32 tiles).
2. Replace WA_Logo_Long.png with a River Security branded version.
3. Add brand-name map properties and interaction zones pointing at riversecurity.eu.
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
SRC_JSON = ROOT / "river_security_office.json"
DST_JSON = ROOT / "river_security_hq.json"
LOGO_PATH = ROOT / "tilesets" / "WA_Logo_Long.png"

TILE = 32

# Brand colours (from riversecurity.eu)
RS_NAVY = (10, 30, 65)
RS_BLUE = (40, 90, 175)
RS_CYAN = (90, 200, 230)
RS_WHITE = (245, 248, 255)


def make_logo():
    """Overwrite the 192x32 WA logo with a River Security wordmark."""
    img = Image.new("RGBA", (192, 32), RS_NAVY)
    d = ImageDraw.Draw(img)
    # Subtle wave / "river" arc accent on the left
    for i, color in enumerate([RS_CYAN, RS_BLUE]):
        d.arc([2 + i, 4 + i, 30 - i, 28 - i], start=200, end=340, fill=color, width=2)
    # Drop pixel
    d.ellipse([13, 20, 17, 24], fill=RS_CYAN)

    font = None
    for candidate in ("arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"):
        try:
            font = ImageFont.truetype(candidate, 14)
            break
        except Exception:
            continue
    if font is None:
        font = ImageFont.load_default()

    d.text((36, 8), "River Security", fill=RS_WHITE, font=font)
    img.save(LOGO_PATH)
    print(f"wrote {LOGO_PATH}")


def main():
    make_logo()

    src = json.loads(SRC_JSON.read_text())
    SW, SH = src["width"], src["height"]  # 31, 21

    # New canvas: duplicate horizontally (shifted by SW-1 so right wall doubles as
    # left wall of the second wing) and add 11 rows of garden below.
    SHIFT = SW - 1  # 30
    NEW_W = SW + SHIFT  # 61
    NEW_H = SH + 11  # 32

    # Grass tile (used for garden) — found by sampling the original map.
    GRASS = 2461

    def expand_tilelayer(data, name):
        new = [0] * (NEW_W * NEW_H)
        for y in range(SH):
            for x in range(SW):
                v = data[y * SW + x]
                if v == 0:
                    continue
                # original wing
                new[y * NEW_W + x] = v
                # duplicated wing — overwrites at x=SHIFT, which is fine since both
                # copies use the same wall tile there (acts as shared partition).
                new[y * NEW_W + (x + SHIFT)] = v
        # Fill the new garden rows of floor1 with grass.
        if name == "floor1":
            for y in range(SH, NEW_H):
                for x in range(NEW_W):
                    new[y * NEW_W + x] = GRASS
        return new

    def transform(layers):
        out = []
        for l in layers:
            if l["type"] == "tilelayer":
                new_l = {
                    **l,
                    "width": NEW_W,
                    "height": NEW_H,
                    "data": expand_tilelayer(l["data"], l["name"]),
                }
                # For the start layer, only keep one spawn point (in the left wing
                # near where the original was).
                if l["name"] == "start":
                    nd = new_l["data"]
                    # keep first non-zero, zero the rest
                    seen = False
                    for i, v in enumerate(nd):
                        if v != 0:
                            if seen:
                                nd[i] = 0
                            else:
                                seen = True
                out.append(new_l)
            elif l["type"] == "group":
                out.append({**l, "layers": transform(l["layers"])})
            elif l["type"] == "objectgroup":
                if l["name"] == "floorLayer":
                    new_objs = []
                    for o in l.get("objects", []):
                        if o.get("type") == "floor" or o.get("name") == "floor":
                            o = {
                                **o,
                                "width": NEW_W * TILE,
                                "height": NEW_H * TILE,
                            }
                        new_objs.append(o)
                    out.append({**l, "objects": new_objs})
                else:
                    out.append(l)
        return out

    new_layers = transform(src["layers"])

    # Add an interactions object layer.
    interactions = {
        "name": "interactions",
        "type": "objectgroup",
        "visible": True,
        "opacity": 1,
        "x": 0,
        "y": 0,
        "draworder": "topdown",
        "objects": [
            {
                "id": 9001,
                "name": "riverSecurityWebsite",
                "type": "",
                "x": 4 * TILE,
                "y": 2 * TILE,
                "width": 4 * TILE,
                "height": 1 * TILE,
                "rotation": 0,
                "visible": True,
                "properties": [
                    {"name": "openWebsite", "type": "string", "value": "https://riversecurity.eu"},
                    {"name": "openWebsiteTrigger", "type": "string", "value": "onaction"},
                    {"name": "openWebsiteTriggerMessage", "type": "string",
                     "value": "Press SPACE to visit riversecurity.eu"},
                ],
            },
            {
                "id": 9002,
                "name": "warRoom",
                "type": "",
                "x": (SW + 9) * TILE,
                "y": 3 * TILE,
                "width": 8 * TILE,
                "height": 6 * TILE,
                "rotation": 0,
                "visible": True,
                "properties": [
                    {"name": "jitsiRoom", "type": "string", "value": "river-security-war-room"},
                    {"name": "jitsiTrigger", "type": "string", "value": "onaction"},
                    {"name": "jitsiTriggerMessage", "type": "string",
                     "value": "Press SPACE to join the War Room"},
                ],
            },
            {
                "id": 9003,
                "name": "activeFocusBriefing",
                "type": "",
                "x": (SW + 1) * TILE,
                "y": 10 * TILE,
                "width": 6 * TILE,
                "height": 4 * TILE,
                "rotation": 0,
                "visible": True,
                "properties": [
                    {"name": "openWebsite", "type": "string",
                     "value": "https://riversecurity.eu/active-focus"},
                    {"name": "openWebsiteTrigger", "type": "string", "value": "onaction"},
                    {"name": "openWebsiteTriggerMessage", "type": "string",
                     "value": "Press SPACE: Active Focus briefing"},
                ],
            },
        ],
    }
    new_layers.append(interactions)

    out = {
        **src,
        "width": NEW_W,
        "height": NEW_H,
        "layers": new_layers,
        "properties": [
            {"name": "mapName", "type": "string", "value": "River Security HQ"},
            {"name": "mapDescription", "type": "string",
             "value": "River Security — Attackers move fast. So do we."},
            {"name": "mapImage", "type": "string", "value": "tilesets/WA_Logo_Long.png"},
            {"name": "mapCopyright", "type": "string",
             "value": "Built on the WorkAdventure starter kit (CC-BY-SA assets)."},
        ],
        "nextlayerid": src.get("nextlayerid", 100) + 1,
        "nextobjectid": 9100,
    }

    DST_JSON.write_text(json.dumps(out, indent=1))
    print(f"wrote {DST_JSON} ({NEW_W}x{NEW_H})")


if __name__ == "__main__":
    main()
