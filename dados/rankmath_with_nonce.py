import requests, sys, re, json
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')
AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")

POSTS_SEO = [
    {
        "id": 10653,
        "title": "SAP Business AI Platform: o que mudou no SAPPHIRE 2026",
        "description": "O SAP Business AI Platform unifica SAP BTP, SAP BDC e AI Foundation em uma arquitetura única. Veja o que mudou no SAPPHIRE 2026 e o impacto para sua empresa.",
        "focuskw": "SAP Business AI Platform",
        "canonical": "https://solveplan.com/blog/sap-business-ai-platform/",
    },
    {
        "id": 10688,
        "title": "SAP Autonomous Suite: o que foi anunciado no SAPPHIRE 2026",
        "description": "O SAP Autonomous Suite automatiza finanças, supply chain e RH com agentes de IA. Entenda os 5 domínios, o Autonomous Close Assistant e o que sua empresa precisa fazer agora.",
        "focuskw": "SAP Autonomous Suite",
        "canonical": "https://solveplan.com/blog/sap-autonomous-suite/",
    },
    {
        "id": 10689,
        "title": "SAP Business Data Cloud: o Knowledge Core que os agentes SAP precisam",
        "description": "O SAP Business Data Cloud transforma o Knowledge Graph da SAP no contexto específico da sua empresa. Entenda data products, Domain Models e governança de dados.",
        "focuskw": "SAP Business Data Cloud",
        "canonical": "https://solveplan.com/blog/sap-bdc-knowledge-core/",
    },
    {
        "id": 10690,
        "title": "SAP Joule Work: o que mudou e o que isso significa para quem usa SAP",
        "description": "O SAP Joule Work executa processos em linguagem natural — lançamentos, workflows e análises no SAP Datasphere. Entenda o que mudou no Joule e o impacto para usuários SAP.",
        "focuskw": "SAP Joule Work",
        "canonical": "https://solveplan.com/blog/sap-joule-work/",
    },
    {
        "id": 10691,
        "title": "SAP Knowledge Graph: o que é e por que os agentes SAP dependem dele",
        "description": "O SAP Knowledge Graph mapeia 452 mil tabelas do S/4HANA para dar contexto real aos agentes SAP. Entenda a abordagem neuro-simbólica e o que isso significa para o seu negócio.",
        "focuskw": "SAP Knowledge Graph",
        "canonical": "https://solveplan.com/blog/sap-knowledge-graph/",
    },
    {
        "id": 10692,
        "title": "SAP e Anthropic: por que o Claude virou o motor dos agentes SAP",
        "description": "A parceria SAP e Anthropic integra o Claude como modelo de raciocínio dos agentes Joule. Entenda o que isso significa para finanças, RH e compras no seu ambiente SAP.",
        "focuskw": "SAP Anthropic",
        "canonical": "https://solveplan.com/blog/sap-anthropic-parceria/",
    },
]

# Step 1: Get a fresh nonce for each post via its editor page
def get_nonce(post_id):
    r = requests.get(
        f"https://solveplan.com/wp-admin/post.php?post={post_id}&action=edit",
        auth=AUTH
    )
    matches = re.findall(r'"nonce"\s*:\s*"([a-zA-Z0-9_-]{8,20})"', r.text)
    # Also try WP REST nonce patterns
    matches2 = re.findall(r'"rest_nonce"\s*:\s*"([a-zA-Z0-9_-]{8,20})"', r.text)
    matches3 = re.findall(r'wpApiSettings.*?"nonce"\s*:\s*"([a-zA-Z0-9_-]{8,20})"', r.text, re.DOTALL)
    all_nonces = matches + matches2 + matches3
    return all_nonces[0] if all_nonces else None

# Step 2: Try updateMeta with nonce in header and body
print("Testando com nonce extraído da página de edição...\n")

nonce = get_nonce(10688)
print(f"Nonce para post 10688: {nonce}")

if nonce:
    # Try with X-WP-Nonce header
    r = requests.post(
        "https://solveplan.com/wp-json/rankmath/v1/updateMeta",
        auth=AUTH,
        headers={"X-WP-Nonce": nonce},
        json={
            "objectID": 10688,
            "objectType": "post",
            "meta": {
                "focuskw": "SAP Autonomous Suite",
                "description": "O SAP Autonomous Suite automatiza finanças, supply chain e RH com agentes de IA. Entenda os 5 domínios, o Autonomous Close Assistant e o que sua empresa precisa fazer agora.",
                "title": "SAP Autonomous Suite: o que foi anunciado no SAPPHIRE 2026",
            }
        }
    )
    print(f"Com X-WP-Nonce: {r.status_code} {r.text[:150]}")

    # Try with security in body
    r2 = requests.post(
        "https://solveplan.com/wp-json/rankmath/v1/updateMeta",
        auth=AUTH,
        json={
            "objectID": 10688,
            "objectType": "post",
            "security": nonce,
            "meta": {
                "focuskw": "SAP Autonomous Suite",
                "description": "O SAP Autonomous Suite automatiza finanças, supply chain e RH com agentes de IA.",
            }
        }
    )
    print(f"Com security no body: {r2.status_code} {r2.text[:150]}")

    # Try admin-ajax.php with the nonce
    r3 = requests.post(
        "https://solveplan.com/wp-admin/admin-ajax.php",
        auth=AUTH,
        data={
            "action": "rank_math_save_post_meta",
            "security": nonce,
            "post_id": 10688,
            "rank_math_focus_keyword": "SAP Autonomous Suite",
            "rank_math_description": "O SAP Autonomous Suite automatiza finanças, supply chain e RH com agentes de IA.",
        }
    )
    print(f"admin-ajax rank_math_save_post_meta: {r3.status_code} {r3.text[:200]}")
