import requests, json, xmlrpc.client

WP_URL = 'https://solveplan.com'
AUTH   = ('administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU')
PAGE_ID = 10736

# ── 1. RankMath via XML-RPC ───────────────────────────────────────────────────
print('Configurando RankMath...')
client = xmlrpc.client.ServerProxy(f'{WP_URL}/xmlrpc.php')
result = client.wp.editPost(1, 'administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU', PAGE_ID, {
    'custom_fields': [
        {'key': 'rank_math_title',
         'value': 'Solve Watch | Monitoramento e Observabilidade para SAP Datasphere'},
        {'key': 'rank_math_description',
         'value': ('Solve Watch e a plataforma de observabilidade para SAP Datasphere da Solveplan. '
                   'Monitoramento 24/7, alertas proativos de falha, controle de Capacity Units e '
                   'historico de ate 6 meses, em uma tela, sem configuracao complexa.')},
        {'key': 'rank_math_focus_keyword',
         'value': 'monitoramento SAP Datasphere'},
        {'key': 'rank_math_seo_score',
         'value': ''},
    ]
})
print(f'  RankMath: {"OK" if result else "ERRO"}')

# ── 2. Fix H1 + heading capitalisation via Elementor API ─────────────────────
print('Corrigindo headings no Elementor...')
r = requests.get(f'{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}', params={'context':'edit'}, auth=AUTH)
el_data = json.loads(r.json().get('meta',{}).get('_elementor_data','[]'))

changes = []

def patch(nodes):
    for node in nodes:
        if node.get('widgetType') == 'heading':
            s = node.get('settings', {})
            nid = node.get('id', '')
            title = s.get('title', '')

            # Fix H1: Solve Watch
            if nid == 'decd53e' and s.get('header_size') != 'h1':
                s['header_size'] = 'h1'
                changes.append('H1 corrigido: Solve Watch')

            # Fix capitalisation
            if 'pROBLEMA' in title:
                s['title'] = 'O Problema'
                changes.append('Capitalização corrigida: O Problema')

            # Fix "SAP Dataphere" typo
            if 'Dataphere' in title:
                s['title'] = title.replace('Dataphere', 'Datasphere')
                changes.append('Typo corrigido: Dataphere -> Datasphere')

        patch(node.get('elements', []))

patch(el_data)

# ── 3. Add internal links to bridge text and solution text ───────────────────
INTERNAL_LINKS = {
    # widget id : inject links into text
    '2e5b137': (
        'Esses problemas tem uma causa comum: o SAP Datasphere nativo nao foi projetado '
        'para monitoramento. O Solve Watch resolve isso com visibilidade real, alertas '
        'proativos e governanca automatica. Saiba mais sobre '
        '<a href="https://solveplan.com/sap-datasphere/">SAP Datasphere</a> e como a '
        '<a href="https://solveplan.com/sobre/">Solveplan</a> pode ajudar.'
    ),
}

def patch_links(nodes):
    for node in nodes:
        nid = node.get('id','')
        if node.get('widgetType') == 'text-editor' and nid in INTERNAL_LINKS:
            node['settings']['editor'] = f'<p>{INTERNAL_LINKS[nid]}</p>'
            changes.append(f'Links internos adicionados: widget {nid}')
        patch_links(node.get('elements', []))

patch_links(el_data)

if changes:
    resp = requests.post(
        f'{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}',
        auth=AUTH,
        json={'meta': {'_elementor_data': json.dumps(el_data)}}
    )
    resp.raise_for_status()
    print('Alteracoes no Elementor:')
    for c in changes:
        print(f'  [OK] {c}')
else:
    print('  Nenhuma alteracao necessaria no Elementor.')

print()
print('SEO configurado. Resumo:')
print('  Title:     Solve Watch | Monitoramento e Observabilidade para SAP Datasphere')
print('  Descricao: Plataforma de observabilidade Solveplan para SAP Datasphere')
print('  Focus KW:  monitoramento SAP Datasphere')
print('  H1:        Solve Watch')
print('  Headings:  corrigidos')
print('  Links int: +2 adicionados')
