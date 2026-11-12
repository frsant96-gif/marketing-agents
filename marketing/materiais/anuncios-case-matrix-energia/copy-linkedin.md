# LinkedIn Ads — Case Matrix Energia (vídeo)

**Solução:** Consolidação societária no SAP Analytics Cloud, integrada ao SAP Business One
**Objetivo:** Visitas ao site (tráfego para o case)
**Destino:** https://solveplan.com/case/matrix-energia/
**Público:** CFO e Controller
**Budget:** R$ 1.500/mês
**Formato:** Video Ad (feed)
**Vídeos:** `dados/video-matrix-energia/clips/` (usar sempre a versão `-legendado.mp4`)

Fatos usados no copy, todos ditos no vídeo ou publicados no case: mais de 70 CNPJs, planos de contas diferentes, intercompany sem sociedade parceira, go-live em 3 meses, consolidação em minutos, fechamento do 22º para o 11º dia útil, especialista da Solveplan que também é contador.

---

## Anúncio 1 — Resultado (vídeo 03, 65s) · prioridade

Arquivo: `03-resultado-fechamento-22-para-11-dias-legendado.mp4`

### Variante A — PAS
- **Intro text:** A Matrix Energia fechava o grupo no 22º dia útil, com a consolidação em Excel. E Excel aceita qualquer coisa, inclusive erros.
- **Headline:** Fechamento do 22º para o 11º dia útil com SAP Analytics Cloud
- **Description:** Case Matrix Energia: consolidação societária em 3 meses
- **CTA:** Saiba mais

### Variante B — BAB
- **Intro text:** Antes: consolidação em Excel e fechamento no 22º dia útil. Hoje: 11º dia útil, com número rastreável. Veja como a Matrix fez.
- **Headline:** Consolidação societária no SAC, integrada ao Business One
- **Description:** Go-live em 3 meses. Veja o case completo.
- **CTA:** Saiba mais

---

## Anúncio 2 — Desafio (vídeo 01, 59s)

Arquivo: `01-desafio-70-cnpjs-intercompany-legendado.mp4`

### Variante A — PAS
- **Intro text:** Mais de 70 CNPJs, planos de contas diferentes e intercompany sem sociedade parceira. Era isso que atrasava o fechamento da Matrix.
- **Headline:** Consolidação de 70+ CNPJs no SAP Analytics Cloud em 3 meses
- **Description:** Regras de eliminação sob medida, integradas ao Business One
- **CTA:** Saiba mais

### Variante B — BAB
- **Intro text:** O grupo usa Business One ou ECC e não tem Group Reporting? A Matrix Energia estava assim. Hoje consolida em poucos minutos.
- **Headline:** Consolidação societária sem Group Reporting: o case Matrix
- **Description:** SAP Analytics Cloud + Business One, go-live em 3 meses
- **CTA:** Saiba mais

---

## Anúncio 3 — Parceria (vídeo 02, 39s)

Arquivo: `02-parceria-solveplan-legendado.mp4`

### Variante A — PAS
- **Intro text:** Projeto de consolidação atrasa quando o fornecedor não entende de contabilidade. Na Matrix Energia, o especialista era contador.
- **Headline:** Consolidação no SAC em 3 meses, sem nenhum atraso
- **Description:** Case Matrix Energia com a Solveplan
- **CTA:** Saiba mais

### Variante B — BAB
- **Intro text:** A primeira tentativa de consolidação da Matrix Energia não resolveu. A segunda entrou no ar em 3 meses, sem atraso.
- **Headline:** O que mudou na segunda tentativa de consolidação da Matrix
- **Description:** Especialista contador + SAP Analytics Cloud
- **CTA:** Saiba mais

---

## Configuração da campanha

**Grupo de campanhas:** `2026-11_case-matrix_consolidacao`
**Campanha:** `matrix_video_website-visits_cfo-controller`
**Objetivo:** Website Visits
**Formato:** Video Ad
**Lance:** Maximum Delivery (automático) nas primeiras 2 semanas
**Budget:** R$ 50/dia (R$ 1.500 em 30 dias)
**Frequência:** 3 a 5 impressões por pessoa por semana

### Segmentação
- **Localização:** Brasil
- **Cargos:** CFO, Diretor Financeiro, Diretor de Controladoria, Controller, Gerente de Controladoria, Gerente de Contabilidade, Contador Geral, Coordenador de Consolidação, Gerente de Planejamento Financeiro
- **Senioridade:** Gerente, Diretor, VP, CXO
- **Porte da empresa:** 200 a 10.000 funcionários
- **Setores:** Energia e utilities, Indústria, Agronegócio, Varejo, Holdings e serviços financeiros
- **Tamanho de audiência ideal:** 40 a 80 mil pessoas (com R$ 50/dia, audiência maior dilui a frequência)
- **Excluir:** clientes atuais (lista de empresas do HubSpot), funcionários da Solveplan, consultorias SAP concorrentes

### Plano de teste com R$ 1.500
O budget está abaixo dos R$ 3.000/mês que costumamos indicar, e não dá pra rodar as 6 variantes ao mesmo tempo sem pulverizar os dados. A ordem sugerida:

- **Semanas 1 e 2:** os 3 vídeos no ar com a Variante A. O objetivo é descobrir qual vídeo performa melhor.
- **Semanas 3 e 4:** pausar o vídeo com pior CTR. No melhor vídeo, colocar a Variante B ao lado da A para testar o ângulo do copy.

**O que olhar:** CTR (referência para vídeo no LinkedIn: acima de 0,4%), custo por clique, taxa de visualização até 50% e 100%, e tempo de permanência na página do case (GA4).

### Rastreamento
- **Insight Tag:** confirmar que está ativo no site antes de subir
- **UTMs:**
  - Anúncio 1A: `https://solveplan.com/case/matrix-energia/?utm_source=linkedin&utm_medium=paid&utm_campaign=case-matrix-consolidacao&utm_content=video-resultado-a`
  - Anúncio 1B: `...&utm_content=video-resultado-b`
  - Anúncio 2A: `...&utm_content=video-desafio-a`
  - Anúncio 2B: `...&utm_content=video-desafio-b`
  - Anúncio 3A: `...&utm_content=video-parceria-a`
  - Anúncio 3B: `...&utm_content=video-parceria-b`

### Especificações do vídeo
- Os arquivos estão dentro do limite do LinkedIn (MP4, de 23 a 33 MB e de 39 a 65s)
- Subir a versão `-legendado.mp4`. A maioria assiste sem som, e a legenda já está queimada no vídeo. Por isso, **não subir o `.srt`**, ou a legenda aparece duplicada
- Os vídeos estão em 16:9. No feed do celular, vídeo quadrado (1:1) ou 4:5 ocupa mais tela e costuma ter melhor visualização. Vale gerar essa versão antes de subir
- Thumbnail personalizada: ver `briefing-visual.md`

### Próximo passo depois do clique
A página do case não tem formulário de contato, só leitura. Para essa campanha gerar pipeline, vale criar depois uma audiência de remarketing com quem assistiu 50% ou mais do vídeo ou visitou o case, e mandar para ela um Lead Gen Form ("Fale com um especialista em consolidação").
