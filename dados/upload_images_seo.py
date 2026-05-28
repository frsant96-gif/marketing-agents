import sys, requests, json, re
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
WP = "https://solveplan.com/wp-json/wp/v2"

POSTS = [
    {
        "id": 10688,
        "slug": "sap-autonomous-suite",
        "title": "SAP Autonomous Suite: como a SAP vai automatizar finanças, supply chain e RH com agentes de IA",
        "excerpt": "O SAP Autonomous Suite automatiza finanças, supply chain e RH com agentes de IA. Entenda os 5 domínios, o Autonomous Close Assistant e o que sua empresa precisa fazer agora.",
        "focus_kw": "SAP Autonomous Suite",
        "alt_text": "SAP Autonomous Suite — agentes de IA automatizando finanças, supply chain e RH no SAPPHIRE 2026",
        "img_url": "https://export-download.canva.com/L7G-4/DAHK-SL7G-4/-1/0/0001-6459792411635889539.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260527%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260527T224939Z&X-Amz-Expires=71373&X-Amz-Signature=44123b0e4d7dfd70b749ea497fed62f8bdc3babb5e89af33188b8a388a49fa67&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Thu%2C%2028%20May%202026%2018%3A39%3A12%20GMT",
        "img_name": "sap-autonomous-suite-featured.jpg",
    },
    {
        "id": 10689,
        "slug": "sap-bdc-knowledge-core",
        "title": "SAP BDC como Knowledge Core: por que os agentes SAP precisam conhecer a sua empresa, não só o SAP",
        "excerpt": "O SAP Business Data Cloud transforma o Knowledge Graph da SAP no contexto específico da sua empresa. Entenda data products, Domain Models e governança de dados.",
        "focus_kw": "SAP Business Data Cloud",
        "alt_text": "SAP Business Data Cloud como Knowledge Core — camada de dados para agentes SAP",
        "img_url": "https://export-download.canva.com/kX0bU/DAHK-SkX0bU/-1/0/0001-5797763267236405844.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260527%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260527T220938Z&X-Amz-Expires=74192&X-Amz-Signature=6e65cee6a92b023d835593d49d77acfbd2ed896bb768fe61ee6f7e023069d35a&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Thu%2C%2028%20May%202026%2018%3A46%3A10%20GMT",
        "img_name": "sap-bdc-knowledge-core-featured.jpg",
    },
    {
        "id": 10690,
        "slug": "sap-joule-work",
        "title": "SAP Joule Work: de assistente de chat a camada operacional do ERP",
        "excerpt": "O SAP Joule Work executa processos em linguagem natural — lançamentos, workflows e análises no SAP Datasphere. Entenda o que mudou no Joule e o impacto para usuários SAP.",
        "focus_kw": "SAP Joule Work",
        "alt_text": "SAP Joule Work — interface de linguagem natural operando processos do ERP SAP",
        "img_url": "https://export-download.canva.com/fhWjw/DAHK-afhWjw/-1/0/0001-6459792412845327561.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260527%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260527T181722Z&X-Amz-Expires=87834&X-Amz-Signature=f2196213468498af4a8c9d7d2cbb1968119fc05db0c299efb716c862da6c20de&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Thu%2C%2028%20May%202026%2018%3A41%3A16%20GMT",
        "img_name": "sap-joule-work-featured.jpg",
    },
    {
        "id": 10691,
        "slug": "sap-knowledge-graph",
        "title": "SAP Knowledge Graph: a camada que faz os agentes SAP entenderem o seu negócio",
        "excerpt": "O SAP Knowledge Graph mapeia 452 mil tabelas do S/4HANA para dar contexto real aos agentes SAP. Entenda a abordagem neuro-simbólica e o que isso significa para o seu negócio.",
        "focus_kw": "SAP Knowledge Graph",
        "alt_text": "SAP Knowledge Graph — rede de conhecimento estruturado para agentes SAP",
        "img_url": "https://export-download.canva.com/mCHqI/DAHK-UmCHqI/-1/0/0001-1749027203431581543.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260528T083643Z&X-Amz-Expires=35521&X-Amz-Signature=d899dda32380e56ba28ac3077b6578f26e314397e708c913759a5f6ad284c866&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Thu%2C%2028%20May%202026%2018%3A28%3A44%20GMT",
        "img_name": "sap-knowledge-graph-featured.jpg",
    },
    {
        "id": 10692,
        "slug": "sap-anthropic-parceria",
        "title": "SAP e Anthropic: por que o Claude se tornou o motor de raciocínio dos agentes SAP",
        "excerpt": "A parceria SAP e Anthropic integra o Claude como modelo de raciocínio dos agentes Joule. Entenda o que isso significa para finanças, RH e compras no seu ambiente SAP.",
        "focus_kw": "SAP Anthropic",
        "alt_text": "Parceria SAP e Anthropic — Claude como motor de raciocínio dos agentes SAP",
        "img_url": "https://export-download.canva.com/248pk/DAHK-Q248pk/-1/0/0001-3085470394549654359.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260528T071102Z&X-Amz-Expires=42460&X-Amz-Signature=eef2a1fe3f1ccd87a1707a9a3d2a5fa54c193428f65c0d35dfa73f1105949e86&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Thu%2C%2028%20May%202026%2018%3A58%3A42%20GMT",
        "img_name": "sap-anthropic-parceria-featured.jpg",
    },
]

# Fetch existing category ID for "Blog" or create mapping
def get_category_id(name="Blog"):
    r = requests.get(f"{WP}/categories?search={name}&per_page=10", auth=AUTH)
    cats = r.json()
    if cats and isinstance(cats, list):
        return cats[0]["id"]
    return None

