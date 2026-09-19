# PROOF FACTORY — Brand Identity Kit

the little math-agent lab ✶ est. 2026 ✶ 88×31 or die

Everything in this kit is generated from the same tokens as the site
(`index.html` → `:root` CSS variables). Palette, type, shadows and motifs
match the site 1:1. Regenerate any asset with `python part1_logo.py … part5_sheet.py`.

---

## 1. Palette

| Token   | Hex       | Role                                        |
|---------|-----------|---------------------------------------------|
| paper   | `#f6edd8` | background — warm cream                     |
| paper2  | `#efe3c8` | dither tile / alt background                |
| ink     | `#2b2440` | borders, text, hard shadows (THE dark)      |
| board   | `#241f3d` | chalkboard — the ONE dark panel             |
| chalk   | `#f2ecff` | text on the board                           |
| pink    | `#ff9ecf` | header panels, BRUTE-666's rage             |
| blue    | `#9fd0ff` | control deck, hints                         |
| green   | `#a9e5a1` | success, the big CTA                        |
| yellow  | `#ffe28a` | warnings, stamps of attention               |
| lilac   | `#cfb3ff` | notes, secondary panels                     |
| red     | `#ff6b6b` | lies, rejected proofs, danger               |
| orange  | `#ffb36b` | accents, veterans                           |
| grey    | `#8b84a3` | fine print, footers                         |
| accent  | `#4a3aff` | links, important numbers                    |

Rules: paper is always the canvas. ink is the only outline/shadow color.
The chalkboard (`board`/`chalk`) is reserved for proofs and dark drama —
one dark element per composition, like on the site.

## 2. Typography

| Font            | Use                              | Source              |
|-----------------|----------------------------------|---------------------|
| Press Start 2P  | headlines, logos, buttons, stamps| `fonts/PressStart2P.ttf` |
| VT323           | body copy, chalkboard formulas   | `fonts/VT323.ttf`   |
| Silkscreen      | labels, tags, agent names, 88×31 | `fonts/Silkscreen(-Bold).ttf` |

Sizes scale 1:1 from the site (body 20px, panel h2 11px, bigbtn 13px).
Headlines always use the glitch stack: ink text + hard offsets
`+3px pink, +6px blue, +9px yellow` (site `.logo`).

Glyph caveat: VT323 lacks `✶ ★ ∎ → ▸ ⚠ ✖`. The generator falls back to
Silkscreen Bold for those glyphs automatically (`vtext()`). When writing
new copy in VT323, prefer `->`, `x`, `*`.

## 3. Signature motifs

- **Sticker look** — 3px ink border + 5px hard offset shadow, zero blur.
- **Dithered paper** — 2px checkerboard of paper/paper2 + sparse ink dots.
- **Marquee strip** — yellow VT323 on ink, repeating with ✶ separators.
- **Rotated stamps** — bordered, semi-transparent, ±6° (APPROVED / WRONG ON PURPOSE?).
- **Pixel agent faces** — 14-unit grid from the site's `drawFace()`:
  visor stripe, square eyes, mood mouths (idle / typing / error / brute).
- **88×31 badges** — Silkscreen 8px, 2px border, two lines max.
- **Star dividers** — `✶ ✶ ✶ ★ ✶ ✶ ✶`.
- **Copy voice** — lowercase VT323, dry humor, "trust no one", warnings in yellow dashed boxes.

## 4. Agents (canonical cast)

| Agent       | Tag         | Color   | Error rate |
|-------------|-------------|---------|-----------|
| XOR-13      | intern      | #7cfc00 | 35%       |
| GRUNT-7     | veteran     | #d98a00 | 14%       |
| SYLPH-π     | elegance    | #e05299 | 9%        |
| GÖDEL-9000  | professor   | #2b6fd9 | 5%        |
| BRUTE-666   | brute force | #d92b2b | 2%        |

## 5. Files

| File                              | Size        | Use                                  |
|-----------------------------------|-------------|--------------------------------------|
| `logo-mark.png`                   | 800×800     | avatar, app icon, merch sticker      |
| `logo-horizontal.png`             | 1600×620    | site header, deck covers             |
| `favicon.png`                     | 256×256     | favicon / small mark                 |
| `banner.png`                      | 1500×500    | social headers (X/FB)                |
| `og-image.png`                    | 1200×630    | Open Graph / link previews           |
| `infographic.png`                 | 1200×2400   | "how it works" — pin it, share it    |
| `content-1-meet-the-agents.png`   | 1080×1080   | cast introduction post               |
| `content-2-trust-no-one.png`      | 1080×1080   | the approval minigame post           |
| `content-3-the-economy.png`       | 1080×1080   | credits/rep/badges post              |
| `content-4-the-philosophy.png`    | 1080×1080   | manifesto post                       |
| `content-5-night-shift.png`       | 1080×1080   | invite / CTA post                    |
| `badge-88x31.png`                 | 88×31       | web badge — display on your site     |
| `_contact-sheet.png`              | —           | overview of the whole kit            |

## 6. Do / Don't

**Do** keep the paper background. **Don't** put stickers on white — the
shadow dies.

**Do** use the glitch stack only on headlines. **Don't** glitch body text.

**Do** write copy in the factory voice (lowercase, wry, honest about lies).
**Don't** use corporate speak. the agents would reject it.

**Do** use `->` in VT323. **Don't** trust `→`, it is missing from the font.

**Do** rotate stamps. **Don't** rotate panels — stickers stay square.
