---
name: anuncio
description: Cria copy, briefing visual (Canva) e configuração sugerida de campanha para anúncios da Solveplan no LinkedIn Ads e Google Ads.
---

# /anuncio

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md`, `_contexto/estrategia.md` e `marca/design-guide.md`.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual o produto ou solução em foco?" — ex: SAP BDC, SAC, Datasphere, FP&A, AMS
2. "Qual o objetivo da campanha?" — opções: Geração de leads / Agendamento de reunião / Awareness / Tráfego para landing page / Remarketing
3. "Qual a plataforma?" — LinkedIn / Google / Ambas
4. "Qual o público-alvo?" — cargo, segmento, porte de empresa
5. "Tem uma landing page de destino? Se sim, qual a URL ou tema da página?"
6. "Qual o budget mensal estimado?" — se não souber, informar "a definir"

Se o usuário já informou algum dado antes de rodar a skill, não perguntar de novo.

## Frameworks de copy (PAS / BAB)

Usar um framework diferente por variante — isso garante que o teste A/B compara ângulos de verdade, não só palavras diferentes pro mesmo ângulo.

- **PAS (Problem-Agitate-Solve):** nomeia a dor → intensifica a consequência de não resolver → apresenta a Solveplan como solução. Funciona bem pra público que já sente o problema (ex: controller com fechamento lento).
- **BAB (Before-After-Bridge):** descreve o cenário atual doloroso → pinta o cenário ideal depois da solução → a Solveplan é a ponte entre os dois. Funciona bem pra público que ainda não nomeou a dor claramente, mas reconhece o estado ideal.

**Regra:** Variante A usa PAS, Variante B usa BAB (ou o inverso) — nunca as duas variantes no mesmo framework.

## Passo 2 — Gerar por plataforma

---

### LinkedIn Ads

#### Copy do anúncio (Single Image Ad — formato principal)

Gerar 2 variantes pra teste A/B, cada uma seguindo um framework diferente (ver seção "Frameworks de copy" acima):

**Variante A — framework PAS:**
- **Intro text** (texto acima da imagem — máximo 150 caracteres): [Problem — nomeia a dor] + [Agitate — consequência de não resolver]
- **Headline** (título do card — máximo 70 caracteres): [Solve — proposta de valor direta com palavra-chave]
- **Description** (subtítulo — máximo 70 caracteres): [complemento ou prova]
- **CTA button:** [opções: Saiba mais / Registre-se / Entre em contato / Baixe agora / Solicite uma demonstração]

**Variante B — framework BAB:**
- **Intro text:** [Before — cenário atual doloroso]
- **Headline:** [After — cenário ideal + Bridge, a Solveplan como ponte]
- **Description:** [complemento]
- **CTA button:** [mesmo ou diferente]

**Regras do copy LinkedIn:**
- Intro text: primeira linha tem que parar o scroll no feed — afirmação forte ou dado
- Headline: clareza > criatividade — o leitor tem 2 segundos
- Nunca usar "transformação digital" sem contexto
- Tom: autoridade, direto, foco em resultado de negócio

#### Briefing visual pro Canva

- **Formato:** 1200x627px (Single Image) — compatível com feed e coluna lateral
- **Variante stories/document ads:** 1080x1920px (se aplicável)
- **Fundo:** `#0A0E19` ou `#0A0837`
- **Elemento principal:** [dado em destaque / mockup de interface / foto corporativa com overlay escuro]
- **Headline na imagem:** [máximo 6 palavras — versão visual do headline do anúncio]
- **Cor de destaque:** `#006AFF` no elemento ou borda
- **Logo:** `logo-escuro.png.png`, canto inferior direito
- **Overlay em fotos:** `#0A0E19` 55-65% de opacidade
- **Fonte:** Prompt ExtraBold pra headline visual | Montserrat pra dados/subheadline

#### Configuração sugerida da campanha

**Objetivo de campanha:** [Website Visits / Lead Gen Form / Brand Awareness — conforme objetivo informado]

**Segmentação sugerida:**
- Localização: Brasil
- Cargo (Job Title): [lista com base no público informado — ex: CIO, CFO, Head de TI, Controller]
- Senioridade: Diretor, VP, C-Level, Gerente Sênior
- Porte da empresa: 200+ funcionários (ou 500+ se enterprise)
- Setor: [sugerir com base no produto — ex: Manufacturing, Financial Services, Retail, Energy]
- Audiência excluída: concorrentes (se aplicável)

**Formato de campanha recomendado:**
- Lead Gen Form se objetivo = leads (evita perda de conversão fora do LinkedIn)
- Website Clicks se tem landing page otimizada
- Document Ad se tem e-book ou material rico pra oferecer

