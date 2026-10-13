"""Gera os 3 ícones dos cards do case Aço Cearense no mesmo estilo dos ícones da SSA
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


def save(im, name):
    im.resize((432, 432), Image.LANCZOS).save(OUT / name)
    print("ok", name)


# 1. Integração: três sistemas conectados (SAC + IBP + S/4HANA)
im = base(); d = ImageDraw.Draw(im)
nodes = [(216, 112), (116, 300), (316, 300)]
for i in range(3):
    for j in range(i + 1, 3):
        d.line(k(*nodes[i], *nodes[j]), fill=WHITE, width=SW)
for x, y in nodes:
    d.ellipse(k(x - 52, y - 52, x + 52, y + 52), fill=(8, 8, 70, 255), outline=WHITE, width=SW)
save(im, "aco-icone-integracao.png")

# 2. Escopo: camadas empilhadas (várias dimensões no mesmo modelo)
im = base(); d = ImageDraw.Draw(im)
r = SW // 2

def poly(pts, closed=False):
    pts = [(x * S, y * S) for x, y in pts]
    d.line(pts + ([pts[0], pts[1]] if closed else []), fill=WHITE, width=SW, joint="curve")
    for x, y in pts:  # pontas e vértices arredondados
        d.ellipse([x - r, y - r, x + r, y + r], fill=WHITE)

poly([(216, 96), (346, 166), (216, 236), (86, 166)], closed=True)   # camada de cima
poly([(86, 236), (216, 306), (346, 236)])                            # 2ª camada
poly([(86, 306), (216, 376), (346, 306)])                            # 3ª camada
save(im, "aco-icone-escopo.png")

# 3. Áreas: organograma (responsabilidades definidas por área)
im = base(); d = ImageDraw.Draw(im)
d.rounded_rectangle(k(166, 86, 266, 166), radius=14 * S, outline=WHITE, width=SW)
h = 13  # meia espessura do traço
d.rectangle(k(216 - h, 166, 216 + h, 216), fill=WHITE)
d.rectangle(k(116 - h, 216 - h, 316 + h, 216 + h), fill=WHITE)
for cx in (116, 216, 316):
    d.rectangle(k(cx - h, 216, cx + h, 266), fill=WHITE)
    d.rounded_rectangle(k(cx - 44, 266, cx + 44, 346), radius=12 * S, outline=WHITE, width=SW)
save(im, "aco-icone-areas.png")
