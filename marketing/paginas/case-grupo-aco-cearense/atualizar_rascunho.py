"""Troca o conteúdo do rascunho 11520 pelo texto aprovado pelo cliente, palavra por palavra
("Case Grupo Aço Cearense planejamento integrado com SAP Analytics Cloud_rev_cliente - Copia.pdf").
Só altera o campo content. Título, resumo, imagem destacada e status ficam como estão.

Uso: WP_APP_PASSWORD="xxxx ..." python atualizar_rascunho.py [--dry-run]
"""
import os, sys, requests

sys.stdout.reconfigure(encoding="utf-8")

WP = "https://solveplan.com/wp-json"
POST_ID = 11520
PLAN_URL = "https://solveplan.com/planejamento-e-simulacao/"
SERVICOS_URL = "https://solveplan.com/servicos/"
VIDEO = "https://youtu.be/wVj2x8VfYQs"


def a(text, url):
    return f'<a href="{url}">{text}</a>'

def spacer(h=33):
    return f'<!-- wp:spacer {{"height":"{h}px"}} -->\n<div style="height:{h}px" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->'

def p(html):
    return f'<!-- wp:paragraph -->\n<p>{html}</p>\n<!-- /wp:paragraph -->'

def h2(text):
    return ('<!-- wp:heading {"style":{"elements":{"link":{"color":{"text":"#006cff"}}},"color":{"text":"#006cff"}}} -->\n'
            f'<h2 class="wp-block-heading has-text-color has-link-color" style="color:#006cff">{text}</h2>\n<!-- /wp:heading -->')


