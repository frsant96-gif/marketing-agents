import sys, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "vjpT R0lO 9c2G vh2w WAqA RPfU")
WP = "https://solveplan.com/wp-json/wp/v2"

BDC_URL = "https://solveplan.com/sap-business-data-cloud/"
DS_URL  = "https://solveplan.com/sap-datasphere/"
SAC_URL = "https://solveplan.com/planejamento-e-simulacao/"

def p(text):
    return f'\n\n<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->'

def h5(text):
    return f'\n\n<!-- wp:heading {{"level":5}} -->\n<h5 class="wp-block-heading"><strong>{text}</strong></h5>\n<!-- /wp:heading -->'

def details(question, answer):
    return (
        '\n\n<!-- wp:details -->\n'
        f'<details class="wp-block-details"><summary>{question}</summary>'
        '<!-- wp:paragraph -->\n'
        f'<p>{answer}</p>\n'
        '<!-- /wp:paragraph --></details>\n'
        '<!-- /wp:details -->'
    )

def a(text, url):
    return f'<a href="{url}">{text}</a>'

CTA = (
    '\n\n<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n'
    '<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"primary","textColor":"white","style":{"border":{"radius":"4px"}}} -->\n'
    '<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-primary-background-color has-text-color has-background wp-element-button" '
    'href="https://bdcstrategy.solveplan.ai/" target="_blank" rel="noopener">Avalie a maturidade dos seus dados com a Solveplan</a></div>\n'
    '<!-- /wp:button --></div>\n'
    '<!-- /wp:buttons -->'
)

