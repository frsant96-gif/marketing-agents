#!/usr/bin/env python3
"""Session recordings e heatmaps do PostHog."""
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


def cmd_list(config, args):
    project_id = _project(config, args)
    params = {"limit": args.limit}
    if args.date_from:
        params["date_from"] = args.date_from
    if args.date_to:
        params["date_to"] = args.date_to
    data = api_get(config, f"/api/projects/{project_id}/session_recordings/", params)
    resultados = data.get("results", data)
    resumo = [
        {
            "id": r.get("id"),
            "inicio": r.get("start_time"),
            "duracao_s": r.get("recording_duration"),
            "pessoa": (r.get("person") or {}).get("name") or (r.get("person") or {}).get("distinct_ids"),
            "cliques": r.get("click_count"),
            "erros_console": r.get("console_error_count"),
        }
        for r in resultados
    ] if args.resumo else resultados
    print(json.dumps(resumo, indent=2, ensure_ascii=False, default=str))


def cmd_heatmap(config, args):
    project_id = _project(config, args)
    body = {
        "query": {
            "kind": "HeatmapQuery",
            "urlPattern": args.url,
            "heatmapType": args.tipo,
            "dateRange": {"date_from": f"-{int(args.days)}d"},
        }
    }
    data = api_post(config, f"/api/projects/{project_id}/query/", body)
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False, default=str))


def main():
    parser = argparse.ArgumentParser(description="PostHog Ratos — session recordings e heatmaps")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--project", help="Nome cadastrado em contas.yaml ou project_id")

    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("list", parents=[common], help="Lista session recordings")
    p.add_argument("--date-from", dest="date_from", help="ISO date, ex: 2026-07-01")
    p.add_argument("--date-to", dest="date_to", help="ISO date, ex: 2026-07-31")
    p.add_argument("--limit", default=20)
    p.add_argument("--resumo", action="store_true", help="Mostra apenas os campos principais")

    p = sub.add_parser("heatmap", parents=[common], help="Dados de heatmap (clique/scroll) de uma URL")
    p.add_argument("--url", required=True, help="URL exata ou padrao, ex: https://solveplan.com.br/*")
    p.add_argument("--tipo", default="click", choices=["click", "rageclick", "scrolldepth"])
    p.add_argument("--days", default=30)

    args = parser.parse_args()
    config = load_config()

    {
        "list": cmd_list,
        "heatmap": cmd_heatmap,
    }[args.command](config, args)


if __name__ == "__main__":
    main()
