"""Gera os 3 ícones dos cards do case Oji Papéis no mesmo estilo dos cases SSA e Aço Cearense
(quadrado arredondado com degradê navy → azul e traço branco), 432x432 px."""
import pathlib
from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).parent
S = 4                     # supersampling
W = 432 * S
SW = 26 * S               # espessura do traço
WHITE = (255, 255, 255, 255)


def base():
    grad = Image.new("RGBA", (W, W))
    px = grad.load()
    a, b = (12, 16, 32), (2, 0, 110)
    for x in range(W):
        t = x / (W - 1)
        c = tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3)) + (255,)
        for y in range(W):
            px[x, y] = c
    mask = Image.new("L", (W, W), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, W - 1, W - 1], radius=70 * S, fill=255)
    im = Image.new("RGBA", (W, W), WHITE)
    im.paste(grad, (0, 0), mask)
    return im


def k(*v):
    return [n * S for n in v]


def dot(d, x, y, r=SW // 2):
    d.ellipse([x * S - r, y * S - r, x * S + r, y * S + r], fill=WHITE)


def save(im, name):
    im.resize((432, 432), Image.LANCZOS).save(OUT / name)
    print("ok", name)


# 1. Agilidade: relógio (ciclo de 15 para 2 dias)
im = base(); d = ImageDraw.Draw(im)
d.ellipse(k(96, 96, 336, 336), outline=WHITE, width=SW)
d.line(k(216, 216, 216, 146), fill=WHITE, width=SW)
d.line(k(216, 216, 268, 248), fill=WHITE, width=SW)
for x, y in [(216, 216), (216, 146), (268, 248)]:
    dot(d, x, y)
save(im, "oji-icone-agilidade.png")

# 2. Projeto: calendário (seis meses de implementação)
im = base(); d = ImageDraw.Draw(im)
d.rounded_rectangle(k(96, 116, 336, 336), radius=22 * S, outline=WHITE, width=SW)
d.line(k(96, 176, 336, 176), fill=WHITE, width=SW)
for x in (156, 276):
    d.line(k(x, 86, x, 120), fill=WHITE, width=SW)
    dot(d, x, 86)
for x in (156, 216, 276):
    for y in (226, 286):
        d.ellipse(k(x - 14, y - 14, x + 14, y + 14), fill=WHITE)
save(im, "oji-icone-projeto.png")

# 3. Centralização: banco de dados (informações em um único ambiente)
im = base(); d = ImageDraw.Draw(im)
L, R, RY, h = 116, 316, 34, 13   # bordas, raio vertical das elipses, meia espessura do traço
d.ellipse(k(L - h, 116 - RY - h, R + h, 116 + RY + h), outline=WHITE, width=SW)   # tampa
for y in (216, 316):                                                             # cintas
    d.arc(k(L - h, y - RY - h, R + h, y + RY + h), 0, 180, fill=WHITE, width=SW)
for x in (L, R):                                                                 # laterais
    d.line(k(x, 116, x, 316), fill=WHITE, width=SW)
save(im, "oji-icone-centralizacao.png")
