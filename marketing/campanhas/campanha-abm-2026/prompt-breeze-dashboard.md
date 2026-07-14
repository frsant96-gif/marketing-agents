# Prompt para o Breeze (HubSpot AI) — Dashboard de ABM

Cole o texto abaixo no Breeze Copilot dentro do HubSpot (ou use como briefing pra criar manualmente em Reports > Dashboards).

Estrutura por canal (não por objeto Campaign) — cobre todo o funil de execução da campanha ABM.

---

Crie um dashboard chamado **"ABM 2026 — Performance por Canal"**, com os relatórios abaixo organizados em 4 blocos. Filtre por campanha **"Campanha de ABM 2026"** (ID do objeto: 539216547952) onde houver essa opção; onde não houver, filtre pela lista de UTMs/URLs dessa campanha.

## Bloco 1 — LinkedIn Ads
1. Investimento (spend)
2. Impressões
3. Alcance
4. Frequência
5. Cliques
6. CTR
7. CPC
8. Engajamento (reações, comentários, compartilhamentos)
9. Desempenho por anúncio (tabela)

*Fonte: integração nativa LinkedIn Ads no HubSpot. Alcance e frequência normalmente só ficam disponíveis para campanhas com objetivo Brand Awareness/Reach — se a campanha ABM não for desse tipo, esses dois itens vêm da API do LinkedIn Campaign Manager, fora do HubSpot.*

## Bloco 2 — Peças (criativos)
1. Impressões por criativo
2. Cliques por criativo
3. CTR por criativo
4. CPC por criativo
5. Engajamento por peça
6. Melhor e pior peça (ranking)

*Fonte: mesma integração do Bloco 1, quebrada por creative ID.*

## Bloco 3 — Landing page
1. Visualizações
2. Visitantes
3. Origem do tráfego
4. Envios de formulário
5. Taxa de conversão
6. Abandono
7. Conversão por UTM

*Fonte: HubSpot nativo (Landing Pages + Forms + Traffic Analytics), filtrado pela(s) landing page(s) dessa campanha.*

## Bloco 4 — E-mail marketing
1. E-mails enviados
2. Entregues
3. Taxa de entrega
4. Aberturas
5. Taxa de abertura
6. Cliques
7. CTR
8. CTOR
9. Descadastros
10. Rejeições (bounces)
11. Resultado por disparo (tabela, um envio por linha)

*Fonte: HubSpot nativo (Marketing Email analytics), filtrado pelos e-mails associados à campanha "Campanha de ABM 2026".*

---

Se algum dado não estiver disponível diretamente (ex: alcance/frequência do LinkedIn), sinalize no relatório em vez de omitir o card.
