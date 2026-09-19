# -*- coding: utf-8 -*-
"""PROOF FACTORY — brand kit generator. Style is copied 1:1 from the site CSS."""
import random
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# ---------- palette (from site :root) ----------
PAPER  = (246, 237, 216)
PAPER2 = (239, 227, 200)
INK    = (43, 36, 64)
BOARD  = (36, 31, 61)
CHALK  = (242, 236, 255)
PINK   = (255, 158, 207)
BLUE   = (159, 208, 255)
GREEN  = (169, 229, 161)
YELLOW = (255, 226, 138)
LILAC  = (207, 179, 255)
RED    = (255, 107, 107)
ORANGE = (255, 179, 107)
GREY   = (139, 132, 163)
ACCENT = (74, 58, 255)
WHITE  = (255, 255, 255)

FD = "fonts/"
_ps2p = {}
_vt   = {}
_silk = {}
def ps2p(sz):
    if sz not in _ps2p: _ps2p[sz] = ImageFont.truetype(FD + "PressStart2P.ttf", sz)
    return _ps2p[sz]
def vt(sz):
    if sz not in _vt: _vt[sz] = ImageFont.truetype(FD + "VT323.ttf", sz)
    return _vt[sz]
def silk(sz, bold=False):
    k = (sz, bold)
    if k not in _silk: _silk[k] = ImageFont.truetype(FD + ("Silkscreen-Bold.ttf" if bold else "Silkscreen.ttf"), sz)
    return _silk[k]

def ts(draw, text, font):
    b = draw.textbbox((0, 0), text, font=font)
    return b[2] - b[0], b[3] - b[1], b

# ---------- VT323 text with glyph fallback (VT323 lacks ✶ ★ ∎ → etc.) ----------
_vt_ok = set()
def _vt_has(ch):
    if ch in _vt_ok: return True
    if ch == " ": return True
    ok = vt(20).getmask(ch).getbbox() is not None
    if ok: _vt_ok.add(ch)
    return ok

def vtext(draw, xy, text, size, fill):
    """draw text in VT323; chars VT323 lacks fall back to Silkscreen bold"""
    x, y = xy
    f = vt(size)
    fs = silk(max(10, int(size * 0.52)), bold=True)
    runs, cur, cok = [], "", None
    for ch in text:
        ok = _vt_has(ch)
        if cok is None or ok == cok:
            cur += ch; cok = ok
        else:
            runs.append((cur, cok)); cur, cok = ch, ok
    runs.append((cur, cok))
    for t, ok in runs:
        if ok:
            draw.text((x, y), t, font=f, fill=fill)
            x += draw.textlength(t, font=f)
        else:
            draw.text((x, y + size * 0.30), t, font=fs, fill=fill)
            x += draw.textlength(t, font=fs)
    return x

