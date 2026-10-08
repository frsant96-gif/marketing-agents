"""Cria o case SSA Alimentos como RASCUNHO no WordPress, no mesmo modelo de blocos do case da Lins (10585).

Uso: WP_APP_PASSWORD="xxxx xxxx ..." python criar_rascunho.py <pasta-dos-icones>
A senha não fica gravada neste arquivo.
"""
import os, sys, json, pathlib, requests

sys.stdout.reconfigure(encoding="utf-8")

WP = "https://solveplan.com/wp-json"
AUTH = ("administrador", os.environ["WP_APP_PASSWORD"])
ICON_DIR = pathlib.Path(sys.argv[1])

DS_URL = "https://solveplan.com/sap-datasphere/"
BDC_URL = "https://solveplan.com/sap-business-data-cloud/"
VIDEO = "https://youtu.be/T3k8MTIggjA"

SLUG = "ssa-alimentos-sap-datasphere"
TITLE = "Como a SSA Alimentos estruturou sua gestão de dados com SAP Datasphere"
EXCERPT = ("A SSA Alimentos adotou o SAP Datasphere como data warehouse com a Solveplan, conectando SAP S/4HANA, "
           "SAP Analytics Cloud, SAP IBP e sistemas não-SAP em uma arquitetura governada, com modelos reutilizáveis e linhagem de dados.")
SEO = {
    "rank_math_title": "SSA Alimentos + SAP Datasphere | Case de Sucesso Solveplan",
    "rank_math_description": ("Como a SSA Alimentos usou o SAP Datasphere como data warehouse para integrar S/4HANA, "
                              "SAC, IBP e sistemas não-SAP em uma base governada e rastreável."),
    "rank_math_focus_keyword": "SAP Datasphere,case SAP Datasphere,governança de dados SAP,SAP Datasphere Data Warehouse,arquitetura de dados SAP",
}

ICONS = [
    ("ssa-icone-indicadores.png", "Ícone de gráfico de barras"),
    ("ssa-icone-integracao.png", "Ícone de banco de dados"),
    ("ssa-icone-frentes.png", "Ícone de grade com nove blocos"),
]
CARDS = [
    "~2.000 indicadores — base analítica que antes exigia replicar a lógica de negócio a cada novo relatório",
    "SAP + não-SAP — S/4HANA, SAC e IBP conectados a AVECOM, Lincros, GEPARDO e Sankhya",
    "9 frentes de análise — da DRE e do CAPEX a fretes, campo, indústria e mercado externo",
]


# ── blocos Gutenberg (mesma marcação do case da Lins) ─────────────────────────
def a(text, url):
    return f'<a href="{url}">{text}</a>'

def spacer(h=33):
    return f'<!-- wp:spacer {{"height":"{h}px"}} -->\n<div style="height:{h}px" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->'

def p(html):
    return f'<!-- wp:paragraph -->\n<p>{html}</p>\n<!-- /wp:paragraph -->'

def h2(text):
    return ('<!-- wp:heading {"style":{"elements":{"link":{"color":{"text":"#006cff"}}},"color":{"text":"#006cff"}}} -->\n'
            f'<h2 class="wp-block-heading has-text-color has-link-color" style="color:#006cff">{text}</h2>\n<!-- /wp:heading -->')

def ul(items, ordered=False):
    tag = "ol" if ordered else "ul"
    attrs = ' {"ordered":true}' if ordered else ""
    lis = "\n\n".join(f"<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->" for i in items)
    return f'<!-- wp:list{attrs} -->\n<{tag} class="wp-block-list">{lis}</{tag}>\n<!-- /wp:list -->'

def card(media_id, url, text):
    return ('<!-- wp:column -->\n<div class="wp-block-column">'
            f'<!-- wp:image {{"id":{media_id},"width":"100px","height":"auto","sizeSlug":"full","linkDestination":"none","align":"center"}} -->\n'
            f'<figure class="wp-block-image aligncenter size-full is-resized"><img src="{url}" alt="" class="wp-image-{media_id}" style="width:100px;height:auto"/></figure>\n'
            '<!-- /wp:image -->\n\n'
            f'<!-- wp:paragraph {{"align":"center"}} -->\n<p class="has-text-align-center">{text}</p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:column -->')