**Lance e budget:**
- Estratégia de lance: Maximum Delivery (automático) no início pra coletar dados
- Frequência ideal: 3-5 impressões por usuário por semana
- Budget mínimo recomendado: R$ 3.000/mês pra ter volume de dados suficiente

**Rastreamento:**
- Insight Tag instalado no site: [confirmar com o usuário se já está ativo]
- UTM sugerido: `utm_source=linkedin&utm_medium=paid&utm_campaign=[nome-campanha]&utm_content=[variante-a-ou-b]`

---

### Google Ads

#### Search Ads (Responsive Search Ad)

Gerar assets pra preencher no Google Ads:

**Headlines (máximo 30 caracteres cada — gerar 8-10 opções):**
1. [palavra-chave principal]
2. [benefício direto]
3. [dor resolvida]
4. [prova / número]
5. [nome da solução]
6. [urgência ou contexto]
7. [diferencial Solveplan]
8. [CTA como headline]

**Descriptions (máximo 90 caracteres cada — gerar 4 opções):**
1. [dor + solução + CTA]
2. [resultado + diferencial + CTA]
3. [prova + proposta de valor]
4. [pergunta + resposta direta]

**Keywords sugeridas (segmentação):**
- **Termos de intenção alta:** [ex: "implementação SAP BDC", "consultoria SAP Analytics Cloud", "projeto SAP Datasphere"]
- **Termos de problema:** [ex: "como integrar dados SAP", "relatórios financeiros automatizados SAP"]
- **Correspondência:** phrase match e exact match — evitar broad sem qualificadores no início
- **Negative keywords:** [sugerir termos a excluir — ex: "grátis", "curso", "trainee", "emprego"]

**Extensions (ativos recomendados):**
- Sitelinks: [4 links sugeridos — ex: "Sobre a Solveplan", "Cases", "SAP BDC", "Falar com especialista"]
- Callout: [4 frases curtas — ex: "Parceiro SAP Gold", "+90 clientes", "Projetos desde 30 dias", "Diagnóstico gratuito"]
- Call extension: [número de telefone se aplicável]

#### Configuração sugerida da campanha

**Tipo de campanha:** Search (pra intenção ativa) / Performance Max (pra escala com assets variados)

**Objetivo:** Leads / Visitas ao site

**Lance:** Target CPA (se tiver histórico) ou Maximize Conversions (se novo)

**Budget:** R$ [sugerir com base no budget informado — mínimo R$ 1.500/mês pra Search com volume]

**Configurações importantes:**
- Rede de pesquisa apenas (desativar Display Network no início)
- Localização: Brasil — só pessoas no local, não "interessadas no local"
- Idioma: Português
- Horário: seg-sex, 8h-19h (ajustar conforme dados)

**UTM sugerido:** `utm_source=google&utm_medium=cpc&utm_campaign=[nome-campanha]&utm_term={keyword}&utm_content=[grupo-de-anuncios]`

---

## Alocação de budget (quando já existe campanha rodando)

Se o usuário já tem campanhas ativas e está pedindo pra alocar budget novo ou redistribuir entre campanhas/anúncios, usar a matriz 70/30:

- **70% pro que já é comprovado** — campanhas/anúncios com CPL ou CTR acima da média histórica da conta
- **30% pra teste** — novos ângulos de copy, novos formatos ou novos segmentos ainda sem dado

Nunca alocar 100% no comprovado (a conta para de aprender) nem mais de 30% em teste sem dado (queima budget sem base). Se o usuário não tiver histórico ainda (conta nova), pular essa lógica e usar o budget mínimo recomendado normalmente.

## Passo 3 — Salvar

Criar pasta `marketing/materiais/anuncios-[slug-do-tema]/` e salvar:
- `copy-linkedin.md` — variantes de copy + configuração LinkedIn (se aplicável)
- `copy-google.md` — headlines, descriptions, keywords + configuração Google (se aplicável)
- `briefing-visual.md` — instruções pro Canva

## Passo 4 — Confirmar

Informar onde foi salvo e perguntar:

> "Quer ajustar algum ângulo de copy, adicionar mais variantes, ou criar a landing page de destino com `/pagina-solucao`?"

## Regras

- Sempre gerar 2 variantes de headline/copy pra teste A/B — anúncio sem teste não aprende
- LinkedIn: Lead Gen Form > landing page externa sempre que o objetivo for captura de lead
- Google: iniciar com search + exact/phrase match antes de escalar pra broad ou PMax
- Copy de anúncio é diferente de copy de conteúdo — mais curto, mais direto, mais urgente
- UTM em todos os anúncios — rastreamento é obrigatório
- SAP BDC como foco principal quando o produto não for especificado
- Nunca prometer resultado sem base: "reduza o tempo de fechamento" exige dado ou case
