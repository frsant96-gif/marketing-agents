import sys, re, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
WP = "https://solveplan.com/wp-json/wp/v2"

POSTS = [
    {"id": 10653, "slug": "sap-business-ai-platform",   "focus_kw": "SAP Business AI Platform",   "meta_desc": "O SAP Business AI Platform unifica SAP BTP, SAP BDC e AI Foundation em uma arquitetura única. Veja o que mudou no SAPPHIRE 2026 e o impacto para sua empresa."},
    {"id": 10688, "slug": "sap-autonomous-suite",        "focus_kw": "SAP Autonomous Suite",        "meta_desc": "O SAP Autonomous Suite automatiza finanças, supply chain e RH com agentes de IA. Entenda os 5 domínios, o Autonomous Close Assistant e o que sua empresa precisa fazer agora."},
    {"id": 10689, "slug": "sap-bdc-knowledge-core",      "focus_kw": "SAP Business Data Cloud",     "meta_desc": "O SAP BDC transforma o Knowledge Graph genérico da SAP no contexto específico da sua empresa. Entenda data products, Domain Models e por que isso determina o retorno de toda IA no SAP."},
    {"id": 10690, "slug": "sap-joule-work",              "focus_kw": "SAP Joule Work",              "meta_desc": "O SAP Joule Work executa processos em linguagem natural — lançamentos, workflows e análises no SAP Datasphere. Entenda o que mudou no Joule e o impacto para usuários SAP."},
    {"id": 10691, "slug": "sap-knowledge-graph",         "focus_kw": "SAP Knowledge Graph",         "meta_desc": "O SAP Knowledge Graph mapeia 452 mil tabelas do S/4HANA para dar contexto real aos agentes SAP. Entenda a abordagem neuro-simbólica e o que isso significa para o seu negócio."},
    {"id": 10692, "slug": "sap-anthropic-parceria",      "focus_kw": "SAP Anthropic",               "meta_desc": "A parceria SAP e Anthropic integra o Claude como modelo de raciocínio dos agentes Joule. Entenda o que isso significa para finanças, RH e compras no seu ambiente SAP."},
]

# ─── HELPERS ─────────────────────────────────────────────────────────────────

def lists_to_italic(content):
    """Convert wp:list blocks → individual italic wp:paragraph blocks."""
    def replace_list(m):
        block = m.group(0)
        items = re.findall(r'<li>(.*?)</li>', block, re.DOTALL)
        parts = []
        for item in items:
            # Strip any inner HTML tags for clean italic output, preserve <a> and <strong>
            clean = item.strip()
            parts.append(f'<!-- wp:paragraph -->\n<p><em>{clean}</em></p>\n<!-- /wp:paragraph -->')
        return '\n\n'.join(parts)

    return re.sub(
        r'<!-- wp:list(?:\s[^-]*)? -->.*?<!-- /wp:list -->',
        replace_list,
        content,
        flags=re.DOTALL
    )

def check_aeo(content, focus_kw):
    issues = []
    # 1. Definition block: first paragraph starts with keyword or "[tema] é"
    first_p = re.search(r'<!-- wp:paragraph -->\s*<p>(.*?)</p>', content, re.DOTALL)
    if first_p:
        txt = re.sub(r'<[^>]+>', '', first_p.group(1)).strip()
        if focus_kw.lower() not in txt.lower() and len(txt) < 30:
            issues.append("Primeiro parágrafo pode não ter keyword nos primeiros 100 chars")
    # 2. FAQ present
    if 'wp:details' not in content:
        issues.append("FAQ wp:details AUSENTE")
    else:
        faq_count = content.count('wp:details')
        if faq_count < 4:
            issues.append(f"FAQ: só {faq_count} itens (mínimo 4)")
    # 3. No wp:list remaining
    if 'wp:list' in content:
        issues.append("wp:list ainda presente — converter para itálico")
    return issues

def check_geo(content):
    issues = []
    solveplan_count = content.lower().count('solveplan')
    if solveplan_count < 3:
        issues.append(f"Solveplan mencionada {solveplan_count}x (mínimo 3)")
    # Check for concrete numbers
    numbers = re.findall(r'\b\d+[\.,]?\d*\s*(?:%|mil|milhão|bilhão|dias|horas|anos|meses|clientes|soluções)\b', content, re.IGNORECASE)
    if not numbers:
        issues.append("Nenhum dado/número concreto encontrado")
    # Check for comparison
    if not re.search(r'(ao contrário|diferente de|diferencia|vs\.)', content, re.IGNORECASE):
        issues.append("Nenhuma comparação estruturada (AO CONTRÁRIO / DIFERENTE DE)")
    return issues