def cards(media):
    cols = "\n\n".join(card(mid, url, txt) for (mid, url), txt in zip(media, CARDS))
    return ('<!-- wp:group {"layout":{"type":"constrained"}} -->\n<div class="wp-block-group"><!-- wp:group {"layout":{"type":"constrained"}} -->\n'
            f'<div class="wp-block-group"><!-- wp:columns -->\n<div class="wp-block-columns">{cols}</div>\n<!-- /wp:columns --></div>\n'
            '<!-- /wp:group --></div>\n<!-- /wp:group -->')

def before_after(before, after):
    def col(label, items):
        return (f'<!-- wp:column -->\n<div class="wp-block-column"><!-- wp:paragraph -->\n<p><em>{label}</em></p>\n<!-- /wp:paragraph -->\n\n'
                f'{ul(items)}</div>\n<!-- /wp:column -->')
    return f'<!-- wp:columns -->\n<div class="wp-block-columns">{col("Antes do SAP Datasphere", before)}\n\n{col("Depois da implementação", after)}</div>\n<!-- /wp:columns -->'

def embed(url):
    return ('<!-- wp:embed {"url":"' + url + '","type":"video","providerNameSlug":"youtube","responsive":true,"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"} -->\n'
            '<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">\n'
            f'{url}\n</div></figure>\n<!-- /wp:embed -->')

def button(text, url, primary=False):
    if primary:
        return ('<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"primary","textColor":"white","style":{"border":{"radius":"4px"}}} -->\n'
                f'<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-primary-background-color has-text-color has-background wp-element-button" href="{url}" target="_blank" rel="noopener">{text}</a></div>\n'
                '<!-- /wp:button --></div>\n<!-- /wp:buttons -->')
    return ('<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n<div class="wp-block-buttons"><!-- wp:button {"style":{"color":{"background":"#006cff"}}} -->\n'
            f'<div class="wp-block-button"><a class="wp-block-button__link has-background wp-element-button" href="{url}" style="background-color:#006cff">{text}</a></div>\n'
            '<!-- /wp:button --></div>\n<!-- /wp:buttons -->')

def faq(q, ans):
    return (f'<!-- wp:details -->\n<details class="wp-block-details"><summary>{q}</summary><!-- wp:paragraph -->\n<p>{ans}</p>\n'
            '<!-- /wp:paragraph --></details>\n<!-- /wp:details -->')


