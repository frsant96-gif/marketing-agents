import sys, re, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
WP = "https://solveplan.com/wp-json/wp/v2"

DS_URL  = "https://solveplan.com/sap-datasphere/"
BDC_URL = "https://solveplan.com/sap-business-data-cloud/"
BLOG    = "https://solveplan.com/blog/"

def a(text, url):
    return f'<a href="{url}">{text}</a>'

def fetch(pid):
    r = requests.get(f"{WP}/posts/{pid}?context=edit", auth=AUTH)
    return r.json()["content"]["raw"]

def save(pid, content):
    r = requests.post(f"{WP}/posts/{pid}", auth=AUTH, json={"content": content})
    return r.status_code

def lists_to_italic(content):
    def replace_list(m):
        block = m.group(0)
        items = re.findall(r'<li>(.*?)</li>', block, re.DOTALL)
        parts = []
        for item in items:
            clean = item.strip()
            parts.append(f'<!-- wp:paragraph -->\n<p><em>{clean}</em></p>\n<!-- /wp:paragraph -->')
        return '\n\n'.join(parts)
    return re.sub(
        r'<!-- wp:list(?:[^-]|-(?!-))*? -->.*?<!-- /wp:list -->',
        replace_list,
        content,
        flags=re.DOTALL
    )

def add_ds_link_first(content):
    """Add /sap-datasphere/ link to first occurrence of SAP Datasphere (unlinked)."""
    # Match SAP Datasphere NOT already inside an <a> tag
    pattern = r'(?<!\w)(?<!href=")(SAP Datasphere)(?![^<]*<\/a>)'
    linked, n = re.subn(
        pattern,
        f'<a href="{DS_URL}">SAP Datasphere</a>',
        content,
        count=1
    )
    return linked, n

# ─────────────────────────────────────────────────────────────────────────────
# POST 10653 — sap-business-ai-platform
# Issues: wp:list remaining (6), /sap-datasphere/ absent
# ─────────────────────────────────────────────────────────────────────────────
print("── POST 10653 ─────────────────────────────────────────────")
c = fetch(10653)
print(f"  wp:list antes: {c.count('wp:list')}")

# Force-convert any remaining lists (some may use different spacing)
c2 = lists_to_italic(c)
# Also try a broader pattern for edge cases
c2 = re.sub(
    r'<!-- wp:list[^>]*>.*?<!-- /wp:list -->',
    lambda m: '\n\n'.join([
        f'<!-- wp:paragraph -->\n<p><em>{item.strip()}</em></p>\n<!-- /wp:paragraph -->'
        for item in re.findall(r'<li>(.*?)</li>', m.group(0), re.DOTALL)
    ]),
    c2,
    flags=re.DOTALL
)
print(f"  wp:list depois: {c2.count('wp:list')}")

# Add /sap-datasphere/ link
c2, added = add_ds_link_first(c2)
print(f"  DS link adicionado: {added > 0}")

print(f"  Salvar: {save(10653, c2)}")

# ─────────────────────────────────────────────────────────────────────────────
# POST 10688 — sap-autonomous-suite
# Issues: /sap-datasphere/ absent, no concrete numbers
# ─────────────────────────────────────────────────────────────────────────────
print("\n── POST 10688 ─────────────────────────────────────────────")
c = fetch(10688)

# Add /sap-datasphere/ link
c, added = add_ds_link_first(c)
print(f"  DS link adicionado: {added > 0}")

# Add concrete number context (GEO) — enrich existing paragraph about SAPPHIRE
# The intro para mentions "mais de 200 agentes e 50 assistentes" — add it if not there
if 'mais de 200 agentes' not in c:
    c = c.replace(
        'O SAP Autonomous Suite é o conjunto de aplicações SAP equipadas com agentes de IA',
        'Com mais de 200 agentes e 50 assistentes prontos para operar no SAP SAPPHIRE 2026, o SAP Autonomous Suite é o conjunto de aplicações SAP equipadas com agentes de IA'
    )
    print("  GEO: número concreto adicionado (200 agentes)")
else:
    print("  GEO: número já presente")

print(f"  Salvar: {save(10688, c)}")

# ─────────────────────────────────────────────────────────────────────────────
# POST 10689 — sap-bdc-knowledge-core
# Issues: keyword "SAP Business Data Cloud" not in meta_desc (uses "SAP BDC")
# Fix: meta_desc already has BDC context — keyword issue is in the checker logic
# Content is fine; just update excerpt to ensure keyword is explicit
# ─────────────────────────────────────────────────────────────────────────────
print("\n── POST 10689 ─────────────────────────────────────────────")
# Meta description already mentions SAP BDC — update to include full "SAP Business Data Cloud"
new_desc_10689 = "O SAP Business Data Cloud (BDC) transforma o Knowledge Graph genérico da SAP no contexto específico da sua empresa. Entenda data products, Domain Models e governança de dados."
upd = requests.post(f"{WP}/posts/10689", auth=AUTH, json={
    "excerpt": new_desc_10689,
    "meta": {"rank_math_description": new_desc_10689}
})
print(f"  Meta desc atualizada: {upd.status_code}")
print(f"  Nova desc: {new_desc_10689[:80]}...")

