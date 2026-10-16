"""Monta a thumbnail do case Oji Papéis com André Ozanan e Cleiton Cabral lado a lado,
a partir de frames do "VT OJI Papéis - v02.mp4" (André 45 s, Cleiton 120 s).
Saída 1400x720 (mesma proporção 700x360 das capas dos cases no site).

Uso: python gerar_thumbnail.py <caminho-do-video>
"""
import sys, pathlib, subprocess, tempfile
from PIL import Image, ImageDraw, ImageEnhance

VIDEO = sys.argv[1]
OUT = pathlib.Path(__file__).parent
W, H, GAP = 1400, 720, 8
NAVY = (10, 8, 55)

# (segundo do vídeo, centro do rosto no eixo x do frame 1920x1080, topo do recorte)
PEOPLE = [(45.0, 1255, 20), (120, 1140, 60)]

half = W // 2
crop_h = 960
crop_w = crop_h * half // H
canvas = Image.new("RGB", (W, H), NAVY)
with tempfile.TemporaryDirectory() as tmp:
    for i, (t, cx, top) in enumerate(PEOPLE):
        png = pathlib.Path(tmp) / f"{t}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", VIDEO, "-frames:v", "1", str(png)], check=True)
        im = Image.open(png).convert("RGB")
        im = ImageEnhance.Color(im).enhance(0.9)          # tira um pouco do roxo/ciano do estande
        left = min(max(cx - crop_w // 2, 0), 1920 - crop_w)
        part = im.crop((left, top, left + crop_w, top + crop_h)).resize((half, H), Image.LANCZOS)
        canvas.paste(part, (i * half, 0))
ImageDraw.Draw(canvas).rectangle([half - GAP // 2, 0, half + GAP // 2 - 1, H], fill=NAVY)

canvas.save(OUT / "capa-oji-papeis-sap-analytics-cloud.jpg", quality=90)
canvas.resize((700, 360), Image.LANCZOS).save(OUT / "_previa-700x360.jpg", quality=90)
print("ok capa-oji-papeis-sap-analytics-cloud.jpg")
