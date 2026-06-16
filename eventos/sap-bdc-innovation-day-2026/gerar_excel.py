import xlsxwriter

OUTPUT = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\eventos\sap-bdc-innovation-day-2026\SAP_BDC_Innovation_Day_2026_Checklist.xlsx"

wb = xlsxwriter.Workbook(OUTPUT)

# ── Cores ──────────────────────────────────────────────
AZUL      = "#002F6C"
AMARELO   = "#F5A800"
BRANCO    = "#FFFFFF"
CZ_CLARO  = "#F4F4F4"
AZ_CLARO  = "#E8F0FE"

# status
PEND_BG   = "#FFCCCC";  PEND_FG  = "#8B0000"
AND_BG    = "#FFF3CC";  AND_FG   = "#7B5800"
OK_BG     = "#CCFFCC";  OK_FG    = "#1A5C2A"

# ── Formatos base ───────────────────────────────────────
def fmt(d): return wb.add_format(d)

F = {
    "header_azul":  fmt({"bold":True,"font_color":BRANCO,"bg_color":AZUL,   "font_size":14,"align":"center","valign":"vcenter","border":0}),
    "header_amar":  fmt({"bold":True,"font_color":AZUL,  "bg_color":AMARELO,"font_size":11,"align":"center","valign":"vcenter","border":0}),
    "col_header":   fmt({"bold":True,"font_color":BRANCO,"bg_color":AZUL,   "font_size":11,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "section":      fmt({"bold":True,"font_color":AZUL,  "bg_color":AMARELO,"font_size":11,"align":"left",  "valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "cell_w":       fmt({"font_color":"#444444","bg_color":BRANCO,   "font_size":10,"align":"left",  "valign":"vcenter","border":1,"border_color":"#CCCCCC","text_wrap":True}),
    "cell_cz":      fmt({"font_color":"#444444","bg_color":CZ_CLARO, "font_size":10,"align":"left",  "valign":"vcenter","border":1,"border_color":"#CCCCCC","text_wrap":True}),
    "cell_ctr_w":   fmt({"font_color":"#444444","bg_color":BRANCO,   "font_size":10,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "cell_ctr_cz":  fmt({"font_color":"#444444","bg_color":CZ_CLARO, "font_size":10,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "check_w":      fmt({"font_color":"#444444","bg_color":BRANCO,   "font_size":12,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "check_cz":     fmt({"font_color":"#444444","bg_color":CZ_CLARO, "font_size":12,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "status_w":     fmt({"bold":True,"font_size":10,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC","bg_color":BRANCO}),
    "status_cz":    fmt({"bold":True,"font_size":10,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC","bg_color":CZ_CLARO}),
    "total":        fmt({"bold":True,"font_color":AMARELO,"bg_color":AZUL,"font_size":11,"align":"center","valign":"vcenter","border":1}),
    "total_lbl":    fmt({"bold":True,"font_color":BRANCO, "bg_color":AZUL,"font_size":11,"align":"left",  "valign":"vcenter","border":1}),
    "nota":         fmt({"italic":True,"font_color":"#888888","font_size":9,"align":"left","valign":"vcenter","border":0,"text_wrap":True}),
    "kpi_lbl":      fmt({"bold":True,"font_color":AZUL,"font_size":10,"align":"left","valign":"vcenter","border":0}),
    "kpi_val":      fmt({"font_color":"#444444","font_size":10,"align":"center","valign":"vcenter","border":0}),
    "apren_lbl":    fmt({"bold":True,"font_color":AZUL,"font_size":10,"align":"left","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "apren_val":    fmt({"font_color":"#444444","font_size":10,"align":"left","valign":"vcenter","border":1,"border_color":"#CCCCCC","bg_color":CZ_CLARO,"text_wrap":True}),
    "meta_base":    fmt({"font_color":"#666666","font_size":10,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "meta_alvo":    fmt({"bold":True,"font_color":AZUL,"font_size":10,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC","bg_color":AZ_CLARO}),
    "meta_real":    fmt({"font_color":"#444444","font_size":10,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    "meta_lbl":     fmt({"bold":True,"font_color":AZUL,"font_size":10,"align":"left","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
}

def add_cond_status(ws, first_row, last_row, col):
    """Conditional formatting para a coluna de status."""
    rng = xlsxwriter.utility.xl_range(first_row, col, last_row, col)
    ref = xlsxwriter.utility.xl_rowcol_to_cell(first_row, col, row_abs=False, col_abs=True)

    ws.conditional_format(rng, {
        "type": "formula",
        "criteria": f'={ref}="Pendente"',
        "format": wb.add_format({"bold":True,"font_color":PEND_FG,"bg_color":PEND_BG,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    })
    ws.conditional_format(rng, {
        "type": "formula",
        "criteria": f'={ref}="Em andamento"',
        "format": wb.add_format({"bold":True,"font_color":AND_FG,"bg_color":AND_BG,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    })
    ws.conditional_format(rng, {
        "type": "formula",
        "criteria": f'={ref}="OK"',
        "format": wb.add_format({"bold":True,"font_color":OK_FG,"bg_color":OK_BG,"align":"center","valign":"vcenter","border":1,"border_color":"#CCCCCC"}),
    })
    ws.data_validation(rng, {
        "validate": "list",
        "source": ["Pendente", "Em andamento", "OK"],
        "input_title": "Status",
        "input_message": "Escolha o status da atividade",
    })

# ══════════════════════════════════════════════════════════
# ABA 1 — CHECKLIST GERAL
# ══════════════════════════════════════════════════════════
ws1 = wb.add_worksheet("Checklist Geral")
ws1.set_column(0, 0, 4)    # A  ✓
ws1.set_column(1, 1, 42)   # B  Atividade
ws1.set_column(2, 2, 20)   # C  Responsável
ws1.set_column(3, 3, 16)   # D  Prazo
ws1.set_column(4, 4, 16)   # E  Status
ws1.set_column(5, 5, 28)   # F  Observações
ws1.set_zoom(90)

ws1.merge_range("A1:F1", "SAP BDC Innovation Day 2026 — Checklist Geral", F["header_azul"])
ws1.set_row(0, 30)
ws1.merge_range("A2:F2", "26 de agosto de 2026  |  SAP Brasil, São Paulo  |  08:30 às 12h", F["header_amar"])
ws1.set_row(1, 20)

r = 3  # row index (0-based)
ws1.write(r, 0, "✓",           F["col_header"])
ws1.write(r, 1, "Atividade",   F["col_header"])
ws1.write(r, 2, "Responsável", F["col_header"])
ws1.write(r, 3, "Prazo",       F["col_header"])
ws1.write(r, 4, "Status",      F["col_header"])
ws1.write(r, 5, "Observações", F["col_header"])
ws1.set_row(r, 20)
r += 1

STATUS_FIRST_ROW = r  # guarda início para conditional formatting

def section(ws, row, title):
    ws.merge_range(row, 0, row, 5, title, F["section"])
    ws.set_row(row, 18)
    return row + 1

def item_row(ws, row, ativ, resp="", prazo="", status="Pendente", obs=""):
    z = row % 2 == 0
    fc = F["check_cz"]  if z else F["check_w"]
    fa = F["cell_cz"]   if z else F["cell_w"]
    fc2= F["cell_ctr_cz"] if z else F["cell_ctr_w"]
    fs = F["status_cz"] if z else F["status_w"]
    ws.write(row, 0, "☐",    fc)
    ws.write(row, 1, ativ,   fa)
    ws.write(row, 2, resp,   fc2)
    ws.write(row, 3, prazo,  fc2)
    ws.write(row, 4, status, fs)
    ws.write(row, 5, obs,    fa)
    ws.set_row(row, 18)
    return row + 1

# ── PLANEJAMENTO ────────────────────────────────────────
r = section(ws1, r, "📋  PLANEJAMENTO E DEFINIÇÕES")
for ativ, resp, prazo in [
    ("Confirmar reserva do Auditório MASP — SAP Brasil",                 "Fran",           "20/06/2026"),
    ("Definir nome definitivo do evento",                                "Fran",           "20/06/2026"),
    ("Confirmar case de sucesso com cliente (VALE / Klabin / Aegea)",    "Fran / Sócios",  "30/06/2026"),
    ("Confirmar speakers e apresentadores internos",                     "Sócios",         "30/06/2026"),
    ("Confirmar presença do time (Sócios + Fran)",                       "Fran",           "30/06/2026"),
    ("Confirmar participação de especialistas SAP para demo",            "Fran",           "30/06/2026"),
    ("Montar lista de convidados (clientes + prospects)",                "Fran",           "15/07/2026"),
    ("Segmentar lista por perfil (MQL, prospect, cliente ativo)",        "Fran",           "15/07/2026"),
]:
    r = item_row(ws1, r, ativ, resp, prazo)

# ── PRODUÇÃO ────────────────────────────────────────────
r = section(ws1, r, "🎨  PRODUÇÃO DE MATERIAIS")
for ativ, resp, prazo in [
    ("Criar landing page / formulário de inscrição",                     "Fran / Design",  "14/07/2026"),
    ("Produzir card WhatsApp do evento",                                 "Fran / Design",  "14/07/2026"),
    ("Redigir e-mail 01 — 1º convite",                                   "Fran",           "18/07/2026"),
    ("Redigir e-mail 02 — 2º convite",                                   "Fran",           "25/07/2026"),
    ("Redigir e-mail 03 — 3º convite",                                   "Fran",           "01/08/2026"),
    ("Redigir e-mail 04 — 4º convite",                                   "Fran",           "08/08/2026"),
    ("Redigir e-mail 05 — RSVP / últimas vagas",                         "Fran",           "15/08/2026"),
    ("Redigir lembrete D-2",                                             "Fran",           "22/08/2026"),
    ("Redigir e-mail de agradecimento pós-evento",                       "Fran",           "25/08/2026"),
    ("Criar anúncios LinkedIn — formato 1200x1200 (mín. 4 versões)",    "Fran / Design",  "18/07/2026"),
    ("Criar anúncios LinkedIn — formato 1200x627 (mín. 4 versões)",     "Fran / Design",  "18/07/2026"),
    ("Preparar apresentação abertura + BDC",                             "Sócios",         "18/08/2026"),
    ("Preparar slides do case de sucesso",                               "Cliente + SP",   "01/08/2026"),
    ("Criar QR Code da pesquisa de satisfação (Qualtrics)",              "Fran",           "20/08/2026"),
    ("Produzir posts pré-evento (LinkedIn + Instagram)",                 "Fran / Design",  "18/07/2026"),
    ("Produzir posts pós-evento",                                        "Fran / Design",  "25/08/2026"),
    ("Preparar lista de presença (digital + impressa backup)",           "Fran",           "22/08/2026"),
]:
    r = item_row(ws1, r, ativ, resp, prazo)

# ── DIVULGAÇÃO ──────────────────────────────────────────
r = section(ws1, r, "📢  DIVULGAÇÃO")
for ativ, resp, prazo in [
    ("Disparar E-mail 01 — 1º convite",                   "Fran", "21/07/2026"),
    ("Ativar LinkedIn Ads — campanha de convite",          "Fran", "21/07/2026"),
    ("Publicar post pré-evento LinkedIn",                  "Fran", "21/07/2026"),
    ("Disparar E-mail 02 — 2º convite",                   "Fran", "28/07/2026"),
    ("Disparar E-mail 03 — 3º convite",                   "Fran", "04/08/2026"),
    ("Disparo WhatsApp para base qualificada",             "Fran", "30/07–04/08"),
    ("Disparar E-mail 04 — 4º convite",                   "Fran", "11/08/2026"),
    ("Período RSVP — confirmação de presença",             "Fran", "11/08–22/08"),
    ("Disparar E-mail 05 — RSVP / últimas vagas",         "Fran", "18/08/2026"),
    ("Publicar post de contagem regressiva",               "Fran", "20/08/2026"),
    ("Disparar lembrete D-2",                             "Fran", "24/08/2026"),
]:
    r = item_row(ws1, r, ativ, resp, prazo)

# ── LOGÍSTICA ───────────────────────────────────────────
r = section(ws1, r, "🏢  LOGÍSTICA E ESTRUTURA")
for ativ, resp, prazo in [
    ("Contratar coffee break para 70 pax (~R$ 4.400,00)",             "Fran",           "30/06/2026"),
    ("Comprar brindes — Moleskine e Caneta (70 unidades)",            "Fran",           "15/07/2026"),
    ("Confirmar camisetas Insider para o time",                       "Fran",           "01/08/2026"),
    ("Reservar equipamento — projetor, áudio, tela",                 "SAP Brasil/Fran","01/08/2026"),
    ("Confirmar acesso à internet no auditório",                      "SAP Brasil/Fran","01/08/2026"),
    ("Verificar disponibilidade sala Experience para demo",           "Fran",           "01/07/2026"),
    ("Visita técnica ao espaço",                                     "Fran",           "19/08/2026"),
    ("Montar plano de contingência (speaker, internet, coffee)",      "Fran",           "19/08/2026"),
]:
    r = item_row(ws1, r, ativ, resp, prazo)

# ── DIA DO EVENTO ───────────────────────────────────────
r = section(ws1, r, "📅  DIA DO EVENTO — 26/08/2026")
for ativ, resp, prazo in [
    ("Chegada 1h antes para montagem e setup",                        "Fran + Sócios",  "26/08 — 07:30"),
    ("Testar projetor, áudio e internet",                             "Fran",           "26/08 — 07:45"),
    ("Validar QR Code da pesquisa de satisfação",                     "Fran",           "26/08 — 07:50"),
    ("Confirmar brindes disponíveis na recepção",                     "Fran",           "26/08 — 08:00"),
    ("Confirmar lista de presença impressa (backup)",                 "Fran",           "26/08 — 08:00"),
    ("Definir quem faz credenciamento",                               "Fran",           "26/08 — 08:00"),
    ("Executar coffee break (08:30–09:00)",                           "Fran+fornecedor","26/08 — 08:30"),
    ("Registrar presença dos participantes",                          "Fran",           "26/08 — durante"),
    ("Capturar fotos e vídeos (Stories/Reels)",                      "A definir",      "26/08 — durante"),
    ("Identificar e abordar leads quentes em tempo real",             "Sócios",         "26/08 — durante"),
    ("Registrar insights: dores, objeções, sistemas usados",          "Fran + Sócios",  "26/08 — após"),
    ("Distribuir brindes mediante QR Code da pesquisa",              "Fran",           "26/08 — encerramento"),
]:
    r = item_row(ws1, r, ativ, resp, prazo)

# ── PÓS-EVENTO ──────────────────────────────────────────
r = section(ws1, r, "📊  PÓS-EVENTO")
for ativ, resp, prazo in [
    ("Disparar e-mail de agradecimento",                              "Fran",           "27/08/2026"),
    ("Publicar post pós-evento LinkedIn + Instagram",                 "Fran",           "27/08/2026"),
    ("Consolidar lista de presença com leads captados",               "Fran",           "29/08/2026"),
    ("Limpar e deduplicar dados de leads",                            "Fran",           "29/08/2026"),
    ("Subir contatos no HubSpot (origem: BDC Innovation Day 2026)",  "Fran",           "29/08/2026"),
    ("Classificar leads: Quente / Morno / Frio",                     "Fran + Sócios",  "29/08/2026"),
    ("Criar tarefas de follow-up no HubSpot",                        "Fran + Comercial","29/08/2026"),
    ("Follow-up D+1 — contato direto com leads quentes",             "Comercial",      "27/08/2026"),
    ("Follow-up D+3 — e-mail com material do evento",                "Comercial",      "29/08/2026"),
    ("Follow-up D+5 — ligação comercial para SQLs",                  "Comercial",      "01/09/2026"),
    ("Follow-up D+7 — último contato / proposta de diagnóstico",     "Comercial",      "03/09/2026"),
    ("Gerar relatório de resultados (leads, pipeline, ROI)",         "Fran",           "05/09/2026"),
    ("Publicar Reels e conteúdo pós-evento",                         "Fran",           "01–12/09/2026"),
    ("Registrar aprendizados para próxima edição",                   "Fran + Sócios",  "05/09/2026"),
]:
    r = item_row(ws1, r, ativ, resp, prazo)

STATUS_LAST_ROW = r - 1
add_cond_status(ws1, STATUS_FIRST_ROW, STATUS_LAST_ROW, 4)  # coluna E = índice 4

# ══════════════════════════════════════════════════════════
# ABA 2 — CRONOGRAMA
# ══════════════════════════════════════════════════════════
ws2 = wb.add_worksheet("Cronograma")
ws2.set_column(0, 0, 22)
ws2.set_column(1, 1, 42)
ws2.set_column(2, 2, 20)
ws2.set_column(3, 3, 16)
ws2.set_column(4, 4, 16)
ws2.set_zoom(90)

ws2.merge_range("A1:E1", "SAP BDC Innovation Day 2026 — Cronograma", F["header_azul"])
ws2.set_row(0, 30)
ws2.merge_range("A2:E2", "26 de agosto de 2026  |  SAP Brasil, São Paulo", F["header_amar"])
ws2.set_row(1, 20)

r2 = 3
for col, h in enumerate(["Fase / Período","Atividade","Responsável","Data Limite","Status"]):
    ws2.write(r2, col, h, F["col_header"])
ws2.set_row(r2, 20)
r2 += 1

S2_FIRST = r2

def section2(ws, row, title):
    ws.merge_range(row, 0, row, 4, title, F["section"])
    ws.set_row(row, 18)
    return row + 1

def item2(ws, row, fase, ativ, resp, prazo):
    z = row % 2 == 0
    fa = F["cell_cz"]    if z else F["cell_w"]
    fc = F["cell_ctr_cz"] if z else F["cell_ctr_w"]
    fs = F["status_cz"]  if z else F["status_w"]
    ws.write(row, 0, fase,   fa)
    ws.write(row, 1, ativ,   fa)
    ws.write(row, 2, resp,   fc)
    ws.write(row, 3, prazo,  fc)
    ws.write(row, 4, "Pendente", fs)
    ws.set_row(row, 16)
    return row + 1

fases = [
    ("JUN 2026 — Planejamento", [
        ("Jun/2026", "Confirmar espaço SAP Brasil",                "Fran",           "20/06/2026"),
        ("Jun/2026", "Definir nome do evento",                     "Fran",           "20/06/2026"),
        ("Jun/2026", "Confirmar case e speakers",                  "Fran / Sócios",  "30/06/2026"),
        ("Jun/2026", "Contratar coffee (70 pax)",                  "Fran",           "30/06/2026"),
        ("Jun/2026", "Comprar brindes",                            "Fran",           "15/07/2026"),
    ]),
    ("JUL 2026 — Criação e Início da Divulgação", [
        ("Jul/2026", "Produzir materiais (LP, e-mails, anúncios, card)","Fran/Design","14/07/2026"),
        ("Jul/2026", "Montar lista de convidados segmentada",      "Fran",           "15/07/2026"),
        ("Jul/2026", "E-mail 01 + LinkedIn Ads",                   "Fran",           "21/07/2026"),
        ("Jul/2026", "E-mail 02",                                  "Fran",           "28/07/2026"),
        ("Jul/2026", "Disparo WhatsApp",                           "Fran",           "30/07–04/08"),
    ]),
    ("AGO 2026 — Divulgação e RSVP", [
        ("Ago/2026", "E-mail 03",                                  "Fran",           "04/08/2026"),
        ("Ago/2026", "E-mail 04",                                  "Fran",           "11/08/2026"),
        ("Ago/2026", "Período RSVP / confirmações",                "Fran",           "11/08–22/08"),
        ("Ago/2026", "E-mail 05 — RSVP / últimas vagas",           "Fran",           "18/08/2026"),
        ("Ago/2026", "Preparação final",                           "Fran",           "25/08/2026"),
        ("Ago/2026", "Lembrete D-2",                               "Fran",           "24/08/2026"),
    ]),
    ("26/08 — EVENTO", [
        ("26/08",    "Execução do evento",                         "Fran + Sócios",  "26/08/2026"),
        ("26/08",    "Captação e qualificação de leads",           "Fran + Sócios",  "26/08/2026"),
        ("26/08",    "Cobertura foto/vídeo",                       "A definir",      "26/08/2026"),
    ]),
    ("SET 2026 — Pós-evento", [
        ("Set/2026", "Agradecimento + post pós-evento",            "Fran",           "27/08/2026"),
        ("Set/2026", "Consolidar leads no HubSpot",                "Fran",           "29/08/2026"),
        ("Set/2026", "Follow-up comercial D+1 a D+7",              "Comercial",      "27/08–03/09"),
        ("Set/2026", "Relatório de resultados",                    "Fran",           "05/09/2026"),
    ]),
]

for nome_fase, itens in fases:
    r2 = section2(ws2, r2, nome_fase)
    for fase, ativ, resp, prazo in itens:
        r2 = item2(ws2, r2, fase, ativ, resp, prazo)

add_cond_status(ws2, S2_FIRST, r2 - 1, 4)

# ══════════════════════════════════════════════════════════
# ABA 3 — SEQUÊNCIA DE E-MAILS
# ══════════════════════════════════════════════════════════
ws3 = wb.add_worksheet("Sequência E-mails")
ws3.set_column(0, 0, 4)
ws3.set_column(1, 1, 24)
ws3.set_column(2, 2, 16)
ws3.set_column(3, 3, 38)
ws3.set_column(4, 4, 18)
ws3.set_column(5, 5, 16)
ws3.set_zoom(90)

ws3.merge_range("A1:F1", "Sequência de E-mails — SAP BDC Innovation Day 2026", F["header_azul"])
ws3.set_row(0, 30)

r3 = 2
for col, h in enumerate(["✓","E-mail","Data Envio","Objetivo","Tx. Abertura Meta","Status"]):
    ws3.write(r3, col, h, F["col_header"])
ws3.set_row(r3, 20)
r3 += 1

S3_FIRST = r3

emails = [
    ("E-mail 01 — 1º Convite",       "21/07/2026", "Primeiro contato — convidar para o evento",      ">20%"),
    ("E-mail 02 — 2º Convite",       "28/07/2026", "Reforço — destacar speakers e case",             ">15%"),
    ("E-mail 03 — 3º Convite",       "04/08/2026", "Urgência leve — vagas se esgotando",             ">18%"),
    ("E-mail 04 — 4º Convite",       "11/08/2026", "Última chamada geral",                           ">14%"),
    ("E-mail 05 — RSVP",             "18/08/2026", "Confirmação de presença / últimas vagas",        ">20%"),
    ("Lembrete D-2",                 "24/08/2026", "Lembrete final para confirmados",                ">30%"),
    ("Agradecimento pós-evento",     "27/08/2026", "Agradecimento + material + próximos passos",     ">40%"),
    ("Confirmação de inscrição",     "Automático", "Confirmar cadastro e fornecer detalhes",         ">40%"),
    ("Recebimento de inscrição",     "Automático", "Notificação interna de novo inscrito",           "—"),
]
for i, (nome, data, obj, meta) in enumerate(emails):
    z = i % 2 == 0
    fc  = F["check_cz"]    if z else F["check_w"]
    fa  = F["cell_cz"]     if z else F["cell_w"]
    fc2 = F["cell_ctr_cz"] if z else F["cell_ctr_w"]
    fs  = F["status_cz"]   if z else F["status_w"]
    fb  = wb.add_format({"bold":True,"font_size":10,"bg_color":CZ_CLARO if z else BRANCO,"align":"left","valign":"vcenter","border":1,"border_color":"#CCCCCC"})
    ws3.write(r3, 0, "☐",    fc)
    ws3.write(r3, 1, nome,   fb)
    ws3.write(r3, 2, data,   fc2)
    ws3.write(r3, 3, obj,    fa)
    ws3.write(r3, 4, meta,   fc2)
    ws3.write(r3, 5, "Pendente", fs)
    ws3.set_row(r3, 18)
    r3 += 1

add_cond_status(ws3, S3_FIRST, r3 - 1, 5)

# ══════════════════════════════════════════════════════════
# ABA 4 — ORÇAMENTO
# ══════════════════════════════════════════════════════════
ws4 = wb.add_worksheet("Orçamento")
ws4.set_column(0, 0, 4)
ws4.set_column(1, 1, 40)
ws4.set_column(2, 2, 20)
ws4.set_column(3, 3, 20)
ws4.set_column(4, 4, 20)
ws4.set_column(5, 5, 28)
ws4.set_zoom(90)

ws4.merge_range("A1:F1", "Orçamento — SAP BDC Innovation Day 2026", F["header_azul"])
ws4.set_row(0, 30)
ws4.merge_range("A2:F2", "Budget total: R$ 6.000,00", F["header_amar"])
ws4.set_row(1, 20)

r4 = 3
for col, h in enumerate(["#","Item","Valor Previsto","Valor Realizado","Diferença","Observações"]):
    ws4.write(r4, col, h, F["col_header"])
ws4.set_row(r4, 20)
r4 += 1

for i, (item, prev, obs) in enumerate([
    ("Coffee break (70 pax)",                    "R$ 4.400,00", ""),
    ("Brindes — Moleskine + Caneta (70 un.)",    "R$ 800,00",  "Condicionado ao QR Code da pesquisa"),
    ("LinkedIn Ads — campanha de convite",        "R$ 800,00",  "Formato 1200x1200 performou melhor na ed. anterior"),
    ("Contingência",                              "R$ 0,00",    "Reserva inclusa no coffee (+10%)"),
]):
    z = i % 2 == 0
    fa  = F["cell_cz"]     if z else F["cell_w"]
    fc2 = F["cell_ctr_cz"] if z else F["cell_ctr_w"]
    ws4.write(r4, 0, i+1,  fc2)
    ws4.write(r4, 1, item,  fa)
    ws4.write(r4, 2, prev,  fc2)
    ws4.write(r4, 3, "—",   fc2)
    ws4.write(r4, 4, "—",   fc2)
    ws4.write(r4, 5, obs,   fa)
    ws4.set_row(r4, 18)
    r4 += 1

ws4.write(r4, 0, "",             F["total_lbl"])
ws4.write(r4, 1, "TOTAL",        F["total_lbl"])
ws4.write(r4, 2, "R$ 6.000,00",  F["total"])
ws4.write(r4, 3, "—",            F["total"])
ws4.write(r4, 4, "—",            F["total"])
ws4.write(r4, 5, "",             F["total_lbl"])
ws4.set_row(r4, 20)
r4 += 2

for lbl, val in [
    ("Custo por inscrito esperado (120):",        "~R$ 50,00"),
    ("Custo por participante esperado (70):",     "~R$ 86,00"),
    ("Custo por oportunidade esperado (6 deals):","~R$ 1.000,00"),
]:
    ws4.write(r4, 1, lbl, F["kpi_lbl"])
    ws4.write(r4, 2, val, F["kpi_val"])
    r4 += 1
r4 += 1
ws4.merge_range(r4, 0, r4, 5,
    "Referência fev/2025: R$ 5.034,80 investidos → 5 deals → ROI 9.824%.",
    F["nota"])

# ══════════════════════════════════════════════════════════
# ABA 5 — RELATÓRIO DE RESULTADOS
# ══════════════════════════════════════════════════════════
ws5 = wb.add_worksheet("Relatório de Resultados")
ws5.set_column(0, 0, 32)
ws5.set_column(1, 1, 20)
ws5.set_column(2, 2, 20)
ws5.set_column(3, 3, 20)
ws5.set_column(4, 4, 28)
ws5.set_zoom(90)

ws5.merge_range("A1:E1", "Relatório de Resultados — SAP BDC Innovation Day 2026", F["header_azul"])
ws5.set_row(0, 30)
ws5.merge_range("A2:E2", "Preencher após o evento (26/08/2026)", F["header_amar"])
ws5.set_row(1, 20)

r5 = 3
for col, h in enumerate(["Métrica","Baseline Fev/2025","Meta Ago/2026","Realizado","Observações"]):
    ws5.write(r5, col, h, F["col_header"])
ws5.set_row(r5, 20)
r5 += 1

for i, (met, base, meta) in enumerate([
    ("Inscrições",             "108",      "120"),
    ("Participantes",          "63",       "70"),
    ("Não participaram",       "46",       "50"),
    ("Taxa de comparecimento", "58%",      "≥ 58%"),
    ("MQLs",                   "60",       "70"),
    ("SQLs",                   "6",        "7"),
    ("Oportunidades (deals)",  "5",        "6"),
    ("Pipeline gerado",        "~R$ 2,5M", "R$ 3.000.000"),
    ("Investimento total",     "R$5.034",  "R$6.000"),
    ("ROI",                    "9.824%",   ">9.000%"),
    ("Custo por inscrito",     "R$46,62",  "~R$50,00"),
    ("Custo por participante", "R$79,92",  "~R$86,00"),
    ("Custo por oportunidade", "R$1.006",  "~R$1.000"),
    ("Tx. abertura e-mail",    "~19%",     ">20%"),
]):
    z = i % 2 == 0
    ws5.write(r5, 0, met,  F["meta_lbl"])
    ws5.write(r5, 1, base, F["meta_base"])
    ws5.write(r5, 2, meta, F["meta_alvo"])
    ws5.write(r5, 3, "—",  F["meta_real"])
    ws5.write(r5, 4, "",   F["cell_cz"] if z else F["cell_w"])
    ws5.set_row(r5, 18)
    r5 += 1

r5 += 1
ws5.merge_range(r5, 0, r5, 4, "Aprendizados e Próximos Passos", F["section"])
ws5.set_row(r5, 18)
r5 += 1
for lbl in ["O que funcionou:", "O que não funcionou:", "O que melhorar:", "Próximos passos:"]:
    ws5.write(r5, 0, lbl, F["apren_lbl"])
    ws5.merge_range(r5, 1, r5, 4, "", F["apren_val"])
    ws5.set_row(r5, 30)
    r5 += 1

wb.close()
print(f"Excel salvo: {OUTPUT}")
