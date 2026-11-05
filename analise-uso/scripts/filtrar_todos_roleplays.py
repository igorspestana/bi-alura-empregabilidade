#!/usr/bin/env python3
"""Atualiza os resultados finais dos três Roleplays a partir dos intermediários."""
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent
FEATURES = (
    "roleplay-entrevista-comportamental",
    "roleplay-entrevista-tecnica",
    "roleplay-defesa-de-case",
)


def main():
    intermediate = ROOT / "resultados" / "intermediarios"
    final = ROOT / "resultados" / "finais"
    final.mkdir(parents=True, exist_ok=True)
    # Primeiro prepara os três arquivos; nenhuma saída é substituída se um filtro falhar.
    with tempfile.TemporaryDirectory(prefix=".roleplay-", dir=final) as temporary:
        tmp = Path(temporary)
        for feature in FEATURES:
            print(f"Processando {feature}:", flush=True)
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "filtrar_roleplay.py"),
                 str(intermediate / "usuarios-student.tsv"), str(intermediate / f"{feature}.tsv"),
                 str(tmp / f"{feature}-student.tsv")],
                check=True,
            )
        for feature in FEATURES:
            filename = f"{feature}-student.tsv"
            (tmp / filename).replace(final / filename)
    print("Resultados finais atualizados.")


if __name__ == "__main__":
    try:
        main()
    except (subprocess.CalledProcessError, OSError) as error:
        print(f"Falha ao atualizar os resultados: {error}", file=sys.stderr)
        sys.exit(1)
