from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Cores Solveplan
AZUL_ESCURO = RGBColor(0x0A, 0x0E, 0x19)
AZUL_MARINHO = RGBColor(0x0A, 0x08, 0x37)
AZUL_VIVO = RGBColor(0x00, 0x6A, 0xFF)
VERDE_NEON = RGBColor(0x94, 0xFF, 0x96)
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)
CINZA_CLARO = RGBColor(0xCC, 0xCC, 0xCC)
AMARELO = RGBColor(0xFF, 0xD7, 0x00)

W = Inches(13.33)
H = Inches(7.5)

prs = Presentation()
prs.slide_width = W
prs.slide_height = H

blank_layout = prs.slide_layouts[6]


def add_slide():
    return prs.slides.add_slide(blank_layout)


def bg(slide, color=AZUL_ESCURO):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def txbox(slide, text, x, y, w, h, size=18, bold=False, color=BRANCO,
          align=PP_ALIGN.LEFT, wrap=True):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = "Montserrat"
    return tb


def rect(slide, x, y, w, h, color=AZUL_VIVO):
    shape = slide.shapes.add_shape(1, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def line(slide, x, y, w, color=AZUL_VIVO, thickness=Pt(1.5)):
    ln = slide.shapes.add_shape(1, x, y, w, Inches(0.02))
    ln.fill.solid()
    ln.fill.fore_color.rgb = color
    ln.line.fill.background()
    return ln


def section_header(slide, title):
    rect(slide, Inches(0.5), Inches(0.3), Inches(12.33), Inches(0.7), AZUL_VIVO)
    txbox(slide, title, Inches(0.7), Inches(0.35), Inches(12), Inches(0.6),
          size=22, bold=True, color=BRANCO, align=PP_ALIGN.LEFT)


def bullet_block(slide, items, x, y, w, size=16, color=BRANCO, spacing=0.42):
    for i, item in enumerate(items):
        txbox(slide, f"▸  {item}", x, y + Inches(i * spacing), w, Inches(0.45),
              size=size, color=color)


def kv_table(slide, rows, x, y, col_w1=Inches(3.5), col_w2=Inches(8)):
    for i, (k, v) in enumerate(rows):
        yy = y + Inches(i * 0.52)
        bg_c = AZUL_MARINHO if i % 2 == 0 else RGBColor(0x10, 0x14, 0x22)
        rect(slide, x, yy, col_w1 + col_w2, Inches(0.48), bg_c)
        txbox(slide, k, x + Inches(0.1), yy + Inches(0.04), col_w1, Inches(0.44),
              size=14, bold=True, color=AZUL_VIVO)
        txbox(slide, v, x + col_w1 + Inches(0.1), yy + Inches(0.04), col_w2, Inches(0.44),
              size=14, color=BRANCO)


def data_table(slide, headers, rows, x, y, col_widths, row_h=0.45):
    # header
    xx = x
    for i, h in enumerate(headers):
        rect(slide, xx, y, col_widths[i], Inches(0.48), AZUL_VIVO)
        txbox(slide, h, xx + Inches(0.05), y + Inches(0.04), col_widths[i], Inches(0.44),
              size=13, bold=True, color=BRANCO, align=PP_ALIGN.CENTER)
        xx += col_widths[i]
    # rows
    for ri, row in enumerate(rows):
        yy = y + Inches(0.48 + ri * row_h)
        bg_c = AZUL_MARINHO if ri % 2 == 0 else RGBColor(0x10, 0x14, 0x22)
        xx = x
        for ci, cell in enumerate(row):
            rect(slide, xx, yy, col_widths[ci], Inches(row_h), bg_c)
            txbox(slide, cell, xx + Inches(0.05), yy + Inches(0.04),
                  col_widths[ci], Inches(row_h),
                  size=12, color=BRANCO, align=PP_ALIGN.CENTER)
            xx += col_widths[ci]


# ─────────────────────────────────────────────
# SLIDE 1 — CAPA
# ─────────────────────────────────────────────
s = add_slide()
bg(s, AZUL_ESCURO)
rect(s, Inches(0), Inches(0), Inches(0.18), H, AZUL_VIVO)
rect(s, Inches(0), H - Inches(0.08), W, Inches(0.08), AZUL_VIVO)

txbox(s, "SAP NOW AI Tour Brazil 2026", Inches(0.6), Inches(1.2), Inches(12), Inches(1.2),
      size=42, bold=True, color=BRANCO, align=PP_ALIGN.LEFT)
txbox(s, "Planejamento Solveplan", Inches(0.6), Inches(2.4), Inches(10), Inches(0.7),
      size=26, bold=False, color=AZUL_VIVO, align=PP_ALIGN.LEFT)

line(s, Inches(0.6), Inches(3.2), Inches(6), AZUL_VIVO)

txbox(s, "9 e 10 de setembro de 2026", Inches(0.6), Inches(3.4), Inches(8), Inches(0.5),
      size=18, color=CINZA_CLARO)
txbox(s, "Transamérica Expo Center — São Paulo", Inches(0.6), Inches(3.9), Inches(8), Inches(0.5),
      size=18, color=CINZA_CLARO)
txbox(s, "Das 8h às 19h", Inches(0.6), Inches(4.4), Inches(8), Inches(0.5),
      size=18, color=CINZA_CLARO)

rect(s, Inches(0.6), Inches(5.4), Inches(5.5), Inches(0.7), AZUL_VIVO)
txbox(s, '"Seus dados existem — mas você ainda demora dias para fechar o mês."',
      Inches(0.7), Inches(5.45), Inches(5.3), Inches(0.65),
      size=13, bold=True, color=BRANCO, align=PP_ALIGN.LEFT)

txbox(s, "CONFIDENCIAL — USO INTERNO", Inches(9), Inches(6.9), Inches(4), Inches(0.4),
      size=10, color=RGBColor(0x66, 0x66, 0x66), align=PP_ALIGN.RIGHT)

# ─────────────────────────────────────────────
# SLIDE 2 — OBJETIVOS
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Objetivos")

objetivos = [
    "Geração de leads qualificados — meta: 130",
    "Geração de reuniões agendadas — meta: 28",
    "Posicionar Solveplan como referência em SAP Business Data Cloud (BDC)",
    "Fomentar relacionamento com clientes e expandir networking",
    "Gerar pipeline de novos negócios — meta: R$ 3.200.000",
]
bullet_block(s, objetivos, Inches(0.7), Inches(1.3), Inches(11.5), size=18)

line(s, Inches(0.7), Inches(5.2), Inches(11.5), VERDE_NEON)
txbox(s, '💡 Mensagem-chave: "Seus dados existem — mas você ainda demora dias para fechar o mês. Em 2026, isso é risco. A Solveplan resolve."',
      Inches(0.7), Inches(5.35), Inches(11.5), Inches(0.8),
      size=15, bold=True, color=VERDE_NEON)

# ─────────────────────────────────────────────
# SLIDE 3 — OVERVIEW
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Overview")

rows = [
    ("Solução", "SAP Business Data Cloud (BDC) — foco principal"),
    ("Objetivo", "Geração de demanda + conversão de leads (deals no pipe)"),
    ("Etapa do funil", "Meio e fundo"),
    ("Período", "Jun, Jul, Ago, Set 2026"),
    ("Target", "+R$500M faturamento / cross industry"),
    ("Persona", "CIO, CFO, Controller, Head de Dados/BI, COO"),
    ("Conversão", "Evento SAP NOW"),
]
kv_table(s, rows, Inches(0.7), Inches(1.2))

# ─────────────────────────────────────────────
# SLIDE 4 — DETALHES DO EVENTO
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Detalhes do Evento")

rows = [
    ("Datas", "9 e 10 de setembro de 2026"),
    ("Horário", "Das 8h às 19h"),
    ("Local", "Transamérica Expo Center — São Paulo"),
    ("Audiência total", "3.900 pessoas"),
    ("Clientes/Prospects", "2.700"),
    ("Decision Makers", "73%"),
    ("Patrocinadores", "70"),
    ("Cota Solveplan", "Gold"),
    ("Tema", "Bring it at SAP NOW AI Tour 2026"),
]
kv_table(s, rows, Inches(0.7), Inches(1.2), col_w1=Inches(3), col_w2=Inches(8.8))

# ─────────────────────────────────────────────
# SLIDE 5 — METAS E CRITÉRIO DE SUCESSO
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Metas e Critério de Sucesso")

headers = ["Métrica", "Meta 2026", "Ref. 2025"]
widths = [Inches(5.5), Inches(3), Inches(3)]
rows = [
    ("Leads totais", "130", "186"),
    ("Leads qualificados", "44", "—"),
    ("Reuniões agendadas", "28", "26"),
    ("Oportunidades abertas", "8", "—"),
    ("Pipeline gerado", "R$ 3.200.000", "—"),
    ("Empresas abordadas SDR", "120+", "72"),
    ("Agendas via SDR", "12", "5"),
    ("Custo por lead", "R$ 2.127", "—"),
    ("ROI esperado", "11,6x", "—"),
]
data_table(s, headers, rows, Inches(0.9), Inches(1.3), widths)

# ─────────────────────────────────────────────
# SLIDE 6 — STAFF
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Staff")

txbox(s, "Time confirmado: a definir com sócios  |  Ref. 2025: 9 pessoas (8 credenciais patrocinador + 1 staff)",
      Inches(0.7), Inches(1.15), Inches(12), Inches(0.4), size=14, color=CINZA_CLARO)

headers = ["#", "Nome", "Credencial", "Obs."]
widths = [Inches(0.6), Inches(4), Inches(3), Inches(4.5)]
rows = [
    ("1–8", "A definir", "Patrocinador", ""),
    ("9", "Fran", "Staff", "Organização geral"),
]
data_table(s, headers, rows, Inches(0.7), Inches(1.7), widths)

txbox(s, "Regras de credencial:", Inches(0.7), Inches(3.1), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
regras = [
    "Até 4 trocas/dia — proibido das 12h às 14h (exige documento)",
    "Retirada dia 08/set no CAEX (8h–18h) ou nos dias 09–10/set no credenciamento (8h–17h)",
    "Credencial pessoal e intransferível — nenhum profissional entra sem credencial visível",
]
bullet_block(s, regras, Inches(0.7), Inches(3.55), Inches(11.5), size=14)

txbox(s, "Escala por turno (preencher com nomes):",
      Inches(0.7), Inches(4.8), Inches(11), Inches(0.4), size=14, bold=True, color=AZUL_VIVO)
headers2 = ["#", "Montagem 08/set", "Dia 1 — Manhã", "Dia 1 — Tarde", "Dia 2 — Manhã", "Dia 2 — Tarde"]
widths2 = [Inches(0.6), Inches(2.2), Inches(2.1), Inches(2.1), Inches(2.1), Inches(2.1)]
rows2 = [("1–8", "A definir", "A definir", "A definir", "A definir", "A definir"),
         ("9 (Fran)", "—", "Fran", "—", "Fran", "—")]
data_table(s, headers2, rows2, Inches(0.7), Inches(5.2), widths2, row_h=0.4)

# ─────────────────────────────────────────────
# SLIDE 7 — ATIVAÇÃO DO ESTANDE — QUIZ BDC
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Ativação do Estande — Quiz BDC")

rect(s, Inches(0.7), Inches(1.2), Inches(5.8), Inches(1.0), AZUL_MARINHO)
txbox(s, "Totem interativo touchscreen 43\"",
      Inches(0.8), Inches(1.25), Inches(5.6), Inches(0.45), size=16, bold=True, color=AZUL_VIVO)
txbox(s, "Visitante descobre qual solução SAP resolve sua dor em ~3 min",
      Inches(0.8), Inches(1.65), Inches(5.6), Inches(0.45), size=13, color=BRANCO)

rect(s, Inches(7.0), Inches(1.2), Inches(5.8), Inches(1.0), AZUL_MARINHO)
txbox(s, "Fornecedor: Entretec  |  Ref. 2025 ✓",
      Inches(7.1), Inches(1.25), Inches(5.5), Inches(0.45), size=16, bold=True, color=VERDE_NEON)
txbox(s, "Investimento ref.: R$ 9.800 + frete R$ 500 + promotor R$ 450/dia",
      Inches(7.1), Inches(1.65), Inches(5.5), Inches(0.45), size=13, color=BRANCO)

txbox(s, "Dor × Solução (6 pares BDC 2026):", Inches(0.7), Inches(2.45),
      Inches(11), Inches(0.4), size=15, bold=True, color=AZUL_VIVO)

headers = ["Dor (vermelho)", "Solução (verde)"]
widths = [Inches(6), Inches(6.2)]
rows = [
    ("Fechamento manual demorado", "SAP BDC + Group Reporting"),
    ("Dados desconectados entre sistemas", "SAP Datasphere"),
    ("Falta de visibilidade em tempo real", "SAP Analytics Cloud"),
    ("Planejamento orçamentário no Excel", "SAP SAC Planning"),
    ("Integrações travando processos", "SAP BTP"),
    ("Gestão fiscal engessada", "SAP PaPM"),
]
data_table(s, headers, rows, Inches(0.7), Inches(2.85), widths, row_h=0.42)

# ─────────────────────────────────────────────
# SLIDE 8 — JORNADA DO VISITANTE
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Jornada do Visitante — Ativação Quiz")

steps = [
    ("1. Atração", "Totem com animações. Equipe aborda: 'Faz um quiz e descobre qual SAP resolve sua dor. Leva brinde!'"),
    ("2. Engajamento", "Visitante participa em menos de 3 min. Preenche: Nome, Cargo, Empresa, E-mail, WhatsApp."),
    ("3. Qualificação", "Quiz revela dor principal + solução SAP. Lead categorizado: Quente / Morno / Frio."),
    ("4. Brinde + Conversa", "Equipe entrega brinde e inicia conversa: 'Vi que você marcou [dor X]… posso mostrar como a Klabin resolveu isso?'"),
    ("5. Lead no CRM", "Dados capturados vão para HubSpot com tag SAP-NOW-2026 e classificação automática."),
    ("6. Follow-up Pós", "SDR contata em até 3 dias: 'Conforme seu quiz, acredito que podemos ajudar com [dor]. Agendamos?'"),
]

cols = 3
for i, (titulo, desc) in enumerate(steps):
    col = i % cols
    row = i // cols
    x = Inches(0.4 + col * 4.3)
    y = Inches(1.2 + row * 2.6)
    rect(s, x, y, Inches(4.1), Inches(2.4), AZUL_MARINHO)
    rect(s, x, y, Inches(4.1), Inches(0.45), AZUL_VIVO)
    txbox(s, titulo, x + Inches(0.1), y + Inches(0.05), Inches(3.9), Inches(0.4),
          size=14, bold=True, color=BRANCO)
    txbox(s, desc, x + Inches(0.1), y + Inches(0.5), Inches(3.9), Inches(1.8),
          size=12, color=CINZA_CLARO, wrap=True)

# ─────────────────────────────────────────────
# SLIDE 9 — BRINDES
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Brindes")

txbox(s, "Fornecedor referência: Unity Brindes (usado em 2025)",
      Inches(0.7), Inches(1.15), Inches(11), Inches(0.4), size=14, color=CINZA_CLARO)

headers = ["Item", "Qtd", "Valor unit.", "Total"]
widths = [Inches(6.5), Inches(1.5), Inches(2), Inches(2)]
rows = [
    ("Bloco A5 capa dura (silk screen 1 cor)", "500", "~R$ 15,59", "~R$ 7.795"),
    ("Caneta esferográfica alumínio (laser)", "500", "~R$ 5,37", "~R$ 2.685"),
    ("TOTAL", "", "", "~R$ 10.480"),
]
data_table(s, headers, rows, Inches(0.7), Inches(1.7), widths)

txbox(s, "Regras SAP para brindes:", Inches(0.7), Inches(3.5), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
regras = [
    "Devem ser sustentáveis — caneta + moleskine = aprovado pela SAP",
    "Aprovação SAP: enviar junto com ativações até 31/07/2026",
    "Entrega prevista: até 14/agosto",
]
bullet_block(s, regras, Inches(0.7), Inches(3.95), Inches(11.5), size=15)

# ─────────────────────────────────────────────
# SLIDE 10 — ESTANDE
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Estande")

txbox(s, "ATENÇÃO: Posição não-privilegiada — estratégia deve ser 100% de atração ativa",
      Inches(0.7), Inches(1.15), Inches(12), Inches(0.4), size=14, bold=True, color=AMARELO)

txbox(s, "Layout:", Inches(0.7), Inches(1.7), Inches(5), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
itens = [
    "Trainel (T1) — ~3,85m x 2,50m + TV 1,45x0,83m + balcão 0,50x1,00m + Selo SAP Gold Partner",
    "Painel (P1) — Logo Solveplan vertical + BDC em destaque",
    "Balcão (B1) — Identidade visual + logo da marca",
]
bullet_block(s, itens, Inches(0.7), Inches(2.15), Inches(6.2), size=14)

txbox(s, "Conceito visual 2026:", Inches(7.0), Inches(1.7), Inches(5.5), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
conceito = [
    "Foco em SAP Business Data Cloud",
    "Identidade Solveplan atualizada",
    "TV para vídeo looping",
    "Destaque: BDC | Datasphere | SAC | Group Reporting",
]
bullet_block(s, conceito, Inches(7.0), Inches(2.15), Inches(5.8), size=14)

line(s, Inches(0.7), Inches(4.0), Inches(11.5))

txbox(s, "Cronograma de produção:", Inches(0.7), Inches(4.2), Inches(7), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
headers = ["Etapa", "Prazo"]
widths = [Inches(6.5), Inches(4.5)]
rows = [
    ("Orçamento com agência", "Até 23/jun"),
    ("Arte final aprovada", "Até 11/jul"),
    ("Pagamento 1ª parcela (50%)", "10/jul"),
    ("Envio das artes exclusivas SAP", "11/jul"),
    ("Pagamento 2ª parcela (50%)", "Na entrega"),
]
data_table(s, headers, rows, Inches(0.7), Inches(4.65), widths, row_h=0.4)

# ─────────────────────────────────────────────
# SLIDE 11 — VESTIMENTA E EQUIPAMENTOS
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Vestimenta e Equipamentos")

txbox(s, "Vestimenta:", Inches(0.7), Inches(1.2), Inches(5), Inches(0.4),
      size=16, bold=True, color=AZUL_VIVO)
vest = [
    "Tech T-Shirt personalizada — 25 un.",
    "Valor unit. ref.: ~R$ 115  |  Total: ~R$ 2.875",
    "Entrega prevista: até 28/jul",
]
bullet_block(s, vest, Inches(0.7), Inches(1.65), Inches(5.5), size=14)

txbox(s, "Serviços CAEX:", Inches(0.7), Inches(3.0), Inches(5), Inches(0.4),
      size=16, bold=True, color=AZUL_VIVO)
headers = ["Item", "Qtd", "Total"]
widths = [Inches(4.5), Inches(1.2), Inches(2)]
rows = [
    ("Coletor de dados (por dia)", "2", "~R$ 1.100"),
    ("KVA energia (totem consume 2–3 KVAs)", "2", "~R$ 780"),
    ("Internet (pacote)", "—", "A definir"),
]
data_table(s, headers, rows, Inches(0.7), Inches(3.45), widths, row_h=0.42)

txbox(s, "Equipamentos:", Inches(7.0), Inches(1.2), Inches(5.5), Inches(0.4),
      size=16, bold=True, color=AZUL_VIVO)
equip = [
    "TV + suporte + cabos",
    "1 Tablet para demos",
    "2 Pens drive vídeo looping (TV)",
    "1 Pen drive backup demos",
    "2 Cabos HDMI + adaptador de rede",
    "Régua de energia / extensão",
    "Carregadores de celular",
    "Agenda das sessões impressa",
    "2 displays QR Code (~R$ 22 un.) + 1 reserva",
]
bullet_block(s, equip, Inches(7.0), Inches(1.65), Inches(5.8), size=13, spacing=0.38)

# ─────────────────────────────────────────────
# SLIDE 12 — CONTEÚDO DO EVENTO
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Conteúdo do Evento — Apresentação Principal")

info = [
    ("Tipo", "Caso de Sucesso — Customer Story"),
    ("Formato", "20 minutos | Auditório ~50 lugares | Sem Q&A"),
    ("Palestrante 1", "Executivo Klabin (CFO/CIO/Head de Dados — a confirmar)"),
    ("Palestrante 2", "Alexandre Kuntgen (Solveplan)"),
    ("Prazo submissão", "⚠️  26/06/2026 — NÃO PODE ATRASAR"),
]
kv_table(s, info, Inches(0.7), Inches(1.2), col_w1=Inches(2.8), col_w2=Inches(9.5))

txbox(s, "Estrutura da sessão (20 min):", Inches(0.7), Inches(3.45), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)

headers = ["Tempo", "Bloco", "Speaker"]
widths = [Inches(1.5), Inches(7.5), Inches(3.5)]
rows = [
    ("0–3 min", "O desafio: como era antes, a dor real de dados na Klabin", "Executivo Klabin"),
    ("3–8 min", "A decisão: por que SAP BDC, por que Solveplan", "Alexandre Kuntgen"),
    ("8–15 min", "O que mudou: antes × depois com números reais", "Executivo Klabin"),
    ("15–18 min", "O futuro: próximos passos com IA (alinha com tema do evento)", "Ambos"),
    ("18–20 min", "CTA: 'Venha ao nosso estande — estamos no slot [X]'", "Alexandre Kuntgen"),
]
data_table(s, headers, rows, Inches(0.7), Inches(3.9), widths, row_h=0.44)

# ─────────────────────────────────────────────
# SLIDE 13 — COMUNICAÇÃO
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Comunicação — Social Media & E-mail")

txbox(s, "Calendário de publicações (LinkedIn):", Inches(0.7), Inches(1.15), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)

headers = ["Data", "Publicação"]
widths = [Inches(1.8), Inches(10.0)]
rows = [
    ("21/jul", "Primeiro post — 'Estaremos no SAP NOW 2026'"),
    ("30/jul", "Post de expectativa / sessão com Klabin anunciada"),
    ("11/ago", "Post de contagem regressiva"),
    ("01/set", "'Em 8 dias estaremos lá'"),
    ("08/set", "'É amanhã!' — com localização do estande"),
    ("09/set", "Cobertura ao vivo — Dia 1"),
    ("10/set", "Cobertura ao vivo — Dia 2"),
    ("11/set", "Post pós-evento — highlights + agradecimento"),
]
data_table(s, headers, rows, Inches(0.7), Inches(1.6), widths, row_h=0.4)

txbox(s, "E-mails Marketing:", Inches(0.7), Inches(5.05), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
emails = [
    "Save the date → Base geral (Mai/Jun)",
    "Convite + link inscrição → Prospects e clientes (Jun/Jul)",
    "Lembrete sessão Klabin → Inscritos confirmados (Ago)",
    "'É amanhã!' → Inscritos confirmados (08/set)",
    "Agradecimento pós-evento → Todos os leads (D+1)",
]
bullet_block(s, emails, Inches(0.7), Inches(5.5), Inches(12), size=13, spacing=0.38)

# ─────────────────────────────────────────────
# SLIDE 14 — ANÚNCIOS
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Comunicação — Anúncios")

# Hotéis
rect(s, Inches(0.6), Inches(1.2), Inches(5.8), Inches(2.8), AZUL_MARINHO)
txbox(s, "1. Anúncios em Hotéis SP", Inches(0.7), Inches(1.3), Inches(5.5), Inches(0.5),
      size=17, bold=True, color=AZUL_VIVO)
h_info = [
    "Período: 8, 9 e 10 de setembro",
    "~28 faces/telas em hotéis da região",
    "Valor ref.: R$ 2.805 (2025)",
    "Aprovação: antes de 31/ago",
]
bullet_block(s, h_info, Inches(0.7), Inches(1.85), Inches(5.5), size=14, spacing=0.4)

# Geolocalização
rect(s, Inches(7.0), Inches(1.2), Inches(5.8), Inches(2.8), AZUL_MARINHO)
txbox(s, "2. Geolocalização no Evento", Inches(7.1), Inches(1.3), Inches(5.5), Inches(0.5),
      size=17, bold=True, color=AZUL_VIVO)
g_info = [
    "Google Ads + LinkedIn Ads",
    "Raio: 20km do Transamerica Expo Center",
    "Período: 8, 9 e 10 de setembro",
    "'Estamos no SAP NOW — venha ao estande Solveplan'",
    "Valor: a orçar",
]
bullet_block(s, g_info, Inches(7.1), Inches(1.85), Inches(5.5), size=14, spacing=0.4)

# UTMs
txbox(s, "UTMs Padrão:", Inches(0.7), Inches(4.2), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
headers = ["Canal", "UTM Source", "UTM Medium", "UTM Campaign"]
widths = [Inches(3.5), Inches(2.2), Inches(2.2), Inches(3.5)]
rows = [
    ("Organic Social", "linkedin", "organic", "sap-now-2026"),
    ("Paid Social", "linkedin", "cpc", "sap-now-2026"),
    ("E-mail Marketing", "email", "newsletter", "sap-now-2026"),
    ("Form inscrição SAP", "sap", "event", "sap-now-2026"),
]
data_table(s, headers, rows, Inches(0.7), Inches(4.65), widths, row_h=0.38)

# ─────────────────────────────────────────────
# SLIDE 15 — GERAÇÃO DE DEMANDA PRÉ-EVENTO
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Geração de Demanda Pré-evento — SDR")

kv_table(s, [
    ("Objetivo", "Preencher slots de diagnóstico BDC no estande antes do evento"),
    ("Meta", "120 empresas abordadas → 12 agendas confirmadas"),
    ("Início", "Junho 2026"),
    ("SDRs", "2 SDRs (nomes a definir)"),
], Inches(0.7), Inches(1.2), col_w1=Inches(2), col_w2=Inches(10.5))

txbox(s, "Processo:", Inches(0.7), Inches(3.0), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
processo = [
    "1. SDR identifica decisor (CIO/CFO/Head de Dados) nas empresas-alvo",
    "2. Abordagem por e-mail + LinkedIn + telefone",
    "3. Convite para slot de diagnóstico BDC no estande (15–20 min)",
    "4. Confirmar agenda + registrar no CRM com tag SAP-NOW-2026",
]
bullet_block(s, processo, Inches(0.7), Inches(3.45), Inches(11.5), size=15)

rect(s, Inches(0.7), Inches(5.3), Inches(12), Inches(0.9), AZUL_MARINHO)
txbox(s, '📞  Script SDR: "[Nome], estaremos no SAP NOW AI Tour em setembro com demo exclusiva de SAP BDC. Tenho um slot de 15 min reservado para você no estande da Solveplan — posso garantir o seu?"',
      Inches(0.8), Inches(5.35), Inches(11.8), Inches(0.85),
      size=14, bold=True, color=VERDE_NEON)

# ─────────────────────────────────────────────
# SLIDE 16 — CRONOGRAMA MACRO
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Cronograma Macro")

headers = ["Data", "Entrega", "Responsável"]
widths = [Inches(1.8), Inches(8.0), Inches(2.5)]
rows = [
    ("18/05", "Receber manual do patrocinador CAEX", "Fran"),
    ("Mai", "Lançar campanha 'Diagnóstico BDC Reservado'", "Fran"),
    ("10/06", "⚡ Alinhar com Klabin — speaker e tema", "Fran"),
    ("26/06", "⚠️  Submeter sessão de conteúdo para SAP", "Fran"),
    ("02/jun", "Liberação site e abertura de registros", "SAP"),
    ("Jun", "Início abordagem SDR (2 SDRs)", "SDRs"),
    ("31/07", "⚠️  Aprovação de ativações e brindes para SAP", "Fran"),
    ("14/ago", "Recebimento de brindes", "Fornecedor"),
    ("25/ago", "App do evento lança / publicar slots diagnóstico", "SAP / Fran"),
    ("Set/1", "Treinamento e kickoff do time", "Fran"),
    ("08/set", "Montagem do estande + entrega todos os itens", "Time"),
    ("09–10/set", "⭐  SAP NOW AI Tour Brazil 2026", "—"),
    ("10/set", "Download mailing + início follow-up", "SDRs + Fran"),
    ("16/set", "Relatório de resultados", "Fran"),
]
data_table(s, headers, rows, Inches(0.5), Inches(1.2), widths, row_h=0.37)

# ─────────────────────────────────────────────
# SLIDE 17 — ORÇAMENTO
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Orçamento Previsto")

headers = ["Item", "Valor previsto"]
widths = [Inches(9.0), Inches(3.5)]
rows = [
    ("Produção do estande (arte + layout)", "~R$ 3.700"),
    ("Quiz/Totem interativo (Entretec)", "~R$ 11.200"),
    ("Brindes (canetas + moleskine — 500 un.)", "~R$ 10.480"),
    ("Camisetas equipe (25 un.)", "~R$ 2.875"),
    ("Cartões de visita", "~R$ 3.700"),
    ("Coletores de dados CAEX (2 un.)", "~R$ 1.100"),
    ("KVA energia (2 un.)", "~R$ 780"),
    ("Anúncios hotéis SP", "~R$ 2.805"),
    ("Vídeo looping + depoimentos + teasers", "~R$ 5.280"),
    ("Anúncios geolocalização (Google + LinkedIn)", "A orçar"),
    ("Hotel equipe + Internet CAEX + Campanha pré-evento", "A definir"),
    ("Adicionais (displays, cabos, etc.)", "~R$ 500"),
    ("TOTAL DISPONÍVEL", "R$ 276.510,21"),
]
data_table(s, headers, rows, Inches(0.7), Inches(1.2), widths, row_h=0.41)

# ─────────────────────────────────────────────
# SLIDE 18 — CONVITE A CLIENTES
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Convite a Clientes C-Level")

rect(s, Inches(0.7), Inches(1.2), Inches(12), Inches(0.6), AZUL_MARINHO)
txbox(s, "Benefício Gold: convites ilimitados para clientes C-level do patrocinador",
      Inches(0.8), Inches(1.28), Inches(11.5), Inches(0.45), size=15, bold=True, color=VERDE_NEON)

txbox(s, "Critérios SAP:", Inches(0.7), Inches(2.0), Inches(5), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
criterios = [
    "C-level / Diretoria — preferencialmente em São Paulo",
    "Máximo 2 contatos por empresa/conta",
    "Todos passam por aprovação SAP antes da confirmação",
]
bullet_block(s, criterios, Inches(0.7), Inches(2.45), Inches(5.8), size=14)

txbox(s, "Processo:", Inches(7.0), Inches(2.0), Inches(5), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
processo = [
    "1. Enviar convite personalizado",
    "2. Participante se inscreve pelo link",
    "3. SAP analisa e confirma",
    "4. Participante recebe e-mail de confirmação",
]
bullet_block(s, processo, Inches(7.0), Inches(2.45), Inches(5.8), size=14)

txbox(s, "Lista estratégica — até 15 clientes (a definir com sócios até 10/ago):",
      Inches(0.7), Inches(4.1), Inches(12), Inches(0.4), size=14, bold=True, color=AZUL_VIVO)
headers = ["Empresa", "Contato", "Cargo", "Status"]
widths = [Inches(4.0), Inches(3.0), Inches(3.0), Inches(2.5)]
rows = [("A definir", "—", "—", "Pendente")] * 5
data_table(s, headers, rows, Inches(0.7), Inches(4.55), widths, row_h=0.4)

# ─────────────────────────────────────────────
# SLIDE 19 — VÍDEO STAND
# ─────────────────────────────────────────────
s = add_slide()
bg(s)
section_header(s, "Vídeo Stand (Looping) + Vídeos do Evento")

txbox(s, "Vídeo looping — TV do estande:", Inches(0.7), Inches(1.2), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
loop_items = [
    "Cortes de cases (Klabin, clientes BDC)",
    "Comerciais SAP BDC / ofertas de produtos",
    "Dashboards de BI ao vivo / demos visuais",
    "Aceleradores Solveplan",
    "Formato: MP4, 16:9, 1920x1080 — looping contínuo | 2 pens drive (principal + backup)",
]
bullet_block(s, loop_items, Inches(0.7), Inches(1.65), Inches(11.5), size=14)

txbox(s, "Prazo de entrega: até 25/ago  |  Produção: a contratar",
      Inches(0.7), Inches(3.3), Inches(11), Inches(0.4), size=13, color=CINZA_CLARO)

line(s, Inches(0.7), Inches(3.85), Inches(11.5))

txbox(s, "Vídeos durante o evento:", Inches(0.7), Inches(4.05), Inches(11), Inches(0.4),
      size=15, bold=True, color=AZUL_VIVO)
video_items = [
    "Shorts para redes sociais (9:16)",
    "Depoimentos curtos com clientes presentes",
    "Gravação de cases (confirmar disponibilidade)",
]
bullet_block(s, video_items, Inches(0.7), Inches(4.5), Inches(6.5), size=14)

kv_table(s, [
    ("Pacote 4 vídeos depoimento", "~R$ 3.680"),
    ("Vídeos teasers (4 un.)", "~R$ 1.600"),
    ("Edição adicional por vídeo", "~R$ 890/un."),
], Inches(7.0), Inches(4.5), col_w1=Inches(3.5), col_w2=Inches(2.5))

# ─────────────────────────────────────────────
# SLIDE 20 — ENCERRAMENTO / PRÓXIMOS PASSOS
# ─────────────────────────────────────────────
s = add_slide()
bg(s, AZUL_ESCURO)
rect(s, Inches(0), Inches(0), Inches(0.18), H, AZUL_VIVO)
rect(s, Inches(0), H - Inches(0.08), W, Inches(0.08), AZUL_VIVO)

txbox(s, "Próximos Passos Críticos", Inches(0.6), Inches(0.8), Inches(12), Inches(0.8),
      size=32, bold=True, color=BRANCO)
line(s, Inches(0.6), Inches(1.65), Inches(6), AZUL_VIVO)

headers = ["Prazo", "Ação", "Status"]
widths = [Inches(2.0), Inches(9.0), Inches(1.5)]
rows = [
    ("Hoje 18/05", "Ler manual CAEX — confirmar posição e regras do estande 2026", "⏳"),
    ("Mai", "Lançar campanha 'Diagnóstico BDC Reservado' (LinkedIn Ads)", "⏳"),
    ("10/06", "Alinhar com Klabin — speaker, cargo, tema da sessão", "⏳"),
    ("26/06", "⚠️  Submeter sessão de conteúdo para SAP (CRÍTICO)", "⏳"),
    ("31/07", "⚠️  Aprovação de ativações + brindes para SAP (CRÍTICO)", "⏳"),
]
data_table(s, headers, rows, Inches(0.6), Inches(1.9), widths, row_h=0.52)

txbox(s, "SAP NOW AI Tour Brazil 2026  |  9–10 Set  |  Transamérica Expo Center",
      Inches(0.6), Inches(6.3), Inches(12), Inches(0.5),
      size=13, color=RGBColor(0x66, 0x66, 0x66), align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
output = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\eventos\sap-now-2026\SAP-NOW-2026-Planejamento-Solveplan.pptx"
prs.save(output)
print(f"PPT salvo: {output}")
print(f"Total de slides: {len(prs.slides)}")
