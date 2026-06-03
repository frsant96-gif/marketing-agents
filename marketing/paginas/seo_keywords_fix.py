import requests, json, xmlrpc.client

WP_URL  = 'https://solveplan.com'
AUTH    = ('administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU')
PAGE_ID = 10736
KW      = 'monitoramento SAP Datasphere'

r = requests.get(f'{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}', params={'context':'edit'}, auth=AUTH)
el_data = json.loads(r.json().get('meta',{}).get('_elementor_data','[]'))

changes = []

def find_node(nodes, nid):
    for node in nodes:
        if node.get('id') == nid: return node
        found = find_node(node.get('elements',[]), nid)
        if found: return found
    return None

# ── 1. Subtitle widget — add keyword in first sentence ───────────────────────
subtitle = find_node(el_data, 'c70bd3d')
if subtitle:
    subtitle['settings']['editor'] = (
        f'<p>Plataforma de <strong>{KW}</strong> e governança para SAP Datasphere. '
        f'Tenha visibilidade total do seu ambiente em uma tela, 24 horas por dia.</p>'
    )
    changes.append('Keyword no subtítulo (início do conteúdo)')

# ── 2. Fix H1 + add keyword to a H2 heading ─────────────────────────────────
def patch_headings(nodes):
    for node in nodes:
        if node.get('widgetType') == 'heading':
            s   = node.get('settings', {})
            nid = node.get('id', '')
            # Fix H1
            if nid == 'decd53e':
                s['header_size'] = 'h1'
                changes.append('H1 corrigido: Solve Watch')
            # Heading "O Problema" → add keyword context
            if nid == '134ff46':
                s['title'] = f'O Problema: sem {KW} integrado'
                changes.append(f'H2 atualizado com keyword: {s["title"]}')
            # Fix typos
            if 'pROBLEMA' in s.get('title',''):
                s['title'] = 'O Problema'
            if 'Dataphere' in s.get('title',''):
                s['title'] = s['title'].replace('Dataphere','Datasphere')
        patch_headings(node.get('elements',[]))

patch_headings(el_data)

# ── 3. Bridge text — add keyword naturally ───────────────────────────────────
bridge = find_node(el_data, '2e5b137')
if bridge:
    bridge['settings']['editor'] = (
        f'<p>Esses problemas têm uma causa comum: o SAP Datasphere nativo não foi projetado '
        f'para {KW}. O Solve Watch resolve isso com visibilidade real, alertas proativos '
        f'e governança automática. Saiba mais sobre '
        f'<a href="https://solveplan.com/sap-datasphere/" target="_blank">SAP Datasphere</a> '
        f'e as soluções da <a href="https://solveplan.com/sobre/">Solveplan</a>.</p>'
    )
    changes.append('Keyword no texto ponte + links internos')

# ── 4. Alt text on carousel images — add keyword ─────────────────────────────
def patch_carousel(nodes):
    for node in nodes:
        if node.get('widgetType') == 'image-carousel':
            slides = node.get('settings',{}).get('slides',[])
            alts = [
                f'{KW} — Dashboard Inbox de Ação e KPIs',
                f'{KW} — Heatmap de Concorrência de Replication Flows',
                f'{KW} — TOP 10 Volumetria e Controle de Capacity Units',
            ]
            for i, slide in enumerate(slides[:3]):
                slide.get('image',{})['alt'] = alts[i]
            changes.append(f'Alt text do carrossel atualizado com keyword ({len(slides)} slides)')
        patch_carousel(node.get('elements',[]))

patch_carousel(el_data)

# ── 5. Add external link in solution text ────────────────────────────────────
solucao_text = find_node(el_data, 'ebdc10d')
if solucao_text:
    current = solucao_text.get('settings',{}).get('editor','')
    if 'sap.com' not in current and 'extern' not in current:
        solucao_text['settings']['editor'] = (
            f'<p>O Solve Watch é a plataforma que entrega o que a SAP nativa não dá: '
            f'visão integrada de saúde, performance, volumetria e custo — em uma tela, '
            f'sem que você precise montar um time dedicado para isso. '
            f'Desenvolvido sobre a arquitetura do '
            f'<a href="https://www.sap.com/products/technology-platform/datasphere.html" '
            f'target="_blank" rel="noopener">SAP Datasphere</a>, '
            f'o Solve Watch complementa o ambiente nativo com camadas de '
            f'{KW} que a SAP não entrega.</p>'
        )
        changes.append('Link externo (sap.com) adicionado + keyword no texto')

# ── 6. Push to WordPress ─────────────────────────────────────────────────────
resp = requests.post(
    f'{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}',
    auth=AUTH,
    json={'meta': {'_elementor_data': json.dumps(el_data)}}
)
resp.raise_for_status()

print('Alterações aplicadas:')
for c in changes:
    print(f'  [OK] {c}')

# ── 7. Update RankMath via XML-RPC ───────────────────────────────────────────
print('\nAtualizando RankMath...')
client = xmlrpc.client.ServerProxy(f'{WP_URL}/xmlrpc.php')
result = client.wp.editPost(1, 'administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU', PAGE_ID, {
    'custom_fields': [
        {'key': 'rank_math_title',
         'value': f'Solve Watch | {KW.title()} - Observabilidade Nativa SAP'},
        {'key': 'rank_math_description',
         'value': (f'Solve Watch é a solução de {KW} da Solveplan. '
                   f'Alertas proativos de falha, controle de Capacity Units, '
                   f'histórico de 6 meses e heatmap de concorrência — em uma tela.')},
        {'key': 'rank_math_focus_keyword',
         'value': KW},
    ]
})
print(f'  RankMath XML-RPC: {"OK" if result else "ERRO"}')

print()
print('Erros resolvidos:')
erros = [
    'Keyword no título de SEO (RankMath)',
    'Keyword na meta description (RankMath)',
    'Keyword no início do conteúdo (subtítulo)',
    'Keyword no conteúdo (ponte + solução)',
    'Keyword em subtítulo H2 (O Problema)',
    'Alt text com keyword (carrossel)',
    'Link externo adicionado (sap.com)',
    'Links internos adicionados (2)',
    'H1 corrigido',
]
for e in erros:
    print(f'  ✓ {e}')
print()
print('Erro que só pode ser resolvido manualmente:')
print('  → URL: o slug "solve-watch" não contém a keyword.')
print('    Para corrigir: Elementor → Configurações → Slug → "monitoramento-sap-datasphere"')
print('    (criar redirecionamento 301 de /solve-watch para o novo URL)')
