import requests, json, copy, uuid

WP_URL  = "https://solveplan.com"
WP_USER = "administrador"
WP_PASS = "vjpT R0lO 9c2G vh2w WAqA RPfU"
AUTH    = (WP_USER, WP_PASS)

REPLACEMENTS = {
    "8dc0258": {"title": "Produto"},
    "825653e": {"title": "Solve Watch"},
    "280198c": {"editor": "<p>Plataforma de observabilidade e governança para SAP Datasphere — visibilidade total do seu ambiente em uma tela, 24 horas por dia.</p>"},
    "f772003": {"title": "O problema"},
    "02c3452": {"editor": "<p>Não é falta de competência. É falta de visibilidade. O Datasphere nativo não foi feito para monitoramento — e isso tem um custo real para o negócio.</p>"},
    "28460fe": {"editor": "<p>Você só descobre que algo falhou quando o usuário reclama — às vezes a falha tem dias</p>"},
    "4c62a13": {"editor": "<p>Capacity Units fora de controle, sem saber quais objetos consomem mais</p>"},
    "3797d8e": {"editor": "<p>Governança impossível de comprovar para auditorias internas, SOX e LGPD</p>"},
    "b4649ad": {"editor": "<p>Ambiente cresceu sem padrão — ninguém tem a visão consolidada do todo</p>"},
    "293de8e": {"editor": "<p>Esses problemas têm uma causa comum: o SAP Datasphere nativo não foi projetado para monitoramento. O Solve Watch resolve isso com visibilidade real, alertas proativos e governança automática.</p>"},
    "a818d41": {"title": "A Solução"},
    "662b096": {"editor": "<p>O Solve Watch é a plataforma que entrega o que a SAP nativa não dá: visão integrada de saúde, performance, volumetria e custo — em uma tela, sem que você precise montar um time dedicado para isso.</p>"},
    "0e8b722": {"icon_list": [
        {"text": "Monitoramento 24/7 sem intervenção manual",    "selected_icon": {"library": "fa-solid", "value": "fas fa-eye"}},
        {"text": "Alertas proativos antes do usuário reclamar",  "selected_icon": {"library": "fa-solid", "value": "fas fa-bell"}},
        {"text": "Histórico de execuções de até 6 meses",        "selected_icon": {"library": "fa-solid", "value": "fas fa-history"}},
    ]},
    "963a368": {"icon_list": [
        {"text": "Heatmap de concorrência de Replication Flows", "selected_icon": {"library": "fa-solid", "value": "fas fa-fire"}},
        {"text": "Ranking TOP 20 de volumetria com tendência",   "selected_icon": {"library": "fa-solid", "value": "fas fa-chart-bar"}},
        {"text": "Score de maturidade e governança do ambiente", "selected_icon": {"library": "fa-solid", "value": "fas fa-shield-alt"}},
    ]},
    "e49a622": {"icon_list": [
        {"text": "Controle e previsão de Capacity Units",        "selected_icon": {"library": "fa-solid", "value": "fas fa-tachometer-alt"}},
        {"text": "Análise de performance por objeto (CPU/RAM)",  "selected_icon": {"library": "fa-solid", "value": "fas fa-bolt"}},
        {"text": "Relatório consolidado pronto para auditoria",  "selected_icon": {"library": "fa-solid", "value": "fas fa-file-alt"}},
    ]},
    "e32373b": {"title": "Calendário de Cargas"},
    "ffadb99": {"editor": "<p>Visão mensal de todas as execuções. Em 2 segundos você sabe se a semana foi tranquila ou problemática — sem abrir nenhum outro painel.</p>"},
    "43395ae": {"title": "Análise de Performance"},
    "ca0e028": {"editor": "<p>Identifica os objetos mais lentos — CDS Views, Analytic Models e Transformation Flows — com duração média, CPU e memória. Tuning onde realmente importa.</p>"},
    "c572847": {"title": "Controle de Capacity Units"},
    "138075c": {"editor": "<p>Visão de consumo por objeto, por Space e por área de negócio. Antecipe o estouro antes da fatura chegar.</p>"},
    "63618e5": {"title": "Cronograma de Concorrência"},
    "ad1d4d2": {"editor": "<p>Heatmap 7 dias x 24 horas dos Replication Flows programados. Identifica janelas críticas de sobrecarga antes do colapso. Funcionalidade única no mercado brasileiro.</p>"},
    "6450175": {"text": "Solicitar demonstração do Solve Watch", "link": {"url": "#demo", "is_external": ""}},
}

def new_id():
    return uuid.uuid4().hex[:7]

def replace_widgets(nodes):
    for node in nodes:
        nid = node.get("id", "")
        if nid in REPLACEMENTS:
            for key, val in REPLACEMENTS[nid].items():
                node["settings"][key] = val
        inner = node.get("elements", [])
        if inner:
            replace_widgets(inner)

def reassign_ids(nodes):
    for node in nodes:
        node["id"] = new_id()
        inner = node.get("elements", [])
        if inner:
            reassign_ids(inner)

print("Buscando template SAP BDC...")
resp = requests.get(
    f"{WP_URL}/wp-json/wp/v2/pages/9913?context=edit",
    auth=AUTH, timeout=20
)
src = resp.json()
meta = src.get("meta", {})
el_json = json.loads(meta.get("_elementor_data", "[]"))
page_settings = meta.get("_elementor_page_settings", "{}")

el_clone = copy.deepcopy(el_json)
replace_widgets(el_clone)
reassign_ids(el_clone)

print("Criando pagina Solve Watch...")
payload = {
    "title":    "Solve Watch — Observabilidade para SAP Datasphere",
    "slug":     "solve-watch",
    "status":   "draft",
    "template": "elementor_header_footer",
    "content":  "",
    "meta": {
        "_elementor_edit_mode":     "builder",
        "_elementor_template_type": "wp-page",
        "_elementor_data":          json.dumps(el_clone),
        "_elementor_page_settings": page_settings,
    }
}

resp2 = requests.post(f"{WP_URL}/wp-json/wp/v2/pages", auth=AUTH, json=payload, timeout=30)

if resp2.status_code in (200, 201):
    d = resp2.json()
    pid = d.get("id")
    print(f"OK - ID: {pid}")
    print(f"Editar: {WP_URL}/wp-admin/post.php?post={pid}&action=edit")
    print(f"Preview: {WP_URL}/?page_id={pid}")
else:
    print(f"ERRO {resp2.status_code}: {resp2.text[:400]}")
