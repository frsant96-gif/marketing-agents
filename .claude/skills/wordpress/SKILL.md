---
name: wordpress
description: Suporte WordPress para quem gerencia o site sem desenvolvedor. Cobre performance, SEO técnico, segurança, publicação de páginas, troubleshooting de erros e manutenção via painel administrativo — sem escrever código.
---

# /wordpress

## Antes de começar

Ler `_contexto/empresa.md`. O site da Solveplan roda em WordPress. Não há desenvolvedor — todas as ações devem ser executáveis pelo painel Admin do WP ou por plugins sem código.

## Como usar essa skill

Descreva o que precisa fazer ou o problema que está enfrentando. Exemplos:

- "O site está lento, o que faço?"
- "Como publico a nova página de solução com SEO certo?"
- "Apareceu um erro 404 em páginas que existiam"
- "Quero instalar um formulário de contato"
- "O site caiu, o que verifico?"
- "Como faço backup antes de atualizar tudo?"

---

## Guias de referência

### 1. Performance — site rápido sem dev

**Meta:** Page load < 3s no mobile, > 80 no PageSpeed Insights.

**Plugins recomendados (instalar um de cada categoria):**

| Categoria | Plugin gratuito | Plugin pago (melhor) |
|-----------|----------------|----------------------|
| Cache | W3 Total Cache / WP Super Cache | WP Rocket |
| Imagens | Smush / ShortPixel (gratuito limitado) | ShortPixel / Imagify |
| CDN | Cloudflare (gratuito) | Cloudflare Pro |
| Minificação | Autoptimize | WP Rocket (já inclui) |

**Checklist de performance (verificar mensalmente):**
- [ ] Imagens novas foram comprimidas antes do upload? (usar TinyPNG ou ShortPixel)
- [ ] Plugin de cache está ativo e o cache foi limpo após publicar conteúdo novo?
- [ ] Cloudflare está configurado como proxy?
- [ ] PageSpeed Insights mostra > 80 no mobile?

**Testar performance:**
- PageSpeed Insights: pagespeed.web.dev
- GTmetrix: gtmetrix.com
- Core Web Vitals no GSC: Search Console → Experiência → Core Web Vitals

**Problema comum — site ficou lento após atualização:**
1. Verificar se algum plugin foi atualizado recentemente (Plugins → Atualizações)
2. Desativar plugins um por um pra identificar o conflito
3. Limpar o cache após cada teste (plugin de cache → "Limpar tudo")

---

### 2. SEO técnico — publicar páginas corretamente

**Plugin obrigatório:** Yoast SEO ou Rank Math (instalar um, não os dois).

**Checklist antes de publicar qualquer página ou post:**

```
[ ] Title tag preenchido (até 60 caracteres) — aparece no Yoast/Rank Math como "SEO Title"
[ ] Meta description preenchida (até 155 caracteres)
[ ] URL slug definido manualmente (não deixar o WP gerar automático com título longo)
    Exemplo: /solucoes/sap-business-data-cloud — NÃO: /solucoes/sap-business-data-cloud-consultoria-especializada-latam
[ ] Imagem destacada adicionada (1200x630px para OG)
[ ] Alt text em todas as imagens do conteúdo
[ ] H1 existe uma única vez na página (geralmente é o título do post)
[ ] Links internos adicionados (pelo menos 2 pra outras páginas do site)
[ ] Schema markup ativo (Yoast/Rank Math gera automaticamente pra posts e páginas)
```

**Configurações iniciais do Yoast/Rank Math (fazer uma vez):**
- Conectar ao Google Search Console dentro do plugin
- Ativar sitemap XML (Yoast: SEO → Geral → Recursos → Mapa do site XML)
- Configurar título padrão do site: [Nome da Página] | Solveplan

**Verificar indexação após publicar:**
- No GSC: URL Inspection → colar a URL → "Solicitar indexação"
- Aguardar 1-7 dias pra aparecer no Google

---

### 3. Segurança — proteger sem dev

**Plugin obrigatório:** Wordfence (gratuito) ou Solid Security (gratuito).

**Configurações mínimas de segurança:**

```
[ ] Usuário admin NÃO se chama "admin" — trocar se necessário
[ ] Senha do painel Admin: mínimo 16 caracteres, gerada por gerenciador de senhas
[ ] Autenticação em dois fatores (2FA) ativada no painel
[ ] Wordfence: firewall ativado + scan semanal programado
[ ] Atualizações automáticas ativas para: WordPress core, plugins, temas
[ ] Login URL customizada (Wordfence ou WPS Hide Login) — NÃO usar /wp-admin público
[ ] SSL ativo (cadeado verde no navegador) — verificar na hospedagem
```

