import openpyxl
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side, GradientFill
)
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ── Cores ──────────────────────────────────────────────────────────────────────
AZUL_ESCURO  = "0D1B3E"   # header principal
AZUL_MEDIO   = "1A56A0"   # header de fase
AZUL_CLARO   = "D6E4F7"   # linha alternada
BRANCO       = "FFFFFF"
AMARELO_ALRT = "FFF3CD"   # status pendente
VERMELHO_ALT = "F8D7DA"   # status crítico
VERDE_OK     = "D4EDDA"   # status feito
CINZA_FUNDO  = "F2F2F2"

def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def bold_font(color="000000", size=10):
    return Font(bold=True, color=color, size=size)

def std_font(size=10):
    return Font(size=size)

def border():
    thin = Side(style="thin", color="CCCCCC")
    return Border(left=thin, right=thin, top=thin, bottom=thin)

def center():
    return Alignment(horizontal="center", vertical="center", wrap_text=True)

def left():
    return Alignment(horizontal="left", vertical="center", wrap_text=True)

# ═══════════════════════════════════════════════════════════════════════════════
# ABA 1 — CHECKLIST POR FASE
# ═══════════════════════════════════════════════════════════════════════════════
ws = wb.active
ws.title = "Checklist por Fase"

col_widths = [45, 18, 14, 22, 55]
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

# Título do documento
ws.merge_cells("A1:E1")
ws["A1"] = "CHECKLIST SAP NOW AI TOUR 2026"
ws["A1"].font = Font(bold=True, color=BRANCO, size=14)
ws["A1"].fill = fill(AZUL_ESCURO)
ws["A1"].alignment = center()
ws.row_dimensions[1].height = 30

ws.merge_cells("A2:E2")
ws["A2"] = "09 e 10 de setembro de 2026  |  Transamérica Expo Center — São Paulo  |  Responsável: Francielle Beline"
ws["A2"].font = Font(color=BRANCO, size=10)
ws["A2"].fill = fill(AZUL_MEDIO)
ws["A2"].alignment = center()
ws.row_dimensions[2].height = 18

HEADERS = ["Atividade", "Prazo", "Status", "Responsável", "OBS"]

def write_phase_header(ws, row, title):
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = title
    ws[f"A{row}"].font = Font(bold=True, color=BRANCO, size=11)
    ws[f"A{row}"].fill = fill(AZUL_MEDIO)
    ws[f"A{row}"].alignment = left()
    ws.row_dimensions[row].height = 22

def write_col_headers(ws, row):
    for col, h in enumerate(HEADERS, 1):
        c = ws.cell(row=row, column=col, value=h)
        c.font = bold_font(BRANCO, 10)
        c.fill = fill(AZUL_ESCURO)
        c.alignment = center()
        c.border = border()
    ws.row_dimensions[row].height = 20

def status_fill(status):
    s = status.upper()
    if "CRÍTICO" in s or "CRITICO" in s:
        return fill(VERMELHO_ALT)
    if "FEITO" in s or "CONCLUÍDO" in s or "CONCLUIDO" in s:
        return fill(VERDE_OK)
    if "PENDENTE" in s:
        return fill(AMARELO_ALRT)
    return fill(BRANCO)