# ---------- backgrounds ----------
def dither(w, h, base=PAPER, alt=PAPER2, dot=0.05, seed=7):
    """cream paper with 2px conic dither + sparse ink dots, like site body"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w]
    checker = ((xx // 2 + yy // 2) % 2) == 0
    dots = rng.random((h, w)) < dot
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[checker] = base
    img[~checker] = alt
    img[dots] = tuple(int(c * 0.94) for c in base)
    return Image.fromarray(img, "RGB")

def board_bg(w, h, seed=3):
    """dark chalkboard with chalk dust"""
    rng = np.random.default_rng(seed)
    img = np.zeros((h, w, 3), dtype=np.uint8); img[:] = BOARD
    dust = rng.random((h, w)) < 0.02
    img[dust] = (52, 46, 82)
    return Image.fromarray(img, "RGB")

# ---------- sticker / panel ----------
def sticker(img, box, fill=WHITE, shadow=6, border=4, scolor=INK, bcolor=INK, dashed=False):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    d.rectangle([x0 + shadow, y0 + shadow, x1 + shadow, y1 + shadow], fill=scolor)
    d.rectangle([x0, y0, x1, y1], fill=fill, outline=bcolor, width=border)
    return d

def dashed_sticker(img, box, fill=YELLOW, border=4, bcolor=INK, shadow=5):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    d.rectangle([x0 + shadow, y0 + shadow, x1 + shadow, y1 + shadow], fill=INK)
    d.rectangle([x0, y0, x1, y1], fill=fill)
    def dashed_line(p0, p1):
        (ax, ay), (bx, by) = p0, p1
        length = max(abs(bx - ax), abs(by - ay)); n = max(1, length // 14)
        for i in range(0, n * 2, 2):
            t0, t1 = i / (n * 2), (i + 1) / (n * 2)
            d.line([ax + (bx - ax) * t0, ay + (by - ay) * t0, ax + (bx - ax) * t1, ay + (by - ay) * t1], fill=bcolor, width=border)
    dashed_line((x0, y0), (x1, y0)); dashed_line((x1, y0), (x1, y1))
    dashed_line((x1, y1), (x0, y1)); dashed_line((x0, y1), (x0, y0))
    return d

# ---------- glitch headline (splash .logo style) ----------
def glitch_text(img, xy, text, font, fill=INK, k=1, align="center"):
    """3px/6px/9px pink/blue/yellow hard stack"""
    x, y = xy
    d = ImageDraw.Draw(img)
    w, h, b = ts(d, text, font)
    if align == "center": x -= w // 2
    elif align == "right": x -= w
    d.text((x + 3 * k, y + 3 * k), text, font=font, fill=PINK)
    d.text((x + 6 * k, y + 6 * k), text, font=font, fill=BLUE)
    d.text((x + 9 * k, y + 9 * k), text, font=font, fill=YELLOW)
    d.text((x, y), text, font=font, fill=fill)
    return w, h

# ---------- pixel agent face (site drawFace logic) ----------
AGENTS = [
    ("XOR-13",  "intern",      (124, 252, 0),  (217, 247, 196), .35),
    ("GRUNT-7", "veteran",     (217, 138, 0),  (255, 225, 168), .14),
    ("SYLPH-\u03c0", "elegance",    (224, 82, 153), (255, 208, 232), .09),
    ("G\u00d6DEL-9000", "professor", (43, 111, 217), (196, 224, 255), .05),
    ("BRUTE-666", "brute force", (217, 43, 43), (255, 196, 196), .02),
]

def pixel_face(size, color, mood="idle", brute=False):
    W = H = size
    img = Image.new("RGB", (W, H), WHITE)
    x = ImageDraw.Draw(img)
    u = max(1, W // 14)
    c = color
    x.rectangle([3 * u, 3 * u, 3 * u + 8 * u - 1, 3 * u + 7 * u - 1], fill=c)
    x.rectangle([3 * u, 3 * u, 3 * u + 8 * u - 1, 3 * u + 2 * u - 1], fill=tuple(min(255, v + 90) for v in c))
    x.rectangle([3 * u, 3 * u, 3 * u + 8 * u - 1, 3 * u + u - 1], fill=INK)
    x.rectangle([3 * u, 3 * u, 3 * u + 2 * u - 1, 3 * u + u - 1], fill=WHITE)
    if mood == "error" or brute:
        x.rectangle([4 * u, 5 * u, 4 * u + 2 * u - 1, 5 * u + 2 * u - 1], fill=RED if brute else INK)
        x.rectangle([8 * u, 5 * u, 8 * u + 2 * u - 1, 5 * u + 2 * u - 1], fill=RED if brute else INK)
        x.rectangle([4 * u, 5 * u, 4 * u + u - 1, 5 * u + u - 1], fill=WHITE)
        x.rectangle([8 * u, 5 * u, 8 * u + u - 1, 5 * u + u - 1], fill=WHITE)
    else:
        x.rectangle([4 * u, 5 * u, 4 * u + 2 * u - 1, 5 * u + 2 * u - 1], fill=INK)
        x.rectangle([8 * u, 5 * u, 8 * u + 2 * u - 1, 5 * u + 2 * u - 1], fill=INK)
    if mood == "typing":
        x.rectangle([5 * u, 8 * u, 5 * u + 4 * u - 1, 8 * u + u - 1], fill=INK)
    elif mood == "error":
        x.rectangle([5 * u, 8 * u, 5 * u + 4 * u - 1, 8 * u + 2 * u - 1], fill=INK)
        x.rectangle([6 * u, 8 * u, 6 * u + 2 * u - 1, 8 * u + u - 1], fill=WHITE)
    elif brute:
        x.rectangle([4 * u, 8 * u, 4 * u + 6 * u - 1, 8 * u + 2 * u - 1], fill=INK)
        x.rectangle([5 * u, 8 * u, 5 * u + 4 * u - 1, 8 * u + u - 1], fill=RED)
    else:
        x.rectangle([5 * u, 8 * u, 5 * u + 4 * u - 1, 8 * u + u - 1], fill=INK)
        x.rectangle([5 * u, 8 * u, 5 * u + 4 * u - 1, 8 * u + max(1, u // 2) - 1], fill=WHITE)
    return img

# ---------- rotated stamp ----------
def stamp(img, xy, text, color=RED, fsize=22, angle=-6, pad=14):
    f = ps2p(fsize)
    tmp = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(tmp)
    w, h, b = ts(d, text, f)
    lay = Image.new("RGBA", (w + pad * 2 + 8, h + pad * 2 + 8), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ld.rectangle([4, 4, 4 + w + pad * 2, 4 + h + pad * 2], outline=color, width=5)
    ld.rectangle([4, 4, 4 + w + pad * 2, 4 + h + pad * 2], fill=(0, 0, 0, 60))
    ld.text((4 + pad - b[0], 4 + pad - b[1]), text, font=f, fill=color)
    lay = lay.rotate(angle, expand=True, resample=Image.NEAREST)
    img.paste(lay, (int(xy[0] - lay.width / 2), int(xy[1] - lay.height / 2)), lay)

# ---------- marquee strip ----------
def marquee(img, box, text, fill=INK, tfill=YELLOW, fsize=26):
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(img)
    d.rectangle(box, fill=fill)
    unit = "  " + text + "  "
    tmp = Image.new("RGB", (10, 10)); td = ImageDraw.Draw(tmp)
    vw = vtext(td, (0, 0), unit, fsize, tfill)
    tx = x0 + 12; ty = y0 + (y1 - y0 - fsize) // 2
    while tx < x1 - 20:
        vtext(d, (tx, ty), unit, fsize, tfill)
        tx += vw

def stars(fsize=30):
    return "\u2736 \u2736 \u2736 \u2605 \u2736 \u2736 \u2736"

# ---------- classic 88x31 badge ----------
def badge88(text_lines, bg=WHITE, border=INK):
    img = Image.new("RGB", (88, 31), bg)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 87, 30], outline=border, width=2)
    f = silk(8, bold=True)
    total = sum(ts(d, t, f)[1] + 1 for t in text_lines) - 1
    y = (31 - total) // 2
    for t in text_lines:
        w, h, b = ts(d, t, f)
        d.text(((88 - w) // 2 - b[0], y - b[1]), t, font=f, fill=INK)
        y += h + 1
    return img
