# Divergência de dados entre sistemas: por que dois relatórios nunca mostram o mesmo número

### O problema não trava na planilha. Trava na reunião de diretoria — e a causa é estrutural, não um erro de digitação.

Divergência de dados entre sistemas é o motivo real por trás da reunião que trava porque financeiro e comercial trazem dois números diferentes para o mesmo indicador. O CFO abre o relatório de receita do ERP. O head de vendas abre o dashboard do CRM. Os dois falam do mesmo mês, do mesmo cliente, da mesma métrica — e os números não batem.

A reação comum é caçar o erro: alguém digitou errado, alguém esqueceu de atualizar a planilha, algum relatório está "desatualizado". Esse diagnóstico resolve o sintoma daquele dia e garante que o mesmo problema volte no próximo fechamento. A causa não está no dado errado. Está na ausência de uma definição única para o que aquele indicador significa.

## O que é divergência de dados entre sistemas?

**Divergência de dados entre sistemas é** a situação em que duas ou mais plataformas — ERP, CRM, planilha, data warehouse, ferramenta de BI — apresentam valores diferentes para o mesmo indicador, no mesmo período, sem que nenhum dos dois esteja tecnicamente "errado". Cada sistema aplica sua própria regra de cálculo, seu próprio corte de data ou sua própria definição de métrica, e o resultado diverge mesmo quando os dados de origem estão corretos.

Esse é o sintoma que toda empresa de médio e grande porte com ambiente SAP conhece bem. O relatório de vendas do S/4HANA não bate com o pipeline do CRM. O EBITDA calculado no SAC diverge do número que a controladoria fecha em planilha paralela. A liderança perde tempo debatendo qual número está certo em vez de decidir com base nele.

Quando isso acontece uma vez, é um incidente. Quando acontece todo mês, em indicadores diferentes, com áreas diferentes, é sinal de um problema estrutural de governança de dados — não de um erro isolado.

## Por que isso importa agora

A desconfiança nos dados corporativos deixou de ser exceção. Segundo a HFS Research, apenas 5% dos executivos têm alto nível de confiança em seus dados, e 75% simplesmente não confiam neles. A KPMG chega a um número parecido: 60% dos executivos não estão muito confiantes em seus próprios insights de dados e analytics.

No financeiro, a situação é ainda mais crítica — é a área que sustenta decisão de investimento, meta e reporte a board e investidor. De acordo com a CIO.com, 37% dos CFOs admitem não confiar completamente nos dados que eles mesmos usam para decidir. Entre profissionais seniores de finanças e contabilidade, esse número sobe para 50% — metade não confia totalmente nos dados financeiros com que trabalha todo dia.

O custo disso é mensurável. O Gartner estima que má qualidade de dados custa, em média, US$ 12,9 milhões por ano para cada organização — em retrabalho, decisão errada e tempo de analista gasto reconciliando em vez de analisando. Segundo a IDC, em sua Data Trust Survey, 67% dos respondentes não confiam completamente nos dados usados para tomar decisão, e entre quem desconfia, 70% aponta qualidade de dados como o maior problema. A confiança cai ainda mais entre quem trabalha na linha de frente — o time que mais depende do dado correto para agir é o que menos confia nele.

Esse gap de confiança tem um efeito colateral direto na produtividade: segundo o Gartner, até 80% do esforço de relatórios e analytics é gasto preparando e reconciliando dados — não analisando-os ou agindo sobre eles. Times inteiros de FP&A e BI passam o mês reconciliando planilha em vez de interpretar resultado e apoiar decisão.

Para empresas que operam com múltiplos sistemas SAP e não-SAP em paralelo, o caminho recomendado é tratar essa divergência como risco de governança — não como incômodo operacional a ser resolvido informalmente por quem perceber a diferença primeiro.

## A causa raiz: por que os números nunca vão bater sozinhos

Ao contrário do que a maioria dos times de TI e finanças assume, a divergência de dados entre sistemas não se resolve corrigindo o dado errado — porque, na maior parte dos casos, não existe dado errado. Existe ausência de single source of truth: uma fonte única de verdade que defina, para toda a empresa, o que cada métrica significa, de onde ela vem e como ela é calculada.

Sem essa fonte única, cada sistema e cada departamento vira sua própria autoridade sobre o dado. O CRM define "cliente" de um jeito. O ERP define de outro. A área comercial chama de "cliente" o que o financeiro ainda trata como "prospect" ou "lead". Os dois relatórios estão certos dentro da própria lógica — e continuam divergindo.

Três causas estruturais explicam praticamente toda divergência de dados entre sistemas em ambiente corporativo complexo:

- *Ausência de fonte única de verdade (single source of truth): quando não existe uma camada central que define e distribui a métrica oficial, cada sistema assume esse papel sozinho, e a divergência se torna inevitável a cada novo relatório.*
- *Definições de métricas divergentes entre times: o mesmo termo de negócio — receita, cliente, margem, headcount — recebe regras de cálculo diferentes em cada ferramenta, gerando "KPI definition drift": o indicador muda de significado sem que ninguém perceba ou documente a mudança.*
- *Integração e ETL superficiais: quando a integração entre sistemas é feita de forma pontual, sem rastreio de origem (data lineage) nem reconciliação estruturada, pequenas diferenças de corte de data, moeda ou regra de negócio se acumulam silenciosamente ao longo dos meses até virarem divergências grandes o suficiente para travar uma reunião de diretoria.*