def write_rows(ws, start_row, rows_data):
    for i, row in enumerate(rows_data):
        r = start_row + i
        bg = fill(AZUL_CLARO) if i % 2 == 0 else fill(BRANCO)
        for col, val in enumerate(row, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = std_font()
            c.border = border()
            c.alignment = left() if col != 2 else center()
            if col == 3:  # Status
                c.fill = status_fill(str(val))
            else:
                c.fill = bg
        ws.row_dimensions[r].height = 30
    return start_row + len(rows_data)

current_row = 3

# ── FASE 1 ────────────────────────────────────────────────────────────────────
write_phase_header(ws, current_row, "FASE 1 — JUNHO (URGENTE)")
current_row += 1
write_col_headers(ws, current_row)
current_row += 1

fase1 = [
    ("Enviar logo em vetor (.ai/.eps, CMYK, fontes em curvas) para SAP", "24/06", "Pendente", "Fran", "Requisito obrigatório do manual do patrocinador"),
    ("Definir título, speakers e descritivo da sessão Klabin", "26/06", "Pendente", "Fran + Molina", "Descritivo até 350 caracteres; tentar incluir Alexandre ou Andrey"),
    ("Enviar indicação de sessão para a SAP", "26/06", "CRÍTICO", "Fran", "Prazo fixo SAP — sem extensão"),
    ("Orçar arte do estande com agência", "Jun", "Pendente", "Fran", "Trainel 3D + Painel 1D + Balcão BPD"),
    ("Definir fornecedor da ativação (totem holográfico)", "Jun", "Pendente", "Fran", "Cubo montando/desmontando — verificar aprovação SAP"),
    ("Validar lista de 10 convidados VIP internamente", "Jun", "Pendente", "Fran + Comercial", "Klabin, Aço Cearense, Citrosuco, Eurofarma, Grupo Comporte, M. Dias Branco, Usina da Pedra, Cocal, Zaffari, MarcoPolo"),
    ("Iniciar abordagem SDR nas empresas-alvo", "Jun", "Pendente", "SDR", "Gancho: demonstração ao vivo, Estande 03, 9 e 10/set"),
    ("Lançar campanha pré-evento LinkedIn + e-mail", "Jun", "Pendente", "Fran", "Diagnóstico BDC Reservado"),
]
current_row = write_rows(ws, current_row, fase1)
current_row += 1

# ── FASE 2 ────────────────────────────────────────────────────────────────────
write_phase_header(ws, current_row, "FASE 2 — JULHO")
current_row += 1
write_col_headers(ws, current_row)
current_row += 1

fase2 = [
    ("Enviar planilha de convidados VIP (10 C-levels) para SAP", "10/07", "Pendente", "Fran", "Máx. 2 contatos por empresa; preferência SP"),
    ("Enviar artes exclusivas conforme cota Gold", "15/07", "Pendente", "Fran", "Arte fechada pela agência"),
    ("Solicitar aprovação de brindes para a SAP", "31/07", "CRÍTICO", "Fran", "Prazo fixo — sem extensão. Enviar briefing do cubo mágico personalizado"),
    ("Fechar pedido com A Cuber Brasil — cubo mágico 250 un.", "Após aprovação SAP", "Pendente", "Fran", "R$ 10.407,50 — UV direto, prazo 4 dias. renan@cuberbrasil.com / (19) 99606-4010"),
    ("Cotar embalagem personalizada para o cubo", "Jul", "Pendente", "Fran", "Fornecedor a definir"),
    ("Solicitar aprovação de ativações para a SAP", "31/07", "CRÍTICO", "Fran", "Prazo fixo — sem extensão"),
    ("Compra de serviços e equipamentos (geral)", "31/07", "Pendente", "Fran", "Todos os itens operacionais"),
    ("Pedido de camisetas e polos", "Jul", "Pendente", "Fran / RH", "27 camisetas + 12 polos — aguardando confirmação de tamanhos"),
    ("Contratar agência para arte do estande", "Jul", "Pendente", "Fran", "Prazo de produção ~3 semanas"),
    ("Contratar DOOH hotéis SP (28 telas, 3 dias)", "Jul", "Pendente", "Fran", "Ref. 2025: R$ 4.988,69 — aprovado"),
    ("Contratar LinkedIn Ads + Google Ads geolocalização", "Jul", "Pendente", "Fran", "Período: 07-11/set"),
    ("Reservar hotel para a equipe", "Jul", "Pendente", "Fran", "Dias 08 e 09/set no mínimo"),
    ("Pedido de displays QR Code para balcão", "Jul", "Pendente", "Fran", "2 un. + 1 reserva — Kalunga"),
    ("Continuar abordagem SDR empresas-alvo", "Jul", "Pendente", "SDR", "Meta: agendar slots no estande antes do evento"),
]
current_row = write_rows(ws, current_row, fase2)
current_row += 1

# ── FASE 3 ────────────────────────────────────────────────────────────────────
write_phase_header(ws, current_row, "FASE 3 — AGOSTO")
current_row += 1
write_col_headers(ws, current_row)
current_row += 1

fase3 = [
    ("Inscrição de credenciais do patrocinador", "28/08", "Pendente", "Fran", "8 credenciais + 1 staff — enviar planilha ao CAEX"),
    ("Produção da apresentação da sessão (20 min)", "Ago", "Pendente", "Fran + Klabin", "Slides aprovados pela SAP antes do evento"),
    ("Aprovação da apresentação pela SAP", "Ago", "Pendente", "Fran", "Obrigatório — planejar tempo para revisão"),
    ("Produção do vídeo looping (futurístico)", "Ago", "Pendente", "Fran + Fornecedor", "R$ 5.280,00 — Prêmio BDC → Cases → Dashboards → IA → CTA"),
    ("Recebimento e conferência dos brindes", "Ago", "Pendente", "Fran", "Conferir personalização antes do evento"),
    ("Recebimento e conferência das camisetas", "Ago", "Pendente", "Fran", "Conferir tamanhos e quantidade"),
    ("Publicar slots de diagnóstico BDC no app do evento", "25-26/08", "Pendente", "Fran", "App lança ~25/08"),
    ("Finalizar campanha pré-evento LinkedIn + e-mail", "Ago", "Pendente", "Fran", "Última onda antes do evento"),
    ("Continuar abordagem SDR empresas-alvo", "Ago", "Pendente", "SDR", "Foco em confirmação de presença e agenda no estande"),
]
current_row = write_rows(ws, current_row, fase3)
current_row += 1

# ── FASE 4 ────────────────────────────────────────────────────────────────────
write_phase_header(ws, current_row, "FASE 4 — PRÉ-EVENTO (SETEMBRO)")
current_row += 1
write_col_headers(ws, current_row)
current_row += 1

fase4 = [
    ("Credenciamento para entrega do estande", "04/09", "Pendente", "Fran", ""),
    ("Treinamento do time (kick off interno)", "Set/1", "Pendente", "Fran", "Abordagem, dor, registro de lead, quem chamar, o que NÃO falar"),
    ("Ativar anúncios DOOH + Google/LinkedIn", "07/09", "Pendente", "Fran", "Iniciar 1 dia antes do evento"),
    ("Retirar credenciais no CAEX", "08/09", "Pendente", "Fran", "CAEX das 08h às 14h — ou 09/set das 7h às 18h"),
    ("Retirar coletores de dados no CAEX", "08/09", "Pendente", "Fran", "RedDoor — R$ 1.601,14"),
    ("Montar estande (4 acessos)", "08/09", "Pendente", "Equipe", "Retirar pulseira CAEX das 09h às 14h"),
    ("Testar totem / ativação (offline + captura)", "08/09", "Pendente", "Fran", "Plano B: notebook com demo"),
    ("Testar QR Code e formulário HubSpot", "08/09", "Pendente", "Fran", "URL curta como backup"),
    ("Testar vídeo looping na TV (pen drive)", "08/09", "Pendente", "Fran", "2 pen drives — 1 de reserva"),
    ("Briefar speaker Klabin (local, horário, slides)", "08/09", "Pendente", "Fran", "Confirmar quem apresenta"),
]
current_row = write_rows(ws, current_row, fase4)
current_row += 1

# ── FASE 5 ────────────────────────────────────────────────────────────────────
write_phase_header(ws, current_row, "FASE 5 — EVENTO (09 e 10/09)")
current_row += 1
write_col_headers(ws, current_row)
current_row += 1

fase5 = [
    ("Operação do estande — Dia 1 manhã", "09/09 8h-13h30", "—", "Alexandre, Andrey, Molina, Fracchetta, Renan, Ferreira, Lucas, Bianca, Fran", ""),
    ("Operação do estande — Dia 1 tarde (troca)", "09/09 13h30-19h", "—", "Eduardo Savoine", "Horário de troca: 12h-14h"),
    ("Operação do estande — Dia 2 manhã", "10/09 8h-13h30", "—", "Alexandre, Andrey, Molina, Fracchetta, Renan, Ferreira, Lucas, Bianca, Fran", ""),
    ("Operação do estande — Dia 2 tarde", "10/09 13h30-19h", "—", "A confirmar", ""),
    ("Sessão de conteúdo Klabin (20 min)", "TBD", "—", "Speakers + Fran", "Encerrar com CTA explícito para Estande 03"),
    ("Captação de leads (coletores + QR + ativação)", "09-10/09", "—", "Toda equipe", "Registrar em tempo real — sem acúmulo para depois"),
    ("Qualificação de leads (Quente / Morno / Frio)", "09-10/09", "—", "Toda equipe", "Quente = acionar sênior imediatamente"),
    ("Demonstração ao vivo de BDC", "09-10/09", "—", "Especialistas", "Demo antes do assessment, não depois"),
    ("Entrega de brindes", "09-10/09", "—", "Toda equipe", "Entregar APÓS conversa — não como atrativo de entrada"),
    ("Registro fotográfico e vídeo", "09-10/09", "—", "Fran", "Posts ao vivo + banco de imagens"),
    ("Gravação de depoimentos com clientes", "09-10/09", "—", "Fornecedor", "LCA (SAP) estará no evento"),
    ("Desmontagem do estande", "10/09 20h-22h", "—", "Equipe", ""),
]
current_row = write_rows(ws, current_row, fase5)
current_row += 1

# ── FASE 6 ────────────────────────────────────────────────────────────────────
write_phase_header(ws, current_row, "FASE 6 — PÓS-EVENTO")
current_row += 1
write_col_headers(ws, current_row)
current_row += 1

fase6 = [
    ("SDR — follow-up nos leads", "Até 48h (12/09)", "—", "SDR", "SLA obrigatório — não passar de 48h"),
    ("Download mailing EventsOnSite (estande + palestra)", "D+1 (10/09)", "—", "Fran", "Origem separada por canal"),
    ("Consolidar leads no CRM", "D+1 (10/09)", "—", "Fran", "Tag: SAP-NOW-2026"),
    ("Enviar e-mail de agradecimento personalizado", "D+1 (10/09)", "—", "Fran", "Segmentar por dor declarada"),
    ("E-mail com valor (case Klabin) para leads mornos", "D+3 (12/09)", "—", "Fran", ""),
    ("Ligação / WhatsApp SDR — leads sem resposta", "D+5 (14/09)", "—", "SDR", ""),
    ("Último contato — oferta de diagnóstico gratuito", "D+7 (16/09)", "—", "SDR", "Leads sem resposta entram em nutrição longa"),
    ("Relatório de resultados vs metas", "D+7 (16/09)", "—", "Fran", "Comparar com 2025"),
    ("Post de cobertura / highlights", "D+2 (11/09)", "—", "Fran", ""),
    ("Edição e publicação dos vídeos de depoimento", "Set/Out", "—", "Fornecedor", "4 vídeos mín. — distribuir LinkedIn + site"),
]
current_row = write_rows(ws, current_row, fase6)

# ═══════════════════════════════════════════════════════════════════════════════
# ABA 2 — ORÇAMENTO
# ═══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Orçamento")

col_widths2 = [35, 25, 18, 12, 12, 40]
for i, w in enumerate(col_widths2, 1):
    ws2.column_dimensions[get_column_letter(i)].width = w

ws2.merge_cells("A1:F1")
ws2["A1"] = "ORÇAMENTO — SAP NOW AI TOUR 2026"
ws2["A1"].font = Font(bold=True, color=BRANCO, size=13)
ws2["A1"].fill = fill(AZUL_ESCURO)
ws2["A1"].alignment = center()
ws2.row_dimensions[1].height = 28

headers2 = ["Item", "Fornecedor", "Valor R$", "N° NF", "CC", "OBS"]
for col, h in enumerate(headers2, 1):
    c = ws2.cell(row=2, column=col, value=h)
    c.font = bold_font(BRANCO, 10)
    c.fill = fill(AZUL_ESCURO)
    c.alignment = center()
    c.border = border()
ws2.row_dimensions[2].height = 20

orcamento = [
    ("Cota de patrocínio Gold",         "RedDoor",          265000.00,  "", "", ""),
    ("Cota extra de comunicação",        "—",                0.00,       "", "", "A confirmar se aplica"),
    ("Coletor de dados (2 un.)",         "RedDoor",          1601.14,    "", "", "R$ 577,72/un + fee e impostos"),
    ("Brindes — Cubo Mágico (250 un.)",  "A Cuber Brasil",   10407.50,   "", "", "R$ 41,63/un — UV direto 5,6cm — renan@cuberbrasil.com"),
    ("Brindes — Embalagem personalizada","A definir",        0.00,       "", "", "A orçar"),
    ("Camisetas e polos",                "A contratar",      0.00,       "", "", "27 camisetas + 12 polos — aguardando RH"),
    ("Anúncios DOOH (hotéis SP)",        "A contratar",      4988.69,    "", "", "28 telas, 07-11/set"),
    ("Vídeos (looping + cases)",         "A contratar",      5280.00,    "", "", "SAP com LCA estará no evento"),
    ("Gráfica — display QR Code",        "Kalunga",          0.00,       "", "", "Impressão de arte para display — a orçar"),
    ("Arte do estande (agência)",        "A contratar",      0.00,       "", "", "Trainel + Painel + Balcão — a orçar"),
    ("Ativação (totem holográfico)",     "A contratar",      0.00,       "", "", "A orçar — aprovação SAP obrigatória"),
    ("LinkedIn Ads + Google Ads",        "A contratar",      0.00,       "", "", "Geolocalização 07-11/set — a orçar"),
    ("Hotel da equipe",                  "A contratar",      0.00,       "", "", "08 e 09/set — a orçar"),
]

for i, row in enumerate(orcamento, 3):
    bg = fill(AZUL_CLARO) if i % 2 == 0 else fill(BRANCO)
    for col, val in enumerate(row, 1):
        c = ws2.cell(row=i, column=col, value=val)
        c.font = std_font()
        c.border = border()
        c.fill = bg
        if col == 3:
            c.alignment = Alignment(horizontal="right", vertical="center")
            if isinstance(val, float) and val > 0:
                c.number_format = 'R$ #,##0.00'
        else:
            c.alignment = left()
    ws2.row_dimensions[i].height = 22

# Linha de total
total_row = len(orcamento) + 3
ws2.merge_cells(f"A{total_row}:B{total_row}")
ws2[f"A{total_row}"] = "TOTAL PARCIAL (itens com valor)"
ws2[f"A{total_row}"].font = bold_font(BRANCO, 10)
ws2[f"A{total_row}"].fill = fill(AZUL_ESCURO)
ws2[f"A{total_row}"].alignment = center()

total_formula = f"=SUM(C3:C{total_row-1})"
ws2[f"C{total_row}"] = total_formula
ws2[f"C{total_row}"].font = bold_font(BRANCO, 10)
ws2[f"C{total_row}"].fill = fill(AZUL_ESCURO)
ws2[f"C{total_row}"].alignment = Alignment(horizontal="right", vertical="center")
ws2[f"C{total_row}"].number_format = 'R$ #,##0.00'
ws2[f"C{total_row}"].border = border()
ws2.row_dimensions[total_row].height = 22

# ═══════════════════════════════════════════════════════════════════════════════
# ABA 3 — BRINDES (comparativo cotações)
# ═══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Cotações Brindes")

col_widths3 = [30, 22, 12, 10, 18, 12, 18, 14, 40]
for i, w in enumerate(col_widths3, 1):
    ws3.column_dimensions[get_column_letter(i)].width = w

ws3.merge_cells("A1:I1")
ws3["A1"] = "COTAÇÕES — BRINDES (CUBO MÁGICO)"
ws3["A1"].font = Font(bold=True, color=BRANCO, size=13)
ws3["A1"].fill = fill(AZUL_ESCURO)
ws3["A1"].alignment = center()
ws3.row_dimensions[1].height = 28

headers3 = ["Item", "Fornecedor", "Qtde", "Unid.", "Prazo Entrega", "Frete", "Custo Unit. (R$)", "Custo Total (R$)", "Observações"]
for col, h in enumerate(headers3, 1):
    c = ws3.cell(row=2, column=col, value=h)
    c.font = bold_font(BRANCO, 10)
    c.fill = fill(AZUL_ESCURO)
    c.alignment = center()
    c.border = border()
ws3.row_dimensions[2].height = 20

cotacoes = [
    ("Cubo Mágico Adesivado/Cromia 6 lados (5,2x5,2cm)", "Comercial Sisters", 250, "un", "12-15 dias", "CIF", 19.10,  4775.00,  "Adesivo Cromia 6 Logos. contato@comercialsisters.com.br"),
    ("Cubo mágico personalizado (5,5x5,5cm)",            "Imprimus",          250, "un", "15 dias",    "—",   13.95,  3487.50,  "Gravação Offset. guilherme@imprimus.com.br / (19) 3245-1615"),
    ("Cubo Mágico Profissional 3x3x3 (5,6cm)",          "A Cuber Brasil ✓",  250, "un", "4 dias",     "—",   41.63, 10407.50,  "UV direto no material. renan@cuberbrasil.com / (19) 99606-4010"),
    ("Cubo mágico 5,5x5,5x5,5",                         "ESP Brindes",        250, "un", "15 dias",    "CIF", 18.40,  4600.00,  "Papel adesivo com brilho envernizado. contato@espbrindes.com.br"),
    ("Embalagem personalizada",                          "A definir",          250, "un", "—",          "—",    0.00,     0.00,  ""),
    ("Cubo Mágico Profissional 3x3x3 (5,6cm)",          "Still Promotion",    250, "un", "A combinar", "CIF", 66.90, 16725.00,  "UV direto no material. fabio@stillpromotion.com.br / 11-3906-0300"),
]

for i, row in enumerate(cotacoes, 3):
    # destaque na linha da escolhida
    chosen = "A Cuber Brasil" in str(row[1])
    bg = fill("C8E6C9") if chosen else (fill(AZUL_CLARO) if i % 2 == 0 else fill(BRANCO))
    for col, val in enumerate(row, 1):
        c = ws3.cell(row=i, column=col, value=val)
        c.font = bold_font() if chosen else std_font()
        c.border = border()
        c.fill = bg
        if col in (7, 8):
            c.alignment = Alignment(horizontal="right", vertical="center")
            if isinstance(val, float) and val > 0:
                c.number_format = 'R$ #,##0.00'
        elif col in (3, 4, 5, 6):
            c.alignment = center()
        else:
            c.alignment = left()
    ws3.row_dimensions[i].height = 28

# ── salvar ────────────────────────────────────────────────────────────────────
path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\eventos\sap-now-2026\checklist-sap-now-2026.xlsx"
wb.save(path)
print(f"Arquivo salvo: {path}")
