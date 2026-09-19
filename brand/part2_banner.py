# -*- coding: utf-8 -*-
"""Part 2: social banner (1500x500) + OG card (1200x630)."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

# ============ BANNER 1500x500 ============
def banner(path):
    W, H = 1500, 500
    img = dither(W, H)
    d = ImageDraw.Draw(img)
    # left text block
    glitch_text(img, (70, 66), "PROOF", ps2p(64), align="left", k=2)
    glitch_text(img, (70, 160), "FACTORY", ps2p(64), align="left", k=2)
    d = ImageDraw.Draw(img)
    vtext(d, (72, 288), "\u2736 the little math-agent lab \u2736", 44, ACCENT)
    d.text((72, 342), "bet on pocket agents. check their proofs.", font=vt(38), fill=INK)
    d.text((72, 390), "trust no one.", font=vt(38), fill=RED)
    # right: agents sticker panel
    px0, py0, px1, py1 = 880, 46, 1440, 384
    sticker(img, [px0, py0, px1, py1], fill=PINK, shadow=8, border=5)
    d = ImageDraw.Draw(img)
    d.text((px0 + 28, py0 + 18), "// BASEMENT AGENTS", font=ps2p(18), fill=INK)
    moods = ["typing", "idle", "idle", "error", "idle"]
    fx = px0 + 30
    for (name, tag, color, bg, err), mood in zip(AGENTS, moods):
        fimg = pixel_face(86, color, mood=mood, brute=(name == "BRUTE-666"))
        img.paste(fimg, (fx, py0 + 78))
        d.rectangle([fx, py0 + 78, fx + 85, py0 + 78 + 85], outline=INK, width=4)
        tw, th, tb = ts(d, name, silk(12, bold=True))
        d.text((fx + 43 - tw // 2 - tb[0], py0 + 178), name, font=silk(12, bold=True), fill=INK)
        tw2, _, tb2 = ts(d, tag, silk(10))
        d.text((fx + 43 - tw2 // 2 - tb2[0], py0 + 200), tag, font=silk(10), fill=(58, 51, 84))
        fx += 106
    d.text((px0 + 28, py1 - 52), "one of them is wrong on purpose.", font=vt(34), fill=INK)
    # marquee strip at bottom
    marquee(img, [0, H - 58, W, H], "\u2736 WELCOME TO THE FACTORY \u2736 AGENTS PROVE THE UNPROVABLE \u2736 BETS CLOSE AT START \u2736 DO NOT ASK ABOUT THE HOLD \u2736")
    img.save(path)

# ============ OG CARD 1200x630 ============
def og(path):
    W, H = 1200, 630
    img = dither(W, H, seed=11)
    d = ImageDraw.Draw(img)
    glitch_text(img, (W // 2, 120), "PROOF", ps2p(76), k=2)
    glitch_text(img, (W // 2, 250), "FACTORY", ps2p(76), k=2)
    d = ImageDraw.Draw(img)
    tmp = Image.new("RGB", (10, 10)); tdr = ImageDraw.Draw(tmp)
    sub = "\u2736 the little math-agent lab \u2736"
    tw = vtext(tdr, (0, 0), sub, 46, ACCENT)
    vtext(d, (W // 2 - tw // 2, 420), sub, 46, ACCENT)
    d.text((W // 2 - tw // 2 + 40, 480), "a cozy research station. agents sometimes lie.", font=vt(38), fill=GREY)
    # agent heads row
    fx = W // 2 - (5 * 74) // 2
    for (name, tag, color, bg, err) in AGENTS:
        fimg = pixel_face(64, color, brute=(name == "BRUTE-666"))
        img.paste(fimg, (fx, 540))
        d.rectangle([fx, 540, fx + 63, 540 + 63], outline=INK, width=4)
        fx += 74
    marquee(img, [0, 0, W, 44], "est. 2026 \u2736 88\u00d731 or die \u2736 best viewed at 800\u00d7600 \u2736")
    img.save(path)

banner(OUT + "banner.png")
og(OUT + "og-image.png")
print("part2 done")
