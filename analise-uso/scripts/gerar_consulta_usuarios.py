#!/usr/bin/env python3
"""Gera consulta MySQL para os usuários presentes nas extrações de uso de Roleplay."""
import argparse
import csv
from pathlib import Path

TENANT = "96785b22-3302-4c34-ae92-b48425346811"
BATCH_SIZE = 1000


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--saida", required=True, type=Path, help="Arquivo SQL gerado (substituído se já existir)")
    parser.add_argument("arquivos", nargs="+", type=Path, help="arquivos CSV ou TSV originais de Roleplay")
    args = parser.parse_args()
    if any(args.saida.resolve() == path.resolve() for path in args.arquivos):
        parser.error("a saída deve ser diferente dos arquivos de entrada")
    ids = set()
    for path in args.arquivos:
        with path.open(encoding="utf-8-sig", newline="") as source:
            reader = csv.DictReader(source, delimiter="\t" if path.suffix.lower() == ".tsv" else ",")
            if not reader.fieldnames or "user_id" not in reader.fieldnames:
                parser.error(f"{path}: é necessária a coluna user_id")
            for row in reader:
                if "tenant_id" in reader.fieldnames and (row.get("tenant_id") or "").strip().lower() != TENANT:
                    parser.error(f"{path}: tenant diferente do configurado")
                value = (row.get("user_id") or "").strip()
                if not value.isascii() or not value.isdecimal() or int(value) <= 0:
                    parser.error(f"{path}: user_id inválido")
                ids.add(int(value))
    ordered = sorted(ids)
    chunks = [ordered[i:i + BATCH_SIZE] for i in range(0, len(ordered), BATCH_SIZE)]
    clauses = ["u.id IN (" + ", ".join(map(str, chunk)) + ")" for chunk in chunks]
    condition = "\n    OR ".join(clauses) if clauses else "1 = 0"
    query = """-- MySQL — Alura; uma linha por aluno e produto válido na consulta.
SELECT DISTINCT u.id AS user_id,
    COALESCE(REPLACE(REPLACE(TO_BASE64(CONVERT(CONCAT(p.code, ' — ', p.name) USING utf8mb4)), CHAR(10), ''), CHAR(13), ''), '') AS produto_base64
FROM `User` u
LEFT JOIN (
    SELECT a.user_id, produto.code, produto.name
    FROM Acquirement a
    JOIN Product produto ON produto.id = a.product_id
    LEFT JOIN BMPayment pagamento ON pagamento.id = a.payment_id
    WHERE a.status IN ('FREE', 'PAID')
      AND produto.status = 'ENABLED'
      AND a.startsAt <= NOW()
      AND a.expirationDate >= CURRENT_DATE()
      AND (pagamento.id IS NULL OR pagamento.status <> 'REIMBURSED')
) p ON p.user_id = u.id
WHERE u.role = 'STUDENT'
  AND (""" + condition + ")\nORDER BY u.id;\n"
    with args.saida.open("w", encoding="utf-8") as output:
        output.write(query)
    print(f"IDs distintos: {len(ids)}; grupos de até {BATCH_SIZE}: {len(chunks)}")


if __name__ == "__main__":
    main()
