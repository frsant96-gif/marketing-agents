#!/usr/bin/env python3
"""Leitura de organizacoes e projetos do PostHog."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib._auth import load_config, api_get, resolve_project  # noqa: E402


def cmd_organizations(config, args):
    data = api_get(config, "/api/organizations/")
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False))


def cmd_projects(config, args):
    data = api_get(config, "/api/projects/")
    print(json.dumps(data.get("results", data), indent=2, ensure_ascii=False))


def cmd_account(config, args):
    project_id = resolve_project(args.project) if args.project else config["project_id"]
    if not project_id:
        sys.exit("Erro: informe --project (nome cadastrado ou project_id) ou configure POSTHOG_PROJECT_ID no .env")
    data = api_get(config, f"/api/projects/{project_id}/")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="PostHog Ratos — leitura de organizacoes e projetos")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("organizations", help="Lista organizacoes acessiveis")
    sub.add_parser("projects", help="Lista projetos acessiveis")

    p_account = sub.add_parser("account", help="Detalhes de um projeto")
    p_account.add_argument("--project", help="Nome cadastrado em contas.yaml ou project_id")

    args = parser.parse_args()
    config = load_config()

    {
        "organizations": cmd_organizations,
        "projects": cmd_projects,
        "account": cmd_account,
    }[args.command](config, args)


if __name__ == "__main__":
    main()