def build():
    blocks = [
        spacer(),
        p("Planejar uma operação industrial de grande porte exige conectar decisões comerciais, produtivas e financeiras que acontecem em ritmos diferentes. No Grupo Aço Cearense, essa complexidade envolvia vendas, suprimentos, pessoas, investimentos, custos, tributos, demonstrativos e diferentes etapas de consolidação."),
        p("Com 46 anos de atuação no mercado brasileiro do aço e presença no Ceará, Pará e Tocantins, o Grupo Aço Cearense reúne operações integradas de comercialização, metalurgia, siderurgia e logística."),
        p("Antes do projeto, determinadas etapas do planejamento e da consolidação dependiam de planilhas e de atividades manuais. Esse cenário ampliava o esforço operacional, dificultava a gestão integrada de versões e reduzia o tempo disponível para análises e simulações."),
        p("A resposta foi estruturar um modelo de planejamento integrado com SAP Analytics Cloud (SAC) Planning, conectado ao SAP IBP e ao SAP S/4HANA."),
        spacer(),
        h2("Por que o SAP Analytics Cloud foi escolhido?"),
        p("O objetivo do Grupo Aço Cearense era evoluir para um planejamento mais integrado, automatizado e governado, conectando projeções operacionais e financeiras em uma arquitetura única."),
        p("Com o SAP Analytics Cloud, cálculos antes realizados em planilhas puderam ser estruturados como regras de negócio no sistema, enquanto workflows de aprovação passaram a apoiar diferentes etapas do planejamento. A integração com SAP IBP e SAP S/4HANA também permitiu aproximar projeções operacionais, dados transacionais e planejamento financeiro."),
        p("A transformação, portanto, não se limitou à troca de ferramenta. O projeto reorganizou a forma como diferentes áreas participam do planejamento e como as informações percorrem o ciclo orçamentário."),
        p(f'Conheça também a atuação da Solveplan em {a("Planejamento e Simulação", PLAN_URL)} com soluções SAP.'),
        spacer(),
        h2("Um escopo que conecta diferentes dimensões do negócio"),
        p("O projeto contemplou diferentes dimensões do negócio, incluindo vendas, produção, custos, estoques, pessoas, despesas operacionais, investimentos, suprimentos, tributos, demonstrativos financeiros, fluxo de caixa, balanço patrimonial, operação florestal e simulações."),
        p("Essa amplitude é especialmente relevante porque o planejamento de uma companhia industrial não acontece de forma isolada. Uma projeção de vendas afeta produção e necessidade de matéria-prima; custos e investimentos influenciam caixa e resultado; movimentações de pessoas impactam despesas; e todas essas variáveis precisam convergir para demonstrativos e cenários consistentes."),
        p("Ao organizar essas frentes em uma arquitetura de planejamento comum, o Grupo Aço Cearense passou a trabalhar com regras, integrações e responsabilidades mais estruturadas."),
        spacer(),
        h2("SAP IBP, SAP S/4HANA e SAC Planning: como as informações se conectam"),
        p("Um dos pontos centrais do projeto foi a integração entre o planejamento operacional e o financeiro."),
        p("Na frente de Supply, por exemplo, as projeções de volume do SAP IBP passaram a se conectar às projeções financeiras no SAP Analytics Cloud. Em outras frentes, o SAC passou a receber dados automaticamente do SAP S/4HANA, reduzindo atividades de extração e preparação manual."),
        p("O material de go-live também registra a substituição de cálculos em planilhas por regras de negócio, a implantação de workflows de aprovação e a eliminação de intermediações de dados entre áreas em determinados processos."),
        p("Na frente financeira, os dados planejados dos diferentes módulos passaram a ser integrados para apoiar consolidação, cálculo de tributos sobre o lucro e revisões periódicas do orçamento."),
        p(f'<strong>Assista ao vídeo do case:</strong> {a("Grupo Aço Cearense | SAP Analytics Cloud + Solveplan", VIDEO)}'),
        spacer(),
        h2("Quais benefícios o SAP Analytics Cloud trouxe para o Grupo Aço Cearense?"),
        p("Os benefícios documentados aparecem em diferentes etapas do planejamento e variam conforme a frente de negócio."),
        p("Entre os principais ganhos estão a redução de atividades manuais, automação de extrações a partir do SAP S/4HANA, workflows de aprovação, maior governança, integração entre SAP IBP e SAC Planning e redução de ciclos de planejamento em áreas como Supply, Payroll, CAPEX e custos."),
        p("Na prática, o projeto reduziu a necessidade de replicar informações entre áreas e liberou mais tempo para análises. A governança também passou a definir responsabilidades para Produção, Suprimentos, Vendas, RH, Logística, Fiscal, Finanças e Controladoria."),
        p("Os materiais do projeto não apresentam um percentual único de redução de tempo ou uma métrica financeira consolidada. Por isso, o resultado deve ser comunicado pelo ganho operacional efetivamente documentado: menos trabalho manual, maior integração, processos mais governados e ciclos de planejamento mais ágeis."),
        spacer(),
        h2("Mais governança para um planejamento que atravessa toda a organização"),
        p("Em projetos de planejamento integrado, tecnologia e governança precisam avançar juntas. No Grupo Aço Cearense, esse aspecto ganhou importância porque diferentes áreas alimentam e consomem informações que impactam o orçamento e os demonstrativos."),
        p("Ao estruturar responsabilidades, regras de negócio e workflows, o projeto cria uma lógica mais clara para participação das áreas e reduz a dependência de controles paralelos."),
        p("Isso também favorece revisões periódicas e simulações de cenários, já que as informações passam a percorrer um processo mais conectado entre operação e finanças."),
        spacer(),
        h2("A atuação da Solveplan no projeto"),
        p("A Solveplan conduziu a transformação em conjunto com o Grupo Aço Cearense, estruturando as diferentes dimensões do planejamento em uma arquitetura integrada."),
        p("A construção por frentes permitiu respeitar particularidades de vendas, suprimentos, pessoas, investimentos, custos e finanças, ao mesmo tempo em que regras de negócio, integrações e governança eram organizadas para sustentar um processo mais conectado e escalável."),
        p("O roteiro validado para o case reforça que a recomendação para outras empresas é tratar uma iniciativa como essa como uma evolução de processo, e não apenas como uma troca de ferramenta: integrar áreas, definir responsabilidades, estruturar regras de negócio e reduzir atividades manuais são partes da mesma transformação."),
        spacer(),
        h2("Uma base mais preparada para ciclos de planejamento e revisão"),
        p("Com uma estrutura mais integrada, automatizada e governada, o Grupo Aço Cearense passa a ter uma base preparada para ciclos de planejamento e revisão mais ágeis, simulações de cenários e análises mais aprofundadas."),
        p("A evolução também cria condições para ampliar a integração entre planejamento operacional e financeiro e utilizar as informações de forma mais consistente na tomada de decisão."),
        p("O principal aprendizado do case está justamente nessa conexão: transformar o planejamento exige aproximar áreas, processos e dados para que a tecnologia consiga reduzir complexidade em vez de apenas digitalizá-la."),
        p(f'<strong>Sua empresa também precisa conectar planejamento operacional e financeiro?</strong> {a("Conheça as soluções da Solveplan", SERVICOS_URL)}.'),
    ]
    return "\n\n".join(blocks)


if __name__ == "__main__":
    content = build()
    if "--dry-run" in sys.argv:
        print(content)
        sys.exit()
    auth = ("administrador", os.environ["WP_APP_PASSWORD"])
    cur = requests.get(f"{WP}/wp/v2/case/{POST_ID}", params={"context": "edit", "_fields": "status,featured_media"}, auth=auth, timeout=30).json()
    if cur.get("status") != "draft":
        sys.exit(f"Post {POST_ID} não está como rascunho ({cur.get('status')}); nada foi alterado.")
    r = requests.post(f"{WP}/wp/v2/case/{POST_ID}", auth=auth, timeout=60, json={"content": content})
    r.raise_for_status()
    post = r.json()
    print(f"Atualizado: ID {post['id']} · status {post['status']} · imagem destacada {post['featured_media']} (antes: {cur['featured_media']})")
