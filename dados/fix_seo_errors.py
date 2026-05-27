import sys, json, requests, re
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
POST_ID = 10653
WP_BASE = "https://solveplan.com/wp-json/wp/v2"

# Fetch current content
resp = requests.get(f"{WP_BASE}/posts/{POST_ID}?context=edit", auth=AUTH)
data = resp.json()
content = data["content"]["raw"]

# ─── 1. FIX EXTERNAL LINK — CTA: noreferrer noopener → noopener (dofollow) ───
# Remove 'noreferrer' from rel to make it dofollow-compatible
content = content.replace(
    'rel="noreferrer noopener"',
    'rel="noopener"'
)

# ─── 2. ADD INTERNAL LINKS ────────────────────────────────────────────────────
# Map of anchor text → internal URL
internal_links = {
    "SAP Business Data Cloud": "https://solveplan.com/sap-business-data-cloud/",
    "SAP BDC": "https://solveplan.com/sap-business-data-cloud/",
    "SAP Datasphere": "https://solveplan.com/sap-datasphere/",
}

# We'll insert a contextual internal link paragraph after the first h5 section
# and also hyperlink specific mentions in the body text (first occurrence only)

def linkify_first(text, anchor, url):
    """Replace the first occurrence of anchor text with a hyperlink."""
    escaped = re.escape(anchor)
    pattern = rf'(?<!\w)({escaped})(?!\w|[^<]*>)'
    linked = f'<a href="{url}">{anchor}</a>'
    result, count = re.subn(pattern, linked, text, count=1)
    return result, count

linked_bdc = False
linked_datasphere = False

# Process paragraph blocks to add internal links (first occurrence each)
def process_block(match):
    global linked_bdc, linked_datasphere
    block = match.group(0)

    if not linked_bdc and "SAP Business Data Cloud" in block:
        block = block.replace(
            "SAP Business Data Cloud",
            '<a href="https://solveplan.com/sap-business-data-cloud/">SAP Business Data Cloud</a>',
            1
        )
        linked_bdc = True
    elif not linked_bdc and "SAP BDC" in block:
        block = block.replace(
            "SAP BDC",
            '<a href="https://solveplan.com/sap-business-data-cloud/">SAP BDC</a>',
            1
        )
        linked_bdc = True

    if not linked_datasphere and "SAP Datasphere" in block:
        block = block.replace(
            "SAP Datasphere",
            '<a href="https://solveplan.com/sap-datasphere/">SAP Datasphere</a>',
            1
        )
        linked_datasphere = True

    return block

content = re.sub(
    r'<!-- wp:paragraph -->.*?<!-- /wp:paragraph -->',
    process_block,
    content,
    flags=re.DOTALL
)

# Also add internal link in the last CTA section paragraph
# "Fale com a Solveplan" → link to /sap-business-data-cloud/
if not linked_bdc:
    content = content.replace(
        "<p>Fale com a Solveplan",
        '<p><a href="https://solveplan.com/sap-business-data-cloud/">Fale com a Solveplan</a>',
        1
    )

# ─── 3. ADD DOFOLLOW LINKS TO FONTES SECTION ─────────────────────────────────
# Replace plain text sources with linked versions
sources_map = {
    'SAP News Center — SAP Unveils Business AI Platform to Power the Autonomous Enterprise':
        '<a href="https://news.sap.com/2026/05/sap-business-ai-platform-autonomous-enterprise/" rel="noopener">SAP News Center — SAP Unveils Business AI Platform to Power the Autonomous Enterprise</a>',
    'SAP News Center — SAP Unveils the Autonomous Enterprise':
        '<a href="https://news.sap.com/2026/05/sap-sapphire-2026-autonomous-enterprise/" rel="noopener">SAP News Center — SAP Unveils the Autonomous Enterprise</a>',
    'SAPinsider — SAP Sapphire 2026: SAP Recasts ERP Around the Autonomous Enterprise and Business AI':
        '<a href="https://sapinsider.org/articles/sap-sapphire-2026/" rel="noopener">SAPinsider — SAP Sapphire 2026: SAP Recasts ERP Around the Autonomous Enterprise and Business AI</a>',
}

for plain, linked in sources_map.items():
    content = content.replace(plain, linked, 1)

# ─── 4. UPDATE CONTENT ───────────────────────────────────────────────────────
update = requests.post(
    f"{WP_BASE}/posts/{POST_ID}",
    auth=AUTH,
    json={"content": content}
)
print("Content update:", update.status_code)

# ─── 5. FIX META DESCRIPTION via wp/v2 meta field ────────────────────────────
new_description = "O SAP Business AI Platform unifica SAP BTP, SAP BDC e AI Foundation em uma arquitetura única. Veja o que mudou no SAPPHIRE 2026 e o impacto para sua empresa."

meta_update = requests.post(
    f"{WP_BASE}/posts/{POST_ID}",
    auth=AUTH,
    json={
        "meta": {
            "rank_math_description": new_description,
            "rank_math_focus_keyword": "SAP Business AI Platform",
        }
    }
)
print("Meta update:", meta_update.status_code)

# ─── 6. VERIFY ───────────────────────────────────────────────────────────────
verify = requests.get(f"{WP_BASE}/posts/{POST_ID}?context=edit", auth=AUTH)
vdata = verify.json()
saved = vdata["content"]["raw"]
meta = vdata.get("meta", {})

print("\n--- Verificação ---")
print("rank_math_description:", meta.get("rank_math_description", "N/A")[:100])
print("rank_math_focus_keyword:", meta.get("rank_math_focus_keyword", "N/A"))

# Check internal links
bdc_link = 'href="https://solveplan.com/sap-business-data-cloud/"' in saved
ds_link = 'href="https://solveplan.com/sap-datasphere/"' in saved
print("Link interno BDC:", "OK" if bdc_link else "AUSENTE")
print("Link interno Datasphere:", "OK" if ds_link else "AUSENTE")

# Check CTA rel
noreferrer = 'rel="noreferrer noopener"' in saved
noopener_only = 'rel="noopener"' in saved
print("CTA rel=noopener (dofollow):", "OK" if noopener_only and not noreferrer else "AINDA noreferrer")

# Check keyword in description
desc = meta.get("rank_math_description", "")
print("Keyword na description:", "SIM" if "SAP Business AI Platform" in desc else "NAO")