def build(media):
    blocks = [
        spacer(),
        p("Quando uma empresa cresce, ter acesso aos dados deixa de ser o desafio. O desafio passa a ser garantir que as diferentes áreas trabalhem com informações organizadas, rastreáveis e prontas para apoiar decisões."),
        p("Esse era o ponto em que a SSA Alimentos estava antes do SAP Datasphere. As informações ficavam distribuídas entre sistemas e estruturas diferentes: dados integrados em uma base Oracle por meio de scripts, planilhas Excel usadas tanto para entrada quanto para análise e modelos semânticos descentralizados no Power BI."),
        spacer(),
        cards(media),
        spacer(),
        h2("O desafio"),
        p("A construção de aproximadamente 2.000 indicadores exigia replicar lógicas de negócio. A cada novo relatório ou dashboard, parte desse trabalho precisava ser reconstruída e validada."),
        p("Ao mesmo tempo, a SSA vivia um momento importante da sua estratégia tecnológica: a implantação do SAP S/4HANA, o projeto de planejamento orçamentário com SAP Analytics Cloud (SAC) e SAP Integrated Business Planning (IBP) e a construção de uma plataforma de dados para suportar a transformação digital. Tudo isso aumentou a necessidade de uma camada de dados integrada ao ecossistema SAP."),
        p("<strong>Era necessário evoluir a arquitetura.</strong>"),
        spacer(),
        h2("Por que a SSA escolheu o SAP Datasphere?"),
        p("O SAP Datasphere passou a exercer o papel de data warehouse da companhia. A plataforma conecta os dashboards em Power BI, o planejamento orçamentário no SAC, o processo de S&amp;OP no IBP e diferentes fontes corporativas, entre elas sistemas SAP e sistemas satélites."),
        p(f'O objetivo não era só centralizar dados. Era criar uma estrutura em que a informação pudesse ser reutilizada, rastreada e consumida com mais eficiência pelas áreas do negócio. Para entender a solução em detalhes, veja a página da Solveplan sobre {a("SAP Datasphere", DS_URL)}.'),
        before_after(
            ["Dados integrados em base Oracle por scripts", "Excel usado para entrada e para análise",
             "Modelos semânticos descentralizados no Power BI", "Lógica de negócio replicada em ~2.000 indicadores",
             "Reconstrução e validação a cada novo relatório"],
            ["SAP Datasphere como data warehouse da companhia", "Fontes SAP e não-SAP integradas em uma única camada",
             "Modelos de dados reutilizáveis por domínio de negócio", "Linhagem de dados para análise de causa raiz",
             "Ambiente analítico separado do transacional"],
        ),
        spacer(),
        p("<strong>Assista o case completo</strong>"),
        embed(VIDEO),
        p("No vídeo, Wesley Medanha, da SSA Alimentos, apresenta a experiência da companhia e a evolução da arquitetura de dados."),
        spacer(),
        h2("De dados descentralizados a modelos reutilizáveis"),
        p("Com o SAP Datasphere, a SSA passou a estruturar modelos de dados para diferentes necessidades da organização. O ambiente suporta desde o pipeline do planejamento orçamentário e do realizado da DRE até análises de CAPEX, gestão de fretes, suprimentos, custos, campo, indústria, inteligência de mercado e operações de mercado externo."),
        p("Essa mudança trouxe um elemento importante para a estratégia da companhia: governança de dados. A arquitetura construída no SAP Datasphere organiza as informações por domínios de negócio e usa linhagem de dados para tornar a análise de causa raiz mais ágil. A separação entre os ambientes analítico e transacional também reduziu o impacto de processamentos complexos sobre o ERP."),
        spacer(),
        h2("Quais resultados o SAP Datasphere trouxe para a SSA?"),
        p("Os benefícios percebidos pela SSA estão em três frentes: integração de fontes, estruturação de modelos reutilizáveis e simplificação da preparação dos dados. A empresa também identificou ganhos em disponibilidade e rastreabilidade das informações, além da redução de atividades manuais e da dependência de dados descentralizados."),
        p("O impacto aparece na capacidade analítica. Com mais dados preparados e disponíveis, construir análises para apoiar decisões ficou mais simples e ágil. Menos esforço para reconstruir e validar a informação a cada nova demanda, mais capacidade para usá-la."),
        spacer(),
        h2("Governança antes de escala"),
        p("A jornada deixou aprendizados que vão além da tecnologia. Para a SSA, três pontos foram fundamentais:"),
        ul(["Preparar os dados para consumo",
            "Estabelecer uma fonte única e confiável de informação, o <em>source of truth</em>",
            "Envolver as áreas de negócio no processo de governança de dados"], ordered=True),
        p("Esses fundamentos valem para qualquer organização que pretende ampliar analytics, planejamento e iniciativas baseadas em dados. Uma arquitetura moderna não começa pelo dashboard. Começa pela qualidade daquilo que o alimenta."),
        spacer(),
        h2("SSA Alimentos, SAP Datasphere e Solveplan"),
        p("A jornada da SSA mostra o SAP Datasphere funcionando como camada estratégica de dados, conectando aplicações e fontes diferentes e criando uma estrutura mais organizada para analytics e planejamento."),
        p(f'O projeto também reforça uma discussão cada vez mais presente em empresas SAP: antes de escalar analytics e inteligência artificial, é preciso saber onde os dados estão, como são transformados e qual informação deve ser considerada confiável. Para quem está evoluindo a arquitetura de dados no ecossistema SAP, veja também como a Solveplan aborda o {a("SAP Business Data Cloud", BDC_URL)}.'),
        spacer(),
        p("<strong>Quer estruturar uma fundação de dados mais integrada e governada?</strong>"),
        button("Fale conosco", "https://solveplan.com/contato/"),
        spacer(),
        '<!-- wp:heading {"level":5} -->\n<h5 class="wp-block-heading"><strong>FAQ — SAP Datasphere na SSA Alimentos</strong></h5>\n<!-- /wp:heading -->',
        faq("Qual solução SAP foi implementada na SSA Alimentos?",
            f'O {a("SAP Datasphere", DS_URL)}, usado como data warehouse da SSA. Ele integra informações do SAP S/4HANA, do SAP Analytics Cloud, do SAP IBP e de outras fontes corporativas.'),
        faq("Qual era o principal desafio da SSA antes do SAP Datasphere?",
            "Os dados estavam distribuídos entre sistemas, scripts, base Oracle, planilhas e modelos semânticos descentralizados no Power BI. A construção de cerca de 2.000 indicadores também exigia replicar a lógica de negócio."),
        faq("Quais benefícios a SSA percebeu com o SAP Datasphere?",
            "Integração de fontes, modelos de dados reutilizáveis, preparação de dados simplificada, maior disponibilidade e rastreabilidade das informações e redução de atividades manuais."),
        faq("Como o SAP Datasphere apoia a tomada de decisão na SSA?",
            "Com mais dados preparados e disponíveis, construir análises para apoiar decisões ficou mais simples e ágil."),
        faq("Qual foi o principal aprendizado do projeto?",
            "Preparar os dados para consumo, estabelecer um <em>source of truth</em> e envolver as áreas de negócio na governança de dados."),
        faq("O SAP Datasphere integra dados SAP e não-SAP?",
            f'Sim. No ambiente da SSA, o {a("SAP Datasphere", DS_URL)} conecta SAP S/4HANA, SAP Analytics Cloud e SAP IBP a sistemas não-SAP como AVECOM, Lincros, GEPARDO e Sankhya.'),
        spacer(39),
        button("Avalie a maturidade dos seus dados com a Solveplan", "https://bdcstrategy.solveplan.ai/", primary=True),
    ]
    return "\n\n".join(blocks)


