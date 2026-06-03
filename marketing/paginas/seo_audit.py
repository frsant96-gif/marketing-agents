import requests, json, re, xmlrpc.client

WP_URL = 'https://solveplan.com'
AUTH   = ('administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU')

r = requests.get(f'{WP_URL}/wp-json/wp/v2/pages/10736', params={'context':'edit'}, auth=AUTH)
page    = r.json()
content = page.get('content',{}).get('rendered','')

# RankMath via XML-RPC
client  = xmlrpc.client.ServerProxy(f'{WP_URL}/xmlrpc.php')
post    = client.wp.getPost(1, 'administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU', 10736, ['custom_fields'])
rm      = {f['key']: f['value'] for f in post.get('custom_fields', []) if 'rank_math' in f['key']}

print('=== RANKMATH ===')
print('Title:      ', rm.get('rank_math_title', 'NAO CONFIGURADO'))
print('Descricao:  ', rm.get('rank_math_description', 'NAO CONFIGURADO'))
print('Focus KW:   ', rm.get('rank_math_focus_keyword', 'NAO CONFIGURADO'))

print()
print('=== HEADINGS ===')
headings = re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', content, re.DOTALL)
for tag, text in headings:
    clean = re.sub(r'<[^>]+>', '', text).strip()[:70]
    if clean:
        print(f'  H{tag}: {clean}')

print()
print('=== IMAGENS ===')
imgs    = re.findall(r'<img[^>]+>', content, re.DOTALL)
no_alt  = [i for i in imgs if 'alt=""' in i]
ok_alt  = [i for i in imgs if 'alt="' in i and 'alt=""' not in i]
print(f'  Total: {len(imgs)} | Com alt: {len(ok_alt)} | Sem alt: {len(no_alt)}')

print()
print('=== SCHEMA MARKUP ===')
has_schema = 'application/ld+json' in content
print(f'  JSON-LD presente: {has_schema}')

print()
print('=== LINKS ===')
int_links = re.findall(r'href="(https?://solveplan\.com[^"]*)"', content)
ext_links = re.findall(r'href="(https?://(?!solveplan\.com)[^"]+)"', content)
print(f'  Internos: {len(int_links)}')
print(f'  Externos: {len(ext_links)}')

print()
print('=== CONTEUDO ===')
text  = re.sub(r'<[^>]+>', ' ', content)
words = len(text.split())
print(f'  Palavras estimadas: {words}')

kws = ['SAP Datasphere', 'monitoramento', 'observabilidade', 'Capacity Units',
       'alertas', 'governanca', 'Solve Watch', 'Solveplan']
print('  Densidade de keywords:')
for kw in kws:
    count = len(re.findall(re.escape(kw), content, re.IGNORECASE))
    print(f'    {kw}: {count}x')