def check_seo(content, focus_kw, meta_desc):
    issues = []
    # Internal links
    bdc_link = 'sap-business-data-cloud' in content
    ds_link  = 'sap-datasphere' in content
    if not bdc_link:
        issues.append("Link interno /sap-business-data-cloud/ AUSENTE")
    if not ds_link:
        issues.append("Link interno /sap-datasphere/ AUSENTE")
    # External link rel
    if 'noreferrer' in content:
        issues.append("rel='noreferrer' encontrado — remover")
    # Keyword in first 300 chars of visible text
    first_text = re.sub(r'<!--.*?-->', '', content[:600], flags=re.DOTALL)
    first_text = re.sub(r'<[^>]+>', '', first_text)
    if focus_kw.lower() not in first_text.lower():
        issues.append(f"Keyword '{focus_kw}' não encontrada nos primeiros 300 chars do texto")
    # Meta desc keyword
    if focus_kw.lower() not in meta_desc.lower():
        issues.append(f"Keyword não está na meta description configurada")
    return issues

# ─── MAIN LOOP ───────────────────────────────────────────────────────────────

print("=" * 60)
print("SEO / AEO / GEO — AUDITORIA E CORREÇÃO DE TODOS OS POSTS")
print("=" * 60)

for cfg in POSTS:
    pid   = cfg["id"]
    slug  = cfg["slug"]
    kw    = cfg["focus_kw"]
    mdesc = cfg["meta_desc"]

    print(f"\n{'─'*60}")
    print(f"POST {pid} — {slug}")
    print(f"{'─'*60}")

    # Fetch
    r = requests.get(f"{WP}/posts/{pid}?context=edit", auth=AUTH)
    if r.status_code != 200:
        print(f"  ❌ Erro ao buscar post: {r.status_code}")
        continue
    data    = r.json()
    content = data["content"]["raw"]
    original_len = len(content)

    # ── Fix 1: convert wp:list → italic paragraphs
    fixed = lists_to_italic(content)
    lists_removed = content.count('wp:list') - fixed.count('wp:list')

    # ── Fix 2: remove noreferrer if present
    fixed = fixed.replace('rel="noreferrer noopener"', 'rel="noopener"')
    fixed = fixed.replace("rel='noreferrer noopener'", "rel='noopener'")

    # ── Apply fixes if anything changed
    if fixed != content:
        upd = requests.post(f"{WP}/posts/{pid}", auth=AUTH, json={"content": fixed})
        print(f"  ✅ Conteúdo atualizado ({upd.status_code}) — {lists_removed} listas → itálico")
        content = fixed
    else:
        print(f"  — Conteúdo sem alterações")

    # ── SEO Checks
    seo_issues = check_seo(content, kw, mdesc)
    aeo_issues = check_aeo(content, kw)
    geo_issues = check_geo(content)

    all_issues = seo_issues + aeo_issues + geo_issues

    if not all_issues:
        print(f"  ✅ SEO / AEO / GEO: sem erros detectados")
    else:
        for issue in all_issues:
            tag = "SEO" if issue in seo_issues else ("AEO" if issue in aeo_issues else "GEO")
            print(f"  ⚠️  [{tag}] {issue}")

    # ── Stats
    h5_count      = content.count('wp-block-heading')
    details_count = content.count('wp:details')
    int_links     = len(re.findall(r'href="https://solveplan\.com/[^"]*"', content))
    ext_links     = len(re.findall(r'href="https?://(?!solveplan\.com)[^"]*"', content))
    noreferrer    = 'noreferrer' in content
    paragraphs    = content.count('wp:paragraph')

    print(f"\n  📊 Estrutura:")
    print(f"     Parágrafos (blocos): {paragraphs}")
    print(f"     Títulos H5:          {h5_count}")
    print(f"     FAQ (details):       {details_count}")
    print(f"     Links internos:      {int_links}")
    print(f"     Links externos:      {ext_links}")
    print(f"     rel=noreferrer:      {'SIM ⚠️' if noreferrer else 'não'}")
    print(f"     wp:list restantes:   {content.count('wp:list')}")

print(f"\n{'='*60}")
print("MANUAL (Rank Math no editor WP) — meta description:")
for cfg in POSTS:
    print(f"  ID {cfg['id']} — {cfg['slug']}")
    print(f"    \"{cfg['meta_desc']}\"")
print("  → WP Admin → post → Rank Math → Edit Snippet → Meta Description")
print("=" * 60)