def upload_icon(fname, alt):
    existing = requests.get(f"{WP}/wp/v2/media", params={"search": fname.rsplit(".", 1)[0], "_fields": "id,source_url"}, auth=AUTH, timeout=30).json()
    if existing:
        return existing[0]["id"], existing[0]["source_url"]
    data = (ICON_DIR / fname).read_bytes()
    r = requests.post(f"{WP}/wp/v2/media", auth=AUTH, data=data, timeout=60,
                      headers={"Content-Disposition": f'attachment; filename="{fname}"', "Content-Type": "image/png"})
    r.raise_for_status()
    m = r.json()
    requests.post(f"{WP}/wp/v2/media/{m['id']}", auth=AUTH, json={"alt_text": alt}, timeout=30)
    return m["id"], m["source_url"]


if __name__ == "__main__":
    # Não duplica: se já existe um case com esse slug, para.
    found = requests.get(f"{WP}/wp/v2/case", params={"slug": SLUG, "status": "any", "_fields": "id,status"}, auth=AUTH, timeout=30).json()
    if found:
        sys.exit(f"Já existe case com slug {SLUG}: {found}")

    media = [upload_icon(f, alt) for f, alt in ICONS]
    print("Ícones:", media)

    r = requests.post(f"{WP}/wp/v2/case", auth=AUTH, timeout=60, json={
        "title": TITLE, "slug": SLUG, "status": "draft", "excerpt": EXCERPT, "content": build(media),
    })
    r.raise_for_status()
    post = r.json()
    pid = post["id"]
    print(f"Rascunho criado: ID {pid} · status {post['status']}")

    seo = requests.post(f"{WP}/rankmath/v1/updateMeta", auth=AUTH, timeout=30,
                        json={"objectType": "post", "objectID": pid, "meta": SEO})
    print("Rank Math:", seo.status_code, seo.text[:200])

    print(f"Editar: https://solveplan.com/wp-admin/post.php?post={pid}&action=edit")
    print(f"Prévia: https://solveplan.com/?post_type=case&p={pid}&preview=true")
