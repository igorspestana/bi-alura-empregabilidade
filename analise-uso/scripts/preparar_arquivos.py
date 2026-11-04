#!/usr/bin/env python3
"""Prepara os arquivos de resultados sem alterar arquivos existentes."""
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent / "resultados" / "finais"
    root.mkdir(parents=True, exist_ok=True)
    files = (
        "code-interview.tsv",
        "system-design.tsv",
        "roleplay-entrevista-comportamental.tsv",
        "roleplay-entrevista-tecnica.tsv",
        "roleplay-defesa-de-case.tsv",
    )
    for name in files:
        path = root / name
        try:
            path.touch(exist_ok=False)
            print(f"Criado: {path}")
        except FileExistsError:
            print(f"Já existe, preservado: {path}")


if __name__ == "__main__":
    main()
