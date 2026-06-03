import requests, json, uuid

WP_URL = 'https://solveplan.com'
AUTH   = ('administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU')

def uid(): return uuid.uuid4().hex[:7]

# Fetch current data
r = requests.get(f'{WP_URL}/wp-json/wp/v2/pages/10736', params={'context':'edit'}, auth=AUTH)
el_data = json.loads(r.json().get('meta',{}).get('_elementor_data','[]'))

def find_node(nodes, nid):
    for node in nodes:
        if node.get('id') == nid: return node
        found = find_node(node.get('elements',[]), nid)
        if found: return found
    return None

# Collect preserved containers
hero_banner  = find_node(el_data, '8b6622f')
problema     = find_node(el_data, '1353cba')
bridge_text  = find_node(el_data, '2e5b137')
solucao      = find_node(el_data, '7b58099')
mais_func    = find_node(el_data, 'd2069dd')
tabela_intro = find_node(el_data, 'f55b293')
tabela_html  = find_node(el_data, 'e9330a2')
logos        = find_node(el_data, 'd11c430')
faq          = find_node(el_data, 'ca7112a')
footer_cta   = find_node(el_data, 'bb5edde')
spacer       = find_node(el_data, '8532acb')
db6c258      = find_node(el_data, 'db6c258')
h1_node      = find_node(el_data, 'decd53e')

# Fix corrupted GEO text
geo_node = find_node([db6c258], '0d2a7bd') if db6c258 else None
if geo_node:
    geo_node['settings']['editor'] = (
        '<p><strong>O Solve Watch e uma plataforma SaaS de observabilidade e governanca '
        'para SAP Datasphere</strong>, desenvolvida pela Solveplan, consultoria SAP com '
        '13 anos de atuacao e mais de 390 projetos entregues na America Latina. '
        'A plataforma oferece monitoramento 24/7 com atualizacao automatica a cada '
        '30 minutos, historico de execucoes de ate 6 meses, alertas proativos de falha '
        'e controle de Capacity Units, funcionalidades que o ambiente nativo do '
        'SAP Datasphere nao entrega nativamente.</p>'
    )
    print('[OK] GEO text restaurado')

# Remove button from inside db6c258/50c9cfe (it will go in CTA section)
fifty_node = find_node([db6c258], '50c9cfe') if db6c258 else None
if fifty_node:
    fifty_node['elements'] = [
        e for e in fifty_node.get('elements', [])
        if e.get('id') not in ('78c6af0',)
    ]
    # Also clean 78c6af0 container (had button + spacer)
    for child in fifty_node.get('elements', []):
        child['elements'] = [
            e for e in child.get('elements', [])
            if e.get('widgetType') not in ('button', 'spacer')
        ]

# Restore logos carousel
LOGO_IDS = [9786, 9778, 9791, 9798, 9789, 9788, 9781, 9784, 9779, 10337]
logo_slides = []
for lid in LOGO_IDS:
    mr = requests.get(f'{WP_URL}/wp-json/wp/v2/media/{lid}', auth=AUTH).json()
    logo_slides.append({
        'image': {'id': lid, 'url': mr.get('source_url',''), 'alt': mr.get('alt_text','')},
        'caption': '', 'link': {'url': ''}
    })
carousel_logos = find_node([logos], 'c7ee312') if logos else None
if carousel_logos:
    carousel_logos['settings']['slides'] = logo_slides
    carousel_logos['settings'].update({
        'autoplay': 'yes', 'autoplay_speed': 3000,
        'slides_to_show': '5', 'navigation': 'none', 'infinite': 'yes'
    })
    print(f'[OK] Logos restaurados: {len(logo_slides)} logos')

# Recreate missing feature sections
def make_feature(title, body):
    return {
        'id': uid(), 'elType': 'container', 'settings': {},
        'elements': [
            {'id': uid(), 'elType': 'widget', 'widgetType': 'heading',
             'settings': {'title': title, 'header_size': 'h2'}, 'elements': []},
            {'id': uid(), 'elType': 'widget', 'widgetType': 'text-editor',
             'settings': {'editor': f'<p>{body}</p>'}, 'elements': []},
        ]
    }

