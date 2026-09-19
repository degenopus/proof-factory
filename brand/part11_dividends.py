# -*- coding: utf-8 -*-
"""Part 11: the 3% dividend stream GIF 480x480. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

W = H = 480

WALLETS = [
    ("0xDE6E\u2026", "HOLDER", 40),
    ("0xC0FF\u2026", "HOLDER", 150),
    ("0xBA5E\u2026", "HOLDER", 260),
    ("PR #1337", "CONTRIBUTOR", 370),
]
COINS_PER = 3        # coins per wallet
COIN_EVERY = 5       # frames between coin launches
COIN_SPEED = 9       # px per frame
COIN_VAL = 2.5       # $PROOF per coin (3 coins x 4 wallets = 30 = 3% of 1000)

PATH_Y = 300         # distributor bar


def path_len(pts):
    return sum(((pts[i + 1][0] - pts[i][0]) ** 2 + (pts[i + 1][1] - pts[i][1]) ** 2) ** .5
               for i in range(len(pts) - 1))


def path_at(pts, dist):
    for i in range(len(pts) - 1):
        seg = ((pts[i + 1][0] - pts[i][0]) ** 2 + (pts[i + 1][1] - pts[i][1]) ** 2) ** .5
        if dist <= seg:
            t = dist / seg if seg else 0
            return (pts[i][0] + (pts[i + 1][0] - pts[i][0]) * t,
                    pts[i][1] + (pts[i + 1][1] - pts[i][1]) * t)
        dist -= seg
    return pts[-1]


def coin_paths():
    """returns list of (launch_frame, pts) for the 3% stream"""
    out = []
    k = 0
    for _, _, wx in WALLETS:
        for j in range(COINS_PER):
            pts = [(240, 152), (240, PATH_Y), (wx + 48, PATH_Y), (wx + 48, 322)]
            out.append((16 + k * COIN_EVERY, pts))
            k += 1
    return out


def build_paths():
    out = []
    for j in range(3):
        out.append((16 + j * 7, [(240, 128), (306, 128)]))
    return out


def draw_coin(img, x, y, big=True):
    d = ImageDraw.Draw(img)
    r = 8 if big else 7
    col = YELLOW if big else GREEN
    d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=INK, width=3)
    d.text((x - 5, y - 9), "$", font=vt(18), fill=INK)


def frame(f, show_stamp=False):
    img = board_bg(W, H, seed=63)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE 3% STREAM", font=silk(14, bold=True), fill=YELLOW)
    d.text((246, 16), "dividends, not promises", font=vt(22), fill=(159, 208, 255))

    # ---- revenue tank (fills frames 0..14) ----
    lvl = min(1.0, f / 14.0)
    tx0, ty0, tx1, ty1 = 24, 64, 130, 196
    d.rectangle([tx0 + 6, ty0 + 6, tx1 + 6, ty1 + 6], fill=INK)
    d.rectangle([tx0, ty0, tx1, ty1], fill=(52, 46, 82), outline=CHALK, width=3)
    fh = int((ty1 - ty0 - 24) * lvl)
    d.rectangle([tx0 + 8, ty1 - 8 - fh, tx1 - 8, ty1 - 8], fill=ACCENT)
    d.text((tx0 + 10, ty0 + 8), "REVENUE", font=silk(10, bold=True), fill=CHALK)
    d.text((tx0 + 8, ty1 + 10), "1000 $PROOFACTORY", font=vt(22), fill=CHALK)
    if f >= 14:
        d.text((tx0 + 8, ty1 + 38), "round settled", font=vt(22), fill=GREEN)

    # ---- pipes ----
    d.rectangle([130, 134, 240, 146], fill=(70, 62, 105))          # tank -> valve
    d.rectangle([240, 122, 252, 146], fill=(70, 62, 105))          # valve stub
    d.rectangle([240, 134, 306, 146], fill=(70, 62, 105))          # 97% branch
    d.rectangle([234, 146, 246, PATH_Y + 4], fill=(70, 62, 105))   # 3% branch
    d.rectangle([40, PATH_Y - 4, 440, PATH_Y + 8], fill=(70, 62, 105))  # distributor
    # valve
    d.ellipse([214, 108, 278, 172], fill=BOARD, outline=YELLOW, width=4)
    d.text((284, 74), "97%", font=vt(22), fill=GREEN)
    d.text((252, 178), "3%", font=vt(26), fill=YELLOW)

    # ---- THE BUILD box ----
    bx0, by0, bx1, by1 = 296, 96, 456, 176
    d.rectangle([bx0 + 6, by0 + 6, bx1 + 6, by1 + 6], fill=INK)
    d.rectangle([bx0, by0, bx1, by1], fill=BOARD, outline=GREEN, width=3)
    d.text((bx0 + 12, by0 + 10), "THE BUILD", font=silk(12, bold=True), fill=GREEN)
    d.text((bx0 + 12, by0 + 38), "compute+servers", font=vt(20), fill=CHALK)
    d.text((bx0 + 12, by0 + 62), "prizes+reserve", font=vt(18), fill=GREY)

    # ---- wallets ----
    landed = {i: 0 for i in range(len(WALLETS))}
    for i, (name, kind, wx) in enumerate(WALLETS):
        flash = 0
        for launch, pts in coin_paths()[i * COINS_PER:(i + 1) * COINS_PER]:
            arr = launch + int(path_len(pts) / COIN_SPEED)
            if f >= arr:
                landed[i] += 1
                if f - arr < 4:
                    flash = 4 - (f - arr)
        wy0, wy1 = 322, 396
        bc = GREEN if flash else CHALK
        d.rectangle([wx + 6, wy0 + 6, wx + 102, wy1 + 6], fill=INK)
        d.rectangle([wx, wy0, wx + 102, wy1], fill=BOARD, outline=bc, width=3)
        d.text((wx + 8, wy0 + 8), name, font=vt(24), fill=CHALK)
        tagc = (255, 158, 207) if kind == "CONTRIBUTOR" else (159, 208, 255)
        d.text((wx + 8, wy0 + 32), kind, font=silk(9, bold=True), fill=tagc)
        bal = landed[i] * COIN_VAL
        d.text((wx + 8, wy0 + 52), f"+{bal:.1f}", font=vt(28), fill=YELLOW if bal else GREY)

    # ---- coins in flight ----
    for launch, pts in build_paths():
        dist = (f - launch) * COIN_SPEED
        if 0 <= dist <= path_len(pts):
            x, y = path_at(pts, dist)
            draw_coin(img, x, y, big=False)
    for launch, pts in coin_paths():
        dist = (f - launch) * COIN_SPEED
        if 0 <= dist <= path_len(pts):
            x, y = path_at(pts, dist)
            draw_coin(img, x, y, big=True)

    # ---- totals ----
    total = sum(landed.values()) * COIN_VAL
    d.rectangle([24, 412, 456, 462], fill=BOARD, outline=CHALK, width=3)
    d.text((38, 418), f"distributed: {total:.1f} / 30 $PROOFACTORY", font=vt(22), fill=YELLOW)
    d.text((38, 442), "no forms. no claims. automatic.",
           font=vt(20), fill=(159, 208, 255))

    if show_stamp:
        stamp(img, (240, 250), "AUTOMATIC", RED, 24, -8)
        stamp(img, (240, 292), "LEDGER DOESN'T LIE", ACCENT, 18, 6)
    return img


def g5(path):
    frames = []
    last = 16 + (len(WALLETS) * COINS_PER - 1) * COIN_EVERY \
        + int(path_len([(240, 152), (240, PATH_Y), (408 + 48, PATH_Y), (408 + 48, 322)]) / COIN_SPEED)
    for f in range(last + 6):
        frames.append(frame(f))
    for _ in range(14):
        frames.append(frame(last + 6, show_stamp=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("frames:", len(frames), "last:", last)


g5(OUT + "content-22-dividend-stream.gif")
print("part11 done")
