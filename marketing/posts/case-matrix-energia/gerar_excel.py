import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

md = open("copy.md", encoding="utf-8").read()
v1 = re.search(r"## Versão 1[^\n]*\n\n(.*?)\n\n---", md, re.S).group(1).strip()
v2 = re.search(r"## Versão 2[^\n]*\n\n(.*?)\n\n---", md, re.S).group(1).strip()
print("v1 chars:", len(v1), "| v2 chars:", len(v2))

facebook = v1.replace("@Matrix Energia", "Matrix Energia").replace("@SolvePlan", "SolvePlan")
facebook = facebook.split("\n\n#")[0]
instagram = """Consolidação societária no Excel. Até quando? 📊

A Matrix Energia fechava os números das sociedades em planilha: sem rastreabilidade, com muito trabalho manual e resultado atrasado para os stakeholders.

Com a SolvePlan, a consolidação foi para o SAP Analytics Cloud, integrada ao SAP Business One. Em 3 meses.

Hoje o time de negócios:
→ administra as próprias regras de eliminação
→ cria relatórios e simula cenários de fusões e aquisições
→ fecha mais rápido, sem depender de TI

📌 Salva para mostrar para o seu time de controladoria.
Case completo no link da bio.

#SAPAnalyticsCloud #ConsolidaçãoSocietária #Controladoria #FechamentoContábil #SAPBusinessOne #SAP #FPeA #CFO"""

headers = ["Data", "Dia", "Linha Editorial", "Tema", "Origem do Post", "Título de Conteúdo",
    "Objetivo", "Persona", "Etapa do Funil", "Copy LinkedIn", "Copy Facebook",
    "Copy Instagram", "Formato", "Horário", "Ref. Texto", "Responsável", "Status"]
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Posts"
ws.append(headers)
ws.append(["", "", "Case/Prova Social", "Case Matrix Energia: consolidação societária com SAP Analytics Cloud em 3 meses",
    "Case de cliente", v1.split("\n")[0], "Credibilidade", "CFO / Controller", "Meio",
    v1, facebook, instagram, "Carrossel", "", "marketing/posts/case-matrix-energia/copy.md", "Fran", "🟡 Criado"])

hf = PatternFill(start_color="0A1A3C", end_color="0A1A3C", fill_type="solid")
alt = PatternFill(start_color="EEF2F8", end_color="EEF2F8", fill_type="solid")
for c in ws[1]:
    c.fill = hf; c.font = Font(color="FFFFFF", bold=True, size=10)
    c.alignment = Alignment(vertical="top", wrap_text=True)
for r in range(2, ws.max_row + 1):
    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=r, column=col)
        cell.alignment = Alignment(vertical="top", wrap_text=True)
        if r % 2 == 0: cell.fill = alt
    s = ws.cell(row=r, column=len(headers))
    s.fill = PatternFill(start_color="FFF9C4", end_color="FFF9C4", fill_type="solid"); s.font = Font(color="7A5A00")
widths = {"Data": 12, "Dia": 10, "Linha Editorial": 18, "Tema": 30, "Origem do Post": 16, "Título de Conteúdo": 40,
    "Objetivo": 14, "Persona": 18, "Etapa do Funil": 14, "Copy LinkedIn": 68, "Copy Facebook": 68, "Copy Instagram": 68,
    "Formato": 14, "Horário": 10, "Ref. Texto": 45, "Responsável": 12, "Status": 12}
for i, h in enumerate(headers, 1): ws.column_dimensions[get_column_letter(i)].width = widths[h]
ws.freeze_panes = "B2"; ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{ws.max_row}"
wb.save("post-dados.xlsx"); print("ok")
