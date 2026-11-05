#!/usr/bin/env python3
"""Prepara os arquivos de resultados sem alterar arquivos existentes."""
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent / "resultados"
    files = {
        "intermediarios": (
            "roleplay-entrevista-comportamental.tsv",
            "roleplay-entrevista-tecnica.tsv",
            "roleplay-defesa-de-case.tsv",
            "usuarios-student.tsv",
        ),
        "finais": (
            "code-interview.tsv",
            "system-design.tsv",
            "roleplay-entrevista-comportamental-student.tsv",
            "roleplay-entrevista-tecnica-student.tsv",
            "roleplay-defesa-de-case-student.tsv",
        ),
    }
    for directory_name, names in files.items():
        directory = root / directory_name
        directory.mkdir(parents=True, exist_ok=True)
        for name in names:
            path = directory / name
            try:
                path.touch(exist_ok=False)
                print(f"Criado: {path}")
            except FileExistsError:
                print(f"Já existe, preservado: {path}")


if __name__ == "__main__":
    main()
