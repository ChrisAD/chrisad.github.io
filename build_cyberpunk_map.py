"""Generate a cyberpunk hacker-space tileset PNG + WorkAdventure Tiled JSON map."""
import json
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

TILE = 32
COLS, ROWS = 8, 4  # 32 tiles total
TS_W, TS_H = COLS * TILE, ROWS * TILE

MAP_W, MAP_H = 40, 28  # in tiles

# Cyberpunk palette
BG = (8, 6, 18)
DARK = (14, 10, 30)
DARK2 = (22, 14, 40)
NEON_CYAN = (0, 240, 255)
NEON_MAG = (255, 30, 200)
NEON_PURPLE = (170, 60, 255)
NEON_GREEN = (60, 255, 130)
NEON_YELLOW = (255, 230, 60)
GRAY = (60, 60, 80)
WHITE = (240, 240, 255)

OUT_DIR = Path(__file__).parent
TILESET_PNG = OUT_DIR / "cyberpunk_tileset.png"
MAP_JSON = OUT_DIR / "cyberpunk_office.json"


def make_tileset():
    img = Image.new("RGBA", (TS_W, TS_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    def tile_rect(idx):
        cx, cy = idx % COLS, idx // COLS
        return cx * TILE, cy * TILE, (cx + 1) * TILE - 1, (cy + 1) * TILE - 1

    def fill(idx, color):
        x0, y0, x1, y1 = tile_rect(idx)
        d.rectangle([x0, y0, x1, y1], fill=color)

    def at(idx, x, y):
        cx, cy = idx % COLS, idx // COLS
        return cx * TILE + x, cy * TILE + y

    # --- Row 0: floors (gids 1-8) ---
    # 0: dark floor with cyan grid
    fill(0, DARK)
    x0, y0, x1, y1 = tile_rect(0)
    d.rectangle([x0, y0, x1, y1], outline=(0, 80, 110))
    d.line([at(0, 16, 0), at(0, 16, 31)], fill=(0, 50, 80))
    d.line([at(0, 0, 16), at(0, 31, 16)], fill=(0, 50, 80))

    # 1: dark floor with magenta accent
    fill(1, DARK2)
    x0, y0, x1, y1 = tile_rect(1)
    d.rectangle([x0, y0, x1, y1], outline=(110, 0, 80))
    for i in range(4, 32, 8):
        d.point(at(1, i, i), fill=NEON_MAG)

    # 2: circuit floor
    fill(2, DARK)
    d.line([at(2, 4, 4), at(2, 28, 4)], fill=(0, 120, 140))
    d.line([at(2, 28, 4), at(2, 28, 16)], fill=(0, 120, 140))
    d.line([at(2, 28, 16), at(2, 16, 16)], fill=(0, 120, 140))
    d.line([at(2, 16, 16), at(2, 16, 28)], fill=(0, 120, 140))
    d.ellipse([at(2, 2, 2), at(2, 6, 6)], fill=NEON_CYAN)
    d.ellipse([at(2, 14, 26), at(2, 18, 30)], fill=NEON_CYAN)

    # 3: glow spot
    fill(3, DARK)
    for r in range(12, 0, -2):
        a = 20 + (12 - r) * 18
        d.ellipse([at(3, 16 - r, 16 - r), at(3, 16 + r, 16 + r)],
                  outline=(0, min(255, a + 40), min(255, a + 40)))

    # 4: hex grid floor
    fill(4, DARK2)
    for hx in (8, 24):
        for hy in (8, 24):
            pts = []
            import math
            for k in range(6):
                ang = math.pi / 3 * k
                pts.append(at(4, int(hx + 5 * math.cos(ang)), int(hy + 5 * math.sin(ang))))
            d.polygon(pts, outline=NEON_PURPLE)

    # 5: scanline floor (entrance pad)
    fill(5, DARK)
    for y in range(2, 32, 4):
        d.line([at(5, 2, y), at(5, 29, y)], fill=(60, 140, 180))

    # 6: floor with arrow (path)
    fill(6, DARK2)
    d.polygon([at(6, 16, 6), at(6, 24, 16), at(6, 16, 26), at(6, 20, 16)],
              fill=NEON_GREEN)

    # 7: warning floor
    fill(7, (50, 40, 0))
    for i in range(-32, 32, 6):
        d.line([at(7, max(0, i), 0), at(7, min(31, i + 32), 31)],
               fill=NEON_YELLOW, width=2)

    # --- Row 1: walls (gids 9-16) ---
    # 8: wall top (cyan trim)
    fill(8, (18, 12, 38))
    x0, y0, x1, y1 = tile_rect(8)
    d.rectangle([x0, y0, x1, y0 + 4], fill=NEON_CYAN)
    d.rectangle([x0, y0 + 6, x1, y1], fill=(28, 18, 50))
    for x in range(4, 32, 8):
        d.line([at(8, x, 10), at(8, x, 28)], fill=(60, 30, 100))

    # 9: wall middle (vertical)
    fill(9, (18, 12, 38))
    d.line([at(9, 4, 0), at(9, 4, 31)], fill=NEON_MAG)
    d.line([at(9, 27, 0), at(9, 27, 31)], fill=NEON_MAG)
    for y in range(6, 32, 8):
        d.rectangle([at(9, 12, y), at(9, 20, y + 4)], fill=(40, 20, 60))

    # 10: wall bottom (purple base)
    fill(10, (18, 12, 38))
    d.rectangle([at(10, 0, 26), at(10, 31, 31)], fill=NEON_PURPLE)
    d.rectangle([at(10, 0, 0), at(10, 31, 24)], fill=(28, 18, 50))

    # 11: corner TL
    fill(11, (18, 12, 38))
    d.rectangle([at(11, 0, 0), at(11, 31, 4)], fill=NEON_CYAN)
    d.rectangle([at(11, 0, 0), at(11, 4, 31)], fill=NEON_CYAN)

    # 12: corner TR
    fill(12, (18, 12, 38))
    d.rectangle([at(12, 0, 0), at(12, 31, 4)], fill=NEON_CYAN)
    d.rectangle([at(12, 27, 0), at(12, 31, 31)], fill=NEON_CYAN)

    # 13: corner BL
    fill(13, (18, 12, 38))
    d.rectangle([at(13, 0, 27), at(13, 31, 31)], fill=NEON_PURPLE)
    d.rectangle([at(13, 0, 0), at(13, 4, 31)], fill=NEON_CYAN)

    # 14: corner BR
    fill(14, (18, 12, 38))
    d.rectangle([at(14, 0, 27), at(14, 31, 31)], fill=NEON_PURPLE)
    d.rectangle([at(14, 27, 0), at(14, 31, 31)], fill=NEON_CYAN)

    # 15: door / opening (lit floor between wall stubs)
    fill(15, DARK)
    d.rectangle([at(15, 0, 0), at(15, 4, 8)], fill=(18, 12, 38))
    d.rectangle([at(15, 27, 0), at(15, 31, 8)], fill=(18, 12, 38))
    d.rectangle([at(15, 6, 14), at(15, 25, 18)], fill=NEON_GREEN)

    # --- Row 2: furniture (gids 17-24) ---
    # 16: desk with monitor (glowing screen)
    fill(16, DARK)
    d.rectangle([at(16, 2, 18), at(16, 29, 28)], fill=(35, 35, 55))  # desk
    d.rectangle([at(16, 2, 18), at(16, 29, 19)], fill=NEON_CYAN)     # desk edge
    d.rectangle([at(16, 8, 4), at(16, 23, 17)], fill=(20, 20, 30))   # monitor
    d.rectangle([at(16, 10, 6), at(16, 21, 14)], fill=NEON_GREEN)    # screen
    for ly in (8, 10, 12):
        d.line([at(16, 11, ly), at(16, 18, ly)], fill=(10, 60, 30))

    # 17: server rack
    fill(17, DARK)
    d.rectangle([at(17, 4, 2), at(17, 27, 29)], fill=(20, 20, 28))
    d.rectangle([at(17, 4, 2), at(17, 27, 3)], fill=NEON_MAG)
    for y in range(6, 28, 4):
        d.rectangle([at(17, 7, y), at(17, 24, y + 2)], fill=(35, 35, 45))
        for lx in (9, 12, 15, 18, 21):
            col = random.choice([NEON_GREEN, NEON_CYAN, NEON_MAG, NEON_YELLOW])
            d.point(at(17, lx, y + 1), fill=col)

    # 18: chair
    fill(18, (0, 0, 0, 0))
    d.ellipse([at(18, 10, 10), at(18, 22, 22)], fill=(40, 20, 60), outline=NEON_MAG)
    d.rectangle([at(18, 15, 22), at(18, 17, 30)], fill=GRAY)
    d.line([at(18, 12, 30), at(18, 20, 30)], fill=GRAY, width=2)

    # 19: hologram emitter
    fill(19, (0, 0, 0, 0))
    d.rectangle([at(19, 12, 26), at(19, 20, 30)], fill=GRAY, outline=NEON_CYAN)
    # holo triangle
    for k in range(8):
        a = 200 - k * 20
        d.polygon([at(19, 16, 4 + k), at(19, 8 + k, 26 - k), at(19, 24 - k, 26 - k)],
                  outline=(0, 200, 255))

    # 20: neon sign (HACK)
    fill(20, DARK)
    d.rectangle([at(20, 0, 0), at(20, 31, 31)], outline=NEON_MAG, width=2)
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None
    d.text(at(20, 4, 10), "HACK", fill=NEON_MAG, font=font)
    d.text(at(20, 5, 11), "HACK", fill=NEON_CYAN, font=font)

    # 21: plant (cyber-foliage)
    fill(21, (0, 0, 0, 0))
    d.rectangle([at(21, 11, 22), at(21, 21, 30)], fill=(60, 40, 80), outline=NEON_PURPLE)
    for _ in range(20):
        px = random.randint(8, 24)
        py = random.randint(4, 22)
        d.point(at(21, px, py), fill=NEON_GREEN)
    d.line([at(21, 16, 22), at(21, 16, 8)], fill=NEON_GREEN)

    # 22: terminal kiosk
    fill(22, DARK)
    d.rectangle([at(22, 6, 4), at(22, 25, 28)], fill=(25, 25, 35), outline=NEON_CYAN)
    d.rectangle([at(22, 9, 7), at(22, 22, 18)], fill=(5, 25, 15))
    for ly in (9, 11, 13, 15):
        d.line([at(22, 10, ly), at(22, 20, ly)], fill=NEON_GREEN)
    d.rectangle([at(22, 9, 20), at(22, 22, 26)], fill=(45, 30, 50))

    # 23: arcade machine
    fill(23, DARK)
    d.rectangle([at(23, 5, 2), at(23, 26, 30)], fill=(20, 10, 35), outline=NEON_MAG)
    d.rectangle([at(23, 8, 5), at(23, 23, 16)], fill=(0, 0, 30))
    for _ in range(15):
        d.point((random.randint(*sorted([tile_rect(23)[0] + 9, tile_rect(23)[0] + 22])),
                 random.randint(*sorted([tile_rect(23)[1] + 6, tile_rect(23)[1] + 15]))),
                fill=random.choice([NEON_CYAN, NEON_MAG, NEON_GREEN]))
    d.rectangle([at(23, 9, 20), at(23, 22, 23)], fill=GRAY)
    d.ellipse([at(23, 11, 25), at(23, 15, 29)], fill=NEON_MAG)
    d.ellipse([at(23, 17, 25), at(23, 21, 29)], fill=NEON_CYAN)

    # --- Row 3: decor/extras (gids 25-32) ---
    # 24: data cable on floor
    fill(24, DARK)
    d.line([at(24, 0, 16), at(24, 31, 16)], fill=NEON_CYAN, width=2)
    d.line([at(24, 0, 18), at(24, 31, 18)], fill=NEON_MAG, width=1)

    # 25: glowing pillar
    fill(25, (18, 12, 38))
    d.rectangle([at(25, 12, 0), at(25, 19, 31)], fill=(30, 20, 50))
    d.rectangle([at(25, 14, 0), at(25, 17, 31)], fill=NEON_CYAN)

    # 26: door/portal
    fill(26, (18, 12, 38))
    d.rectangle([at(26, 4, 2), at(26, 27, 30)], fill=(0, 30, 50))
    d.rectangle([at(26, 4, 2), at(26, 27, 30)], outline=NEON_CYAN, width=2)
    for y in range(6, 30, 4):
        d.line([at(26, 6, y), at(26, 25, y)], fill=(0, 80, 120))

    # 27: rug/mat (decorative)
    fill(27, (40, 0, 60))
    d.rectangle([at(27, 2, 2), at(27, 29, 29)], outline=NEON_MAG)
    d.rectangle([at(27, 6, 6), at(27, 25, 25)], outline=NEON_CYAN)
    d.text(at(27, 9, 12), "0xR$", fill=NEON_CYAN, font=font)

    # 28: empty (fully transparent — for overlay tiles to leave blank)
    fill(28, (0, 0, 0, 0))

    # 29: small drone
    fill(29, (0, 0, 0, 0))
    d.ellipse([at(29, 10, 12), at(29, 22, 20)], fill=GRAY, outline=NEON_CYAN)
    d.line([at(29, 6, 14), at(29, 10, 16)], fill=GRAY)
    d.line([at(29, 22, 16), at(29, 26, 14)], fill=GRAY)
    d.ellipse([at(29, 14, 14), at(29, 18, 18)], fill=NEON_MAG)

    # 30: coffee/energy drink
    fill(30, (0, 0, 0, 0))
    d.rectangle([at(30, 12, 8), at(30, 20, 26)], fill=(0, 60, 90), outline=NEON_CYAN)
    d.rectangle([at(30, 12, 8), at(30, 20, 12)], fill=NEON_MAG)

    # 31: neon strip floor accent
    fill(31, DARK)
    d.rectangle([at(31, 0, 14), at(31, 31, 18)], fill=NEON_MAG)
    d.rectangle([at(31, 0, 15), at(31, 31, 17)], fill=WHITE)

    img.save(TILESET_PNG)
    print(f"Wrote {TILESET_PNG}")


# -------- Map JSON --------

# Tile gid helpers (firstgid = 1)
def gid(i):
    return i + 1


# floor variants
FLOOR_BASE = gid(0)
FLOOR_MAG = gid(1)
FLOOR_CIRCUIT = gid(2)
FLOOR_GLOW = gid(3)
FLOOR_HEX = gid(4)
FLOOR_SCAN = gid(5)
FLOOR_ARROW = gid(6)
FLOOR_WARN = gid(7)

WALL_TOP = gid(8)
WALL_MID = gid(9)
WALL_BOT = gid(10)
CORNER_TL = gid(11)
CORNER_TR = gid(12)
CORNER_BL = gid(13)
CORNER_BR = gid(14)
DOOR = gid(15)

DESK = gid(16)
SERVER = gid(17)
CHAIR = gid(18)
HOLO = gid(19)
SIGN = gid(20)
PLANT = gid(21)
TERMINAL = gid(22)
ARCADE = gid(23)

CABLE = gid(24)
PILLAR = gid(25)
PORTAL = gid(26)
RUG = gid(27)
EMPTY = 0
DRONE = gid(29)
COFFEE = gid(30)
STRIP = gid(31)


def make_layer_data(fill_val=0):
    return [fill_val] * (MAP_W * MAP_H)


def put(data, x, y, v):
    if 0 <= x < MAP_W and 0 <= y < MAP_H:
        data[y * MAP_W + x] = v


def make_map():
    random.seed(1337)

    ground = make_layer_data(FLOOR_BASE)
    decor = make_layer_data(0)
    walls = make_layer_data(0)
    furniture = make_layer_data(0)
    overlay = make_layer_data(0)
    collision = make_layer_data(0)
    start = make_layer_data(0)

    # vary the ground a bit
    for y in range(MAP_H):
        for x in range(MAP_W):
            r = random.random()
            if r < 0.04:
                put(ground, x, y, FLOOR_CIRCUIT)
            elif r < 0.07:
                put(ground, x, y, FLOOR_HEX)
            elif r < 0.085:
                put(ground, x, y, FLOOR_MAG)

    # entrance strip / scanline pad near bottom-center
    for x in range(17, 23):
        put(ground, x, MAP_H - 3, FLOOR_SCAN)
    for x in range(17, 23):
        put(ground, x, MAP_H - 4, FLOOR_SCAN)

    # arrow pointing into the room from the entrance
    put(decor, 20, MAP_H - 5, FLOOR_ARROW)

    # neon strip down the main aisle
    for x in range(2, MAP_W - 2):
        put(decor, x, MAP_H // 2, STRIP)

    # warning floor near server room
    for x in range(MAP_W - 9, MAP_W - 3):
        put(decor, x, 2, FLOOR_WARN)

    # ----- Outer walls -----
    for x in range(1, MAP_W - 1):
        put(walls, x, 0, WALL_TOP)
        put(walls, x, MAP_H - 1, WALL_BOT)
    for y in range(1, MAP_H - 1):
        put(walls, 0, y, WALL_MID)
        put(walls, MAP_W - 1, y, WALL_MID)
    put(walls, 0, 0, CORNER_TL)
    put(walls, MAP_W - 1, 0, CORNER_TR)
    put(walls, 0, MAP_H - 1, CORNER_BL)
    put(walls, MAP_W - 1, MAP_H - 1, CORNER_BR)

    # Entrance opening at bottom-center
    for x in range(18, 22):
        put(walls, x, MAP_H - 1, DOOR)

    # ----- Inner partition (server room on the right) -----
    sx = MAP_W - 11
    for y in range(1, 10):
        put(walls, sx, y, WALL_MID)
    # opening into server room
    put(walls, sx, 6, DOOR)
    put(walls, sx, 7, DOOR)

    # ----- Inner partition (meeting room on the left) -----
    mx = 10
    for y in range(1, 9):
        put(walls, mx, y, WALL_MID)
    put(walls, mx, 5, DOOR)
    put(walls, mx, 6, DOOR)
    for x in range(1, mx):
        put(walls, x, 9, WALL_TOP)
    put(walls, mx, 9, WALL_MID)

    # corner of meeting room
    put(walls, mx, 0, CORNER_TR)
    put(walls, mx, 9, CORNER_BR)
    put(walls, 0, 9, CORNER_BL)

    # ----- Furniture -----
    # Server room: server racks along the right wall
    for y in range(2, 9):
        put(furniture, MAP_W - 3, y, SERVER)
        put(furniture, MAP_W - 5, y, SERVER)
    # warning glow
    put(overlay, MAP_W - 4, 5, FLOOR_GLOW)

    # Meeting room: holo table + chairs
    put(furniture, 5, 4, HOLO)
    put(furniture, 4, 4, CHAIR)
    put(furniture, 6, 4, CHAIR)
    put(furniture, 5, 3, CHAIR)
    put(furniture, 5, 5, CHAIR)
    put(decor, 5, 4, FLOOR_GLOW)

    # neon sign over meeting room door
    put(furniture, 2, 1, SIGN)

    # Open workspace: rows of desks
    for row_y in (12, 17):
        for x in range(3, MAP_W - 14, 3):
            put(furniture, x, row_y, DESK)
            put(furniture, x, row_y + 1, CHAIR)

    # Pillars
    put(furniture, 15, 14, PILLAR)
    put(furniture, 25, 14, PILLAR)

    # Lounge area top-right of workspace
    put(furniture, MAP_W - 4, 12, ARCADE)
    put(furniture, MAP_W - 6, 12, ARCADE)
    put(furniture, MAP_W - 4, 16, TERMINAL)
    put(furniture, MAP_W - 6, 16, COFFEE)
    put(furniture, MAP_W - 5, 18, PLANT)
    put(furniture, MAP_W - 3, 18, PLANT)

    # Plants near entrance
    put(furniture, 17, MAP_H - 6, PLANT)
    put(furniture, 22, MAP_H - 6, PLANT)

    # Drones floating around
    put(overlay, 14, 3, DRONE)
    put(overlay, 28, 20, DRONE)

    # Rug under spawn / lobby area
    for x in range(18, 22):
        for y in range(MAP_H - 6, MAP_H - 4):
            put(decor, x, y, RUG)

    # Cable runs
    for x in range(1, MAP_W - 1):
        if x not in range(17, 23):
            put(decor, x, MAP_H - 8, CABLE)

    # Portal at top-left (exit / next zone hook)
    put(furniture, 3, 1, PORTAL)

    # ----- Collision: walls and furniture solids -----
    # walls and most furniture should block movement
    SOLID_GIDS = {
        WALL_TOP, WALL_MID, WALL_BOT, CORNER_TL, CORNER_TR, CORNER_BL, CORNER_BR,
        DESK, SERVER, HOLO, SIGN, PLANT, TERMINAL, ARCADE, PILLAR, PORTAL, COFFEE,
    }
    for y in range(MAP_H):
        for x in range(MAP_W):
            if walls[y * MAP_W + x] in SOLID_GIDS or furniture[y * MAP_W + x] in SOLID_GIDS:
                put(collision, x, y, FLOOR_BASE)  # any gid; layer is marked collides

    # ----- Start position: entrance lobby -----
    put(start, 20, MAP_H - 5, FLOOR_BASE)

    # ----- Read tileset PNG dimensions -----
    with Image.open(TILESET_PNG) as im:
        iw, ih = im.size

    def tile_layer(name, data, extra_props=None):
        layer = {
            "data": data,
            "height": MAP_H,
            "width": MAP_W,
            "name": name,
            "opacity": 1,
            "type": "tilelayer",
            "visible": True,
            "x": 0,
            "y": 0,
        }
        if extra_props:
            layer["properties"] = extra_props
        return layer

    layers = [
        tile_layer("start", start),
        tile_layer("ground", ground),
        tile_layer("decor", decor),
        tile_layer("walls", walls),
        tile_layer("furniture", furniture),
        tile_layer("overlay", overlay),
        tile_layer("collision", collision, [
            {"name": "collides", "type": "bool", "value": True}
        ]),
        {
            "name": "floorLayer",
            "type": "objectgroup",
            "visible": True,
            "opacity": 1,
            "x": 0,
            "y": 0,
            "draworder": "topdown",
            "objects": [
                {
                    "id": 1,
                    "name": "floor",
                    "type": "floor",
                    "x": 0,
                    "y": 0,
                    "width": MAP_W * TILE,
                    "height": MAP_H * TILE,
                    "rotation": 0,
                    "visible": True,
                }
            ],
        },
        {
            "name": "interactions",
            "type": "objectgroup",
            "visible": True,
            "opacity": 1,
            "x": 0,
            "y": 0,
            "draworder": "topdown",
            "objects": [
                {
                    "id": 100,
                    "name": "meetingRoom",
                    "type": "",
                    "x": 1 * TILE,
                    "y": 1 * TILE,
                    "width": 9 * TILE,
                    "height": 8 * TILE,
                    "rotation": 0,
                    "visible": True,
                    "properties": [
                        {"name": "jitsiRoom", "type": "string", "value": "rs-hackerspace-meeting"},
                        {"name": "jitsiTrigger", "type": "string", "value": "onaction"},
                    ],
                },
                {
                    "id": 101,
                    "name": "serverRoom",
                    "type": "",
                    "x": (MAP_W - 10) * TILE,
                    "y": 1 * TILE,
                    "width": 9 * TILE,
                    "height": 8 * TILE,
                    "rotation": 0,
                    "visible": True,
                    "properties": [
                        {"name": "openWebsite", "type": "string",
                         "value": "https://riversecurity.eu"},
                        {"name": "openWebsiteTrigger", "type": "string", "value": "onaction"},
                    ],
                },
                {
                    "id": 102,
                    "name": "arcade",
                    "type": "",
                    "x": (MAP_W - 7) * TILE,
                    "y": 11 * TILE,
                    "width": 4 * TILE,
                    "height": 3 * TILE,
                    "rotation": 0,
                    "visible": True,
                    "properties": [
                        {"name": "openWebsite", "type": "string",
                         "value": "https://hackertyper.net"},
                        {"name": "openWebsiteTrigger", "type": "string", "value": "onaction"},
                    ],
                },
            ],
        },
    ]

    tileset = {
        "columns": COLS,
        "firstgid": 1,
        "image": "cyberpunk_tileset.png",
        "imageheight": ih,
        "imagewidth": iw,
        "margin": 0,
        "name": "cyberpunk_tileset",
        "spacing": 0,
        "tilecount": COLS * ROWS,
        "tileheight": TILE,
        "tilewidth": TILE,
    }

    out = {
        "compressionlevel": -1,
        "height": MAP_H,
        "width": MAP_W,
        "infinite": False,
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "tileheight": TILE,
        "tilewidth": TILE,
        "tiledversion": "1.10.2",
        "type": "map",
        "version": "1.10",
        "nextlayerid": 100,
        "nextobjectid": 200,
        "layers": layers,
        "tilesets": [tileset],
        "properties": [
            {"name": "mapName", "type": "string",
             "value": "River Security Cyberpunk Hacker Office"},
            {"name": "mapDescription", "type": "string",
             "value": "A neon-lit hackerspace built for WorkAdventure."},
        ],
    }

    MAP_JSON.write_text(json.dumps(out, indent=1))
    print(f"Wrote {MAP_JSON}")


if __name__ == "__main__":
    make_tileset()
    make_map()
