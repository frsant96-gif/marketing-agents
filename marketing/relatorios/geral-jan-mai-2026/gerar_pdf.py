from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import re

# Cores Solveplan
AZUL = colors.HexColor('#006AFF')
AZUL_ESCURO = colors.HexColor('#0A0E19')
VERDE = colors.HexColor('#00C4A7')
LARANJA = colors.HexColor('#FF6B35')
CINZA_CLARO = colors.HexColor('#F5F5F5')
CINZA = colors.HexColor('#888888')
BRANCO = colors.white
PRETO = colors.HexColor('#1A1A1A')

PAGE_W, PAGE_H = A4

def safe_add(styles, style):
    if style.name in styles:
        styles[style.name].__dict__.update(style.__dict__)
    else:
        styles.add(style)

def build_styles():
    styles = getSampleStyleSheet()

    safe_add(styles, ParagraphStyle(
        'H1', parent=styles['Normal'],
        fontSize=22, fontName='Helvetica-Bold',
        textColor=AZUL, spaceAfter=8, spaceBefore=16,
        leading=26,
    ))
    safe_add(styles, ParagraphStyle(
        'H2', parent=styles['Normal'],
        fontSize=15, fontName='Helvetica-Bold',
        textColor=AZUL_ESCURO, spaceAfter=6, spaceBefore=14,
        leading=18, borderPad=4,
    ))
    safe_add(styles, ParagraphStyle(
        'H3', parent=styles['Normal'],
        fontSize=12, fontName='Helvetica-Bold',
        textColor=AZUL, spaceAfter=4, spaceBefore=10,
        leading=15,
    ))
    safe_add(styles, ParagraphStyle(
        'Body', parent=styles['Normal'],
        fontSize=10, fontName='Helvetica',
        textColor=PRETO, spaceAfter=4, spaceBefore=2,
        leading=14,
    ))
    safe_add(styles, ParagraphStyle(
        'CodeBlock', parent=styles['Normal'],
        fontSize=9, fontName='Courier',
        textColor=colors.HexColor('#333333'),
        backColor=colors.HexColor('#F0F0F0'),
        spaceAfter=4, spaceBefore=4,
        leading=13, leftIndent=10, rightIndent=10,
        borderPad=6,
    ))
    safe_add(styles, ParagraphStyle(
        'Bullet', parent=styles['Normal'],
        fontSize=10, fontName='Helvetica',
        textColor=PRETO, spaceAfter=3, spaceBefore=1,
        leading=14, leftIndent=16, bulletIndent=6,
    ))
    safe_add(styles, ParagraphStyle(
        'Subtitle', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica',
        textColor=CINZA, spaceAfter=4, spaceBefore=0,
        leading=14,
    ))
    safe_add(styles, ParagraphStyle(
        'TableHeader', parent=styles['Normal'],
        fontSize=9, fontName='Helvetica-Bold',
        textColor=BRANCO, alignment=TA_CENTER,
    ))
    safe_add(styles, ParagraphStyle(
        'TableCell', parent=styles['Normal'],
        fontSize=9, fontName='Helvetica',
        textColor=PRETO, alignment=TA_LEFT,
        leading=12,
    ))
    safe_add(styles, ParagraphStyle(
        'TableCellCenter', parent=styles['Normal'],
        fontSize=9, fontName='Helvetica',
        textColor=PRETO, alignment=TA_CENTER,
        leading=12,
    ))
    return styles


def make_table(rows, col_widths=None, header=True):
    if not rows:
        return None

    style_cmds = [
        ('BACKGROUND', (0,0), (-1,0), AZUL),
        ('TEXTCOLOR', (0,0), (-1,0), BRANCO),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (0,1), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [BRANCO, CINZA_CLARO]),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#DDDDDD')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ROWHEIGHT', (0,0), (-1,0), 20),
    ]
    t = Table(rows, colWidths=col_widths)
    t.setStyle(TableStyle(style_cmds))
    return t


