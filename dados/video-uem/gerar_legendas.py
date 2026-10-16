"""Legendas dos cortes do case U&M: texto revisado à mão (a legenda automática do YouTube erra
Datasphere, Solveplan e U&M), com os tempos tirados do video.pt.vtt (tempo por palavra).

Gera, para cada corte em clips/:
  <corte>.srt               legenda para subir separada (LinkedIn, YouTube)
  <corte>.ass               mesma legenda com o estilo da tarja (usado para queimar no vídeo)
  <corte>-legendado.mp4     vídeo com a legenda queimada, no padrão do corte 1 da SSA

Uso: python gerar_legendas.py
"""
import pathlib, subprocess

BASE = pathlib.Path(__file__).parent / "clips"

# tempos em segundos, relativos ao início de cada corte
CUES = {
    "01-desafio-antes-datasphere": [
        (0.38, 1.95, "Antes de implementar o Datasphere,"),
        (1.98, 3.90, "nós tínhamos um desafio muito grande"),
        (3.93, 7.60, "para disponibilizar dados para as áreas de negócio."),
        (8.46, 11.47, "Às vezes dependia muito de customizações,"),
        (11.50, 13.87, "retirada manual de relatórios."),
        (13.90, 16.75, "Então a gente tinha um cenário realmente desafiador"),
        (16.78, 19.27, "e era muito demorada a disponibilização"),
        (19.30, 20.20, "dessas informações."),
    ],
    "02-implementacao-parceria-solveplan": [
        (0.38, 3.63, "A implementação foi rápida."),
        (3.66, 5.60, "Eu acredito que em torno de dois meses"),
        (5.63, 7.80, "a gente já estava com a plataforma pronta"),
        (7.83, 10.63, "e construindo os relatórios,"),
        (10.66, 12.83, "as informações que a gente precisava."),
        (12.86, 15.00, "O ponto-chave foi a agilidade"),
        (15.03, 18.19, "de ter a plataforma já disponibilizada"),
        (18.22, 20.43, "e já começar a fazer a conversão"),
        (20.46, 23.91, "dos ETLs antigos para esse modelo novo,"),
        (23.94, 25.19, "que é o que a gente precisava:"),
        (25.22, 29.59, "uma ferramenta mais em compliance com a SAP."),
        (29.62, 32.50, "A Solveplan foi muito parceira"),
        (32.53, 34.55, "nossa no dia a dia."),
        (34.58, 35.95, "Eles têm uma agilidade muito grande"),
        (35.98, 37.11, "no atendimento"),
        (37.14, 39.47, "e o entendimento de todo o ecossistema,"),
        (39.50, 42.15, "que facilitou muito o trabalho no dia a dia."),
        (42.18, 43.87, "Eles foram sempre muito solícitos,"),
        (43.90, 45.91, "parceiros"),
        (45.94, 47.50, "e sempre entregando muita agilidade pra gente."),
    ],
    "03-resultado-dados-tempo-real": [
        (0.05, 1.90, "O grande benefício que a gente tem"),
        (1.93, 3.54, "hoje é ter os dados"),
        (3.57, 5.26, "praticamente em tempo real."),
        (5.29, 8.26, "Isso facilita muito a tomada de decisão"),
        (8.29, 10.46, "das áreas da empresa como um todo."),
        (10.49, 11.82, "A gente disponibiliza os dados"),
        (11.85, 13.30, "para algumas áreas específicas,"),
        (13.33, 15.14, "mas também de forma corporativa,"),
        (15.17, 17.38, "e consegue agregar também"),
        (17.41, 18.78, "dados de outros sistemas"),
        (18.81, 22.50, "para fornecer essas informações"),
        (22.53, 24.22, "para a tomada de decisão na empresa."),
        (24.25, 26.10, "Acho que o principal fator transformador"),
        (26.13, 28.42, "foi ter uma base de dados centralizada,"),
        (28.45, 30.40, "confiável, com governança,"),
        (30.43, 32.02, "e automaticamente"),
        (32.05, 34.54, "dando subsídios para as áreas tomarem"),
        (34.57, 36.30, "decisões de uma forma muito mais segura."),
    ],
    "04-conselho-governanca": [
        (0.18, 3.59, "Eu acho que o principal objetivo"),
        (3.62, 5.83, "é as empresas começarem de uma forma"),
        (5.86, 7.63, "organizada, com governança,"),
        (7.66, 9.91, "entenderem o benefício que isso"),
        (9.94, 11.83, "vai estar trazendo para elas"),
        (11.86, 14.03, "no curto prazo,"),
        (14.06, 16.35, "porque vão ter informações"),
        (16.38, 17.83, "mais confiáveis,"),
        (17.86, 20.11, "e que vão apoiar a tomada de decisão"),
        (20.14, 21.40, "final de cada área de negócio."),
    ],
}

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Tarja,Segoe UI Semibold,58,&H00FFFFFF,&H00FFFFFF,&H40000000,&H40000000,0,0,0,0,100,100,0,0,3,16,0,2,60,60,62,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def srt_ts(x):
    ms = int(round(x * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def ass_ts(x):
    cs = int(round(x * 100)); return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


for name, cues in CUES.items():
    (BASE / f"{name}.srt").write_text(
        "\n".join(f"{i}\n{srt_ts(a)} --> {srt_ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(cues, 1)), encoding="utf-8")
    (BASE / f"{name}.ass").write_text(
        ASS_HEAD + "".join(f"Dialogue: 0,{ass_ts(a)},{ass_ts(b)},Tarja,,0,0,0,,{t}\n" for a, b, t in cues), encoding="utf-8")
    # caminho do .ass relativo (o filtro do ffmpeg não lida bem com "C:" e espaços)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{name}.mp4",
                    "-vf", f"ass={name}.ass:fontsdir=C\\\\:/Windows/Fonts",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
                    "-c:a", "copy", "-movflags", "+faststart", f"{name}-legendado.mp4"], cwd=BASE, check=True)
    print("ok", name)
