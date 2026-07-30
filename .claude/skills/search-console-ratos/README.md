# Search Console Ratos

Skill de consulta e diagnóstico do Google Search Console via `google-api-python-client` (API `webmasters` v3 + `searchconsole` v1).

## Instalação

```bash
pip3 install google-api-python-client google-auth
```

## Setup

Ver `SKILL.md` — seção "Setup (primeira vez)".

## Estrutura

```
scripts/
  lib/__init__.py    — auth, .env loader, helpers
  read.py            — sites, sitemaps
  reports.py          — queries, pages, countries, devices, dates, custom, compare
  url_inspect.py      — URL Inspection API (status de indexação)
contas.yaml           — cadastro de sites por nome de cliente
```
