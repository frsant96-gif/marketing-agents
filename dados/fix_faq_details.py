import sys, json, requests, re
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

faqs = [
    {
        "question": "O que é o SAP Business AI Platform?",
        "answer": "O SAP Business AI Platform é a arquitetura unificada da SAP que integra SAP BTP, SAP Business Data Cloud e SAP AI Foundation em uma fundação única para construir, implantar e governar agentes de IA com contexto de negócio real. Foi apresentada no SAP SAPPHIRE Orlando 2026 como base da visão Autonomous Enterprise."
    },
    {
        "question": "Qual é a diferença entre SAP Business AI Platform e SAP BTP?",
        "answer": "O SAP BTP é o ambiente de desenvolvimento e integração da SAP. O SAP Business AI Platform é a arquitetura mais ampla que unifica SAP BTP, SAP Business Data Cloud e SAP AI Foundation. O BTP continua sendo o ambiente de desenvolvimento, agora como parte de uma estrutura orientada a agentes."
    },
    {
        "question": "O que é o Joule e como ele se encaixa na plataforma?",
        "answer": "Joule é o assistente de IA da SAP e a camada de orquestração de agentes dentro do SAP Business AI Platform. Coordena workflows fim-a-fim em RH, compras, supply chain e analytics — disponível em mais de 35 soluções SAP, incluindo o SAP Datasphere."
    },
    {
        "question": "Quem já tem SAP BDC precisa migrar para o SAP Business AI Platform?",
        "answer": "Não é uma migração — é uma evolução. O SAP Business Data Cloud é um dos componentes centrais do SAP Business AI Platform. Quem já implementou BDC está na fundação correta para adotar os agentes Joule e o SAP Autonomous Suite."
    },
    {
        "question": "Qual é o papel da parceria entre SAP e Anthropic?",
        "answer": "A Anthropic fornece modelos Claude como opção dentro do SAP AI Foundation, ao lado de OpenAI, Google e outros. A empresa escolhe o provedor; a governança e o contexto de negócio são mantidos centralizados dentro do ecossistema SAP."
    },
    {
        "question": "Como a Solveplan apoia empresas nessa transição?",
        "answer": "A Solveplan implementa SAP BDC e SAP Datasphere — a fundação de dados necessária para operar o SAP Business AI Platform com contexto real de negócio. Para empresas que querem avaliar seu posicionamento atual, a Solveplan realiza diagnósticos de maturidade analítica como ponto de partida."
    }
]

# Build native wp:details blocks (WordPress 6.1+ accordion)
details_blocks = ""
for f in faqs:
    details_blocks += (
        f'\n<!-- wp:details -->\n'
        f'<details class="wp-block-details"><summary>{f["question"]}</summary>'
        f'<!-- wp:paragraph -->\n'
        f'<p>{f["answer"]}</p>\n'
        f'<!-- /wp:paragraph --></details>\n'
        f'<!-- /wp:details -->\n'
    )

# Fetch current content
resp = requests.get(
    "https://solveplan.com/wp-json/wp/v2/posts/10653?context=edit",
    auth=HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
)
current_content = resp.json()["content"]["raw"]

# Replace the wp:html FAQ block with wp:details blocks
new_content = re.sub(
    r'<!-- wp:html -->.*?<!-- /wp:html -->',
    details_blocks,
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
start = saved.find("wp:details")
print("\nBloco salvo:")
print(saved[start:start+300] if start > 0 else "wp:details nao encontrado")
