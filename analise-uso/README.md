# Análise de uso das features de empregabilidade

## Passo a passo diário

### 1. Preparar os arquivos

No terminal, entre neste diretório e execute:

```bash
cd /home/igor/repos/alura/bi-alura-empregabilidade/analise-uso
python3 scripts/preparar_arquivos.py
```

O script cria os arquivos ausentes e preserva os existentes. Se quiser guardar uma rodada anterior, arquive-a antes de substituir seu conteúdo.

### 2. Executar as consultas das features

No BI, execute cada arquivo de `consultas/` no banco indicado. Copie o resultado **com o cabeçalho** e cole no arquivo correspondente, substituindo o conteúdo anterior:

| Banco | Feature | Consulta | Onde colar o resultado |
| --- | --- | --- | --- |
| Alura | Code Interview | `code-interview.sql` | `resultados/finais/code-interview.tsv` |
| Alura | System Design | `system-design.sql` | `resultados/finais/system-design.tsv` |
| Gnarus AI | Entrevista comportamental | `roleplay-entrevista-comportamental.sql` | `resultados/finais/roleplay-entrevista-comportamental.tsv` |
| Gnarus AI | Entrevista técnica | `roleplay-entrevista-tecnica.sql` | `resultados/finais/roleplay-entrevista-tecnica.tsv` |
| Gnarus AI | Defesa de Case | `roleplay-defesa-de-case.sql` | `resultados/finais/roleplay-defesa-de-case.tsv` |

As consultas devem explicitar o período e o escopo considerados. Se uma consulta não retornar linhas, mantenha o cabeçalho no arquivo e registre qualquer falha separadamente.

### 3. Solicitar a análise

Os cinco arquivos para análise estão em `resultados/finais/`. Peça ao Codex: **“Execute as instruções de [prompt-gerar-relatorio.md](prompt-gerar-relatorio.md)”**. Informe se alguma consulta falhou ou não retornou dados.

O relatório será salvo em `relatorios/` com a data de hoje. As extrações e os relatórios são ignorados pelo Git.
