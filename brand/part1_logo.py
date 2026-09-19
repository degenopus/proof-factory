# -*- coding: utf-8 -*-
"""Part 1: logo assets — mark, horizontal lockup, favicon."""
from brandkit import *

OUT = "out/"
import os
os.makedirs(OUT, exist_ok=True)

# ============ LOGO MARK (800x800) ============
def logo_mark(path, S=800):
    img = dither(S, S)
    d = ImageDraw.Draw(img)
    # outer sticker
    m = 90
    sticker(img, [m, m, S - m, S - m], fill=WHITE, shadow=12, border=8)
    # inner chalkboard square
    b0 = m + 60
    b1 = S - m - 60
    d.rectangle([b0 + 10, b0 + 10, b1 + 10, b1 + 10], fill=INK)
    d.rectangle([b0, b0, b1, b1], fill=BOARD, outline=INK, width=8)
    # glitch PF monogram in chalk
    glitch_text(img, ((b0 + b1) // 2, b0 + 90), "PF", ps2p(150), fill=CHALK, k=2)
    d = ImageDraw.Draw(img)
    # chalk dust underline + formula
    d.text((b0 + 40, b1 - 150), "P \u2260 NP (probably)", font=vt(54), fill=CHALK)
    d.text((b0 + 40, b1 - 92), "trust no one.", font=vt(54), fill=(159, 208, 255))
    # pixel head peeking from bottom-right (the "factory worker")
    face = pixel_face(240, PINK)
    img.paste(face, (S - m - 210, S - m - 150))
    d.rectangle([S - m - 210, S - m - 150, S - m - 210 + 239, S - m - 150 + 239], outline=INK, width=8)
    # est ribbon
    rw, rh = 300, 66
    rx, ry = m + 30, m - 30
    d.rectangle([rx + 6, ry + 6, rx + rw + 6, ry + rh + 6], fill=INK)
    d.rectangle([rx, ry, rx + rw, ry + rh], fill=YELLOW, outline=INK, width=6)
    tw, th, tb = ts(d, "EST. 2026", ps2p(26))
    d.text((rx + (rw - tw) // 2 - tb[0], ry + (rh - th) // 2 - tb[1]), "EST. 2026", font=ps2p(26), fill=INK)
    img.save(path)

# ============ HORIZONTAL LOGO (1600x620) ============
def logo_horizontal(path):
    W, H = 1600, 620
    img = dither(W, H)
    d = ImageDraw.Draw(img)
    # mark on the left
    face = pixel_face(300, PINK)
    img.paste(face, (110, 160))
    d.rectangle([110, 160, 409, 459], outline=INK, width=8)
    d.rectangle([122, 172, 421, 471], outline=INK, width=4)  # double frame quirk
    # wordmark
    glitch_text(img, (500, 150), "PROOF", ps2p(88), align="left", k=2)
    glitch_text(img, (500, 300), "FACTORY", ps2p(88), align="left", k=2)
    d = ImageDraw.Draw(img)
    vtext(d, (505, 470), "\u2736 the little math-agent lab \u2736", 52, ACCENT)
    vtext(d, (505, 530), "est. 2026  \u2736  88\u00d731 or die  \u2736  best viewed at 800\u00d7600", 40, GREY)
    img.save(path)

# ============ FAVICON (256) ============
def favicon(path):
    S = 256
    img = Image.new("RGB", (S, S), BOARD)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, S - 1, S - 1], outline=INK, width=12)
    glitch_text(img, (S // 2, S // 2 - 62), "PF", ps2p(88), fill=CHALK, k=1)
    img.save(path)

logo_mark(OUT + "logo-mark.png")
logo_horizontal(OUT + "logo-horizontal.png")
favicon(OUT + "favicon.png")
print("part1 done")
