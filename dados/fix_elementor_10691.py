import json

path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_10691.json"

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

elements = data[0]['elements']

# ── Widget 339db3b8 — article body ──────────────────────────────────────────
article = next(e for e in elements if e['id'] == '339db3b8')
html = article['settings']['editor']

# 1. Remove empty H5 spacers
html = html.replace('<h5> </h5>\n', '')
html = html.replace('<h5>&nbsp;</h5>\n', '')

# 2. H5 → H2
html = html.replace('<h5 class="wp-block-heading">', '<h2 class="wp-block-heading">')
html = html.replace('</h5>', '</h2>')
html = html.replace('<!-- wp:heading {"level":5} -->', '<!-- wp:heading {"level":2} -->')

h2_count = html.count('<h2 class="wp-block-heading">')
h5_count = html.count('<h5')
print(f"H2 headings: {h2_count}, H5 restantes: {h5_count}")

article['settings']['editor'] = html

# ── New FAQ widget ────────────────────────────────────────────────────────────
faq_html = (
    '<p><strong style="color: inherit; font-family: inherit; font-size: 1.25rem;">FAQ — SAP Knowledge Graph</strong></p>\n'
    '<details class="wp-block-details">\n'
    '<summary>O que é o SAP Knowledge Graph?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>O SAP Knowledge Graph é a camada de conhecimento estruturado que fornece contexto empresarial para os agentes de IA do ecossistema SAP. Mapeia 452.000 tabelas e 7,3 milhões de campos do S/4HANA em relações semânticas compreensíveis por máquina — processos, entidades, políticas e hierarquias de aprovação codificados para uso por agentes.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>Como o SAP Knowledge Graph diferencia os agentes SAP de modelos de IA genéricos?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>Modelos genéricos operam sobre conhecimento textual da internet. O SAP Knowledge Graph ancora cada agente em 50 anos de engenharia ERP — processos, regras de aprovação, tolerâncias e hierarquias organizacionais específicas da empresa. O resultado é IA que não apenas gera respostas plausíveis — raciocina dentro de um mapa verificável do negócio.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>O que é a abordagem neuro-simbólica do SAP Knowledge Graph?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>A abordagem neuro-simbólica combina redes neurais com conhecimento simbólico explícito. Isso garante que os agentes SAP possam explicar suas decisões — mostrando o caminho de raciocínio que levou a uma ação — o que é essencial para auditoria e conformidade regulatória.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>O que é o SAP AI Foundation?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>O SAP AI Foundation é a plataforma que sustenta os agentes SAP. Inclui o Knowledge Graph como mapa de decisões, modelos especializados em dados ERP (finanças, logística, RH) e o Agent Hub — centralizando registro de agentes, controles de acesso por papel, trilhas de auditoria de decisões e mecanismos de override humano.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>Qual a diferença entre o SAP Knowledge Graph e o SAP Business Data Cloud?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>O SAP Knowledge Graph fornece o contexto genérico do universo SAP — processos, tabelas e relações comuns a toda a base de clientes. O SAP Business Data Cloud é a extensão que personaliza esse mapa para a empresa específica, integrando dados de múltiplas fontes com semântica de negócio — hierarquias, políticas, histórico e exceções próprias da organização.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>Por que o SAP Knowledge Graph é importante para ambientes SAP complexos?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>Em empresas com múltiplas entidades jurídicas, moedas e legislações, o Knowledge Graph garante que cada agente opere com as regras certas para cada contexto. Um agente com acesso ao Knowledge Graph sabe, por exemplo, que uma variação de custo acima de determinado percentual exige aprovação do controller — porque essa regra está mapeada no processo, não apenas no manual.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
)

faq_widget = {
    "id": "faq_section_kg",
    "elType": "widget",
    "settings": {"editor": faq_html, "text_color": "#000000"},
    "elements": [],
    "widgetType": "text-editor"
}

# Insert FAQ widget before the CTA button container (e7428a6)
cta_idx = next(i for i, e in enumerate(elements) if e['id'] == 'e7428a6')
elements.insert(cta_idx, faq_widget)
print(f"FAQ widget inserido na posicao {cta_idx} (antes do CTA)")

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_10691_updated.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

size = len(json.dumps(data, ensure_ascii=False))
print(f"Arquivo salvo: {out_path}")
print(f"Tamanho: {size} chars")
