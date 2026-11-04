#!/usr/bin/env python3
"""Cruza exportações CSV de Roleplay com os IDs STUDENT do banco Alura."""
import argparse
import base64
import csv
from pathlib import Path

TENANT = "96785b22-3302-4c34-ae92-b48425346811"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("usuarios", type=Path, help="CSV ou TSV de usuários STUDENT")
    parser.add_argument("roleplay", type=Path, help="CSV ou TSV original do Gnarus AI")
    parser.add_argument("saida", type=Path, help="Novo arquivo filtrado CSV ou TSV")
    args = parser.parse_args()
    if args.saida.resolve() in (args.usuarios.resolve(), args.roleplay.resolve()):
        parser.error("a saída deve ser diferente dos arquivos de entrada")
    with args.usuarios.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, delimiter="\t" if args.usuarios.suffix.lower() == ".tsv" else ",")
        if not reader.fieldnames or "user_id" not in reader.fieldnames:
            parser.error("o CSV de usuários precisa da coluna user_id")
        students = {row["user_id"].strip() for row in reader if row["user_id"] and row["user_id"].strip()}
    with args.roleplay.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, delimiter="\t" if args.roleplay.suffix.lower() == ".tsv" else ",")
        if not reader.fieldnames or not {"user_id", "tenant_id"}.issubset(reader.fieldnames):
            parser.error("o CSV de roleplay precisa das colunas user_id e tenant_id")
        output_fields = [name.removesuffix("_base64") for name in reader.fieldnames]
        rows = []
        total = 0
        for row in reader:
            total += 1
            if (row.get("tenant_id") or "").strip().lower() != TENANT:
                parser.error("o CSV de roleplay contém tenant diferente do configurado")
            if (row.get("user_id") or "").strip() in students:
                decoded = {}
                for key, value in row.items():
                    if key.endswith("_base64") and value:
                        decoded[key.removesuffix("_base64")] = base64.b64decode(value, validate=True).decode("utf-8")
                    else:
                        decoded[key.removesuffix("_base64")] = value
                rows.append(decoded)
        try:
            output = args.saida.open("x", encoding="utf-8", newline="")
        except FileExistsError:
            output = args.saida.open("r+", encoding="utf-8", newline="")
            if output.read(1):
                output.close()
                parser.error("o arquivo de saída já contém dados")
            output.seek(0)
        with output:
            writer = csv.DictWriter(output, fieldnames=output_fields, delimiter="\t" if args.saida.suffix.lower() == ".tsv" else ",")
            writer.writeheader()
            writer.writerows(rows)
    print(f"Linhas de roleplay: {total}; mantidas: {len(rows)}; excluídas: {total - len(rows)}")


if __name__ == "__main__":
    main()
