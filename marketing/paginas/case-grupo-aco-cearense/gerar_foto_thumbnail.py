"""Monta a foto do círculo da thumbnail do vídeo do case (Alexandre Faraco, Renan Lacerda e Jonys Arcanjo),
a partir de frames do "VT Aço Cearense - v02.mp4", em 3 faixas verticais. Saída quadrada 1200x1200.

Uso: python gerar_foto_thumbnail.py <pasta-com-alexandre.png-renan.png-jonys.png> [arte.png]
Os frames saem do vídeo com ffmpeg: alexandre 197 s, renan 58,5 s, jonys 102 s.
"""
import sys, pathlib
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(__file__).parent
SIZE, STRIP, GAP = 1200, 400, 8
DROP = 170                               # quanto os rostos descem para ficar no meio do círculo
NAVY = (10, 8, 55)

# (arquivo, centro do rosto no eixo x do frame 1920x1080)
PEOPLE = [("alexandre.png", 1282), ("renan.png", 1190), ("jonys.png", 1184)]

canvas = Image.new("RGB", (SIZE, SIZE), NAVY)
w = 1080 * STRIP // SIZE                 # recorte na altura cheia, proporção da faixa
for i, (fname, cx) in enumerate(PEOPLE):
    im = Image.open(SRC / fname).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.92)          # tira um pouco do ciano/magenta do estande
    strip = im.crop((cx - w // 2, 0, cx + w // 2, 1080)).resize((STRIP, SIZE), Image.LANCZOS)
    # o enquadramento do vídeo é fechado: desce o rosto e completa o topo com o fundo desfocado
    top = strip.crop((0, 0, STRIP, 40)).resize((STRIP, DROP + 80)).filter(ImageFilter.GaussianBlur(30))
    canvas.paste(top, (i * STRIP, 0))
    fade = Image.linear_gradient("L").resize((STRIP, 80))           # transição suave na emenda
    mask = Image.new("L", (STRIP, SIZE), 255); mask.paste(fade, (0, 0))
    canvas.paste(strip, (i * STRIP, DROP), mask)
d = ImageDraw.Draw(canvas)
for x in (STRIP, 2 * STRIP):
    d.rectangle([x - GAP // 2, 0, x + GAP // 2 - 1, SIZE], fill=NAVY)
canvas.save(OUT / "thumb-aco-cearense-3-pessoas.jpg", quality=92)
print("ok thumb-aco-cearense-3-pessoas.jpg")

# prévia dentro da arte (opcional): círculo da arte em ~ (552, 307), raio ~145, em 942x527
if len(sys.argv) > 2:
    art = Image.open(sys.argv[2]).convert("RGB")
    cx, cy, r = 552, 311, 157
    face = canvas.resize((2 * r, 2 * r), Image.LANCZOS)
    mask = Image.new("L", face.size, 0)
    ImageDraw.Draw(mask).ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
    art.paste(face, (cx - r, cy - r), mask)
    art.save(OUT / "_previa-thumbnail.jpg", quality=92)
    print("ok _previa-thumbnail.jpg")