# Content check — no changes needed
c = fetch(10689)
c2, added = add_ds_link_first(c)
if c2 != c:
    print(f"  DS link adicionado: {added > 0}")
    print(f"  Salvar: {save(10689, c2)}")
else:
    print("  DS link já presente")

# ─────────────────────────────────────────────────────────────────────────────
# POST 10690 — sap-joule-work
# Issues: no concrete numbers (GEO)
# ─────────────────────────────────────────────────────────────────────────────
print("\n── POST 10690 ─────────────────────────────────────────────")
c = fetch(10690)

# Add concrete number — "mais de 35 soluções SAP" is already in the Word doc content
if 'mais de 35' not in c and '35 soluções' not in c:
    c = c.replace(
        'O Joule está disponível no <a href="https://solveplan.com/sap-datasphere/">SAP Datasphere</a>',
        'O Joule está disponível em mais de 35 soluções SAP, incluindo o <a href="https://solveplan.com/sap-datasphere/">SAP Datasphere</a>'
    )
    print("  GEO: '35 soluções SAP' adicionado")
else:
    print("  GEO: número já presente")

# Check DS link
if DS_URL not in c:
    c, added = add_ds_link_first(c)
    print(f"  DS link adicionado: {added > 0}")

print(f"  Salvar: {save(10690, c)}")

# ─────────────────────────────────────────────────────────────────────────────
# POST 10691 — sap-knowledge-graph
# Issues: /sap-datasphere/ absent
# ─────────────────────────────────────────────────────────────────────────────
print("\n── POST 10691 ─────────────────────────────────────────────")
c = fetch(10691)
c2, added = add_ds_link_first(c)
print(f"  DS link adicionado: {added > 0}")
print(f"  Salvar: {save(10691, c2)}")

# ─────────────────────────────────────────────────────────────────────────────
# POST 10692 — sap-anthropic-parceria
# Issues: keyword "SAP Anthropic" not in first 300 chars, not in meta_desc,
#         no concrete numbers, no comparison phrase
# ─────────────────────────────────────────────────────────────────────────────
print("\n── POST 10692 ─────────────────────────────────────────────")
c = fetch(10692)

# Fix 1: keyword in first paragraph — add "SAP Anthropic" to opening
old_intro = 'A parceria entre SAP e Anthropic vai além de adicionar um modelo de linguagem ao portfólio.'
new_intro = 'A parceria SAP e Anthropic vai além de adicionar um modelo de linguagem ao portfólio.'
c = c.replace(old_intro, new_intro, 1)

# Fix 2: add concrete number (GEO) — the word doc mentions "200+ agentes"
if '200' not in c and 'mais de 200' not in c:
    c = c.replace(
        'Claude passa a ser a camada de raciocínio dos agentes que vão operar seus processos SAP.',
        'Claude passa a ser a camada de raciocínio dos mais de 200 agentes SAP que operam seus processos de ponta a ponta.'
    )
    print("  GEO: '200 agentes' adicionado")

# Fix 3: add comparison phrase (GEO)
if 'ao contrário' not in c.lower() and 'diferente de' not in c.lower():
    old_para = 'Fluxos de trabalho no ERP raramente são lineares.'
    new_para = 'Ao contrário de modelos de linguagem genéricos, que respondem com base em texto da internet, o Claude opera dentro do contexto do SAP Knowledge Graph — com acesso às políticas reais da empresa. Fluxos de trabalho no ERP raramente são lineares.'
    c = c.replace(old_para, new_para, 1)
    print("  GEO: comparação 'Ao contrário de' adicionada")

# Fix 4: DS link
c2, added = add_ds_link_first(c)
if added:
    c = c2
    print(f"  DS link adicionado: sim")

print(f"  Salvar: {save(10692, c)}")

# Update meta_desc to include keyword explicitly
new_desc_10692 = "A parceria SAP e Anthropic integra o Claude como modelo de raciocínio dos agentes Joule. Entenda o que isso significa para finanças, RH e compras no seu ambiente SAP."
upd = requests.post(f"{WP}/posts/10692", auth=AUTH, json={
    "excerpt": new_desc_10692,
    "meta": {"rank_math_description": new_desc_10692}
})
print(f"  Meta desc atualizada: {upd.status_code}")

# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("VERIFICAÇÃO FINAL")
print("="*60)

post_ids = [10653, 10688, 10689, 10690, 10691, 10692]
for pid in post_ids:
    c = fetch(pid)
    lists_left   = c.count('wp:list')
    ds_link      = DS_URL in c
    bdc_link     = BDC_URL in c
    faq          = c.count('wp:details')
    noreferrer   = 'noreferrer' in c
    numbers      = bool(re.search(r'\b\d+\s*(?:%|mil|mais de \d|agentes|soluções|tabelas|campos|anos|dias)', c, re.IGNORECASE))

    status = "✅" if (lists_left == 0 and ds_link and bdc_link and faq >= 4 and not noreferrer) else "⚠️"
    print(f"  {status} {pid}: wp:list={lists_left} | DS={ds_link} | BDC={bdc_link} | FAQ={faq} | noreferrer={noreferrer}")
