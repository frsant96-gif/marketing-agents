# -*- coding: utf-8 -*-
"""
Junta os resultados de pesquisa na internet (result_XX.json) na planilha.
Só aplica domínio no upload principal quando confidence == "high".
Tudo com confidence medium/low/not_found vai para uma aba separada de
revisão manual (não entra na lista de upload pronta).
"""
import glob
import json

import pandas as pd

from dedup import normalize_key

XLSX = "Empresas_SAP_NOW_LinkedIn_Ads.xlsx"


def main():
    high_conf = {}
    review_rows = []

    for path in sorted(glob.glob("result_*.json")):
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
        for item in items:
            name = item.get("name")
            domain = item.get("domain")
            conf = item.get("confidence")
            if not name:
                continue
            key = normalize_key(name)
            if conf == "high" and domain:
                high_conf[key] = domain
            elif domain:
                review_rows.append({
                    "companyname": name,
                    "domain_sugerido": domain,
                    "confidence": conf,
                    "fonte": path,
                })

    df = pd.read_excel(XLSX, sheet_name="LinkedIn Upload")
    for col in ["companydomain", "linkedincompanypageurl", "city", "state", "companycountry", "industry"]:
        df[col] = df[col].astype("object")
        df[col] = df[col].where(df[col].notna(), "")

    applied = 0
    for idx, row in df.iterrows():
        if row["companydomain"]:
            continue  # já tinha domínio do HubSpot, não sobrescreve
        key = normalize_key(str(row["companyname"]))
        domain = high_conf.get(key)
        if domain:
            df.at[idx, "companydomain"] = domain
            applied += 1

    review_df = pd.DataFrame(review_rows)

    with pd.ExcelWriter(XLSX, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name="LinkedIn Upload", index=False)
    # aba de revisão manual: precisa ser recriada do zero (remove se já existir)
    import openpyxl
    wb = openpyxl.load_workbook(XLSX)
    if "Sugestoes p revisar manualmente" in wb.sheetnames:
        del wb["Sugestoes p revisar manualmente"]
    wb.save(XLSX)
    with pd.ExcelWriter(XLSX, engine="openpyxl", mode="a") as writer:
        review_df.to_excel(writer, sheet_name="Sugestoes p revisar manualmente", index=False)

    total_domain_filled = (df["companydomain"] != "").sum()
    print(f"Dominios de alta confianca aplicados nesta rodada (pesquisa web): {applied}")
    print(f"Total de empresas com dominio preenchido agora (HubSpot + web high-confidence): {total_domain_filled} de {len(df)}")
    print(f"Sugestoes medium/low para revisao manual: {len(review_df)}")


if __name__ == "__main__":
    main()
