# Sua empresa já ajustou o SAP para a reforma tributária. O modelo de orçamento no SAC também foi?

**Autor:** Alexandre Kuntgen, Partner na Solveplan
**Formato:** Artigo LinkedIn (long-form)

---

Nas últimas semanas ouço a mesma frase de CFOs e controllers que já rodam SAP Analytics Cloud para planejamento: "a gente já ajustou o SAP pra IBS e CBS." Ajustaram o ERP. Aplicaram as SAP Notes, revisaram CFOP, testaram a nota fiscal.

O modelo de orçamento, na maioria dos casos, continua rodando com a lógica tributária antiga.

**Impacto da reforma tributária no orçamento** é o conjunto de mudanças que a transição para IBS e CBS impõe às premissas do modelo de planejamento financeiro — receita líquida no lugar de receita bruta, ciclo de caixa mais curto, margem recalculada — independente de o ERP já emitir a nota fiscal corretamente. É um problema de modelo, não de sistema transacional.

**Ajustar o SAP resolve a nota fiscal. Não resolve o orçamento**

O trabalho que a maioria das empresas já fez em 2026 foi de compliance fiscal: atualizar tabelas de imposto, sequências de acesso, layout de XML, para que a operação continue emitindo documento fiscal válido. É trabalho de TI e fiscal, necessário e urgente.

A Volkswagen do Brasil tratou esse movimento como programa formal, não como patch de sistema — modernizou a gestão fiscal com SAP Document and Reporting Compliance como pré-requisito tecnológico para a reforma. Como resumiu Jackson Borges, VP Regional de Finanças da SAP América Latina, sobre esse tipo de movimento: "a evolução para plataformas em nuvem e soluções integradas é fundamental."

O ponto que costuma ficar de fora desse programa é o modelo de planejamento. Se o orçamento da sua empresa roda no SAP Analytics Cloud, ele tem lógica própria de alíquota, de composição de receita e de margem — parametrizada há anos, sob o regime de ICMS, PIS e COFINS. Corrigir o ERP não corrige essa lógica. Alguém precisa remapear o modelo.

**O que muda de fato na conta**

Com o split payment, o tributo é retido no momento da liquidação financeira. Isso muda a base da receita: o modelo deixa de trabalhar sobre valor bruto e passa a considerar o valor líquido, já descontado de IBS e CBS. Se a fórmula de receita do seu modelo em SAC ainda assume entrada bruta, a projeção de caixa nasce errada.

A alíquota combinada estimada de IBS e CBS gira em torno de 26,5% — mas incide sobre valor líquido, já descontados os créditos tributários da não cumulatividade plena. Isso significa que a margem projetada no modelo antigo, calculada sob a lógica cumulativa de PIS/COFINS, não reflete mais a estrutura de custo real da operação.

E o efeito não para na margem. Um estudo da Tax Group de agosto de 2026 estima que cerca de 981 mil empresas — 56,2% do universo de 1,75 milhão de empresas no lucro real e presumido — têm potencial de piora no fluxo de caixa com o split payment, pela perda do float entre o recebimento da venda e o recolhimento do imposto. A conta: R$ 117 bilhões em capital de giro adicional necessário, com custo financeiro nacional estimado entre R$ 32 e R$ 38 bilhões por ano.

Nenhum desses números aparece automaticamente no seu modelo de orçamento só porque o ERP está em conformidade.

**O prazo não é 2033, é agora**

O cronograma de sete anos até o modelo consolidado em 2033 passa a impressão de que dá tempo. Não dá, para o orçamento. 2026 já é ano de teste, com CBS e IBS cobrados a alíquota simbólica desde janeiro. O Comitê Gestor do IBS e a Receita Federal já publicaram o calendário de obrigatoriedade dos documentos fiscais eletrônicos: NF-e, NFC-e e CT-e a partir de agosto de 2026, NFS-e em outubro, e o restante das operações até janeiro de 2027 — quando a CBS passa a valer com alíquota cheia e PIS/COFINS são extintos.

Ao contrário do que aconteceu com o ERP, que teve ano inteiro de SAP Notes e correção guiada, não existe pacote de atualização automática para o modelo de planejamento. Uma pesquisa da IOB com mais de 4.500 empresas do regime regular encontrou inconsistência cadastral ou tributária em 93% dos produtos analisados na adaptação ao IBS e CBS — e isso é só o cadastro fiscal. O orçamento constrói em cima desse dado.

