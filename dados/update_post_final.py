import sys, json, requests, re
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
POST_ID = 10653

# Fetch current content
resp = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit", auth=AUTH)
content = resp.json()["content"]["raw"]

# 1. Convert all H2 headings to H5 bold
# <!-- wp:heading --> ... <h2 ...>Title</h2> ... <!-- /wp:heading -->
# → <!-- wp:heading {"level":5} --> ... <h5 ...><strong>Title</strong></h5> ... <!-- /wp:heading -->

def convert_heading(match):
    full = match.group(0)
    # Extract inner text (strip existing tags)
    inner = re.sub(r'<[^>]+>', '', full)
    inner = inner.replace('<!-- wp:heading', '').replace('<!-- /wp:heading -->', '').strip()
    # Keep H3 subheadings as-is, only convert top-level H2
    if '<h2' in full:
        return (
            '<!-- wp:heading {"level":5} -->\n'
            f'<h5 class="wp-block-heading"><strong>{inner}</strong></h5>\n'
            '<!-- /wp:heading -->'
        )
    elif '<h3' in full:
        return (
            '<!-- wp:heading {"level":5} -->\n'
            f'<h5 class="wp-block-heading"><strong>{inner}</strong></h5>\n'
            '<!-- /wp:heading -->'
        )
    return full

content = re.sub(
    r'<!-- wp:heading[^-]*-->.*?<!-- /wp:heading -->',
    convert_heading,
    content,
    flags=re.DOTALL
)

# 2. Replace CTA button with correct URL and style
cta_block = """<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons">
<!-- wp:button {"backgroundColor":"primary","textColor":"white","style":{"border":{"radius":"4px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-primary-background-color has-text-color has-background wp-element-button" href="https://bdcstrategy.solveplan.ai/" target="_blank" rel="noreferrer noopener">Avalie a maturidade dos seus dados com a Solveplan</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->"""

content = re.sub(
    r'<!-- wp:buttons -->.*?<!-- /wp:buttons -->',
    cta_block,
    content,
    flags=re.DOTALL
)

# 3. Update post content
update_resp = requests.post(
    f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}",
    auth=AUTH,
    json={"content": content}
)
print("Content update:", update_resp.status_code)

# 4. Set Rank Math SEO meta
rank_math_meta = {
    "rank_math_title": "SAP Business AI Platform: o que mudou no SAPPHIRE 2026 e o que isso significa para sua empresa",
    "rank_math_description": "Durante o SAP SAPPHIRE Orlando 2026, a SAP unificou BTP, BDC e AI Foundation em uma única plataforma de IA. Entenda o que muda e o que sua empresa precisa fazer agora.",
    "rank_math_focus_keyword": "SAP Business AI Platform",
    "rank_math_robots": ["index", "follow"],
    "rank_math_og_title": "SAP Business AI Platform: o que a SAP anunciou no SAPPHIRE 2026",
    "rank_math_og_description": "Joule, Knowledge Graph, Anthropic e SAP BDC em uma nova arquitetura. Entenda o impacto prático para quem já usa SAP.",
    "rank_math_twitter_title": "SAP Business AI Platform: o que a SAP anunciou no SAPPHIRE 2026",
    "rank_math_twitter_description": "Joule, Knowledge Graph, Anthropic e SAP BDC em uma nova arquitetura. Entenda o impacto prático para quem já usa SAP.",
    "rank_math_canonical_url": "https://solveplan.com/blog/sap-business-ai-platform/",
}

seo_resp = requests.post(
    f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}",
    auth=AUTH,
    json={"meta": rank_math_meta}
)
print("SEO meta update:", seo_resp.status_code)

# 5. Verify
verify = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit", auth=AUTH)
data = verify.json()
meta = data.get("meta", {})
saved_content = data.get("content", {}).get("raw", "")

print("\n--- Verificação ---")
print("rank_math_title:", meta.get("rank_math_title", "não encontrado"))
print("rank_math_description:", meta.get("rank_math_description", "não encontrado"))
print("rank_math_focus_keyword:", meta.get("rank_math_focus_keyword", "não encontrado"))

# Check first heading
h5_match = re.search(r'<h5[^>]*><strong>(.*?)</strong></h5>', saved_content)
print("Primeiro H5:", h5_match.group(1) if h5_match else "não encontrado")

# Check CTA
cta_match = re.search(r'bdcstrategy\.solveplan\.ai', saved_content)
print("CTA link:", "OK" if cta_match else "não encontrado")
