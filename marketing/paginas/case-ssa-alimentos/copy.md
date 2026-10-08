# Case SSA Alimentos — SAP Datasphere

**Status:** rascunho para aprovação · não publicado
**Tipo de post no WordPress:** `case` (mesmo modelo da Lins Agroindustrial, em Elementor)
**Fonte:** "[Texto do Site] Case SSA SAP Datasphere.pdf" + vídeo https://youtu.be/T3k8MTIggjA
**Prévia visual:** `preview.html` (nesta pasta)

A estrutura segue a ordem de seções do case da Lins (`/case/lins-agroindustrial-sap-analytics-cloud/`), para dar pra duplicar aquela página no Elementor e trocar o conteúdo.

---

## Configuração SEO (Rank Math)

| Campo | Valor |
|---|---|
| URL | `https://solveplan.com/case/ssa-alimentos-sap-datasphere/` |
| Slug | `ssa-alimentos-sap-datasphere` |
| Meta title (58 caracteres) | SSA Alimentos + SAP Datasphere \| Case de Sucesso Solveplan |
| Meta description (149 caracteres) | Como a SSA Alimentos usou o SAP Datasphere como data warehouse para integrar S/4HANA, SAC, IBP e sistemas não-SAP em uma base governada e rastreável. |
| Palavra-chave principal | SAP Datasphere |
| Palavras-chave secundárias | case SAP Datasphere; SAP Datasphere case de sucesso; gestão de dados SAP; governança de dados SAP; SAP Datasphere Data Warehouse; SAP S/4HANA e Datasphere; SAP Analytics Cloud e Datasphere; SAP IBP e Datasphere; arquitetura de dados SAP; Solveplan SAP Datasphere |
| Resumo (excerpt) | A SSA Alimentos adotou o SAP Datasphere como data warehouse com a Solveplan, conectando SAP S/4HANA, SAP Analytics Cloud, SAP IBP e sistemas não-SAP em uma arquitetura governada, com modelos reutilizáveis e linhagem de dados. |

---

## 1. Título (H1)

**Como a SSA Alimentos estruturou sua gestão de dados com SAP Datasphere**

## 2. Introdução

Quando uma empresa cresce, ter acesso aos dados deixa de ser o desafio. O desafio passa a ser garantir que as diferentes áreas trabalhem com informações organizadas, rastreáveis e prontas para apoiar decisões.

Esse era o ponto em que a SSA Alimentos estava antes do SAP Datasphere. As informações ficavam distribuídas entre sistemas e estruturas diferentes: dados integrados em uma base Oracle por meio de scripts, planilhas Excel usadas tanto para entrada quanto para análise e modelos semânticos descentralizados no Power BI.

## 3. Cards de destaque (3)

| Número | Legenda |
|---|---|
| **~2.000 indicadores** | Base analítica que antes exigia replicar a lógica de negócio a cada novo relatório |
| **SAP + não-SAP** | S/4HANA, SAC e IBP conectados a AVECOM, Lincros, GEPARDO e Sankhya |
| **9 frentes de análise** | Da DRE e do CAPEX a fretes, campo, indústria e mercado externo |

> Os três cards descrevem o escopo do projeto, não ganhos de desempenho. A SSA informou que ainda não tem métricas de impacto, então a página não traz percentuais de ROI, custo ou produtividade.

## 4. O desafio

A construção de aproximadamente 2.000 indicadores exigia replicar lógicas de negócio. A cada novo relatório ou dashboard, parte desse trabalho precisava ser reconstruída e validada.

Ao mesmo tempo, a SSA vivia um momento importante da sua estratégia tecnológica: a implantação do SAP S/4HANA, o projeto de planejamento orçamentário com SAP Analytics Cloud (SAC) e SAP Integrated Business Planning (IBP) e a construção de uma plataforma de dados para suportar a transformação digital. Tudo isso aumentou a necessidade de uma camada de dados integrada ao ecossistema SAP.

**Era necessário evoluir a arquitetura.**

