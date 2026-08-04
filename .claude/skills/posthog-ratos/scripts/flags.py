#!/usr/bin/env python3
"""Feature flags e experimentos do PostHog."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib._auth import load_config, api_get, resolve_project  # noqa: E402


def _project(config, args):
    project_id = resolve_project(args.project) if args.project else config["project_id"]
    if not project_id:
        sys.exit("Erro: informe --project (nome cadastrado ou project_id) ou configure POSTHOG_PROJECT_ID no .env")
    return project_id


def cmd_flags(config, args):
    project_id = _project(config, args)
    data = api_get(config, f"/api/projects/{project_id}/feature_flags/", {"limit": args.limit})
    resultados = data.get("results", data)
    resumo = [
        {
            "key": f.get("key"),
            "nome": f.get("name"),
            "ativo": f.get("active"),
            "rollout": f.get("filters", {}).get("aggregation_group_type_index"),
            "grupos": f.get("filters", {}).get("groups"),
        }
        for f in resultados
    ] if args.resumo else resultados
    print(json.dumps(resumo, indent=2, ensure_ascii=False))


def cmd_experiments(config, args):
    project_id = _project(config, args)
    data = api_get(config, f"/api/projects/{project_id}/experiments/", {"limit": args.limit})
    resultados = data.get("results", data)
    resumo = [
        {
            "nome": e.get("name"),
            "feature_flag_key": e.get("feature_flag_key"),
            "inicio": e.get("start_date"),
            "fim": e.get("end_date"),
            "arquivado": e.get("archived"),
        }
        for e in resultados
    ] if args.resumo else resultados
    print(json.dumps(resumo, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="PostHog Ratos — feature flags e experimentos")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--project", help="Nome cadastrado em contas.yaml ou project_id")
    common.add_argument("--limit", default=100)
    common.add_argument("--resumo", action="store_true", help="Mostra apenas os campos principais")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", parents=[common], help="Lista feature flags")
    sub.add_parser("experiments", parents=[common], help="Lista experimentos")

    args = parser.parse_args()
    config = load_config()

    {
        "list": cmd_flags,
        "experiments": cmd_experiments,
    }[args.command](config, args)


if __name__ == "__main__":
    main()