**Sinais de que o site foi comprometido:**
- Google mostra aviso "Este site pode prejudicar seu computador"
- Conteúdo estranho aparece em páginas
- Hospedagem enviou alerta de uso excessivo de CPU
- Usuários admin desconhecidos no painel

**O que fazer se suspeitar de invasão:**
1. Rodar scan completo no Wordfence
2. Mudar imediatamente as senhas do WP e do painel da hospedagem
3. Contatar a hospedagem — eles têm ferramentas de detecção
4. Restaurar um backup limpo se necessário (ver seção Backup)

---

### 4. Backup — nunca atualizar sem backup

**Plugin recomendado:** UpdraftPlus (gratuito) — configurar pra salvar no Google Drive automaticamente.

**Rotina de backup:**
- **Automático:** 1x por semana (configurar no UpdraftPlus)
- **Manual obrigatório antes de:** atualizar plugins, trocar tema, publicar alterações grandes no site

**Como fazer backup manual no UpdraftPlus:**
1. Painel WP → UpdraftPlus → "Fazer backup agora"
2. Marcar: banco de dados + arquivos
3. Aguardar concluir — verificar que o arquivo foi pra nuvem

**Como restaurar:**
1. UpdraftPlus → "Backups existentes" → escolher data → "Restaurar"
2. Selecionar o que restaurar (banco + arquivos)
3. Confirmar — o WP vai ao estado da data escolhida

---

### 5. Troubleshooting — erros comuns

**Tela branca / erro 500:**
1. Desativar todos os plugins via FTP ou painel da hospedagem (renomear pasta `/plugins`)
2. Se resolver, reativar um por um pra achar o culpado
3. Trocar temporariamente pro tema padrão do WP (Twenty Twenty-Four) pra testar se é tema

**Erro 404 em páginas que existiam:**
1. Painel WP → Configurações → Links permanentes → Salvar (sem mudar nada) — isso regenera o `.htaccess`
2. Se persistir: verificar se a URL foi alterada — adicionar redirecionamento 301 (plugin Redirection)

**Plugin de cache quebrando o site:**
1. Desativar o plugin de cache
2. Limpar cache do navegador (Ctrl+Shift+Del)
3. Testar o site — se voltou ao normal, o problema é configuração do cache
4. Reativar e ajustar as configurações de exclusão de URLs

**WP travou após atualização:**
1. Restaurar o backup feito antes da atualização
2. Aguardar versão corrigida do plugin/tema antes de atualizar de novo

**Formulário de contato não envia emails:**
1. Instalar plugin WP Mail SMTP
2. Configurar com conta de email real (não o email padrão da hospedagem)
3. Testar envio pelo painel do plugin

---

### 6. Plugins essenciais — kit base recomendado

| Função | Plugin |
|--------|--------|
| SEO | Yoast SEO ou Rank Math |
| Cache | WP Rocket (pago) ou W3 Total Cache (grátis) |
| Imagens | ShortPixel ou Smush |
| Segurança | Wordfence |
| Backup | UpdraftPlus |
| Redirecionamentos | Redirection |
| Email | WP Mail SMTP |
| Formulários | WPForms Lite ou Contact Form 7 |
| Analytics | Site Kit by Google (conecta GSC + GA4) |
| Anti-spam | Akismet |

**Regra de ouro:** menos plugins = site mais rápido e seguro. Desinstalar plugins inativos.

---

### 7. Manutenção mensal — checklist

```
Todo mês, verificar:
[ ] Atualizações pendentes (WP core, plugins, tema) — fazer backup antes
[ ] Scan de segurança no Wordfence — resolver alertas
[ ] PageSpeed Insights — score ainda acima de 80?
[ ] GSC — novos erros de crawl ou cobertura?
[ ] GSC — Core Web Vitals com alguma URL em vermelho?
[ ] Backup automático funcionando — checar que arquivo chegou no Google Drive
[ ] Links quebrados — plugin Broken Link Checker ou ferramenta externa
```

---

## Regras

- Sempre fazer backup antes de qualquer atualização ou mudança estrutural
- Nunca instalar plugin de fonte desconhecida (só do repositório oficial wordpress.org ou desenvolvedores reconhecidos)
- Ao encontrar erro que não resolve com os guias acima, descrever o erro exato aqui — mensagem completa + quando aparece
- Se o problema exigir editar código PHP diretamente: contratar desenvolvedor pontual (Workana, 99Freelas) — não tentar editar sem experiência
