# Post LinkedIn — Case U&M

**Tema:** Case SAP Datasphere
**Objetivo:** Promover case / Autoridade
**Plataforma:** LinkedIn (página Solveplan)
**Referência de estilo:** padrão Aço Cearense, Lins Agroindustrial e SSA Alimentos (versões D e E)
**Persona:** CIO, Head de Dados/BI (secundária: Gerente de TI / SAP)
**Vídeo:** https://youtu.be/b2ftt2R33CU
**Case no site:** https://solveplan.com/case/um-sap-datasphere-arquitetura-dados/ (em rascunho; até publicar, usar o link do vídeo)
**Fonte dos fatos:** texto do case aprovado pelo cliente

**Marcar no LinkedIn:** U&M Mineração e Construção, SolvePlan, Ednaldo Teixeira, Bruner Filgueiras

---

## Versão D — padrão Aço/Lins/SSA

```
A U&M Mineração e Construção, com cerca de 4.000 funcionários, 10 filiais e duas centrais especializadas, precisava de dados confiáveis no ritmo da operação. Antes do projeto, cada nova necessidade de informação podia virar um relatório customizado no SAP e uma demanda de desenvolvimento ABAP. ETLs fora da governança e a falta de uma base centralizada faziam cada área tratar os dados por conta própria, com retrabalho e risco de números divergentes.

Com o SAP Datasphere implementado pela SolvePlan, a empresa estruturou uma arquitetura governada em três camadas, que reúne dados do SAP S/4HANA e de fontes como RM TOTVS, SQL Server e arquivos externos. Onde havia mais de 55 tabelas dispersas em um único banco, hoje há 155 views e 133 tabelas locais estruturadas e catalogadas. Em determinados cenários, os dados chegam próximos do tempo real.

O ganho aparece na operação: na manutenção, desvios no consumo de lubrificantes e custos elevados passaram a ser identificados mais rápido, antes da falha.

Assista ao depoimento de Ednaldo Teixeira, Gerente de TI, e Bruner Filgueiras, Especialista em Sistemas da U&M: [link]

#SAPDatasphere #GovernancaDeDados #ArquiteturaDeDados #SAP #SAPBusinessDataCloud #SolvePlan
```

---

## Versão E — Versão D + FAQ

```
A U&M Mineração e Construção, com cerca de 4.000 funcionários, 10 filiais e duas centrais especializadas, precisava de dados confiáveis no ritmo da operação. Antes do projeto, cada nova necessidade de informação podia virar um relatório customizado no SAP e uma demanda de desenvolvimento ABAP. ETLs fora da governança e a falta de uma base centralizada faziam cada área tratar os dados por conta própria, com retrabalho e risco de números divergentes.

Com o SAP Datasphere implementado pela SolvePlan, a empresa estruturou uma arquitetura governada em três camadas, que reúne dados do SAP S/4HANA e de fontes como RM TOTVS, SQL Server e arquivos externos. Onde havia mais de 55 tabelas dispersas em um único banco, hoje há 155 views e 133 tabelas locais estruturadas e catalogadas. Em determinados cenários, os dados chegam próximos do tempo real.

O ganho aparece na operação: na manutenção, desvios no consumo de lubrificantes e custos elevados passaram a ser identificados mais rápido, antes da falha.

Perguntas frequentes

Qual solução foi implementada?
SAP Datasphere, como camada central entre o SAP S/4HANA e o consumo de dados pelas áreas de negócio.

Como a arquitetura foi organizada?
Em três camadas: Bronze (dados brutos replicados do SAP), Silver (views harmonizadas) e Gold (objetos de negócio por área, como Manutenção, Produção, Compras e Controladoria).

O que mudou no dia a dia?
Dados mais rápidos e confiáveis, menos dependência de filas de desenvolvimento e áreas trabalhando sobre as mesmas informações.

Assista ao depoimento de Ednaldo Teixeira, Gerente de TI, e Bruner Filgueiras, Especialista em Sistemas da U&M: [link]

#SAPDatasphere #GovernancaDeDados #ArquiteturaDeDados #SAP #SAPBusinessDataCloud #SolvePlan
```

---

## Versão F — mesma linha, abrindo pelo número

