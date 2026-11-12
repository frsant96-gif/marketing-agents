---
name: email-tarefas
description: Envia para a Fran um e-mail com as tarefas da semana de um projeto (hoje, o Projeto AEO/GEO em marketing/planos/projeto-aeo-geo/plano.md) — o que fazer, quanto tempo leva, o que está atrasado, o que o Claude já preparou e o que vem na próxima semana. Também marca tarefas como feitas quando ela avisar. Use quando a Fran disser "me manda as tarefas", "e-mail da semana", "o que tenho pra fazer", "/email-tarefas", "terminei a T07", "marca como feito".
---

# /email-tarefas

Lembrete semanal por e-mail para quem trabalha sozinha: curto, com no máximo 3 a 5 tarefas, cada uma com tempo estimado e o caminho exato no painel.

## Fonte das tarefas

Ler `marketing/planos/projeto-aeo-geo/plano.md` (ou outro `plano.md` que a Fran indicar).

Cada tarefa segue o formato:
```
- [ ] T07 | Fran | 2h | descrição
- [x] T01 | Fran | 5 min | descrição        ← feita
```
As semanas são títulos `### Semana N — DD/MM a DD/MM · tema`.

## Modo 1 — Enviar o e-mail da semana

1. **Descobrir a semana atual** pela data de hoje (`date`), comparando com os intervalos dos títulos `### Semana`. Antes da Semana 1, usar a Semana 1. Se estiver entre semanas (ex.: feriado), usar a próxima.
2. **Separar as tarefas:**
   - **Da semana:** as `[ ]` da semana atual.
   - **Atrasadas:** as `[ ]` de semanas anteriores.
   - **Próxima semana:** só os títulos, como prévia.
   - **Do Claude:** tarefas em que o Claude escreve ou prepara. Antes de enviar, verificar se o material já existe na pasta do projeto ou nas pastas das skills. Se não existir, dizer à Fran no chat que vai preparar e oferecer para fazer já.
3. **Somar o tempo da Fran** (só a coluna de tempo dela).
4. **Montar o e-mail** (HTML simples, sem imagens):
   - **Assunto:** `[AEO/GEO] Semana N · X tarefas · ~Yh — tema`
   - **Corpo:**
     - 1 linha de abertura: tema da semana + meta do projeto ("subir de 3 para 5 citações em 10 nas IAs até 15/01").
     - **Atrasadas** (se houver), em primeiro, com fundo amarelo claro.
     - **Tarefas da semana:** lista numerada com ID, o que fazer, tempo e caminho no painel. Destacar em negrito a primeira tarefa a fazer.
     - **O que já está pronto para você:** links/caminhos dos textos que o Claude preparou.
     - **Lembretes fixos:** backup antes de mexer no site; nada de mudanças na sexta; marcar de novo a opção do Wordfence ao terminar.
     - **Próxima semana:** 1 linha.
     - Fechamento: "Quando terminar uma tarefa, me diga 'feito T07' no Claude Code que eu atualizo o plano."
   - Tom: direto, sem floreio, em português. Cores da marca só em detalhes (#0A0837 títulos, #006AFF links).
5. **Enviar para `francielle.beline@solveplan.com`** (a própria Fran). **Nunca** enviar para outra pessoa sem ela pedir explicitamente.
   - **Caminho 1:** conector Microsoft 365 (`outlook_send_mail`, ou `outlook_create_draft` + `outlook_send_draft`), se a ferramenta estiver disponível na sessão.
   - **Caminho 2:** Outlook do computador via PowerShell (COM). Salvar o HTML num arquivo UTF-8 no scratchpad e enviar:
     ```powershell
     $o = New-Object -ComObject Outlook.Application
     $m = $o.CreateItem(0)
     $m.To = 'francielle.beline@solveplan.com'
     $m.Subject = $assunto
     $m.HTMLBody = [IO.File]::ReadAllText($arquivoHtml, [Text.Encoding]::UTF8)
     $m.Send()
     ```
   - **Se nenhum funcionar:** salvar o HTML em `marketing/planos/projeto-aeo-geo/emails/semana-N.html`, abrir o arquivo e avisar.
6. **Registrar o envio** na tabela "Registro" do `plano.md` (data + "e-mail da Semana N enviado").
7. **Responder no chat em 2 a 3 linhas:** enviado para onde, quantas tarefas, total de horas e o que o Claude pode adiantar agora.

## Modo 2 — Marcar tarefas como feitas

Quando a Fran disser "feito T07", "terminei T02 e T03" ou "pula a T18":
- **Feito:** trocar `[ ]` por `[x]` na linha da tarefa.
- **Pular/adiar:** mover a linha para a semana que ela disser ou para "Se sobrar tempo", e anotar o motivo no Registro.
- Adicionar uma linha no **Registro** com a data e o que mudou.
- Responder com o andamento: "X de 25 tarefas feitas · próxima: T08 (10 min)".

## Modo 3 — Andamento do projeto

Se ela perguntar "como está o projeto?": contar feitas, atrasadas e restantes, mostrar a % e a próxima tarefa, sem mandar e-mail.

## Regras

- Máximo de 5 tarefas no e-mail. Se houver mais, mostrar as 5 primeiras e escrever "+N no plano".
- Não inventar tarefas. Só o que está no `plano.md`.
- Tarefas que mexem no site sempre com o lembrete de backup.
- Se o plano tiver terminado, mandar um e-mail de fechamento com o resultado e sugerir rodar a auditoria GEO de novo.