CASES = [
    {
        "id": 10585,
        "slug": "lins-agroindustrial-sap-analytics-cloud",
        "kw": "SAP Analytics Cloud",
        "excerpt": "Lins Agroindustrial reduziu 90% do tempo de processamento ao migrar do SAP BPC para o SAP Analytics Cloud com a Solveplan — de ~8h para minutos em cada etapa do planejamento.",
        "faq_title": "FAQ — SAP Analytics Cloud na Lins Agroindustrial",
        "faqs": [
            ("O que é o SAP Analytics Cloud e como foi aplicado na Lins Agroindustrial?",
             f'O {a("SAP Analytics Cloud", SAC_URL)} é a plataforma de planejamento e analytics da SAP. Na Lins Agroindustrial, substituiu o SAP BPC e passou a centralizar o planejamento de safra, simulações e análises financeiras — reduzindo o tempo de cada etapa de processamento de aproximadamente 8 horas para poucos minutos.'),
            ("Qual foi a redução de tempo obtida com o SAP Analytics Cloud?",
             "90% de redução no tempo de processamento por etapa de cálculo. O que levava cerca de 8 horas passou a ser concluído em minutos, liberando a equipe para análise em vez de consolidação."),
            ("Por que a Lins substituiu o SAP BPC pelo SAP Analytics Cloud?",
             f'O {a("SAP Analytics Cloud", SAC_URL)} oferece maior agilidade, integração nativa com o ecossistema SAP e interface moderna em comparação ao BPC. Para a Lins Agroindustrial, a transição representou mais velocidade nas 4 etapas de cálculo e maior confiabilidade dos dados de planejamento.'),
            ("Como a Solveplan conduziu a implementação do SAP Analytics Cloud na Lins?",
             f'A Solveplan, parceira SAP Gold especializada em {a("SAP Analytics Cloud", SAC_URL)} e {a("SAP Business Data Cloud", BDC_URL)} na América Latina, estruturou a migração do BPC para o SAC mantendo a continuidade operacional — preservando a lógica de negócio e adaptando os modelos de planejamento para o ambiente cloud.'),
        ],
    },
    {
        "id": 10310,
        "slug": "zilor-implementa-sac-em-6-meses-e-elimina-uso-de-planilhas-eletronicas",
        "kw": "SAP Analytics Cloud",
        "excerpt": "Zilor implementou o SAP Analytics Cloud em 6 meses com a Solveplan, eliminando planilhas eletrônicas e reduzindo de 14 dias úteis para agilidade total na consolidação orçamentária.",
        "faq_title": "FAQ — SAP Analytics Cloud na Zilor",
        "faqs": [
            ("Por que a Zilor escolheu o SAP Analytics Cloud?",
             f'A Zilor precisava substituir planilhas eletrônicas que circulavam por e-mail e geravam 14 dias úteis de consolidação orçamentária. O {a("SAP Analytics Cloud", SAC_URL)} foi escolhido pela integração nativa com o SAP S/4HANA, agilidade em simulações e capacidade de eliminar controles paralelos.'),
            ("Em quanto tempo a Zilor implementou o SAP Analytics Cloud?",
             f'O projeto de implementação do {a("SAP Analytics Cloud", SAC_URL)} na Zilor foi concluído em 6 meses pela Solveplan, dentro do prazo e escopo definidos — cobrindo planejamento orçamentário, integração com S/4HANA e Go-Live.'),
            ("Quais resultados a Zilor obteve com o SAP Analytics Cloud?",
             f'A Zilor eliminou o uso de planilhas eletrônicas no processo orçamentário, ganhou agilidade na consolidação de dados e reduziu a dependência de controles paralelos. O {a("SAP Analytics Cloud", SAC_URL)} trouxe simulações mais rápidas e confiáveis para uma operação com 4.400 colaboradores e 14 milhões de toneladas de capacidade de moagem por safra.'),
            ("Como a Solveplan conduziu a implementação do SAP Analytics Cloud na Zilor?",
             f'A Solveplan, parceira SAP Gold com expertise em {a("SAP Analytics Cloud", SAC_URL)} e planejamento financeiro, estruturou o projeto com foco na integração entre o SAC e o SAP S/4HANA — garantindo que os dados de ERP alimentassem diretamente os modelos de planejamento orçamentário da Zilor.'),
        ],
    },
    {
        "id": 10305,
        "slug": "natulab-sap-datasphere-analytics-cloud",
        "kw": "SAP Datasphere",
        "excerpt": "Natulab integrou SAP Datasphere e SAP Analytics Cloud com a Solveplan, eliminando erros de carga, conquistando dados em tempo real e transformando a análise financeira da maior indústria farmacêutica independente do Brasil.",
        "faq_title": "FAQ — SAP Datasphere na Natulab",
        "faqs": [
            ("O que é o SAP Datasphere e por que a Natulab adotou?",
             f'O {a("SAP Datasphere", DS_URL)} é a plataforma de dados da SAP que integra, governa e disponibiliza dados de múltiplas fontes com semântica de negócio. A Natulab adotou o SAP Datasphere para substituir um serviço de extração que não atualizava indicadores em tempo real e gerava erros de carga que comprometiam relatórios.'),
            ("Como o SAP Datasphere resolveu os problemas de dados da Natulab?",
             f'O {a("SAP Datasphere", DS_URL)} centralizou a integração de dados da Natulab, eliminando erros de carga e garantindo atualização em tempo real. Com dados confiáveis disponíveis, a equipe passou a dedicar mais tempo a análises estratégicas e menos a consolidação manual de planilhas.'),
            ("Como o SAP Datasphere se integra com o SAP Analytics Cloud?",
             f'O {a("SAP Datasphere", DS_URL)} funciona como a camada de dados que alimenta o SAP Analytics Cloud com informações governadas e semanticamente estruturadas. Na Natulab, essa integração permitiu que os dashboards do Analytics Cloud refletissem dados reais e atualizados — sem necessidade de extração manual.'),
            ("Qual foi o impacto da implementação do SAP Datasphere na Natulab?",
             f'A Natulab passou a ter visibilidade em tempo real sobre suas operações, eliminou erros de carga em relatórios e reduziu o tempo gasto em consolidação de planilhas. Para uma indústria farmacêutica com mais de 160 produtos e operação nacional, o {a("SAP Datasphere", DS_URL)} trouxe a confiabilidade de dados que processos regulados exigem.'),
        ],
    },
    {
        "id": 10297,
        "slug": "m-dias-branco-implementa-sap-analytics-cloud-em-10-meses-com-96-de-reducao",
        "kw": "SAP Analytics Cloud",
        "excerpt": "M. Dias Branco implementou o SAP Analytics Cloud em 10 meses com a Solveplan, alcançando 96% de retenção e substituindo um processo orçamentário dependente de planilhas por simulações integradas ao SAP S/4HANA.",
        "faq_title": "FAQ — SAP Analytics Cloud na M. Dias Branco",
        "faqs": [
            ("Por que a M. Dias Branco escolheu o SAP Analytics Cloud?",
             f'A M. Dias Branco precisava substituir uma ferramenta orçamentária com mais de 10 anos de uso, que não integrava com o SAP S/4HANA e dependia de planilhas para simulações. O {a("SAP Analytics Cloud", SAC_URL)} foi escolhido pela integração nativa com o ecossistema SAP e pela capacidade de suportar simulações de cenários em escala.'),
            ("Quanto tempo levou a implementação do SAP Analytics Cloud na M. Dias Branco?",
             f'O projeto de implementação do {a("SAP Analytics Cloud", SAC_URL)} na M. Dias Branco foi concluído em 10 meses pela Solveplan — coincidindo com a finalização da implementação do SAP S/4HANA, o que exigiu execução paralela e coordenação de alto nível entre os projetos.'),
            ("O que significa 96% de retenção no SAP Analytics Cloud?",
             f'A taxa de 96% de retenção indica que praticamente todos os usuários que adotaram o {a("SAP Analytics Cloud", SAC_URL)} na M. Dias Branco continuaram usando a plataforma ativamente. É um indicador de que a solução resolveu de fato os problemas do processo orçamentário — e não apenas foi implementada tecnicamente.'),
            ("Como a Solveplan implementou o SAP Analytics Cloud na M. Dias Branco?",
             f'A Solveplan conduziu a implementação do {a("SAP Analytics Cloud", SAC_URL)} integrado ao SAP S/4HANA, estruturando os modelos de planejamento e simulação de cenários para uma operação com mais de 17 mil colaboradores e 21 unidades no Brasil. O projeto foi entregue dentro do prazo, mesmo com a execução paralela ao projeto de S/4HANA.'),
        ],
    },
    {
        "id": 10307,
        "slug": "oji-papeis-sap-analytics-cloud",
        "kw": "SAP Analytics Cloud",
        "excerpt": "Oji Papéis Especiais implementou o SAP Analytics Cloud em 6 meses com a Solveplan, reduzindo o ciclo orçamentário de 15 para 2 dias e eliminando planilhas em uma multinacional japonesa com 90% do market share de papel térmico no Brasil.",
        "faq_title": "FAQ — SAP Analytics Cloud na Oji Papéis",
        "faqs": [
            ("Por que a Oji Papéis escolheu o SAP Analytics Cloud?",
             f'Já usuária do SAP ERP, a Oji Papéis expandiu seu ecossistema para o {a("SAP Analytics Cloud", SAC_URL)} para resolver a dependência de planilhas e sistemas paralelos que tornavam o ciclo orçamentário lento — chegando a 15 dias para respostas. A escolha pelo SAC veio da integração nativa com o ambiente SAP já existente.'),
            ("Qual foi a redução no ciclo orçamentário com o SAP Analytics Cloud?",
             f'Com o {a("SAP Analytics Cloud", SAC_URL)}, a Oji Papéis reduziu o ciclo orçamentário de 15 para 2 dias — uma redução de 87%. O que antes exigia mais de duas semanas de consolidação passou a ser concluído em 2 dias, com dados centralizados e acessíveis.'),
            ("Em quanto tempo a Oji implementou o SAP Analytics Cloud?",
             f'O projeto de implementação do {a("SAP Analytics Cloud", SAC_URL)} na Oji Papéis foi concluído em 6 meses pela Solveplan, cobrindo revisão de processos financeiros, mapeamento de dados, padronização e estruturação de dashboards.'),
            ("Como a Solveplan conduziu o projeto do SAP Analytics Cloud na Oji?",
             f'A Solveplan estruturou a implementação do {a("SAP Analytics Cloud", SAC_URL)} com foco na eliminação de planilhas e na integração com o ERP SAP da Oji Papéis — garantindo que os dados financeiros fluíssem diretamente para os modelos de planejamento orçamentário, sem processos manuais intermediários.'),
        ],
    },
    {
        "id": 704,
        "slug": "matrix-energia",
        "kw": "SAP Analytics Cloud",
        "excerpt": "Matrix Energia implementou o SAP Analytics Cloud com a Solveplan em 3 meses, conquistando automação, agilidade e autonomia na consolidação societária — eliminando o Excel e acelerando o fechamento financeiro.",
        "faq_title": "FAQ — SAP Analytics Cloud na Matrix Energia",
        "faqs": [
            ("O que é o SAP Analytics Cloud e como ele foi aplicado na Matrix Energia?",
             f'O {a("SAP Analytics Cloud", SAC_URL)} é a plataforma de analytics e consolidação da SAP. Na Matrix Energia, foi implementado para resolver problemas de rastreabilidade financeira, substituir o Excel na consolidação societária e eliminar a perda de timing na divulgação de resultados para stakeholders.'),
            ("Em quanto tempo a Matrix Energia implementou o SAP Analytics Cloud?",
             f'O projeto de implementação do {a("SAP Analytics Cloud", SAC_URL)} na Matrix Energia foi concluído em 3 meses pela Solveplan — resultado rápido mesmo diante de desafios técnicos como múltiplos planos de contas e ausência de conceito pré-configurado de sociedade parceira no SAP Business One.'),
            ("Quais desafios a Matrix Energia tinha antes do SAP Analytics Cloud?",
             f'Antes do {a("SAP Analytics Cloud", SAC_URL)}, a Matrix Energia enfrentava falta de rastreabilidade financeira, insegurança nas informações, perda de tempo com atividades manuais e uma tentativa frustrada de implantação de outra solução. A consolidação societária dependia do Excel, o que causava atrasos na divulgação de resultados.'),
            ("Como a Solveplan superou os desafios técnicos na implementação do SAP Analytics Cloud?",
             f'A Solveplan criou regras e códigos personalizados para contornar a ausência de conceito pré-configurado de sociedade parceira no SAP Business One e a complexidade de múltiplos planos de contas — entregando uma implementação do {a("SAP Analytics Cloud", SAC_URL)} funcional em 3 meses, com automação completa da consolidação societária da Matrix Energia.'),
        ],
    },
]