**O que eu recomendo pra quem já tem o modelo em SAC**

Se a sua empresa já usa SAP Analytics Cloud para o ciclo de orçamento e forecast, o caminho recomendado é tratar a revisão do modelo como projeto formal, com dono e prazo — não como ajuste que "a equipe de planejamento faz quando sobrar tempo". Isso significa remapear a lógica de alíquota nas data actions e fórmulas do modelo, redefinir receita e margem sobre base líquida, e incorporar cenário de capital de giro para o efeito do split payment antes de 2027.

A Solveplan tem trabalhado com empresas nesse exato ponto de virada: ambiente SAP Analytics Cloud maduro, mas modelo de premissas desatualizado em relação à reforma. O diagnóstico costuma revelar o mesmo padrão — o sistema está pronto, o modelo não está.

**Perguntas frequentes**

**Se o ERP já está ajustado para IBS e CBS, o orçamento no SAC também está?**
Não necessariamente. O ajuste no ERP corrige a emissão fiscal. O modelo de orçamento tem lógica própria de alíquota e composição de receita, parametrizada separadamente, e precisa de revisão específica.

**Qual o principal risco para quem não revisar o modelo de orçamento?**
Projetar receita, margem e caixa sobre premissas de um regime tributário que está sendo extinto — gerando forecast estruturalmente errado a partir de 2027, quando a CBS passa a valer com alíquota cheia.

**O split payment afeta todas as empresas do mesmo jeito?**
Não. O impacto é maior em empresas com prazo de recebimento longo ou vendas parceladas, que hoje usam o intervalo entre venda e recolhimento do imposto como capital de giro informal.

**Quando isso precisa estar pronto?**
O calendário oficial prevê obrigatoriedade escalonada de documentos fiscais entre agosto de 2026 e janeiro de 2027. O modelo de orçamento deveria estar revisado antes da CBS entrar em vigor com alíquota cheia, em 2027.

---

Sua empresa já ajustou o SAP. E o modelo de orçamento, já foi revisado pra nova base tributária?

Se esse é um ponto em aberto no seu ambiente SAP Analytics Cloud, vale uma conversa. A Solveplan avalia a maturidade do modelo de planejamento frente à reforma tributária e estrutura a revisão com cronograma e critério de sucesso definidos.

**[Avalie a maturidade dos seus dados com a Solveplan](https://bdcstrategy.solveplan.ai/)**

---

### Fontes

- [Receita Federal e Comitê Gestor do IBS — Cronograma de Implementação dos Documentos Fiscais Eletrônicos da Reforma Tributária do Consumo](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/julho/receita-federal-e-comite-gestor-do-ibs-publicam-o-cronograma-de-implementacao-dos-documentos-fiscais-eletronicos-da-reforma-tributaria-do-consumo)
- [IOB — Reforma Tributária: adiamento da rejeição de notas sem IBS e CBS (pesquisa com 4.500+ empresas, 93% de inconsistências)](https://noticias.iob.com.br/reforma-adiamento-rejeicao-notas-ibs-cbs/)
- [Tax Group — Fluxo de caixa na Reforma Tributária: split payment e capital de giro (agosto de 2026)](https://www.taxgroup.com.br/intelligence/fluxo-de-caixa-na-reforma-tributaria-entenda-os-impactos-e-o-que-muda-para-a-sua-empresa/)
- [Treasy — Reforma Tributária: impacto no caixa e nas empresas](https://www.treasy.com.br/blog/reforma-tributaria-2026/)
- [Qive — Reforma Tributária: impactos no planejamento financeiro](https://qive.com.br/blog/reforma-tributaria-impactos-planejamento-financeiro)
- [SAP News Brasil — Volkswagen moderniza gestão fiscal em preparação para a reforma tributária com SAP DRC](https://news.sap.com/brazil/2026/05/volkswagen-moderniza-gestao-fiscal-em-preparacao-para-a-reforma-tributaria-com-sap-drc/)

---

#SAP #ReformaTributaria #SAPAnalyticsCloud #FPandA #CFO