## 5. Citação 1 — [PENDENTE]

> "[Trecho do vídeo]" — Wesley Medanha, [cargo], SSA Alimentos

*O case da Lins tem duas citações do cliente. O texto da SSA não traz nenhuma. Se houver uma fala boa no vídeo, ela entra aqui. Se não houver, a seção sai.*

## 6. Antes e depois (H2: Por que a SSA escolheu o SAP Datasphere?)

O SAP Datasphere passou a exercer o papel de data warehouse da companhia. A plataforma conecta os dashboards em Power BI, o planejamento orçamentário no SAC, o processo de S&OP no IBP e diferentes fontes corporativas, entre elas sistemas SAP e sistemas satélites.

O objetivo não era só centralizar dados. Era criar uma estrutura em que a informação pudesse ser reutilizada, rastreada e consumida com mais eficiência pelas áreas do negócio. Para entender a solução em detalhes, veja a página da Solveplan sobre [SAP Datasphere](https://solveplan.com/sap-datasphere/).

**Antes do SAP Datasphere**
- Dados integrados em base Oracle por scripts
- Excel usado para entrada e para análise
- Modelos semânticos descentralizados no Power BI
- Lógica de negócio replicada em ~2.000 indicadores
- Reconstrução e validação a cada novo relatório

**Depois da implementação**
- SAP Datasphere como data warehouse da companhia
- Fontes SAP e não-SAP integradas em uma única camada
- Modelos de dados reutilizáveis por domínio de negócio
- Linhagem de dados para análise de causa raiz
- Ambiente analítico separado do transacional

## 7. Vídeo — "Assista o case completo"

Embed: `https://www.youtube.com/embed/T3k8MTIggjA` (título no YouTube: "SSA Alimentos", canal SolvePlan)

Legenda: No vídeo, Wesley Medanha, [cargo] da SSA Alimentos, apresenta a experiência da companhia e a evolução da arquitetura de dados.

## 8. Desenvolvimento

### H2: De dados descentralizados a modelos reutilizáveis

Com o SAP Datasphere, a SSA passou a estruturar modelos de dados para diferentes necessidades da organização. O ambiente suporta desde o pipeline do planejamento orçamentário e do realizado da DRE até análises de CAPEX, gestão de fretes, suprimentos, custos, campo, indústria, inteligência de mercado e operações de mercado externo.

Essa mudança trouxe um elemento importante para a estratégia da companhia: governança de dados. A arquitetura construída no SAP Datasphere organiza as informações por domínios de negócio e usa linhagem de dados para tornar a análise de causa raiz mais ágil. A separação entre os ambientes analítico e transacional também reduziu o impacto de processamentos complexos sobre o ERP.

### H2: Quais resultados o SAP Datasphere trouxe para a SSA?

Os benefícios percebidos pela SSA estão em três frentes: integração de fontes, estruturação de modelos reutilizáveis e simplificação da preparação dos dados. A empresa também identificou ganhos em disponibilidade e rastreabilidade das informações, além da redução de atividades manuais e da dependência de dados descentralizados.

O impacto aparece na capacidade analítica. Com mais dados preparados e disponíveis, construir análises para apoiar decisões ficou mais simples e ágil. Menos esforço para reconstruir e validar a informação a cada nova demanda, mais capacidade para usá-la.

### H2: Governança antes de escala

A jornada deixou aprendizados que vão além da tecnologia. Para a SSA, três pontos foram fundamentais:

1. Preparar os dados para consumo
2. Estabelecer uma fonte única e confiável de informação, o *source of truth*
3. Envolver as áreas de negócio no processo de governança de dados

Esses fundamentos valem para qualquer organização que pretende ampliar analytics, planejamento e iniciativas baseadas em dados. Uma arquitetura moderna não começa pelo dashboard. Começa pela qualidade daquilo que o alimenta.

### H2: SSA Alimentos, SAP Datasphere e Solveplan

A jornada da SSA mostra o SAP Datasphere funcionando como camada estratégica de dados, conectando aplicações e fontes diferentes e criando uma estrutura mais organizada para analytics e planejamento.

O projeto também reforça uma discussão cada vez mais presente em empresas SAP: antes de escalar analytics e inteligência artificial, é preciso saber onde os dados estão, como são transformados e qual informação deve ser considerada confiável. Para quem está evoluindo a arquitetura de dados no ecossistema SAP, veja também como a Solveplan aborda o [SAP Business Data Cloud](https://solveplan.com/sap-business-data-cloud/).

## 9. CTA intermediário

**Quer estruturar uma fundação de dados mais integrada e governada?**
Botão: **Fale conosco** → página de contato (mesmo botão da Lins)

## 10. FAQ — SAP Datasphere na SSA Alimentos

(bloco `<details>` no mesmo formato dos outros cases)

**Qual solução SAP foi implementada na SSA Alimentos?**
O [SAP Datasphere](https://solveplan.com/sap-datasphere/), usado como data warehouse da SSA. Ele integra informações do SAP S/4HANA, do SAP Analytics Cloud, do SAP IBP e de outras fontes corporativas.

**Qual era o principal desafio da SSA antes do SAP Datasphere?**
Os dados estavam distribuídos entre sistemas, scripts, base Oracle, planilhas e modelos semânticos descentralizados no Power BI. A construção de cerca de 2.000 indicadores também exigia replicar a lógica de negócio.

**Quais benefícios a SSA percebeu com o SAP Datasphere?**
Integração de fontes, modelos de dados reutilizáveis, preparação de dados simplificada, maior disponibilidade e rastreabilidade das informações e redução de atividades manuais.

**Como o SAP Datasphere apoia a tomada de decisão na SSA?**
Com mais dados preparados e disponíveis, construir análises para apoiar decisões ficou mais simples e ágil.

**Qual foi o principal aprendizado do projeto?**
Preparar os dados para consumo, estabelecer um *source of truth* e envolver as áreas de negócio na governança de dados.

**O SAP Datasphere integra dados SAP e não-SAP?**
Sim. No ambiente da SSA, o SAP Datasphere conecta SAP S/4HANA, SAP Analytics Cloud e SAP IBP a sistemas não-SAP como AVECOM, Lincros, GEPARDO e Sankhya.

## 11. CTA final

Botão: **Avalie a maturidade dos seus dados com a Solveplan** → `https://bdcstrategy.solveplan.ai/` (padrão dos demais cases)

---

## Links internos

- SAP Datasphere → `https://solveplan.com/sap-datasphere/` (seção 6 e FAQ)
- SAP Business Data Cloud → `https://solveplan.com/sap-business-data-cloud/` (seção 8)
- Serviços Solveplan → definir URL (o PDF cita, mas não traz o link)
- Vídeo → `https://youtu.be/T3k8MTIggjA`

## Ajustes feitos em relação ao PDF

- Slug: o PDF indica `/cases/...`, mas os cases do site ficam em `/case/...`. Mantive `/case/ssa-alimentos-sap-datasphere/`.
- Meta description: a do PDF tem cerca de 205 caracteres e seria cortada no Google. Reduzi para 149.
- Correções de texto: "SAP e sistema satélites" → "sistemas SAP e sistemas satélites"; vírgula removida em "Wesley Medanha, apresenta".
- Estrutura: o conteúdo foi encaixado no modelo da Lins (cards, antes/depois, vídeo, FAQ, CTA de maturidade).
- FAQ: a pergunta sobre SAP e não-SAP ganhou um "Sim." no começo da resposta (melhor para snippet).
- Nenhum número de impacto foi incluído, conforme a observação editorial do PDF.

## Pendências antes de publicar

1. Cargo do Wesley Medanha (aparece na legenda do vídeo)
2. Citação do vídeo para a seção 5 (opcional; sem ela, a seção sai)
3. Logo da SSA e imagem destacada do case
4. URL da página de serviços
5. Backup do site (hPanel) antes de criar o post
