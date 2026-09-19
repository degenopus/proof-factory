# -*- coding: utf-8 -*-
"""Part 8: three social GIFs 480x480. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os, random
os.makedirs(OUT, exist_ok=True)

W = H = 480


def stamp_layer(text, color, fsize=22, pad=14):
    f = ps2p(fsize)
    tmp = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(tmp)
    w, h, b = ts(d, text, f)
    lay = Image.new("RGBA", (w + pad * 2 + 8, h + pad * 2 + 8), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ld.rectangle([4, 4, 4 + w + pad * 2, 4 + h + pad * 2], outline=color, width=5)
    ld.rectangle([4, 4, 4 + w + pad * 2, 4 + h + pad * 2], fill=(0, 0, 0, 60))
    ld.text((4 + pad - b[0], 4 + pad - b[1]), text, font=f, fill=color)
    return lay


def save_gif(frames, path, duration=130):
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=duration, loop=0, optimize=True)


# ============ G1: LIE INJECTOR ============
def g1(path):
    lines = [
        ("TASK: x\u00b2 - 7x + 12 = 0", YELLOW),
        ("D = 49 - 48 = 1", CHALK),
        ("x = (7 \u00b1 1) / 2", CHALK),
        ("x1 = 4   x2 = 3", CHALK),
    ]
    lies = ["OFF-BY-ONE", "SIGN FLIP", "PLUS TWO", "TIMES TEN"]

    def base():
        img = board_bg(W, H, seed=21)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        d.text((28, 20), "THE FLAWED-PROOF ENGINE", font=silk(12, bold=True), fill=(159, 208, 255))
        return img, d

    frames = []
    # type out the clean proof
    li, ci, step = 0, 0, 0
    while li < len(lines):
        img, d = base()
        y = 74
        for j, (t, c) in enumerate(lines):
            if j < li:
                d.text((34, y), t, font=vt(32), fill=c)
            elif j == li:
                d.text((34, y), t[:ci], font=vt(32), fill=c)
                if step % 2 == 0:
                    cw = d.textlength(t[:ci], font=vt(32))
                    d.rectangle([36 + cw, y + 4, 36 + cw + 15, y + 32], fill=CHALK)
            y += 48
        frames.append(img)
        step += 1
        ci += 2
        if ci >= len(lines[li][0]) + 2:
            li += 1
            ci = 0
    for _ in range(4):
        frames.append(frames[-1])
    # injection point: dot pulses
    img0, d0 = base()
    y = 74
    for t, c in lines:
        d0.text((34, y), t, font=vt(32), fill=c)
        y += 48
    for k in range(4):
        img = img0.copy()
        d = ImageDraw.Draw(img)
        r = 6 + k * 5
        cx, cy = 240, y + 26
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RED, width=4)
        frames.append(img)
    # flash + stamp slam
    slam = stamp_layer("LIE INJECTED", RED, 24)
    rng = random.Random(4)
    for k in range(5):
        img = img0.copy()
        sc = 0.5 + k * 0.16
        lay = slam.resize((int(slam.width * sc), int(slam.height * sc)), Image.NEAREST)
        img.paste(lay, (240 - lay.width // 2 + rng.randint(-6, 6),
                        y + 20 - lay.height // 2 + rng.randint(-6, 6)), lay)
        frames.append(img)
    flash = Image.new("RGB", (W, H), RED)
    frames.append(flash)
    img = img0.copy()
    lay = slam.resize((int(slam.width * 1.35), int(slam.height * 1.35)), Image.NEAREST)
    img.paste(lay, (240 - lay.width // 2, y + 20 - lay.height // 2), lay)
    for _ in range(8):
        frames.append(img)
    # lie type cycles
    for cycle in range(2):
        for t in lies:
            img = img0.copy()
            lay = slam.resize((int(slam.width * 1.35), int(slam.height * 1.35)), Image.NEAREST)
            img.paste(lay, (240 - lay.width // 2, y + 20 - lay.height // 2), lay)
            d = ImageDraw.Draw(img)
            d.text((34, y + 84), "INJECTED LIE TYPE:", font=silk(12, bold=True), fill=GREY)
            d.text((34, y + 112), "> " + t, font=vt(40), fill=RED)
            frames.append(img)
    for _ in range(3):
        frames.append(frames[-1])
    # end card
    img, d = base()
    y2 = 90
    for t, c in lines:
        d.text((34, y2), t, font=vt(32), fill=c)
        y2 += 48
    d.text((34, y2 + 14), "one of these lines is a lie.", font=vt(36), fill=RED)
    d.text((34, y2 + 56), "find it. -> prooffactory.icu", font=vt(30), fill=CHALK)
    for _ in range(14):
        frames.append(img)
    save_gif(frames, path)


# ============ G2: COFFEE SABOTAGE ============
def g2(path):
    rng = random.Random(9)

    def mug(d, x, y, s=1):
        u = int(10 * s)
        d.rectangle([x, y, x + 7 * u, y + 8 * u], fill=WHITE, outline=INK, width=3)
        d.rectangle([x + u, y + u, x + 6 * u, y + 2 * u], fill=(120, 80, 40))
        d.rectangle([x + 7 * u, y + 2 * u, x + 9 * u, y + 5 * u], outline=INK, width=3)
        d.rectangle([x, y + 8 * u, x + 7 * u, y + 9 * u], fill=(120, 80, 40))

    def scene(d, coffee_y=None, splash=None, glitch=False):
        # leaderboard
        d.text((28, 20), "ROUND LEADERBOARD", font=silk(12, bold=True), fill=INK)
        rows = [("1. GRUNT-7", 0.86, (217, 138, 0)), ("2. SYLPH-\u03c0", 0.62, (224, 82, 153))]
        y = 56
        for name, spd, col in rows:
            d.text((28, y), name, font=vt(30), fill=INK)
            d.rectangle([210, y + 4, 452, y + 30], outline=INK, width=3)
            d.rectangle([213, y + 7, 213 + int(236 * spd), y + 27], fill=col)
            y += 48
        # big leader face
        fx, fy = 176, 190
        mood = "error" if coffee_y is not None else "idle"
        face = pixel_face(128, (217, 138, 0), mood=mood)
        if coffee_y is not None:
            face = face.copy()
            fd = ImageDraw.Draw(face)
            fd.rectangle([20, 76, 108, 96], fill=(120, 80, 40))  # coffee over eyes
            for _ in range(6):
                bx0, by0 = rng.randint(24, 100), rng.randint(60, 116)
                fd.rectangle([bx0, by0, bx0 + 4, by0 + 4], fill=(120, 80, 40))
        if glitch:
            face = face.copy()
            fd = ImageDraw.Draw(face)
            for _ in range(5):
                yy = rng.randint(0, 120)
                fd.line([0, yy, 127, yy], fill=(255, 255, 255))
        return fx, fy, face

    frames = []
    # mug descends
    for cy in range(-140, 178, 18):
        img = dither(W, H, seed=33)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        fx, fy, face = scene(d)
        img.paste(face, (fx, fy))
        d.rectangle([fx, fy, fx + 127, fy + 127], outline=INK, width=4)
        mug(d, fx + 24, cy, 1.1)
        frames.append(img)
    # splash frames
    for k in range(6):
        img = dither(W, H, seed=33)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        fx, fy, face = scene(d, coffee_y=1, splash=k)
        img.paste(face, (fx, fy))
        d.rectangle([fx, fy, fx + 127, fy + 127], outline=INK, width=4)
        mug(d, fx + 24, 178, 1.1)
        for _ in range(4 + k * 3):
            sx = fx + 20 + rng.randint(-30, 120)
            sy = fy + 60 + rng.randint(-50, 70)
            d.rectangle([sx, sy, sx + 5, sy + 5], fill=(120, 80, 40))
        frames.append(img)
    # sticker slap
    sab = stamp_layer("SABOTAGED", RED, 22)
    for k in range(5):
        img = dither(W, H, seed=33)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        fx, fy, face = scene(d, coffee_y=1)
        img.paste(face, (fx, fy))
        d.rectangle([fx, fy, fx + 127, fy + 127], outline=INK, width=4)
        mug(d, fx + 24, 178, 1.1)
        sc = 0.5 + k * 0.18
        lay = sab.resize((int(sab.width * sc), int(sab.height * sc)), Image.NEAREST)
        img.paste(lay, (240 - lay.width // 2 + rng.randint(-6, 6),
                        250 - lay.height // 2 + rng.randint(-6, 6)), lay)
        frames.append(img)
    # glitch hold
    for k in range(10):
        img = dither(W, H, seed=33)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        fx, fy, face = scene(d, coffee_y=1, glitch=(k % 3 == 0))
        img.paste(face, (fx, fy))
        d.rectangle([fx, fy, fx + 127, fy + 127], outline=INK, width=4)
        mug(d, fx + 24, 178, 1.1)
        lay = sab.resize((int(sab.width * 1.4), int(sab.height * 1.4)), Image.NEAREST)
        img.paste(lay, (240 - lay.width // 2, 250 - lay.height // 2), lay)
        frames.append(img)
    # speed bar wobble + overtaken
    for k in range(12):
        img = dither(W, H, seed=33)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        d.text((28, 20), "ROUND LEADERBOARD", font=silk(12, bold=True), fill=INK)
        t = k / 11
        spd1 = 0.86 - 0.45 * t + (0.05 if k % 2 else -0.05)
        spd2 = 0.62 + 0.22 * t
        rows = [("1. GRUNT-7", spd1, (217, 138, 0)), ("2. SYLPH-\u03c0", spd2, (224, 82, 153))]
        if k > 7:
            rows = [("1. SYLPH-\u03c0", spd2, (224, 82, 153)), ("2. GRUNT-7", spd1, (217, 138, 0))]
        y = 56
        for name, spd, col in rows:
            d.text((28, y), name, font=vt(30), fill=INK)
            d.rectangle([210, y + 4, 452, y + 30], outline=INK, width=3)
            d.rectangle([213, y + 7, 213 + int(236 * max(0.1, spd)), y + 27], fill=col)
            y += 48
        fx, fy, face = scene(d, coffee_y=1, glitch=(k % 2 == 0))
        img.paste(face, (fx, fy))
        d.rectangle([fx, fy, fx + 127, fy + 127], outline=INK, width=4)
        mug(d, fx + 24, 178, 1.1)
        lay = sab.resize((int(sab.width * 1.4), int(sab.height * 1.4)), Image.NEAREST)
        img.paste(lay, (240 - lay.width // 2, 250 - lay.height // 2), lay)
        frames.append(img)
    # end card
    img = dither(W, H, seed=33)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((28, 40), "THE SABOTAGE DECK", font=silk(14, bold=True), fill=INK)
    d.text((28, 90), "coffee the leader.", font=vt(38), fill=INK)
    d.text((28, 140), "steal the round.", font=vt(38), fill=ACCENT)
    d.text((28, 190), "costs credits.", font=vt(38), fill=GREY)
    d.text((28, 240), "worth every one.", font=vt(38), fill=RED)
    d.text((28, 330), "no referee. no mercy.", font=vt(34), fill=INK)
    d.text((28, 376), "-> prooffactory.icu", font=vt(34), fill=ACCENT)
    for _ in range(14):
        frames.append(img)
    save_gif(frames, path)


# ============ G3: PICK YOUR AGENT ============
def g3(path):
    frames = []

    def slot(i, active_idx, err_frac):
        name, role, col, lite, err, = AGENTS[i]
        x0 = 36
        y0 = 120 + i * 64
        w, h = 408, 56
        fill = (52, 46, 82) if i == active_idx else BOARD
        d.rectangle([x0 + 5, y0 + 5, x0 + w + 5, y0 + h + 5], fill=INK)
        d.rectangle([x0, y0, x0 + w, y0 + h], fill=fill, outline=(YELLOW if i == active_idx else (70, 62, 105)), width=3)
        face = pixel_face(44, col)
        img.paste(face, (x0 + 6, y0 + 6))
        d.text((x0 + 62, y0 + 8), name, font=silk(13, bold=True), fill=lite)
        d.text((x0 + 62, y0 + 30), role, font=vt(24), fill=GREY)
        # error bar
        d.rectangle([x0 + 250, y0 + 16, x0 + 394, y0 + 40], outline=CHALK, width=2)
        frac = err_frac if i == active_idx else err / 0.35
        bw = int(140 * min(1, frac))
        colr = RED if err > 0.3 else (ORANGE if err > 0.1 else GREEN)
        if bw > 0:
            d.rectangle([x0 + 252, y0 + 18, x0 + 252 + bw, y0 + 38], fill=colr)
        d.text((x0 + 226, y0 + 16), f"{int(err * 100)}%", font=vt(24), fill=CHALK)

    # two cycles of the selector
    for cycle in range(2):
        for i in range(len(AGENTS)):
            err = AGENTS[i][4]
            for f in range(7):
                img = board_bg(W, H, seed=55)
                d = ImageDraw.Draw(img)
                d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
                d.text((28, 22), "AGENT SELECT // TERMINAL 05", font=silk(12, bold=True), fill=(159, 208, 255))
                frac = err * min(1.0, f / 5)
                for j in range(len(AGENTS)):
                    slot(j, i, frac)
                d.text((36, 452), "stake high. doubt everything.", font=vt(24), fill=GREY)
                frames.append(img)
    # all slots lit, blink prompt
    for k in range(6):
        img = board_bg(W, H, seed=55)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        d.text((28, 22), "AGENT SELECT // TERMINAL 05", font=silk(12, bold=True), fill=(159, 208, 255))
        for j in range(len(AGENTS)):
            slot(j, j, AGENTS[j][4])
        if k % 2 == 0:
            d.text((36, 452), "> choose wisely. -> prooffactory.icu", font=vt(24), fill=YELLOW)
        else:
            d.text((36, 452), "  choose wisely. -> prooffactory.icu", font=vt(24), fill=GREY)
        frames.append(img)
    for _ in range(8):
        frames.append(frames[-1])
    save_gif(frames, path)


g1(OUT + "content-17-lie-injector.gif")
g2(OUT + "content-18-sabotage.gif")
g3(OUT + "content-19-agent-select.gif")
print("part8 done")
