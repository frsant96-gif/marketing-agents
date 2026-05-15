# LinkedIn Marketing API — Referencia Rapida

## Autenticacao

- OAuth 2.0 Authorization Code Flow
- Scopes necessarios: `r_ads rw_ads r_ads_reporting`
- Access token expira em ~60 dias; refresh token em ~1 ano
- Header obrigatorio: `LinkedIn-Version: 202405`

## Hierarquia de objetos

```
Ad Account
└── Campaign Group  (objetivo, orcamento total, datas)
    └── Campaign    (tipo, formato, targeting, budget/dia, bid)
        └── Creative (conteudo: post, imagem, video, texto)
```

## Tipos de campanha (type)

| Tipo | Descricao |
|------|-----------|
| `SPONSORED_UPDATES` | Sponsored Content (imagem, video, carrossel, documento) |
| `TEXT_AD` | Anuncios de texto simples na sidebar |
| `SPONSORED_INMAILS` | Message Ads (InMail patrocinado) |
| `DYNAMIC` | Dynamic Ads (spotlight, follower, jobs) |

## Formatos de campanha (format)

| Formato | Tipo pai |
|---------|----------|
| `STANDARD_UPDATE` | Sponsored Content — post unico |
| `CAROUSEL` | Sponsored Content — carrossel |
| `VIDEO` | Sponsored Content — video |
| `SINGLE_IMAGE` | Sponsored Content — imagem unica |
| `DOCUMENT` | Sponsored Content — PDF/documento |
| `CONVERSATION` | Message Ads |
| `TEXT_AD` | Text Ads |

## Objetivos (objectiveType)

| Objetivo | Quando usar |
|----------|-------------|
| `BRAND_AWARENESS` | Alcance e visibilidade |
| `WEBSITE_VISITS` | Trafego para site |
| `ENGAGEMENT` | Curtidas, comentarios, seguidores |
| `VIDEO_VIEWS` | Visualizacoes de video |
| `LEAD_GENERATION` | Formulario nativo LinkedIn |
| `WEBSITE_CONVERSIONS` | Conversoes no site (pixel) |
| `JOB_APPLICANTS` | Candidatos a vagas |

## Tipos de lance (costType)

| Tipo | Descricao |
|------|-----------|
| `CPM` | Custo por 1000 impressoes |
| `CPC` | Custo por clique |
| `CPV` | Custo por visualizacao (video) |
| `CPL` | Custo por lead (Lead Gen Forms) |

## Segmentacao — facetas principais

| Faceta URN | Descricao |
|------------|-----------|
| `urn:li:adTargetingFacet:titles` | Cargos |
| `urn:li:adTargetingFacet:seniorities` | Senioridade |
| `urn:li:adTargetingFacet:industries` | Setores |
| `urn:li:adTargetingFacet:companySizes` | Tamanho da empresa |
| `urn:li:adTargetingFacet:companies` | Empresas especificas |
| `urn:li:adTargetingFacet:skills` | Habilidades |
| `urn:li:adTargetingFacet:memberBehaviors` | Comportamentos |
| `urn:li:adTargetingFacet:locations` | Localizacao |

## Metricas de analytics

| Metrica | Descricao |
|---------|-----------|
| `clicks` | Cliques |
| `impressions` | Impressoes |
| `costInLocalCurrency` | Gasto na moeda local |
| `leads` | Leads (Lead Gen Form) |
| `oneClickLeads` | Leads com 1 clique |
| `externalWebsiteConversions` | Conversoes no site |
| `videoViews` | Visualizacoes de video |
| `opens` | Aberturas (InMail) |

## URNs de objetos

```
Conta:          urn:li:sponsoredAccount:{id}
Grupo:          urn:li:sponsoredCampaignGroup:{id}
Campanha:       urn:li:sponsoredCampaign:{id}
Criativo:       urn:li:sponsoredCreative:{id}
Post organico:  urn:li:ugcPost:{id}  ou  urn:li:share:{id}
```

## Documentacao oficial

- Marketing API: https://learn.microsoft.com/en-us/linkedin/marketing/
- Ad Analytics: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting
- OAuth: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow
