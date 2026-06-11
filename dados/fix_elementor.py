import json

path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_10689.json"

with open(path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

elements = data[0]['elements']

# ── Widget 661ffa62 — article body ──────────────────────────────────────────
article = next(e for e in elements if e['id'] == '661ffa62')
html = article['settings']['editor']

# 1. H5 → H2
html = html.replace('<h5 class="wp-block-heading">', '<h2 class="wp-block-heading">')
html = html.replace('</h5>', '</h2>')
html = html.replace('<!-- wp:heading {"level":5} -->', '<!-- wp:heading {"level":2} -->')
print(f"H2 headings: {html.count('<h2 class=\"wp-block-heading\">')}, H5 restantes: {html.count('<h5')}")

# 2. Italic paragraphs → <ul>
old_list = (
    '<p><em><strong>Hierarquias organizacionais reais:</strong> quais entidades jurídicas existem, como estão estruturadas, quais são as relações de aprovação entre elas.</em></p>\n'
    '<p><!-- /wp:paragraph --><!-- wp:paragraph --></p>\n'
    '<p><em><strong>Dados mestre governados:</strong> clientes, fornecedores, materiais, centros de custo — com identidade unificada e sem duplicação entre sistemas.</em></p>\n'
    '<p><!-- /wp:paragraph --><!-- wp:paragraph --></p>\n'
    '<p><em><strong>Histórico transacional:</strong> o que aconteceu, quando, quem aprovou e por quê.</em></p>\n'
    '<p><!-- /wp:paragraph --><!-- wp:paragraph --></p>\n'
    '<p><em><strong>Regras de processo:</strong> políticas internas, limites de alçada, exceções negociadas.</em></p>\n'
    '<p><!-- /wp:paragraph --><!-- wp:paragraph --></p>\n'
    '<p><em><strong>Dados externos integrados:</strong> fontes fora do ecossistema SAP trazidas ao mesmo contexto semântico.</em></p>'
)
new_list = (
    '<ul>\n'
    '<li><strong>Hierarquias organizacionais reais:</strong> quais entidades jurídicas existem, como estão estruturadas, quais são as relações de aprovação entre elas.</li>\n'
    '<li><strong>Dados mestre governados:</strong> clientes, fornecedores, materiais, centros de custo — com identidade unificada e sem duplicação entre sistemas.</li>\n'
    '<li><strong>Histórico transacional:</strong> o que aconteceu, quando, quem aprovou e por quê.</li>\n'
    '<li><strong>Regras de processo:</strong> políticas internas, limites de alçada, exceções negociadas.</li>\n'
    '<li><strong>Dados externos integrados:</strong> fontes fora do ecossistema SAP trazidas ao mesmo contexto semântico.</li>\n'
    '</ul>'
)
if old_list in html:
    html = html.replace(old_list, new_list)
    print("Lista convertida para <ul>: OK")
else:
    print("AVISO: trecho de lista nao encontrado — tentando fallback")
    # Try without the intermediate paragraph comments
    markers = [
        ('<p><em><strong>Hierarquias organizacionais reais:</strong>', '<p><em><strong>Dados mestre governados:</strong>'),
    ]
    print(f"  Verificando presenca de 'Hierarquias': {'Hierarquias organizacionais reais' in html}")
    print(f"  Verificando presenca de 'em><strong>': {'<em><strong>' in html}")

article['settings']['editor'] = html

# ── Widget 2ae2686 — FAQ section ─────────────────────────────────────────────
faq_widget = next(e for e in elements if e['id'] == '2ae2686')
faq_html = faq_widget['settings']['editor']

old_faq6 = 'Como a Solveplan implementa o BDC como Knowledge Core?</summary>\n</details>'
new_faq6 = (
    'Como a Solveplan implementa o BDC como Knowledge Core?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>A Solveplan inicia com uma avaliação de maturidade de dados: unificação de dados mestre, mapeamento de hierarquias organizacionais e identificação das fontes a integrar. A implementação é estruturada em camadas — começando pelos fundamentos de governança — para garantir que os agentes SAP operem com o contexto correto desde o primeiro uso em produção.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>'
)
if old_faq6 in faq_html:
    faq_html = faq_html.replace(old_faq6, new_faq6)
    print("FAQ item 6 resposta adicionada: OK")
else:
    print(f"AVISO: FAQ item 6 nao encontrado. Buscando 'Como a Solveplan': {'Como a Solveplan' in faq_html}")

faq_widget['settings']['editor'] = faq_html

# ── Add FAQ JSON-LD schema widget ─────────────────────────────────────────────
faq_schema_html = (
    '<script type="application/ld+json">\n'
    '{\n'
    '  "@context": "https://schema.org",\n'
    '  "@type": "FAQPage",\n'
    '  "mainEntity": [\n'
    '    {\n'
    '      "@type": "Question",\n'
    '      "name": "O que é o Knowledge Core no contexto do SAP BDC?",\n'
    '      "acceptedAnswer": {\n'
    '        "@type": "Answer",\n'
    '        "text": "Knowledge Core é o papel do SAP Business Data Cloud como camada de dados governados e semanticamente estruturados que alimenta o SAP Knowledge Graph com o contexto específico da empresa — hierarquias, dados mestre, histórico transacional e regras de processo."\n'
    '      }\n'
    '    },\n'
    '    {\n'
    '      "@type": "Question",\n'
    '      "name": "Qual a diferença entre o SAP Knowledge Graph e o BDC como Knowledge Core?",\n'
    '      "acceptedAnswer": {\n'
    '        "@type": "Answer",\n'
    '        "text": "O SAP Knowledge Graph é o mapa genérico de processos do universo SAP — compartilhado por todos os clientes. O BDC como Knowledge Core é a camada que personaliza esse mapa com os dados reais da empresa: sua estrutura, suas políticas, seu histórico."\n'
    '      }\n'
    '    },\n'
    '    {\n'
    '      "@type": "Question",\n'
    '      "name": "O que são SAP Domain Models?",\n'
    '      "acceptedAnswer": {\n'
    '        "@type": "Answer",\n'
    '        "text": "SAP Domain Models são modelos pré-treinados na lógica de processo SAP que traduzem dados estruturados pelo BDC em contexto de negócio interpretável por agentes. Operam sobre data products certificados e permitem que agentes tomem decisões dentro do processo, não apenas sobre os dados."\n'
    '      }\n'
    '    },\n'
    '    {\n'
    '      "@type": "Question",\n'
    '      "name": "O que é um data product no SAP BDC?",\n'
    '      "acceptedAnswer": {\n'
    '        "@type": "Answer",\n'
    '        "text": "Um data product é um ativo de dado certificado no BDC — verificado pelo SAP Master Data Governance, alinhado às políticas da empresa e documentado para uso por agentes de IA. É a unidade de dado confiável sobre a qual decisões autônomas podem ser tomadas."\n'
    '      }\n'
    '    },\n'
    '    {\n'
    '      "@type": "Question",\n'
    '      "name": "Por que a governança de dados mestre importa para agentes SAP?",\n'
    '      "acceptedAnswer": {\n'
    '        "@type": "Answer",\n'
    '        "text": "Agentes que operam sobre dados mestre duplicados ou inconsistentes não conseguem distinguir o mesmo cliente com três registros conflitantes. A governança de dados mestre — integrada nativamente ao BDC desde 2026 — garante que o contexto usado pelo agente para decidir seja único, verificado e atualizado."\n'
    '      }\n'
    '    },\n'
    '    {\n'
    '      "@type": "Question",\n'
    '      "name": "Como a Solveplan implementa o BDC como Knowledge Core?",\n'
    '      "acceptedAnswer": {\n'
    '        "@type": "Answer",\n'
    '        "text": "A Solveplan inicia com uma avaliação de maturidade de dados: unificação de dados mestre, mapeamento de hierarquias organizacionais e identificação das fontes a integrar. A implementação é estruturada em camadas — começando pelos fundamentos de governança — para garantir que os agentes SAP operem com o contexto correto desde o primeiro uso em produção."\n'
    '      }\n'
    '    }\n'
    '  ]\n'
    '}\n'
    '</script>'
)

schema_widget = {
    "id": "faq_schema_ld",
    "elType": "widget",
    "settings": {"html": faq_schema_html},
    "elements": [],
    "widgetType": "html"
}

last_spacer_idx = next(i for i, e in enumerate(elements) if e['id'] == '34ec670')
elements.insert(last_spacer_idx, schema_widget)
print(f"FAQ JSON-LD widget inserido na posicao {last_spacer_idx}")

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_10689_updated.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

size = len(json.dumps(data, ensure_ascii=False))
print(f"\nArquivo salvo: {out_path}")
print(f"Tamanho: {size} chars")
