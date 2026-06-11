import re, sys, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "vjpT R0lO 9c2G vh2w WAqA RPfU")
WP = "https://solveplan.com/wp-json/wp/v2"

CSS = """<style>
.sw-faq-section{max-width:800px;margin:0 auto;padding:0 16px}
.sw-faq-section h2{font-size:22px;font-weight:700;color:#1a2e4a;margin-bottom:32px;text-align:center}
.sw-faq-item{border-bottom:1px solid #e2e8f0;padding:0}
.sw-faq-item:first-of-type{border-top:1px solid #e2e8f0}
.sw-faq-question{width:100%;background:none!important;border:none!important;outline:none!important;box-shadow:none!important;-webkit-appearance:none;appearance:none;text-align:left;padding:20px 8px;font-size:16px;font-weight:600;color:#1a2e4a!important;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;line-height:1.4;text-decoration:none!important}
.sw-faq-question:hover,.sw-faq-question:focus,.sw-faq-question:active,.sw-faq-question:visited{color:#0b1a2e!important;background:none!important;border:none!important;outline:none!important;box-shadow:none!important;text-decoration:none!important}
.sw-faq-icon{flex-shrink:0;width:24px;height:24px;border-radius:50%;background:#0057B8;color:#fff;display:flex;align-items:center;justify-content:center;font-size:18px;line-height:1;transition:transform 0.2s}
.sw-faq-item.open .sw-faq-icon{transform:rotate(45deg)}
.sw-faq-answer{display:none;padding:0 8px 20px;font-size:15px;color:#4a5568;line-height:1.7}
.sw-faq-item.open .sw-faq-answer{display:block}
</style>"""

JS = """<script>
function swToggleFaq(btn){var item=btn.closest('.sw-faq-item');var isOpen=item.classList.contains('open');document.querySelectorAll('.sw-faq-item.open').forEach(function(el){el.classList.remove('open')});if(!isOpen)item.classList.add('open')}
</script>"""


def build_faq_html(title, faqs):
    clean = lambda s: re.sub(r'<[^>]+>', '', s).replace('"', "'")
    schema_items = ',\n'.join(
        f'    {{"@type":"Question","name":"{clean(q)}","acceptedAnswer":{{"@type":"Answer","text":"{clean(a)}"}}}}'
        for q, a in faqs
    )
    schema = (
        '<script type="application/ld+json">\n'
        '{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n  "mainEntity": [\n'
        + schema_items + '\n  ]\n}\n</script>'
    )

    items_html = '\n\n'.join(
        f'  <div class="sw-faq-item">\n'
        f'    <button class="sw-faq-question" onclick="swToggleFaq(this)">\n'
        f'      {q}\n'
        f'      <span class="sw-faq-icon">+</span>\n'
        f'    </button>\n'
        f'    <div class="sw-faq-answer">{a}</div>\n'
        f'  </div>'
        for q, a in faqs
    )

    div = f'<div class="sw-faq-section">\n  <h2>{title}</h2>\n\n{items_html}\n</div>'

    return (
        '\n\n<!-- wp:html -->\n'
        + schema + '\n\n'
        + CSS + '\n\n'
        + div + '\n\n'
        + JS
        + '\n<!-- /wp:html -->'
    )


def extract_faq_details(raw):
    """Extrai (title, [(q, a)]) dos wp:details existentes no conteudo."""
    title_m = re.search(
        r'<!-- wp:heading \{"level":5\} -->\s*<h5[^>]*><strong>(FAQ[^<]+)</strong></h5>\s*<!-- /wp:heading -->',
        raw
    )
    title = title_m.group(1).strip() if title_m else "FAQ"

    pattern = re.compile(
        r'<!-- wp:details -->\s*'
        r'<details[^>]*><summary>(.*?)</summary>'
        r'<!-- wp:paragraph -->\s*<p>(.*?)</p>\s*<!-- /wp:paragraph -->'
        r'</details>\s*<!-- /wp:details -->',
        re.DOTALL
    )
    faqs = [(m.group(1).strip(), m.group(2).strip()) for m in pattern.finditer(raw)]
    return title, faqs


def replace_faq(raw, new_block):
    """Substitui do H5 FAQ (inclusive) até o H5 Fontes (exclusive) ou fim."""
    # Localiza inicio do bloco FAQ (H5 ou wp:details direto)
    faq_h5 = re.search(
        r'\n\n<!-- wp:heading \{"level":5\} -->\s*<h5[^>]*><strong>FAQ',
        raw
    )
    if not faq_h5:
        # Tenta achar primeiro wp:details
        faq_h5 = re.search(r'\n\n<!-- wp:details -->', raw)

    if not faq_h5:
        print("  Nenhuma secao FAQ encontrada — appendando")
        return raw + new_block

    start = faq_h5.start()

    # Para posts de blog: preservar secao Fontes
    fontes = re.search(
        r'\n\n<!-- wp:heading \{"level":5\} -->\s*<h5[^>]*><strong>Fontes</strong>',
        raw[start:]
    )
    if fontes:
        end = start + fontes.start()
        return raw[:start] + new_block + '\n\n' + raw[end:].lstrip('\n')
    else:
        return raw[:start] + new_block


POSTS = [
    {"id": 10689, "type": "posts"},
    {"id": 10692, "type": "posts"},
    {"id": 10653, "type": "posts"},
    {"id": 10688, "type": "posts"},
    {"id": 10690, "type": "posts"},
    {"id": 10691, "type": "posts"},
    {"id": 10585, "type": "case"},
    {"id": 10310, "type": "case"},
    {"id": 10305, "type": "case"},
    {"id": 10297, "type": "case"},
    {"id": 10307, "type": "case"},
    {"id": 704,   "type": "case"},
]

for item in POSTS:
    pid = item["id"]
    endpoint = f"{WP}/{item['type']}/{pid}"
    print(f"\n{'='*50}")
    print(f"Post {pid} ({item['type']})")

    r = requests.get(f"{endpoint}?context=edit", auth=AUTH)
    raw = r.json()["content"]["raw"]

    title, faqs = extract_faq_details(raw)
    if not faqs:
        print(f"  AVISO: nenhum wp:details encontrado — pulando")
        continue

    print(f"  FAQ: {len(faqs)} itens — '{title}'")
    new_block = build_faq_html(title, faqs)
    new_raw = replace_faq(raw, new_block)

    r2 = requests.post(endpoint, auth=AUTH, json={"content": new_raw})
    print(f"  Update: {r2.status_code}")

    v = requests.get(f"{endpoint}?context=edit", auth=AUTH).json()["content"]["raw"]
    print(f"  wp:details restantes: {v.count('wp:details') // 2}")
    print(f"  wp:html FAQ:          {'OK' if 'sw-faq-section' in v else 'AUSENTE'}")
    print(f"  JSON-LD FAQPage:      {'OK' if 'FAQPage' in v else 'AUSENTE'}")
    print(f"  CTA:                  {'OK' if 'bdcstrategy' in v else 'AUSENTE'}")

print("\nConcluido.")
