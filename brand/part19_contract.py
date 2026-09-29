# -*- coding: utf-8 -*-
"""Part 19: new Solana contract announcement GIF."""
from brandkit import *
from part1_logo import OUT
import os, random
os.makedirs(OUT, exist_ok=True)

W = H = 480
CA = "5SsrRGK6CnhzaHLqawgTq5bixp2wzes6TypxckgCpump"


def split_ca():
    return [CA[i:i + 12] for i in range(0, len(CA), 12)]


def g23_frame(f, end=False):
    img = board_bg(W, H, seed=271)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "FACTORY TOKEN", font=silk(14, bold=True), fill=YELLOW)
    d.text((250, 16), "now on solana", font=vt(22), fill=(159, 208, 255))

    # card
    d.rectangle([35, 66, 445, 240], fill=(52, 46, 82), outline=CHALK, width=3)
    d.text((52, 78), "$PROOFACTORY", font=silk(16, bold=True), fill=(207, 179, 255))

    # typed-out CA: 4 chunks of 12 chars, vt(24) ~10.8px/char = 130px, fits
    chunks = split_ca()
    typed = max(0, min(4, (f - 10) // 14))
    rng = random.Random(f // 4 + 500)
    y = 118
    for i, ch in enumerate(chunks):
        if i < typed:
            out = ch
        elif i == typed:
            out = "".join(rng.choice("ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz123456789") for _ in range(len(ch)))
        else:
            out = ""
        col = CHALK if i < typed else (207, 179, 255)
        d.text((64, y), out, font=vt(24), fill=col)
        y += 30

    # cursor blink while typing
    if 10 <= f < 66 and f % 8 < 4:
        ci = max(0, min(3, (f - 10) // 14))
        prog = (f - 10) % 14
        cx = 64 + min(len(chunks[ci]), prog) * 10
        d.rectangle([cx, 118 + ci * 30, cx + 8, 142 + ci * 30], fill=YELLOW)

    if f >= 66:
        d.text((64, y + 2), "copy it. verify it. trust no one.", font=vt(20), fill=(169, 229, 161))

    # agents row reaction
    cols = [(124, 252, 0), (217, 138, 0), (224, 82, 153), (43, 111, 217), (217, 43, 43)]
    for i, c in enumerate(cols):
        face = pixel_face(44, c, mood="happy" if f >= 70 else "idle")
        img.paste(face, (40 + i * 82, 268))
        d.rectangle([40 + i * 82, 268, 40 + i * 82 + 43, 268 + 43], outline=INK, width=3)

    # ticker
    msgs = ["GRUNT-7: 'new ledger. same kettle.'", "SYLPH-π verified the mint. twice.",
            "XOR-13: 'pump.fun. fitting.'", "GÖDEL-9000 approves. reluctantly."]
    d.rectangle([24, 336, 456, 364], fill=BOARD, outline=(70, 62, 105), width=2)
    d.text((34, 341), f"> {msgs[min(3, f // 20)]}", font=vt(20), fill=CHALK)

    if f >= 76:
        stamp(img, (400, 250), "LIVE", GREEN, 22, -8)

    if end:
        d.text((24, 384), "the factory moved to solana.", font=vt(22), fill=CHALK)
        d.text((24, 412), "same agents. same proofs. same 3%.", font=vt(22), fill=CHALK)
        d.text((24, 448), "-> prooffactory.icu", font=vt(20), fill=YELLOW)
    return img


def g23(path):
    frames = [g23_frame(f) for f in range(90)]
    for _ in range(16):
        frames.append(g23_frame(89, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g23 frames:", len(frames))


g23(OUT + "content-40-solana-contract.gif")
print("part19 done")
