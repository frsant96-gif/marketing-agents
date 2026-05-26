import sys, json, requests, re
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

faqs = [
    {
        "id": "faq-question-584d1895",
        "question": "O que é o SAP Business AI Platform?",
        "answer": "O SAP Business AI Platform é a arquitetura unificada da SAP que integra SAP BTP, SAP Business Data Cloud e SAP AI Foundation em uma fundação única para construir, implantar e governar agentes de IA com contexto de negócio real. Foi apresentada no SAP SAPPHIRE Orlando 2026 como base da visão Autonomous Enterprise."
    },
    {
        "id": "faq-question-3a1c8bcc",
        "question": "Qual é a diferença entre SAP Business AI Platform e SAP BTP?",
        "answer": "O SAP BTP é o ambiente de desenvolvimento e integração da SAP. O SAP Business AI Platform é a arquitetura mais ampla que unifica SAP BTP, SAP Business Data Cloud e SAP AI Foundation. O BTP continua sendo o ambiente de desenvolvimento, agora como parte de uma estrutura orientada a agentes."
    },
    {
        "id": "faq-question-d9737f64",
        "question": "O que é o Joule e como ele se encaixa na plataforma?",
        "answer": "Joule é o assistente de IA da SAP e a camada de orquestração de agentes dentro do SAP Business AI Platform. Coordena workflows fim-a-fim em RH, compras, supply chain e analytics — disponível em mais de 35 soluções SAP, incluindo o SAP Datasphere."
    },
    {
        "id": "faq-question-cc4a1a80",
        "question": "Quem já tem SAP BDC precisa migrar para o SAP Business AI Platform?",
        "answer": "Não é uma migração — é uma evolução. O SAP Business Data Cloud é um dos componentes centrais do SAP Business AI Platform. Quem já implementou BDC está na fundação correta para adotar os agentes Joule e o SAP Autonomous Suite."
    },
    {
        "id": "faq-question-eb1a9a6a",
        "question": "Qual é o papel da parceria entre SAP e Anthropic?",
        "answer": "A Anthropic fornece modelos Claude como opção dentro do SAP AI Foundation, ao lado de OpenAI, Google e outros. A empresa escolhe o provedor; a governança e o contexto de negócio são mantidos centralizados dentro do ecossistema SAP."
    },
    {
        "id": "faq-question-2160b2d9",
        "question": "Como a Solveplan apoia empresas nessa transição?",
        "answer": "A Solveplan implementa SAP BDC e SAP Datasphere — a fundação de dados necessária para operar o SAP Business AI Platform com contexto real de negócio. Para empresas que querem avaliar seu posicionamento atual, a Solveplan realiza diagnósticos de maturidade analítica como ponto de partida."
    }
]

questions_json = json.dumps([
    {"id": f["id"], "title": f["question"], "content": f["answer"]}
    for f in faqs
], ensure_ascii=False)

html_items = ""
for f in faqs:
    html_items += (
        f'<div class="rank-math-faq-item" id="{f["id"]}">'
        f'<h3 class="rank-math-question">{f["question"]}</h3>'
        f'<div class="rank-math-answer"><p>{f["answer"]}</p></div>'
        f'</div>'
    )

faq_block = (
    f'<!-- wp:rank-math/faq-block {{"questions":{questions_json}}} -->\n'
    f'<div class="rank-math-faq wp-block-rank-math-faq-block">{html_items}</div>\n'
    f'<!-- /wp:rank-math/faq-block -->'
)

# Fetch current content
resp = requests.get(
    "https://solveplan.com/wp-json/wp/v2/posts/10653?context=edit",
    auth=HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
)
current_content = resp.json()["content"]["raw"]

# Replace the Yoast FAQ block with Rank Math FAQ block
new_content = re.sub(
    r'<!-- wp:yoast/faq-block.*?<!-- /wp:yoast/faq-block -->',
    faq_block,
    current_content,
    flags=re.DOTALL
)

update = requests.post(
    "https://solveplan.com/wp-json/wp/v2/posts/10653",
    auth=HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU"),
    json={"content": new_content}
)

print("Status HTTP:", update.status_code)

# Verify
verify = requests.get(
    "https://solveplan.com/wp-json/wp/v2/posts/10653?context=edit",
    auth=HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
)
saved = verify.json()["content"]["raw"]
faq_start = saved.find("rank-math-faq-item")
print("\nHTML salvo (primeira pergunta):")
print(saved[faq_start:faq_start+250] if faq_start > 0 else "rank-math block nao encontrado")