for case in CASES:
    pid = case["id"]
    print(f"\n{'='*50}")
    print(f"Processando {pid} — {case['slug']}")

    # Fetch current content
    r = requests.get(f"{WP}/case/{pid}?context=edit", auth=AUTH)
    d = r.json()
    raw = d["content"]["raw"]

    # Build FAQ block
    faq_block = h5(case["faq_title"])
    for q, a_text in case["faqs"]:
        faq_block += details(q, a_text)

    # Append CTA + FAQ to existing content
    addition = CTA + faq_block

    new_raw = raw + addition

    # Build update payload
    payload = {"content": new_raw}

    # Fix slug if needed
    current_slug = d.get("slug", "")
    if current_slug != case["slug"]:
        payload["slug"] = case["slug"]
        print(f"  Slug: {current_slug} → {case['slug']}")

    # Add excerpt if missing
    current_excerpt = d.get("excerpt", {}).get("raw", "").strip()
    if not current_excerpt:
        payload["excerpt"] = case["excerpt"]
        print(f"  Excerpt: adicionado")

    # Update post
    r2 = requests.post(f"{WP}/case/{pid}", auth=AUTH, json=payload)
    print(f"  Update: {r2.status_code}")

    # Verify
    v = requests.get(f"{WP}/case/{pid}?context=edit", auth=AUTH).json()
    vraw = v["content"]["raw"]
    kw_count = vraw.count(case["kw"])
    words = len(vraw.split())
    density = kw_count / words * 100 if words else 0
    print(f"  KW ({case['kw']}): {kw_count}x = {density:.2f}%")
    print(f"  FAQ (details): {vraw.count('wp:details')//2}")
    print(f"  CTA: {'OK' if 'bdcstrategy' in vraw else 'AUSENTE'}")
    print(f"  Slug: {v.get('slug')}")

print("\nConcluído.")
