---
name: release-pr
description: Cria release para imprensa e pitch para jornalistas. Acionado por cases de sucesso ou anúncios importantes da Solveplan.
---

# /release-pr

## Antes de começar

Ler `_contexto/empresa.md` e `_contexto/preferencias.md`.

## Quando usar

- Publicação de case de sucesso com cliente
- Anúncio importante: parceria, certificação, conquista, lançamento
- Cobertura de evento relevante pós-execução

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual o assunto do release?" — case de cliente / anúncio / conquista / evento
2. "Qual o fato principal — o que aconteceu, com quem, com que resultado?"
3. "Tem dados ou resultados concretos? (ex: X% de redução, Y meses de projeto, Z usuários impactados)"
4. "Tem uma citação da Fran ou de alguém da Solveplan que quer incluir?"
5. "Tem nome de cliente? (se confidencial, descrever o segmento e porte)"
6. "Qual veículo ou tipo de veículo você quer atingir?" — opções: TI corporativa (CIO) / Financeiro/gestão (CFO) / SAP/ERP / Business geral / Todos

Se o usuário já forneceu as informações antes de rodar a skill, não perguntar de novo.

## Passo 2 — Gerar o release

Escrever o release no formato padrão jornalístico:

**Estrutura:**
```
[CIDADE, DATA] — [Lead: o fato principal em 2-3 linhas, com o quê, quem, resultado]

[Parágrafo 2: contexto — por que isso importa, qual o cenário de mercado]

[Parágrafo 3: desenvolvimento — como foi feito, detalhes do projeto ou conquista]

[Parágrafo 4: citação] — "[Nome], [cargo] da Solveplan: '[frase direta, sem jargão, com convicção]'"

[Parágrafo 5: ponto de prova adicional ou dado de contexto]

[Parágrafo 6 — opcional: citação do cliente, se aplicável]

Sobre a Solveplan
[Boilerplate — 3-4 linhas]

Contato para imprensa
[Nome] | [email] | [telefone]
```

**Boilerplate padrão da Solveplan:**
> A Solveplan é uma consultoria especializada em soluções SAP para dados, analytics, planejamento financeiro e consolidação. Com mais de 200 soluções entregues, 90 clientes atendidos e 280 mil horas de projetos, a empresa é parceira SAP Gold na América Latina e referência em SAP Business Data Cloud (BDC), SAP Analytics Cloud (SAC) e SAP Datasphere. Mais em: solveplan.com.br

**Diretrizes do copy:**
- Primeira linha: fato direto — sem "A Solveplan tem o prazer de anunciar"
- Linguagem jornalística: clara, objetiva, sem hype
- Dados sempre que disponíveis
- Citação humana, com convicção, não corporativa
- Extensão: 350-500 palavras

## Passo 3 — Gerar o pitch para jornalista

Escrever email curto de pitch pra acompanhar o release:

**Estrutura do email:**
```
Assunto: [fato principal em até 8 palavras — ex: "Solveplan reduz tempo de fechamento em 40% com SAP BDC"]

[Nome do jornalista / Redação],

[1 parágrafo — o fato e por que é relevante pro leitor do veículo]

[1 parágrafo — quem é a Solveplan e por que ela é fonte confiável sobre isso]

Tenho o release completo + [dado adicional / possibilidade de entrevista com a Fran / case detalhado] disponível.

[Nome]
[Cargo] | Solveplan
[Email] | [Telefone]
```

**Diretrizes:**
- Máximo 150 palavras no corpo do email
- Assunto: jornalístico, não marqueteiro
- Sem "espero que esse email te encontre bem"
- Deixar espaço pra personalizar o nome do jornalista/veículo

## Passo 4 — Salvar

Criar pasta `marketing/releases/[slug-do-tema]/` e salvar:
- `release.md` — release completo
- `pitch.md` — email de pitch

Nomear a pasta com o tema em minúsculas, sem acentos, com hífens.

## Passo 5 — Confirmar

Informar onde foi salvo e perguntar:

> "Quer ajustar o tom da citação, adicionar mais dados, ou adaptar o pitch pra algum veículo específico?"

## Regras

- Release é jornalismo, não marketing — escrever pra editor, não pra cliente
- Dados concretos sempre que disponíveis — sem dados, release perde força
- Citação tem que soar humana — não corporativa
- Não exagerar resultado — jornalista verifica
- Foco em SAP BDC quando o tema envolver dados/analytics/planejamento
