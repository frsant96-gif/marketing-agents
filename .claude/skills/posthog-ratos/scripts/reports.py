#!/usr/bin/env python3
"""Relatorios de eventos, tendencias e funis do PostHog (via HogQL e Query API)."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib._auth import load_config, api_get, api_post, resolve_project  # noqa: E402


def _project(config, args):
    project_id = resolve_project(args.project) if args.project else config["project_id"]
    if not project_id:
        sys.exit("Erro: informe --project (nome cadastrado ou project_id) ou configure POSTHOG_PROJECT_ID no .env")
    return project_id


def _hogql(config, project_id, query):
    body = {"query": {"kind": "HogQLQuery", "query": query}}
    return api_post(config, f"/api/projects/{project_id}/query/", body)


def cmd_overview(config, args):
    project_id = _project(config, args)
    query = f"""
        SELECT toDate(timestamp) AS dia, count() AS eventos, count(DISTINCT distinct_id) AS usuarios
        FROM events
        WHERE timestamp >= now() - INTERVAL {int(args.days)} DAY
        GROUP BY dia
        ORDER BY dia
    """
    data = _hogql(config, project_id, query)
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False, default=str))


def cmd_top_events(config, args):
    project_id = _project(config, args)
    query = f"""
        SELECT event, count() AS total, count(DISTINCT distinct_id) AS usuarios_unicos
        FROM events
        WHERE timestamp >= now() - INTERVAL {int(args.days)} DAY
        GROUP BY event
        ORDER BY total DESC
        LIMIT {int(args.limit)}
    """
    data = _hogql(config, project_id, query)
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False, default=str))


def cmd_trend(config, args):
    project_id = _project(config, args)
    query = f"""
        SELECT toDate(timestamp) AS dia, count() AS total
        FROM events
        WHERE event = '{args.event}' AND timestamp >= now() - INTERVAL {int(args.days)} DAY
        GROUP BY dia
        ORDER BY dia
    """
    data = _hogql(config, project_id, query)
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False, default=str))


def cmd_funnel(config, args):
    project_id = _project(config, args)
    steps = [s.strip() for s in args.steps.split(",") if s.strip()]
    if len(steps) < 2:
        sys.exit("Erro: --steps precisa de pelo menos 2 eventos separados por virgula, ex: 'pageview,signup,purchase'")

    body = {
        "query": {
            "kind": "FunnelsQuery",
            "series": [{"kind": "EventsNode", "event": step, "name": step} for step in steps],
            "dateRange": {"date_from": f"-{int(args.days)}d"},
            "funnelsFilter": {"funnelOrderType": "ordered"},
        }
    }
    data = api_post(config, f"/api/projects/{project_id}/query/", body)
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False, default=str))


def cmd_insights(config, args):
    project_id = _project(config, args)
    data = api_get(config, f"/api/projects/{project_id}/insights/", {"limit": args.limit})
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False))


def cmd_custom(config, args):
    project_id = _project(config, args)
    data = _hogql(config, project_id, args.query)
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False, default=str))


def main():
    parser = argparse.ArgumentParser(description="PostHog Ratos — relatorios de eventos, tendencias e funis")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--project", help="Nome cadastrado em contas.yaml ou project_id")

    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("overview", parents=[common], help="Eventos e usuarios unicos por dia")
    p.add_argument("--days", default=30, help="Janela em dias (default 30)")

    p = sub.add_parser("top-events", parents=[common], help="Eventos mais frequentes no periodo")
    p.add_argument("--days", default=30)
    p.add_argument("--limit", default=20)

    p = sub.add_parser("trend", parents=[common], help="Serie diaria de um evento especifico")
    p.add_argument("--event", required=True, help="Nome do evento, ex: purchase")
    p.add_argument("--days", default=30)

    p = sub.add_parser("funnel", parents=[common], help="Funil de conversao entre eventos, em ordem")
    p.add_argument("--steps", required=True, help="Eventos em ordem, separados por virgula")
    p.add_argument("--days", default=30)

    p = sub.add_parser("insights", parents=[common], help="Lista insights salvos no projeto")
    p.add_argument("--limit", default=50)

    p = sub.add_parser("custom", parents=[common], help="Query HogQL livre")
    p.add_argument("--query", required=True, help="Query HogQL, ex: \"SELECT event, count() FROM events GROUP BY event\"")

    args = parser.parse_args()
    config = load_config()

    {
        "overview": cmd_overview,
        "top-events": cmd_top_events,
        "trend": cmd_trend,
        "funnel": cmd_funnel,
        "insights": cmd_insights,
        "custom": cmd_custom,
    }[args.command](config, args)


if __name__ == "__main__":
    main()
