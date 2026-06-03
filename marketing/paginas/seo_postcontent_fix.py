import requests, xmlrpc.client

WP_URL  = 'https://solveplan.com'
AUTH    = ('administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU')
PAGE_ID = 10736
KW      = 'monitoramento SAP Datasphere'

# post_content que o RankMath le — deve conter keyword, links e headings
POST_CONTENT = f"""
<h1>Solve Watch</h1>

<p>Plataforma de <strong>{KW}</strong> e governança para SAP Datasphere.
Tenha visibilidade total do seu ambiente em uma tela, 24 horas por dia,
com <strong>{KW}</strong> automatico e sem configuracao complexa.</p>

<figure>
<img src="https://solveplan.com/wp-content/uploads/2026/06/Imagem1.png"
     alt="{KW} — Dashboard Inbox de Acao e KPIs" />
</figure>

<h2>O Problema: falta de {KW} no ambiente nativo</h2>

<p>As empresas nao tem visibilidade dos dados de consumo do SAP Datasphere.</p>
<p>Quando uma carga falha, o primeiro aviso nao vem do sistema. Vem do usuario reclamando que o dashboard esta desatualizado.</p>
<p>O cliente recebe alerta da SAP de que esta perto do limite quando ja ultrapassou.</p>
<p>Auditoria interna, SOX, LGPD — e nao ha registro consolidado de como os dados sao monitorados.</p>

<p>Esses problemas tem uma causa comum: o SAP Datasphere nativo nao foi projetado para {KW}.
O Solve Watch resolve isso com visibilidade real, alertas proativos e governanca automatica.
Saiba mais sobre <a href="https://solveplan.com/sap-datasphere/">SAP Datasphere</a>
e as solucoes da <a href="https://solveplan.com/sobre/">Solveplan</a>.</p>

<h2>O que o {KW} nativo da SAP nao entrega</h2>

<p>O SAP Datasphere tem paineis nativos, mas eles mostram o que esta acontecendo agora,
sem historico, sem alertas e sem analise. Veja o comparativo:</p>

<ul>
<li>Visao consolidada em uma tela: Solve Watch sim, Datasphere Nativo nao</li>
<li>Historico de ate 6 meses: Solve Watch sim, Datasphere Nativo nao</li>
<li>Alertas proativos de falha: Solve Watch sim, Datasphere Nativo nao</li>
<li>Controle e previsao de Capacity Units: Solve Watch sim, Datasphere Nativo parcial</li>
<li>Governanca e score de maturidade: Solve Watch sim, Datasphere Nativo nao</li>
</ul>

<h2>A Solucao: {KW} com o Solve Watch</h2>

<p>O Solve Watch e a plataforma de <strong>{KW}</strong> que entrega o que a SAP nativa nao da:
visao integrada de saude, performance, volumetria e custo — em uma tela.
Desenvolvido sobre a arquitetura do
<a href="https://www.sap.com/products/technology-platform/datasphere.html"
   target="_blank" rel="noopener">SAP Datasphere</a>,
o Solve Watch complementa o ambiente nativo com camadas de {KW} que a SAP nao entrega.</p>

<h2>Funcionalidades de {KW}</h2>

<h3>Calendario de Cargas</h3>
<p>Visao mensal de todas as execucoes.</p>
<p>Em 2 segundos voce sabe se a semana foi tranquila ou problematica, sem abrir nenhum outro painel.</p>

<h3>Analise de Performance</h3>
<p>Identifica os objetos mais lentos: CDS Views, Analytic Models e Transformation Flows.</p>
<p>Duracao media, CPU e memoria. Tuning onde realmente importa.</p>

<h3>Controle de Capacity Units</h3>
<p>Visao de consumo por objeto, por Space e por area de negocio.</p>
<p>Antecipe o estouro antes da fatura chegar.</p>

<h3>Heatmap de Concorrencia</h3>
<p>Heatmap 7 dias x 24 horas dos Replication Flows programados.</p>
<p>Identifica janelas criticas de sobrecarga antes do colapso.</p>
<p>Funcionalidade unica no mercado brasileiro de {KW}.</p>

<h2>Mais Funcionalidades de {KW}</h2>

<p>Alem do {KW} de cargas, o Solve Watch entrega visao operacional, financeira e de governanca.</p>

<ul>
<li>Resumo Inteligente do Dia: indicadores acionaveis sem abrir o sistema</li>
<li>TOP 20 volumetria: ranking dos maiores objetos com tendencia de crescimento</li>
<li>Score de maturidade: nota de 0 a 100 do seu ambiente Datasphere</li>
<li>Saude de Cargas: scorecard mensal com percentual de sucesso e falhas</li>
</ul>

<p><a href="https://solveplan.com/contato/">Solicite uma demonstracao do Solve Watch</a></p>

<h2>Perguntas frequentes sobre {KW}</h2>

<p><strong>O que e o Solve Watch?</strong></p>
<p>O Solve Watch e uma plataforma SaaS de <strong>{KW}</strong>, desenvolvida pela Solveplan.</p>

<p><strong>Como funciona o {KW} do SAP Datasphere?</strong></p>
<p>O Solve Watch monitora o SAP Datasphere automaticamente, com atualizacao a cada 30 minutos.</p>

<p><strong>Como controlar os Capacity Units do SAP Datasphere?</strong></p>
<p>O Solve Watch exibe o consumo por objeto, por Space e por area de negocio com historico de tendencia.</p>
"""

# Update post_content via REST API
print('Atualizando post_content...')
resp = requests.post(
    f'{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}',
    auth=AUTH,
    json={'content': POST_CONTENT}
)
resp.raise_for_status()
print('[OK] post_content atualizado')

# Update RankMath title with number
print('Atualizando RankMath...')
client = xmlrpc.client.ServerProxy(f'{WP_URL}/xmlrpc.php')
result = client.wp.editPost(1, 'administrador', 'vjpT R0lO 9c2G vh2w WAqA RPfU', PAGE_ID, {
    'custom_fields': [
        {'key': 'rank_math_title',
         'value': f'Solve Watch | {KW.title()} em 1 Tela'},
        {'key': 'rank_math_description',
         'value': (f'Solve Watch e a solucao de {KW} da Solveplan. '
                   f'Alertas proativos de falha, controle de Capacity Units, '
                   f'historico de 6 meses e heatmap — em 1 tela.')},
        {'key': 'rank_math_focus_keyword',
         'value': KW},
    ]
})
print(f'[OK] RankMath: {"salvo" if result else "erro"}')

print()
print('Erros resolvidos:')
print('  [OK] Keyword no inicio do conteudo (1o paragrafo)')
print('  [OK] Keyword no conteudo (multiplas ocorrencias)')
print('  [OK] Keyword em H2 e H3')
print('  [OK] Alt text com keyword (imagem do carrossel)')
print('  [OK] Links internos (SAP Datasphere + Sobre + Contato)')
print('  [OK] Link externo DoFollow (sap.com)')
print('  [OK] Titulo com numero (em 1 Tela)')
print('  [OK] Paragrafos curtos')
print()
print('Erro que exige acao manual:')
print('  -> URL slug: altere para "solve-watch-monitoramento-sap-datasphere" no Elementor')
print('     Configuracoes da pagina -> URL -> alterar slug')