def parse_md_to_flowables(md_text, styles):
    flowables = []
    lines = md_text.split('\n')
    i = 0
    in_table = False
    table_rows = []
    in_code = False
    code_lines = []

    while i < len(lines):
        line = lines[i]

        # Code block
        if line.strip().startswith('```'):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                in_code = False
                code_text = '\n'.join(code_lines)
                for cl in code_lines:
                    flowables.append(Paragraph(cl.replace('<','&lt;').replace('>','&gt;') or '&nbsp;', styles['CodeBlock']))
                flowables.append(Spacer(1, 4))
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # Table detection
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            # skip separator row
            if not all(re.match(r'^[-: ]+$', c) for c in cells):
                table_rows.append(cells)
            i += 1
            continue
        else:
            if in_table and table_rows:
                # emit table
                max_cols = max(len(r) for r in table_rows)
                col_w = (PAGE_W - 4*cm) / max_cols
                col_widths = [col_w] * max_cols
                # pad rows
                padded = []
                for r in table_rows:
                    while len(r) < max_cols:
                        r.append('')
                    padded.append(r)
                t = make_table(padded, col_widths=col_widths)
                if t:
                    flowables.append(t)
                    flowables.append(Spacer(1, 8))
                in_table = False
                table_rows = []

        stripped = line.strip()

        if not stripped:
            flowables.append(Spacer(1, 6))
            i += 1
            continue

        # HR
        if stripped.startswith('---') and len(stripped) >= 3 and all(c == '-' for c in stripped):
            flowables.append(Spacer(1, 4))
            flowables.append(HRFlowable(width='100%', thickness=1, color=AZUL))
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # Headings
        if stripped.startswith('# ') and not stripped.startswith('## '):
            text = stripped[2:].strip()
            flowables.append(Spacer(1, 8))
            flowables.append(Paragraph(escape_html(text), styles['H1']))
            flowables.append(HRFlowable(width='100%', thickness=2, color=AZUL))
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        if stripped.startswith('## '):
            text = stripped[3:].strip()
            flowables.append(Spacer(1, 6))
            flowables.append(Paragraph(escape_html(text), styles['H2']))
            i += 1
            continue

        if stripped.startswith('### '):
            text = stripped[4:].strip()
            flowables.append(Paragraph(escape_html(text), styles['H3']))
            i += 1
            continue

        if stripped.startswith('#### '):
            text = stripped[5:].strip()
            flowables.append(Paragraph('<b>' + escape_html(text) + '</b>', styles['Body']))
            i += 1
            continue

        # Bullets
        if stripped.startswith('- ') or stripped.startswith('* '):
            text = stripped[2:].strip()
            flowables.append(Paragraph('• ' + format_inline(text), styles['Bullet']))
            i += 1
            continue

        if re.match(r'^\d+\. ', stripped):
            text = re.sub(r'^\d+\. ', '', stripped)
            num = re.match(r'^(\d+)\.', stripped).group(1)
            flowables.append(Paragraph(f'{num}. ' + format_inline(text), styles['Bullet']))
            i += 1
            continue

        # Blockquote
        if stripped.startswith('> '):
            text = stripped[2:].strip()
            flowables.append(Paragraph(
                format_inline(text),
                ParagraphStyle('Quote', parent=styles['Body'],
                    leftIndent=20, borderColor=AZUL, borderWidth=3,
                    borderPad=8, backColor=colors.HexColor('#EEF4FF'))
            ))
            i += 1
            continue

        # Normal paragraph
        if stripped:
            flowables.append(Paragraph(format_inline(stripped), styles['Body']))
        i += 1

    return flowables


def escape_html(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def format_inline(text):
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic *text*
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Code `text`
    text = re.sub(r'`(.+?)`', r'<font name="Courier" size="9">\1</font>', text)
    # Links [text](url) — show text only
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    # Escape remaining html
    # (already done partially, don't double-escape)
    return text


def generate_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    styles = build_styles()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=2.5*cm,
        bottomMargin=2*cm,
        title='Guia Power BI — Solveplan H1 2026',
        author='Solveplan',
    )

    def header_footer(canvas, doc):
        canvas.saveState()
        # Header bar
        canvas.setFillColor(AZUL)
        canvas.rect(0, PAGE_H - 1.2*cm, PAGE_W, 1.2*cm, fill=1, stroke=0)
        canvas.setFillColor(BRANCO)
        canvas.setFont('Helvetica-Bold', 10)
        canvas.drawString(2*cm, PAGE_H - 0.85*cm, 'Guia Power BI — Solveplan H1 2026')
        canvas.setFont('Helvetica', 9)
        canvas.drawRightString(PAGE_W - 2*cm, PAGE_H - 0.85*cm, 'solveplan.com')

        # Footer
        canvas.setFillColor(CINZA)
        canvas.setFont('Helvetica', 8)
        canvas.drawString(2*cm, 0.8*cm, f'Página {doc.page}')
        canvas.drawCentredString(PAGE_W/2, 0.8*cm, 'Solveplan — Dados e Analytics SAP')
        canvas.drawRightString(PAGE_W - 2*cm, 0.8*cm, 'Gerado em 08/06/2026')
        canvas.restoreState()

    flowables = parse_md_to_flowables(md_text, styles)
    doc.build(flowables, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f'PDF gerado: {pdf_path}')


if __name__ == '__main__':
    import os
    base = os.path.dirname(os.path.abspath(__file__))
    md = os.path.join(base, 'guia-powerbi-passo-a-passo.md')
    pdf = os.path.join(base, 'Guia_PowerBI_Solveplan_H1_2026.pdf')
    generate_pdf(md, pdf)
