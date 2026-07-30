#!/usr/bin/env python3
"""
Search Console Ratos - Relatorios (core da skill)
Subcomandos: queries, pages, countries, devices, dates, page-queries, custom, compare
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (
    init_webmasters_client,
    resolve_site_url,
    add_site_arg,
    add_date_args,
    add_limit_arg,
    build_date_range,
    build_dimension_filter_groups,
    format_search_analytics_response,
    print_json,
    print_error,
    handle_gsc_error,
)


def _run_query(site_url, dimensions, start_date, end_date, row_limit=25,
                dimension_filter_groups=None, search_type="web", start_row=0):
    """Helper generico pra rodar searchanalytics.query."""
    client = init_webmasters_client()

    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "startRow": start_row,
        "type": search_type,
    }

    if dimension_filter_groups:
        body["dimensionFilterGroups"] = dimension_filter_groups

    response = client.searchanalytics().query(siteUrl=site_url, body=body).execute()
    return format_search_analytics_response(response)


def _rename_dims(result, names):
    """Renomeia dim_0, dim_1... pros nomes reais das dimensoes."""
    for row in result["rows"]:
        keys_present = [k for k in row.keys() if k.startswith("dim_")]
        for i, name in enumerate(names):
            key = f"dim_{i}"
            if key in row:
                row[name] = row.pop(key)
    return result


# ---------------------------------------------------------------------------
# queries — Termos de busca com mais cliques/impressoes
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_queries(args):
    """Termos de busca (queries) com clicks, impressions, CTR e posicao media."""
    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    result = _run_query(site_url, ["query"], start_date, end_date, row_limit=args.limit)
    _rename_dims(result, ["query"])
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url

    print_json(result)


# ---------------------------------------------------------------------------
# pages — Paginas com mais cliques/impressoes
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_pages(args):
    """Paginas com clicks, impressions, CTR e posicao media."""
    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    result = _run_query(site_url, ["page"], start_date, end_date, row_limit=args.limit)
    _rename_dims(result, ["page"])
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url

    print_json(result)


# ---------------------------------------------------------------------------
# page-queries — Queries que trazem trafego pra uma pagina especifica
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_page_queries(args):
    """Queries que geram impressoes/cliques pra uma URL especifica (diagnostico por pagina)."""
    if not args.page:
        print_error("--page e obrigatorio. Ex: --page https://solveplan.com/blog/artigo")
        sys.exit(1)

    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    filters = build_dimension_filter_groups([("page", "equals", args.page)])
    result = _run_query(
        site_url, ["query"], start_date, end_date,
        row_limit=args.limit, dimension_filter_groups=filters,
    )
    _rename_dims(result, ["query"])
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url
    result["page"] = args.page

    print_json(result)


# ---------------------------------------------------------------------------
# countries — Breakdown por pais
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_countries(args):
    """Breakdown de performance por pais."""
    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    result = _run_query(site_url, ["country"], start_date, end_date, row_limit=args.limit)
    _rename_dims(result, ["country"])
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url

    print_json(result)


# ---------------------------------------------------------------------------
# devices — Breakdown por dispositivo
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_devices(args):
    """Breakdown de performance por dispositivo (desktop, mobile, tablet)."""
    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    result = _run_query(site_url, ["device"], start_date, end_date, row_limit=10)
    _rename_dims(result, ["device"])
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url

    print_json(result)


# ---------------------------------------------------------------------------
# dates — Evolucao diaria
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_dates(args):
    """Evolucao diaria de clicks, impressions, CTR e posicao media."""
    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    result = _run_query(site_url, ["date"], start_date, end_date, row_limit=1000)
    _rename_dims(result, ["date"])
    result["rows"].sort(key=lambda r: r["date"])
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url

    print_json(result)


# ---------------------------------------------------------------------------
# search-appearance — Rich results / breakdown por tipo de aparencia na busca
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_search_appearance(args):
    """Breakdown por tipo de aparencia na busca (rich results, AMP, etc)."""
    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    result = _run_query(site_url, ["searchAppearance"], start_date, end_date, row_limit=args.limit)
    _rename_dims(result, ["search_appearance"])
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url

    print_json(result)


# ---------------------------------------------------------------------------
# custom — Query custom (dimensoes livres + filtro opcional)
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_custom(args):
    """Query custom com dimensoes livres (query, page, country, device, date, searchAppearance)."""
    site_url = resolve_site_url(args.site)
    start_date, end_date = build_date_range(args)

    dimensions = [d.strip() for d in args.dimensions.split(",")] if args.dimensions else ["query"]

    filters = None
    if args.filter_dimension and args.filter_expression:
        op = args.filter_operator or "equals"
        filters = build_dimension_filter_groups([(args.filter_dimension, op, args.filter_expression)])

    result = _run_query(
        site_url, dimensions, start_date, end_date,
        row_limit=args.limit, dimension_filter_groups=filters,
        search_type=args.search_type,
    )
    _rename_dims(result, dimensions)
    result["period"] = {"start_date": start_date, "end_date": end_date}
    result["site"] = site_url

    print_json(result)


# ---------------------------------------------------------------------------
# compare — Compara dois periodos (ex: mes atual vs anterior)
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_compare(args):
    """Compara metricas totais entre dois periodos (clicks, impressions, CTR, posicao)."""
    from datetime import date, timedelta

    site_url = resolve_site_url(args.site)

    end_current = date.today() - timedelta(days=2)
    start_current = end_current - timedelta(days=args.days)
    end_previous = start_current - timedelta(days=1)
    start_previous = end_previous - timedelta(days=args.days)

    client = init_webmasters_client()

    def _totals(start, end):
        body = {
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "dimensions": [],
            "rowLimit": 1,
        }
        response = client.searchanalytics().query(siteUrl=site_url, body=body).execute()
        rows = response.get("rows", [])
        if not rows:
            return {"clicks": 0, "impressions": 0, "ctr": 0, "position": 0}
        r = rows[0]
        return {
            "clicks": r.get("clicks", 0),
            "impressions": r.get("impressions", 0),
            "ctr": r.get("ctr", 0),
            "position": r.get("position", 0),
        }

    current = _totals(start_current, end_current)
    previous = _totals(start_previous, end_previous)

    def _delta(cur, prev):
        if prev == 0:
            return None
        return round((cur - prev) / prev * 100, 2)

    print_json({
        "site": site_url,
        "current_period": {"start_date": start_current.isoformat(), "end_date": end_current.isoformat(), **current},
        "previous_period": {"start_date": start_previous.isoformat(), "end_date": end_previous.isoformat(), **previous},
        "delta_pct": {
            "clicks": _delta(current["clicks"], previous["clicks"]),
            "impressions": _delta(current["impressions"], previous["impressions"]),
            "ctr": _delta(current["ctr"], previous["ctr"]),
            "position": _delta(current["position"], previous["position"]),
        },
    })


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Search Console Ratos - Relatorios")
    sub = parser.add_subparsers(dest="command")

    p_queries = sub.add_parser("queries", help="Termos de busca com mais cliques/impressoes")
    add_site_arg(p_queries)
    add_date_args(p_queries)
    add_limit_arg(p_queries)

    p_pages = sub.add_parser("pages", help="Paginas com mais cliques/impressoes")
    add_site_arg(p_pages)
    add_date_args(p_pages)
    add_limit_arg(p_pages)

    p_page_queries = sub.add_parser("page-queries", help="Queries que trazem trafego pra uma pagina especifica")
    add_site_arg(p_page_queries)
    add_date_args(p_page_queries)
    add_limit_arg(p_page_queries)
    p_page_queries.add_argument("--page", help="URL completa da pagina")

    p_countries = sub.add_parser("countries", help="Breakdown por pais")
    add_site_arg(p_countries)
    add_date_args(p_countries)
    add_limit_arg(p_countries)

    p_devices = sub.add_parser("devices", help="Breakdown por dispositivo")
    add_site_arg(p_devices)
    add_date_args(p_devices)

    p_dates = sub.add_parser("dates", help="Evolucao diaria")
    add_site_arg(p_dates)
    add_date_args(p_dates)

    p_appearance = sub.add_parser("search-appearance", help="Breakdown por tipo de aparencia na busca")
    add_site_arg(p_appearance)
    add_date_args(p_appearance)
    add_limit_arg(p_appearance)

    p_custom = sub.add_parser("custom", help="Query custom com dimensoes livres")
    add_site_arg(p_custom)
    add_date_args(p_custom)
    add_limit_arg(p_custom, default=50)
    p_custom.add_argument("--dimensions", help="Dimensoes separadas por virgula (query,page,country,device,date,searchAppearance)")
    p_custom.add_argument("--search-type", default="web", help="Tipo de busca: web, image, video, news (default: web)")
    p_custom.add_argument("--filter-dimension", help="Dimensao pra filtrar (ex: page)")
    p_custom.add_argument("--filter-operator", help="Operador do filtro: equals, contains, notContains, includingRegex, excludingRegex (default: equals)")
    p_custom.add_argument("--filter-expression", help="Valor do filtro (ex: /blog/)")

    p_compare = sub.add_parser("compare", help="Compara dois periodos consecutivos")
    add_site_arg(p_compare)
    p_compare.add_argument("--days", type=int, default=28, help="Tamanho de cada periodo em dias (default: 28)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "queries": cmd_queries,
        "pages": cmd_pages,
        "page-queries": cmd_page_queries,
        "countries": cmd_countries,
        "devices": cmd_devices,
        "dates": cmd_dates,
        "search-appearance": cmd_search_appearance,
        "custom": cmd_custom,
        "compare": cmd_compare,
    }

    cmd = commands.get(args.command)
    if cmd:
        cmd(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
