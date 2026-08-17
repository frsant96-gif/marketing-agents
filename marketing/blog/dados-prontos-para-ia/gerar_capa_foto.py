from PIL import Image, ImageDraw

SRC = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\business-analyst-reviewing-data-digital-screen.jpg"
OUT = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\marketing\blog\dados-prontos-para-ia\capa-foto.png"

TARGET_W, TARGET_H = 1200, 630
target_ratio = TARGET_W / TARGET_H

img = Image.open(SRC).convert("RGB")
w, h = img.size
cur_ratio = w / h

if cur_ratio > target_ratio:
    # image is wider than target -> crop width
    new_w = int(h * target_ratio)
    left = (w - new_w) // 2
    img = img.crop((left, 0, left + new_w, h))
else:
    # image is taller than target -> crop height (bias slightly toward top, where the face is)
    new_h = int(w / target_ratio)
    top = int((h - new_h) * 0.35)
    img = img.crop((0, top, w, top + new_h))

img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)

# brand-color overlay: subtle dark navy gradient from left (for potential future text safety)
# and an overall cool duotone-ish tint to tie the photo to the Solveplan dark palette,
# without obscuring the person. No text is added.
overlay = Image.new("RGBA", (TARGET_W, TARGET_H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

BRAND_DARK = (10, 14, 25)     # #0A0E19
BRAND_NAVY = (10, 8, 55)      # #0A0837

# left-to-right gradient: darker on the left, clear on the right (keeps the person/screen visible)
for x in range(TARGET_W):
    t = x / TARGET_W
    alpha = int(max(0, (0.55 - t * 0.65)) * 255)
    draw.line([(x, 0), (x, TARGET_H)], fill=(*BRAND_DARK, alpha))

# soft bottom vignette for grounding
for y in range(TARGET_H):
    t = y / TARGET_H
    alpha = int(max(0, (t - 0.62)) / 0.38 * 130)
    draw.line([(0, y), (TARGET_W, y)], fill=(*BRAND_NAVY, alpha))

base = img.convert("RGBA")
final = Image.alpha_composite(base, overlay).convert("RGB")

# thin brand-blue accent line at the very bottom edge (subtle, no text)
draw2 = ImageDraw.Draw(final)
draw2.rectangle([(0, TARGET_H - 5), (TARGET_W, TARGET_H)], fill=(0, 106, 255))

final.save(OUT, "PNG")
print("saved", OUT, final.size)
