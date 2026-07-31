import sys, json, re, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "vjpT R0lO 9c2G vh2w WAqA RPfU")
POST_ID = 10484

faqs = [
    {
        "q": "O que é sustentação analítica SAP?",
        "a": "É um conjunto de processos, ferramentas e especialistas dedicados a garantir que a camada de dados de um ERP SAP permaneça íntegra após a implementação, permitindo que os dados sejam usados para apoiar decisões de negócio em ferramentas como SAP Analytics Cloud e Power BI."
    },
    {
        "q": "Qual a diferença entre implementação e sustentação analítica de um ERP SAP?",
        "a": "A implementação é o projeto que coloca o ERP SAP em funcionamento, com o go-live como marco final. A sustentação analítica SAP começa depois do go-live e garante que o sistema continue gerando valor: dados corretos, governança de qualidade e regras de negócio atualizadas conforme o mercado muda."
    },
    {
        "q": "Quais são os 3 pilares da sustentação analítica SAP?",
        "a": "Única fonte da verdade (dado correto do ERP até ferramentas como Power BI e SAP Analytics Cloud), governança e qualidade (identificação de erros de cadastro) e evolução de contexto (atualização das regras de negócio conforme o mercado muda)."
    },
    {
        "q": "Quanto tempo depois do go-live devo contratar sustentação analítica SAP?",
        "a": "O ideal é planejar a sustentação analítica SAP já durante o projeto de implementação, para que ela comece a atuar a partir do go-live. Quanto mais tempo o ERP SAP opera sem esse acompanhamento, maior o risco de dados fragmentados e processos burocráticos se consolidarem."
    },
    {
        "q": "Como a Solveplan ajuda na sustentação analítica SAP pós go-live?",
        "a": "A Solveplan atua em quatro dimensões — Pessoas, Processos, Tecnologia e Governança — para garantir que o ERP SAP continue gerando valor estratégico depois do go-live, com mais de 200 soluções entregues e 90 clientes atendidos."
    },
]

schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
        for f in faqs
    ]
}
schema_json = json.dumps(schema, ensure_ascii=False)

items_html = ""
for f in faqs:
    items_html += f"""  <div class="site-faq-item">
    <button class="site-faq-question" onclick="siteToggleFaq(this)">
      {f["q"]}
      <span class="site-faq-icon">+</span>
    </button>
    <div class="site-faq-answer">
      {f["a"]}
    </div>
  </div>
"""

faq_html_block = f"""<script type="application/ld+json">
{schema_json}
</script>

<style>
.site-faq-section {{
  max-width: 800px;
  margin: 0 auto;
  padding: 0 16px;
}}
.site-faq-section h2 {{
  font-size: 22px;
  font-weight: 700;
  color: #1a2e4a;
  margin-bottom: 32px;
  text-align: center;
}}
.site-faq-item {{
  border-bottom: 1px solid #e2e8f0;
  padding: 0;
}}
.site-faq-item:first-of-type {{
  border-top: 1px solid #e2e8f0;
}}
.site-faq-question {{
  width: 100%;
  background: none !important;
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  -webkit-appearance: none;
  appearance: none;
  text-align: left;
  padding: 20px 8px;
  font-size: 16px;
  font-weight: 600;
  color: #1a2e4a !important;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  line-height: 1.4;
  text-decoration: none !important;
}}
.site-faq-question:hover,
.site-faq-question:focus,
.site-faq-question:active,
.site-faq-question:visited {{
  color: #0b1a2e !important;
  background: none !important;
  border: none !important;
  outline: none !important;
  box-shadow: none !important;
  text-decoration: none !important;
}}
.site-faq-icon {{
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #0057B8;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  line-height: 1;
  transition: transform 0.2s;
}}
.site-faq-item.open .site-faq-icon {{
  transform: rotate(45deg);
}}
.site-faq-answer {{
  display: none;
  padding: 0 8px 20px;
  font-size: 15px;
  color: #4a5568;
  line-height: 1.7;
}}
.site-faq-item.open .site-faq-answer {{
  display: block;
}}
</style>

<div class="site-faq-section">
  <h2>Perguntas frequentes sobre sustentação analítica SAP</h2>
{items_html}</div>

<script>
function siteToggleFaq(btn) {{
  var item = btn.closest('.site-faq-item');
  var isOpen = item.classList.contains('open');
  document.querySelectorAll('.site-faq-item.open').forEach(function(el) {{
    el.classList.remove('open');
  }});
  if (!isOpen) item.classList.add('open');
}}
</script>"""

new_faq_block = f"<!-- wp:html -->\n{faq_html_block}\n<!-- /wp:html -->"

resp = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit", auth=AUTH)
content = resp.json()["content"]["raw"]

# Remove the old "FAQ — ..." H2 heading (the standalone one before the rank-math block)
old_heading_pattern = re.compile(
    r'<!-- wp:heading[^>]*-->\s*<h[2-6][^>]*>FAQ.{0,3}Sustenta.{0,3}o anal.{0,3}tica SAP em ERP</h[2-6]>\s*<!-- /wp:heading -->\s*'
)
content, n1 = old_heading_pattern.subn("", content)
print("Removida heading FAQ antiga:", n1)

# Replace the rank-math faq-block with the new themed HTML block
old_faq_pattern = re.compile(r'<!-- wp:rank-math/faq-block.*?<!-- /wp:rank-math/faq-block -->', re.DOTALL)
new_content, n2 = old_faq_pattern.subn(new_faq_block, content)
print("Substituido bloco FAQ:", n2)

if n1 == 0 or n2 == 0:
    print("AVISO: algum padrao nao foi encontrado, nada sera salvo.")
    sys.exit(1)

update = requests.post(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}", auth=AUTH, json={"content": new_content})
print("Update content - Status:", update.status_code)
if update.status_code >= 400:
    print(update.json())

elementor_data = [{
    "id": "seo10484root",
    "elType": "container",
    "settings": {},
    "elements": [{
        "id": "seo10484widget",
        "elType": "widget",
        "settings": {"editor": new_content, "text_color": "#000000"},
        "elements": [],
        "widgetType": "text-editor"
    }],
    "isInner": False
}]
update2 = requests.post(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}", auth=AUTH, json={"meta": {"_elementor_data": json.dumps(elementor_data, ensure_ascii=False)}})
print("Update elementor_data - Status:", update2.status_code)

verify = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit&_fields=content", auth=AUTH)
c = verify.json()["content"]["raw"]
print("Tem site-faq-section:", "site-faq-section" in c)
print("Tem rank-math/faq-block ainda:", "rank-math/faq-block" in c)
print("Tem script FAQPage:", "FAQPage" in c)
