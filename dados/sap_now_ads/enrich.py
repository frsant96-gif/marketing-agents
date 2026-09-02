# -*- coding: utf-8 -*-
"""
Cruza a lista de empresas do SAP NOW (companyname) com os dados de
domínio/cidade/estado/setor vindos do HubSpot, usando normalização de nome
para o match (mesma lógica do dedup.py).
"""
import json
import re
import unicodedata

import pandas as pd

from dedup import normalize_key  # reaproveita a mesma normalização

SRC_XLSX = "Empresas_SAP_NOW_LinkedIn_Ads.xlsx"
OUT_XLSX = "Empresas_SAP_NOW_LinkedIn_Ads.xlsx"  # sobrescreve, mesmo arquivo único

HUBSPOT_FILES = [
    "hubspot_batch_00.json",
    r"C:\Users\franc\.claude\projects\c--Users-franc-solveplan-com-Roberto-Molina---Marketing-1--MKT-Estrategy-3--Agentes-de-IA-ccos-ratos\df5bcf56-c222-4002-b473-a82a5bac3e93\tool-results\mcp-claude_ai_HubSpot-search_crm_objects-1788308377496.txt",
    r"C:\Users\franc\.claude\projects\c--Users-franc-solveplan-com-Roberto-Molina---Marketing-1--MKT-Estrategy-3--Agentes-de-IA-ccos-ratos\df5bcf56-c222-4002-b473-a82a5bac3e93\tool-results\mcp-claude_ai_HubSpot-search_crm_objects-1788308534745.txt",
    r"C:\Users\franc\.claude\projects\c--Users-franc-solveplan-com-Roberto-Molina---Marketing-1--MKT-Estrategy-3--Agentes-de-IA-ccos-ratos\df5bcf56-c222-4002-b473-a82a5bac3e93\tool-results\mcp-claude_ai_HubSpot-search_crm_objects-1788308536639.txt",
    "hubspot_400_599.json",
]

COUNTRY_MAP = {
    "brazil": "BR", "brasil": "BR", "united states": "US", "germany": "DE",
    "switzerland": "CH", "canada": "CA", "united kingdom": "GB", "moldova": "MD",
}


def load_records(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        return data.get("results", [])
    return data


def main():
    hs_by_key = {}
    total_loaded = 0
    for path in HUBSPOT_FILES:
        try:
            records = load_records(path)
        except FileNotFoundError:
            print(f"[aviso] arquivo nao encontrado, pulando: {path}")
            continue
        for rec in records:
            props = rec.get("properties", {})
            name = props.get("name")
            if not name:
                continue
            key = normalize_key(name)
            if not key:
                continue
            total_loaded += 1
            # se ja existe, mantem o primeiro (evita sobrescrever com duplicata pior)
            if key not in hs_by_key:
                hs_by_key[key] = props

    print(f"Registros HubSpot carregados: {total_loaded}")
    print(f"Chaves unicas HubSpot: {len(hs_by_key)}")

    df = pd.read_excel(SRC_XLSX, sheet_name="LinkedIn Upload")
    for col in ["companydomain", "linkedincompanypageurl", "city", "state", "companycountry", "industry"]:
        df[col] = df[col].astype("object")
        df[col] = df[col].where(df[col].notna(), "")

    matched = 0
    for idx, row in df.iterrows():
        name = str(row["companyname"])
        key = normalize_key(name)
        hs = hs_by_key.get(key)
        if not hs:
            continue
        matched += 1
        domain = hs.get("domain", "")
        if domain:
            df.at[idx, "companydomain"] = domain
        city = hs.get("city", "")
        if city:
            df.at[idx, "city"] = city
        state = hs.get("state", "")
        if state:
            df.at[idx, "state"] = state
        country_raw = (hs.get("country") or "").strip().lower()
        if country_raw:
            df.at[idx, "companycountry"] = COUNTRY_MAP.get(country_raw, hs.get("country"))
        industry = hs.get("industry", "")
        if industry:
            df.at[idx, "industry"] = industry.replace("_", " ").title()

    # Para o restante (sem match no HubSpot), assume Brasil como pais --
    # e a lista é majoritariamente de empresas brasileiras convidadas do
    # SAP NOW Brasil, entao esse default é seguro.
    no_country = df["companycountry"].isna() | (df["companycountry"] == "")
    df.loc[no_country, "companycountry"] = "BR"

    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name="LinkedIn Upload", index=False)

    print(f"Empresas casadas com HubSpot (domínio/cidade/setor): {matched} de {len(df)}")


if __name__ == "__main__":
    main()
