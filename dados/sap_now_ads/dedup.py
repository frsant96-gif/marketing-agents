# -*- coding: utf-8 -*-
"""
Deduplica a lista de empresas do SAP NOW.
Normaliza (remove acentos, maiusculas, pontuacao, sufixos societarios) para
agrupar variações do mesmo nome, e escolhe uma forma "canônica" (mais comum
e mais bem formatada) para representar cada grupo.
"""
import re
import unicodedata
from collections import defaultdict, Counter

import pandas as pd

RAW_PATH = "empresas_raw.txt"
OUT_XLSX = "Empresas_SAP_NOW_LinkedIn_Ads.xlsx"

LINKEDIN_EXTRA_COLUMNS = [
    "companydomain",
    "linkedincompanypageurl",
    "city",
    "state",
    "companycountry",
    "industry",
]

SUFFIXES = [
    r"\bS\s*/\s*A\b", r"\bS\.?A\.?A?\b", r"\bLTDA\.?\b", r"\bLTD\.?\b",
    r"\bCIA\.?\b", r"\bCOMPANHIA\b", r"\bIND(?:USTRIA|\.)?\b",
    r"\bCOM(?:ERCIO|\.)?\b", r"\bDO BRASIL\b", r"\bBRASIL\b",
    r"\bGROUP\b", r"\bGRUPO\b", r"\bCORP(?:ORATION)?\.?\b",
    r"\bCOMPANY\b", r"\bINC\.?\b", r"\bHOLDING\b", r"\bPARTICIPACOES\b",
    r"\bPARTICIPAÇÕES\b", r"\bE\s+SERVICOS\b",
]

def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)
    )

def normalize_key(name: str) -> str:
    s = strip_accents(name).upper()
    for suf in SUFFIXES:
        s = re.sub(suf, " ", s)
    s = re.sub(r"[^A-Z0-9& ]+", " ", s)
    # sufixos societarios que só sobram como letras soltas depois da limpeza
    # de pontuação (S/A, S.A., S.A.A -> "S A", "S A A")
    s = re.sub(r"\b(S\s*A\s*A?)\b\s*$", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def clean_display(name: str) -> str:
    return re.sub(r"\s+", " ", name).strip()

def score(name: str) -> tuple:
    # Prefer names that are NOT all-uppercase (mixed case = provavelmente
    # digitado com cuidado), sem sufixo societário, mais curtos.
    has_lower = any(c.islower() for c in name)
    no_suffix = not re.search(r"S\.?A\.?|LTDA|LTD\b", name, re.IGNORECASE)
    return (has_lower, no_suffix, -len(name))

def main():
    with open(RAW_PATH, encoding="utf-8") as f:
        lines = [clean_display(l) for l in f if clean_display(l)]

    groups = defaultdict(list)
    for name in lines:
        key = normalize_key(name)
        if not key:
            continue
        groups[key].append(name)

    rows = []
    for key, names in groups.items():
        counts = Counter(names)
        # escolhe a variante mais frequente; empate -> melhor "score"
        best = sorted(counts.items(), key=lambda kv: (-kv[1], score(kv[0])))[0][0]
        rows.append({
            "Empresa (nome final)": best,
            "Ocorrencias na lista original": len(names),
            "Variantes encontradas": "; ".join(sorted(set(names), key=str.lower)),
        })

    rows.sort(key=lambda r: r["Empresa (nome final)"].lower())

    df = pd.DataFrame(rows)

    # Aba pronta pra upload no LinkedIn Campaign Manager: header oficial
    # "companyname" + colunas opcionais (vazias, pra melhorar match rate
    # quando preenchidas com dado real).
    upload_df = pd.DataFrame({"companyname": df["Empresa (nome final)"]})
    for col in LINKEDIN_EXTRA_COLUMNS:
        upload_df[col] = ""

    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as writer:
        upload_df.to_excel(writer, sheet_name="LinkedIn Upload", index=False)
        df.to_excel(writer, sheet_name="Auditoria da deduplicacao", index=False)

    print(f"Total de linhas originais: {len(lines)}")
    print(f"Total de empresas unicas: {len(df)}")
    print(f"Arquivo gerado: {OUT_XLSX}")

if __name__ == "__main__":
    main()
