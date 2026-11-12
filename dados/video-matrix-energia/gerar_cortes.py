"""Cortes do case Matrix Energia (YouTube 0y47YGHZ5gQ).

Texto das legendas revisado à mão (a legenda automática erra Solveplan, SAP, "três", "assíduo"),
tempos tirados do video.pt.vtt (tempo por palavra, ver palavras.json). Tempos em segundos ABSOLUTOS
do vídeo original; o script converte para relativo ao início de cada corte.

Gera em clips/:
  <corte>.mp4               corte sem legenda
  <corte>.srt               legenda para subir separada (LinkedIn, YouTube)
  <corte>.ass               legenda com o estilo da tarja (queimada no vídeo)
  <corte>-legendado.mp4     corte com a legenda queimada (mesmo padrão dos cortes SSA/U&M)

Uso: python gerar_cortes.py
"""
import pathlib, subprocess

BASE = pathlib.Path(__file__).parent
CLIPS = BASE / "clips"
CLIPS.mkdir(exist_ok=True)

CORTES = {
    "01-desafio-70-cnpjs-intercompany": (49.5, 109.0, [
        (49.84, "A parte de consolidação dos números da empresa"),
        (52.72, "é onde apresentava bastante dificuldade,"),
        (55.40, "principalmente em relação ao prazo de fechamento."),
        (57.88, "É aí que entraram as ferramentas da SAP,"),
        (61.04, "que nos ajudaram a encurtar esse prazo de fechamento."),
        (63.16, "O processo de implementação foi em três meses,"),
        (66.24, "o que foi um sucesso aqui pra gente."),
        (68.12, "O processo apresentou alguns desafios."),
        (70.64, "Primeiro, o plano de contas."),
        (71.64, "A Matrix tem várias empresas, vários CNPJs."),
        (75.16, "Na época da implementação, eram mais de 70 CNPJs."),
        (78.92, "Conseguimos criar um código para cada plano de contas,"),
        (82.36, "superando esse desafio."),
        (84.36, "Outro desafio foram as regras de eliminação intercompany."),
        (87.64, "Não utilizávamos sociedade parceira,"),
        (90.36, "então tivemos que criar regras mais detalhadas"),
        (93.44, "para cada intercompany."),
        (94.64, "Esse desafio também foi superado."),
        (97.00, "E no meio de todo esse processo, aqui na Matrix,"),
        (101.36, "estamos passando por uma migração de bases"),
        (103.92, "pelo Business One."),
        (105.36, "E conseguimos fazer esse go-live em três meses."),
    ]),
    "02-parceria-solveplan": (149.6, 189.0, [
        (149.92, "A Solveplan foi muito boa."),
        (151.76, "Digo que foi excelente,"),
        (153.44, "desde a construção do cronograma."),
        (156.12, "O cronograma foi bem detalhado,"),
        (157.88, "tínhamos reuniões mensais"),
        (160.32, "que contribuíram para não ter nenhum tipo de atraso."),
        (163.16, "O especialista que ficou aqui comigo na implantação"),
        (168.44, "era muito assíduo, muito pontual."),
        (171.08, "Tinha muito conhecimento,"),
        (173.64, "já parecia ser muito experiente."),
        (175.56, "Além disso, ele é contador,"),
        (177.36, "o que facilitou muito nas normas contábeis"),
        (180.08, "e em entender as minhas dores."),
        (181.84, "Uma parceria do começo ao fim."),
        (185.40, "Não tenho nada a dizer."),
        (186.80, "Foi realmente um casamento que deu muito certo."),
    ]),
    "03-resultado-fechamento-22-para-11-dias": (189.0, 253.6, [
        (189.16, "Os benefícios que as ferramentas da SAP nos trouxeram:"),
        (193.64, "o primeiro é a questão da confiança."),
        (196.08, "Antes, toda a consolidação era feita em Excel."),
        (199.44, "E como a gente diz no mercado,"),
        (200.76, "Excel aceita qualquer coisa, inclusive erros."),
        (204.24, "O segundo ponto é a agilidade."),
        (207.08, "A elaboração do número levava um prazo muito extenso."),
        (210.48, "Hoje a gente consegue fazer isso"),
        (211.76, "de maneira muito mais ágil e eficiente"),
        (214.56, "do que fazíamos antes."),
        (216.04, "A consolidação agora é em poucos minutos."),
        (220.56, "Temos seis consolidações intermediárias,"),
        (223.12, "então o processo está muito mais rápido."),
        (225.80, "Temos também o orçado x realizado,"),
        (228.20, "o outro fechamento que a gente tem aqui na Matrix."),
        (230.64, "O SAC está ajudando também nesse processo"),
        (234.24, "de fechamento com o orçamento da empresa."),
        (237.44, "Até um ano atrás, fechávamos os números"),
        (240.20, "da companhia no 22º dia útil."),
        (243.20, "Hoje estamos fechando com segurança no 11º dia útil."),
        (247.04, "Com a implementação da ferramenta,"),
        (249.80, "tiramos 10 dias úteis do closing da companhia."),
    ]),
}

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
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


for name, (ini, fim, linhas) in CORTES.items():
    # corte com reencode (corte exato no frame, não só em keyframe)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{ini}", "-to", f"{fim}", "-i", "video.mp4",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", "-af", "afade=t=in:d=0.15,afade=t=out:st=%.2f:d=0.3" % (fim - ini - 0.3),
                    "-movflags", "+faststart", f"clips/{name}.mp4"], cwd=BASE, check=True)

    cues = []
    for i, (t, txt) in enumerate(linhas):
        fim_cue = (linhas[i + 1][0] - 0.03) if i + 1 < len(linhas) else fim - 0.1
        cues.append((t - ini, fim_cue - ini, txt))

    (CLIPS / f"{name}.srt").write_text(
        "\n".join(f"{i}\n{srt_ts(a)} --> {srt_ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(cues, 1)), encoding="utf-8")
    (CLIPS / f"{name}.ass").write_text(
        ASS_HEAD + "".join(f"Dialogue: 0,{ass_ts(a)},{ass_ts(b)},Tarja,,0,0,0,,{t}\n" for a, b, t in cues), encoding="utf-8")
    # caminho do .ass relativo (o filtro do ffmpeg não lida bem com "C:" e espaços)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{name}.mp4",
                    "-vf", f"ass={name}.ass:fontsdir=C\\\\:/Windows/Fonts",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
                    "-c:a", "copy", "-movflags", "+faststart", f"{name}-legendado.mp4"], cwd=CLIPS, check=True)
    print("ok", name, f"{fim - ini:.1f}s")