```
Em apenas um dos bancos SQL Server usados pelos ETLs antigos da U&M havia mais de 55 tabelas dispersas, sem padronização nem governança.

Para uma empresa com cerca de 4.000 funcionários e 10 filiais, que atua em grandes movimentações de solo e rocha em obras de infraestrutura e mineração, isso significava retrabalho, risco de divergência entre relatórios e uma demanda de desenvolvimento ABAP a cada nova necessidade de informação.

Com a SolvePlan, a U&M passou a usar o SAP Datasphere como camada central entre o SAP S/4HANA e as áreas de negócio. Dados SAP e não-SAP, como RM TOTVS, SQL Server e arquivos Parquet e CSV, agora seguem uma arquitetura em camadas Bronze, Silver e Gold, com 155 views e 133 tabelas locais catalogadas.

O resultado aparece na ponta. As áreas passaram a trabalhar sobre as mesmas informações, e a manutenção identifica mais rápido desvios no consumo de lubrificantes, antecipando ações antes da falha.

Ednaldo Teixeira, Gerente de TI, e Bruner Filgueiras, Especialista em Sistemas da U&M, contam como foi essa jornada: [link]

#SAPDatasphere #SAPS4HANA #GovernancaDeDados #SAPBusinessDataCloud #SolvePlan
```

---

## Versão G — pergunta → dor → case → link nos comentários

```
Na U&M Mineração e Construção, cada pedido de informação nova podia virar um relatório Z no SAP e entrar na fila do ABAP.

Fora do SAP, ETLs paralelos. Só em um dos bancos SQL Server eram mais de 55 tabelas, sem padrão nem governança, e cada área extraía e tratava os dados por conta própria.

No projeto, colocamos o SAP Datasphere no meio do caminho. Os dados do S/4HANA, do RM TOTVS e do SQL Server passam por ele antes de chegar ao Power BI. Hoje são 155 views e 133 tabelas locais catalogadas, e em alguns cenários a informação chega quase em tempo real.

Um efeito prático: a manutenção passou a perceber mais cedo quando o consumo de lubrificante sai do normal, antes de o equipamento falhar.

Ednaldo Teixeira, Gerente de TI, e Bruner Filgueiras, Especialista em Sistemas, falaram sobre o projeto no SAP NOW AI Tour. O vídeo está no nosso canal do YouTube, link nos comentários.

#SAPDatasphere #GovernancaDeDados #SAPBusinessDataCloud
```

**1º comentário:** Assista ao case completo da U&M: https://youtu.be/b2ftt2R33CU

---

## Versão H — curta, no modelo da Fran

```
A U&M Mineração e Construção, empresa especializada em serviços e locação de equipamentos para grandes movimentações de solo e rocha em obras de infraestrutura e mineração, estruturou com a SolvePlan uma arquitetura de dados governada com SAP Datasphere.

Neste case, Ednaldo Teixeira, Gerente de TI, e Bruner Filgueiras, Especialista em Sistemas, contam como a empresa saiu de mais de 55 tabelas dispersas para uma base governada, e como isso chegou até a manutenção dos equipamentos.

Assista ao case completo em nosso site: https://solveplan.com/case/um-sap-datasphere-arquitetura-dados/

#SAPDatasphere #GovernancaDeDados #ArquiteturaDeDados #SAPBusinessDataCloud #SolvePlan
```

---

## Observações

- Números usados como estão no texto aprovado (55 tabelas, 155 views, 133 tabelas locais), sem converter em percentual.
- Cargos como no texto aprovado. A tarja do vídeo mostra o Ednaldo como "Gerente Corporativo de TI". Usar o mesmo cargo no post, no site e na descrição do YouTube.
- Subir o vídeo nativo no LinkedIn rende mais alcance do que o link do YouTube. Se usar o vídeo nativo, colocar o link do case no 1º comentário.
- A versão D tem cerca de 1.250 caracteres. A versão E passa de 1.300 por causa do FAQ, como nos outros cases.

## Checklist

- [x] Primeira linha situa empresa e porte sem "Você sabia que"
- [x] Dor real de CIO/Head de Dados (relatórios Z, fila de ABAP, ETLs paralelos, números divergentes)
- [x] SolvePlan como quem implementou, não como vendedor
- [x] Fatos e números do texto aprovado
- [x] Conexão com SAP Business Data Cloud na hashtag, como no texto do case
- [x] Sem "transformação digital" genérico
- [x] Hashtags específicas