Uma camada semântica bem definida — o semantic layer que padroniza a definição de métrica entre ferramentas e departamentos — resolve estruturalmente esse problema, porque garante que "receita" signifique a mesma coisa no ERP, no CRM e no relatório executivo. Sem ela, qualquer esforço de reconciliação de dados vira remendo mensal, refeito do zero a cada fechamento.

Sinais de que a empresa já tem esse problema, mesmo sem ter nomeado ainda:

- *Times diferentes chegam a reuniões com números diferentes para o mesmo indicador, e ninguém sabe dizer com segurança qual está certo.*
- *Existe uma planilha "de ajuste" que alguém mantém manualmente para reconciliar relatórios de sistemas diferentes antes de qualquer apresentação executiva.*
- *A definição de uma métrica-chave (cliente, receita, margem) muda dependendo de quem você pergunta na empresa.*
- *Cada novo relatório ou dashboard aumenta a desconfiança em vez de resolver a dúvida sobre qual número usar.*

## Como a Solveplan estrutura governança de dados de forma contínua

Resolver divergência de dados entre sistemas com um projeto pontual — reconciliar uma vez, entregar um relatório "corrigido" e encerrar o contrato — não resolve a causa raiz. Sem monitoramento contínuo e sem dono formal da definição de métrica, a divergência volta assim que um sistema muda, um time cria uma planilha nova ou uma integração é ajustada sem governança.

A Solveplan é consultoria SAP Gold na América Latina, com mais de 13 anos de atuação, 150 empresas atendidas e mais de 390 projetos entregues por um time de 60 ou mais especialistas SAP dedicados a dados, analytics, planejamento financeiro e consolidação. Em 2026, a Solveplan foi reconhecida como Melhor Parceiro SAP Business Data Cloud da América Latina pelo SAP Partner Awards — reconhecimento direto da capacidade de estruturar ambiente de dados único e governado em escala.

Empresas de grande porte como COPEL, Klabin, Aegea, VALE, Alpargatas e ACHE já passaram pelo mesmo diagnóstico: ambiente fragmentado entre SAP, planilha paralela e ferramentas de BI isoladas, sem uma definição comum de métrica entre áreas. A abordagem da Solveplan nesses casos nunca foi corrigir o relatório do mês — foi tirar a empresa do modelo manual e estruturar um ambiente integrado, com governança formal sobre os quatro pilares que sustentam dado confiável: pessoas, processos, tecnologia e governança.

É esse o raciocínio por trás da Fábrica de Analytics: um squad dedicado e contínuo da Solveplan, não um projeto com data de encerramento. O time monitora definição de métrica, rastreia origem de dado (data lineage), mantém a camada semântica atualizada conforme o negócio muda e garante que divergência de dados entre sistemas seja prevenida antes de aparecer em uma reunião de diretoria — não descoberta depois. Plataformas como SAP Business Data Cloud e SAP Datasphere entram como base tecnológica dessa fonte única de verdade, mas a governança contínua é o que garante que a plataforma continue confiável seis meses ou dois anos depois da implementação.

## O próximo passo é entender onde a divergência começa na sua empresa

Nenhuma empresa resolve divergência de dados entre sistemas revisando manualmente cada relatório antes de cada reunião. Esse modelo não escala, consome hora de analista sênior em tarefa que deveria ser automática e não impede que o problema volte no mês seguinte.

Empresas que não estruturam uma fonte única de verdade continuam pagando o custo identificado pelo Gartner — até 80% do esforço de analytics gasto reconciliando, não decidindo. Sem esse modelo de governança contínua, cada novo sistema, integração ou dashboard aumenta o risco de divergência em vez de reduzi-lo.

O primeiro passo é mapear onde e por que a divergência acontece hoje — quais métricas têm definição conflitante, quais integrações não têm rastreio de origem, quais times operam com fonte de dado própria. A Solveplan faz esse diagnóstico antes de qualquer proposta de solução.

## Perguntas frequentes

**O que causa a divergência de dados entre sistemas?**
Principalmente três fatores: ausência de uma fonte única de verdade, definições de métricas diferentes entre sistemas e departamentos, e integração ou ETL superficial que acumula pequenas diferenças ao longo do tempo até virarem divergências relevantes.

**Qual a diferença entre divergência de dados e erro de dados?**
Erro de dado é um valor incorreto na origem. Divergência de dados entre sistemas geralmente ocorre com dados corretos em cada sistema individual — o problema é a falta de definição comum sobre o que a métrica representa.

**O que é single source of truth (fonte única de verdade)?**
É uma camada central — geralmente uma plataforma de dados com semantic layer — que define oficialmente cada métrica de negócio e distribui essa definição para todos os sistemas, eliminando a possibilidade de cada área calcular o mesmo indicador de um jeito diferente.

**Quanto tempo leva para reconciliar de forma definitiva os dados de uma empresa?**
Reconciliação pontual leva semanas, mas não é definitiva — a divergência volta assim que um sistema ou processo muda. Resolver de forma definitiva exige governança contínua, não um projeto com data de encerramento.

**Ferramentas de BI resolvem a divergência de dados entre sistemas?**
Não sozinhas. Um dashboard bonito sobre dados sem definição comum de métrica só torna a divergência mais visível e mais rápida de aparecer, não a elimina. A camada semântica e a governança precisam vir antes da visualização.

**Como a Solveplan ajuda a resolver esse problema?**
Com a Fábrica de Analytics: um squad dedicado e contínuo que estrutura governança de dados, define métricas únicas entre sistemas e monitora a consistência do dado de forma permanente — não como projeto pontual.

---

**Diagnóstico gratuito — Fábrica de Analytics**
Descubra onde a divergência de dados começa na sua empresa antes que ela apareça na próxima reunião de diretoria.