features_section = {
    'id': uid(), 'elType': 'container', 'settings': {},
    'elements': [
        make_feature('Calendario de Cargas',
            'Visao mensal de todas as execucoes. Em 2 segundos voce sabe se a semana foi tranquila ou problematica sem abrir nenhum outro painel.'),
        make_feature('Analise de Performance',
            'Identifica os objetos mais lentos como CDS Views, Analytic Models e Transformation Flows com duracao media, CPU e memoria. Tuning onde realmente importa.'),
        make_feature('Controle de Capacity Units',
            'Visao de consumo por objeto, por Space e por area de negocio. Antecipe o estouro antes da fatura chegar.'),
        make_feature('Heatmap de Concorrencia',
            'Heatmap 7 dias por 24 horas dos Replication Flows programados. Identifica janelas criticas de sobrecarga antes do colapso. Funcionalidade unica no mercado brasileiro.'),
    ]
}
print('[OK] Feature sections recriadas')

# CTA section
cta_html = (
    '<style>'
    '.sw-cta-final{text-align:center;padding:48px 24px}'
    '.sw-cta-final p{font-size:18px;color:#1a2e4a;margin-bottom:24px;line-height:1.6}'
    '.sw-cta-final a{display:inline-block;background:#0057B8;color:#fff!important;'
    'padding:16px 36px;border-radius:6px;font-size:15px;font-weight:600;'
    'text-decoration:none!important;transition:background .2s}'
    '.sw-cta-final a:hover{background:#0041a0!important}'
    '</style>'
    '<div class="sw-cta-final">'
    '<p>Pronto para ter visibilidade real do seu ambiente SAP Datasphere?</p>'
    '<a href="#demo">Solicitar demonstracao do Solve Watch</a>'
    '</div>'
)
cta_section = {
    'id': uid(), 'elType': 'container', 'settings': {},
    'elements': [{'id': uid(), 'elType': 'widget', 'widgetType': 'html',
                  'settings': {'html': cta_html}, 'elements': []}]
}

# Subtitle widget
subtitle = {
    'id': 'c70bd3d', 'elType': 'widget', 'widgetType': 'text-editor',
    'settings': {'editor': '<p>Plataforma de observabilidade e governanca para SAP Datasphere. Tenha visibilidade total do seu ambiente em uma tela, 24 horas por dia.</p>'},
    'elements': []
}

# Final storytelling order
main_elements = [
    h1_node,           # 1. H1: Solve Watch
    subtitle,          # 2. Subtitulo
    db6c258,           # 3. Hero: carousel 3 telas + GEO text
    problema,          # 4. O Problema (dor)
    bridge_text,       # 5. Causa comum (ponte)
    tabela_intro,      # 6. O que o SAP nativo nao entrega (amplifica dor)
    tabela_html,       # 7. Tabela comparativa
    solucao,           # 8. A Solucao
    features_section,  # 9. Como funciona (features)
    mais_func,         # 10. Mais Funcionalidades
    cta_section,       # 11. CTA
    logos,             # 12. Logos clientes (prova social)
    faq,               # 13. FAQ (quebra objecoes)
    footer_cta,        # 14. Dados que movem decisoes
    spacer,            # 15. Spacer
]

main_container = {
    'id': 'ad9763c',
    'elType': 'container',
    'settings': find_node(el_data, 'ad9763c').get('settings', {}),
    'elements': [e for e in main_elements if e is not None]
}

new_el_data = [hero_banner, main_container]

# Push to WordPress
resp = requests.post(
    f'{WP_URL}/wp-json/wp/v2/pages/10736',
    auth=AUTH,
    json={'meta': {'_elementor_data': json.dumps(new_el_data)}}
)
resp.raise_for_status()
print('\n[OK] Pagina reconstruida e publicada.')
print('\nOrdem final do storytelling:')
labels = [
    'H1: Solve Watch', 'Subtitulo', 'Hero: carousel + GEO text',
    'O Problema', 'Causa comum (ponte)', 'O que o SAP nativo nao entrega',
    'Tabela comparativa', 'A Solucao', 'Features (Calendario/Performance/Capacity/Heatmap)',
    'Mais Funcionalidades', 'CTA', 'Logos clientes', 'FAQ', 'Footer CTA', 'Spacer'
]
for i, label in enumerate(labels, 1):
    print(f'  {i:02d}. {label}')
