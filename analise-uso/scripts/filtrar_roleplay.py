#!/usr/bin/env python3
"""Cruza exportações CSV de Roleplay com os IDs STUDENT do banco Alura."""
import argparse
import base64
import csv
import json
import binascii
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
        if not reader.fieldnames or not {"user_id", "produto_base64"}.issubset(reader.fieldnames):
            parser.error("a exportação de usuários precisa das colunas user_id e produto_base64; execute novamente a consulta de usuários atualizada")
        students = {}
        for line, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                parser.error(f"linha {line}: número de colunas inválido na exportação de usuários")
            user_id = row["user_id"].strip()
            if not user_id.isascii() or not user_id.isdecimal() or int(user_id) <= 0:
                parser.error(f"linha {line}: user_id inválido")
            products = students.setdefault(user_id, set())
            encoded = row["produto_base64"].strip()
            if encoded:
                try:
                    products.add(base64.b64decode(encoded, validate=True).decode("utf-8"))
                except (binascii.Error, UnicodeDecodeError):
                    parser.error(f"linha {line}: produto_base64 inválido")
    with args.roleplay.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, delimiter="\t" if args.roleplay.suffix.lower() == ".tsv" else ",")
        if not reader.fieldnames or not {"user_id", "tenant_id"}.issubset(reader.fieldnames):
            parser.error("o CSV de roleplay precisa das colunas user_id e tenant_id")
        output_fields = [name.removesuffix("_base64") for name in reader.fieldnames]
        product_field = "produtos_validos_no_momento_da_consulta"
        if product_field in output_fields:
            parser.error("a exportação de roleplay já contém a coluna de produtos")
        output_fields.append(product_field)
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
                decoded[product_field] = json.dumps(sorted(students[row["user_id"].strip()]), ensure_ascii=False)
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
