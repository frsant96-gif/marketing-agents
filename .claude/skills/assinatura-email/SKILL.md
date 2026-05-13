---
name: assinatura-email
description: Gera assinatura de email em HTML com a identidade visual da Solveplan. Pede nome, cargo, contatos e retorna o HTML pronto pra copiar no cliente de email.
---

# /assinatura-email

## Antes de começar

Ler `marca/design-guide.md` pra garantir uso correto da identidade visual.

## Passo 1 — Coletar dados

Perguntar os dados abaixo, uma informação por vez:

1. "Nome completo"
2. "Cargo"
3. "Email"
4. "Site (ex: solveplan.com.br)"
5. "Telefone / WhatsApp (com DDD)"
6. "Quer incluir LinkedIn? Se sim, qual a URL do perfil?"

Se o usuário já passou os dados antes de rodar a skill, não perguntar de novo.

## Passo 2 — Gerar o HTML

Gerar o HTML completo da assinatura seguindo o modelo visual da Solveplan:

**Especificações visuais:**
- Fundo: gradiente escuro (`#0A0837` → `#0A0E19`)
- Círculo azul com logo: `#006AFF`
- Logo: `marca/logo-escuro.png.png` (ou usar URL absoluta se configurada)
- Texto nome: `#FFFFFF`, Prompt Bold, 16px
- Texto cargo: `#94FF96`, Montserrat Medium, 12px
- Ícones de contato: `#FFFFFF` ou SVG inline minimalista
- Texto de contato: `#FFFFFF`, Montserrat Regular, 12px
- Separador: linha fina `#FFFFFF` com 15% opacidade
- Largura total: 500px max

**Estrutura do HTML:**

```html
<!-- Assinatura Solveplan -->
<table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, sans-serif; max-width: 500px; background: linear-gradient(135deg, #0A0837 0%, #0A0E19 100%); border-radius: 8px; overflow: hidden;">
  <tr>
    <td style="padding: 20px 24px; vertical-align: middle; width: 80px;">
      <!-- Círculo com logo -->
      <div style="width: 64px; height: 64px; background-color: #006AFF; border-radius: 50%; display: flex; align-items: center; justify-content: center; overflow: hidden;">
        <img src="[URL_LOGO]" alt="Solveplan" style="width: 44px; height: auto;" />
      </div>
    </td>
    <td style="padding: 20px 24px 20px 0; vertical-align: middle; border-left: 1px solid rgba(255,255,255,0.15);">
      <p style="margin: 0 0 2px 0; font-size: 16px; font-weight: 700; color: #FFFFFF; letter-spacing: 0.3px;">[NOME]</p>
      <p style="margin: 0 0 12px 0; font-size: 12px; font-weight: 500; color: #94FF96;">[CARGO]</p>
      <p style="margin: 0 0 4px 0; font-size: 12px; color: #FFFFFF;">✉ [EMAIL]</p>
      <p style="margin: 0 0 4px 0; font-size: 12px; color: #FFFFFF;">🌐 [SITE]</p>
      <p style="margin: 0; font-size: 12px; color: #FFFFFF;">📱 [TELEFONE]</p>
    </td>
  </tr>
</table>
```

Preencher os placeholders com os dados fornecidos.

Se o usuário não tiver URL absoluta pra logo, usar path relativo `marca/logo-escuro.png.png` e avisar:

> "O logo está referenciado como arquivo local. Para funcionar em todos os clientes de email, sobe o logo pra um servidor e troca pelo link público."

## Passo 3 — Salvar e apresentar

Salvar em `marketing/assinatura-[nome-em-slug].html`.

Apresentar o HTML e instruções de uso:

> "Assinatura gerada. Para usar:
>
> **Gmail:** Configurações > Ver todas as configurações > Assinatura > Criar nova > colar o HTML (ativar modo HTML se necessário via extensão como 'Signature'
>
> **Outlook:** Arquivo > Opções > Email > Assinaturas > Nova > colar o HTML na aba 'HTML'
>
> O arquivo também foi salvo em `marketing/assinatura-[nome].html`."

## Regras

- Sempre usar as cores da marca — nunca mudar paleta
- Logo sempre circular em fundo azul `#006AFF`
- Cargo em verde neon `#94FF96` — é o único lugar onde o verde aparece com força na marca
- HTML compatível com clientes de email principais (Gmail, Outlook) — usar apenas tags inline e table-based layout
- Sem JavaScript ou CSS externo — assinaturas de email não suportam
