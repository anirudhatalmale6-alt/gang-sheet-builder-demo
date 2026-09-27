#!/usr/bin/env python3
"""Generate placeholder DTF transfer artwork (transparent PNGs) for the demo."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
os.makedirs(OUT, exist_ok=True)

DPI = 300
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
COND = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype(BOLD, size)


def text_img(lines, colors, fonts, pad=40, spacing=14, outline=None):
    """Render stacked lines of text onto a transparent canvas, cropped tight."""
    probe = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(probe)
    sizes = []
    for txt, f in zip(lines, fonts):
        box = d.textbbox((0, 0), txt, font=f, stroke_width=outline[1] if outline else 0)
        sizes.append((box[2] - box[0], box[3] - box[1], box[0], box[1]))
    w = max(s[0] for s in sizes) + pad * 2
    h = sum(s[1] for s in sizes) + spacing * (len(lines) - 1) + pad * 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y = pad
    for (txt, f, col, (tw, th, ox, oy)) in zip(lines, fonts, colors, sizes):
        x = (w - tw) // 2 - ox
        if outline:
            d.text((x, y - oy), txt, font=f, fill=col,
                   stroke_width=outline[1], stroke_fill=outline[0])
        else:
            d.text((x, y - oy), txt, font=f, fill=col)
        y += th + spacing
    return img


def save(img, name):
    img.save(os.path.join(OUT, name), "PNG", dpi=(DPI, DPI))
    print(f"{name}: {img.width}x{img.height}px  ->  "
          f"{img.width/DPI:.2f}in x {img.height/DPI:.2f}in @ {DPI}dpi")


# 1. Mama Bear
save(text_img(
    ["MAMA", "BEAR"],
    [(28, 28, 30, 255), (196, 106, 42, 255)],
    [font(BOLD, 300), font(SERIF, 200)],
    outline=((255, 255, 255, 255), 10),
), "mama-bear.png")

# 2. Friday Night Lights
save(text_img(
    ["FRIDAY NIGHT", "LIGHTS"],
    [(18, 32, 74, 255), (176, 30, 45, 255)],
    [font(COND, 150), font(BOLD, 260)],
    outline=((255, 255, 255, 255), 8),
), "friday-night-lights.png")

# 3. Blessed (script-ish)
save(text_img(
    ["blessed"],
    [(63, 107, 84, 255)],
    [font(SERIF, 320)],
), "blessed.png")

# 4. Small pocket logo — circle badge
badge = Image.new("RGBA", (900, 900), (0, 0, 0, 0))
d = ImageDraw.Draw(badge)
d.ellipse((20, 20, 880, 880), outline=(28, 28, 30, 255), width=34)
d.ellipse((70, 70, 830, 830), outline=(196, 106, 42, 255), width=14)
f1, f2 = font(BOLD, 150), font(COND, 74)
for txt, f, yy, col in (("EST.", f2, 300, (110, 110, 115, 255)),
                        ("2019", f1, 380, (28, 28, 30, 255)),
                        ("SOUTHERN", f2, 540, (196, 106, 42, 255))):
    box = d.textbbox((0, 0), txt, font=f)
    d.text(((900 - (box[2] - box[0])) // 2 - box[0], yy), txt, font=f, fill=col)
save(badge, "pocket-badge.png")

# 5. Wide sleeve strip
strip = Image.new("RGBA", (2600, 360), (0, 0, 0, 0))
d = ImageDraw.Draw(strip)
f = font(COND, 190)
txt = "SALT  ·  SAND  ·  SUNSHINE"
box = d.textbbox((0, 0), txt, font=f)
d.text(((2600 - (box[2] - box[0])) // 2 - box[0], 60 - box[1]), txt, font=f,
       fill=(24, 84, 122, 255))
save(strip, "sleeve-strip.png")

# 6. Tall vertical design
save(text_img(
    ["GAME", "DAY", "READY"],
    [(176, 30, 45, 255), (28, 28, 30, 255), (176, 30, 45, 255)],
    [font(BOLD, 240), font(BOLD, 300), font(COND, 150)],
    spacing=4,
    outline=((255, 255, 255, 255), 8),
), "game-day.png")

# 7. Tiny name decal
save(text_img(
    ["Harper"],
    [(140, 66, 140, 255)],
    [font(SERIF, 200)],
), "name-decal.png")