cat_id = get_category_id("Blog")
print(f"Categoria Blog ID: {cat_id}")

# Also check for SAP category
r_cats = requests.get(f"{WP}/categories?per_page=50", auth=AUTH)
all_cats = {c["name"]: c["id"] for c in r_cats.json()} if r_cats.ok else {}
print("Categorias disponíveis:", list(all_cats.keys())[:15])

results = []

for cfg in POSTS:
    pid = cfg["id"]
    print(f"\n{'─'*50}")
    print(f"POST {pid} — {cfg['slug']}")

    # ── 1. Download image from Canva
    img_resp = requests.get(cfg["img_url"], timeout=30)
    if img_resp.status_code != 200:
        print(f"  ❌ Falha ao baixar imagem: {img_resp.status_code}")
        continue
    print(f"  ✅ Imagem baixada: {len(img_resp.content)//1024}KB")

    # ── 2. Upload to WordPress media
    upload = requests.post(
        f"{WP}/media",
        auth=AUTH,
        headers={
            "Content-Disposition": f'attachment; filename="{cfg["img_name"]}"',
            "Content-Type": "image/jpeg",
        },
        data=img_resp.content,
    )
    if upload.status_code not in (200, 201):
        print(f"  ❌ Falha upload: {upload.status_code} {upload.text[:100]}")
        continue

    media_id = upload.json()["id"]
    print(f"  ✅ Upload OK — Media ID: {media_id}")

    # ── 3. Set alt text on media
    alt_update = requests.post(
        f"{WP}/media/{media_id}",
        auth=AUTH,
        json={"alt_text": cfg["alt_text"]}
    )
    print(f"  ✅ Alt text ({alt_update.status_code}): {cfg['alt_text'][:60]}")

    # ── 4. Update post: featured image + excerpt + title + categories
    post_payload = {
        "featured_media": media_id,
        "excerpt": cfg["excerpt"],
    }
    if cat_id:
        post_payload["categories"] = [cat_id]

    post_update = requests.post(
        f"{WP}/posts/{pid}",
        auth=AUTH,
        json=post_payload
    )
    print(f"  ✅ Post atualizado ({post_update.status_code}) — featured_media={media_id}")

    results.append({
        "post_id": pid,
        "slug": cfg["slug"],
        "media_id": media_id,
        "alt_text": cfg["alt_text"],
    })

# ── 5. Summary
print(f"\n{'='*50}")
print("RESUMO FINAL")
print(f"{'='*50}")
for r in results:
    print(f"  ✅ Post {r['post_id']} ({r['slug']}) → Media {r['media_id']}")

print(f"\n{'='*50}")
print("O QUE NÃO É POSSÍVEL VIA API — FAZER MANUAL")
print(f"{'='*50}")
print("""
Rank Math não expõe seus campos via REST API externa.
Requer login no WP Admin + sessão autenticada.

Para cada post, abrir o editor e configurar:
  WP Admin → post → painel Rank Math → Edit Snippet

  ┌─────────────────────────────────────────────────────────────────────────┐
  │ ID 10688 — sap-autonomous-suite                                          │
  │   Focus Keyword:   SAP Autonomous Suite                                  │
  │   SEO Title:       SAP Autonomous Suite: o que foi anunciado no SAPPHIRE │
  │   Meta Description: O SAP Autonomous Suite automatiza finanças, supply   │
  │                     chain e RH com agentes de IA. Entenda os 5 domínios. │
  ├─────────────────────────────────────────────────────────────────────────┤
  │ ID 10689 — sap-bdc-knowledge-core                                        │
  │   Focus Keyword:   SAP Business Data Cloud                               │
  │   SEO Title:       SAP Business Data Cloud: o Knowledge Core que os      │
  │                    agentes SAP precisam                                   │
  │   Meta Description: O SAP Business Data Cloud transforma o Knowledge     │
  │                     Graph da SAP no contexto específico da sua empresa.  │
  ├─────────────────────────────────────────────────────────────────────────┤
  │ ID 10690 — sap-joule-work                                                │
  │   Focus Keyword:   SAP Joule Work                                        │
  │   SEO Title:       SAP Joule Work: o que mudou e o que isso significa    │
  │   Meta Description: O SAP Joule Work executa processos em linguagem      │
  │                     natural — lançamentos e análises no SAP Datasphere.  │
  ├─────────────────────────────────────────────────────────────────────────┤
  │ ID 10691 — sap-knowledge-graph                                           │
  │   Focus Keyword:   SAP Knowledge Graph                                   │
  │   SEO Title:       SAP Knowledge Graph: o que é e por que os agentes     │
  │                    SAP dependem dele                                      │
  │   Meta Description: O SAP Knowledge Graph mapeia 452 mil tabelas do      │
  │                     S/4HANA para dar contexto real aos agentes SAP.      │
  ├─────────────────────────────────────────────────────────────────────────┤
  │ ID 10692 — sap-anthropic-parceria                                        │
  │   Focus Keyword:   SAP Anthropic                                         │
  │   SEO Title:       SAP e Anthropic: por que o Claude virou o motor dos   │
  │                    agentes SAP                                            │
  │   Meta Description: A parceria SAP e Anthropic integra o Claude como     │
  │                     modelo de raciocínio dos agentes Joule no SAP.       │
  └─────────────────────────────────────────────────────────────────────────┘

Post 10653 (sap-business-ai-platform) — mesmo fix manual necessário.
""")
