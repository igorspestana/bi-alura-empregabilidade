# Análise dos resultados de empregabilidade

## Passo a passo diário

### 1. Preparar os arquivos

No terminal, entre neste diretório e execute:

```bash
cd /home/igor/repos/alura/bi-alura-empregabilidade/analise-resultados
python3 scripts/preparar_arquivos.py
```

O script cria os arquivos ausentes e preserva os existentes. Se quiser guardar uma rodada anterior, arquive-a antes de substituir seu conteúdo.

### 2. Executar as consultas das features

No BI, execute cada arquivo de `consultas/` no banco indicado. Copie o resultado **com o cabeçalho** e cole no arquivo correspondente, substituindo o conteúdo anterior:

| Banco | Consulta | Onde colar o resultado |
| --- | --- | --- |
| Alura | `code-interview.sql` | `resultados/finais/code-interview.tsv` |
| Alura | `system-design.sql` | `resultados/finais/system-design.tsv` |
| Gnarus AI | `roleplay-entrevista-comportamental.sql` | `resultados/intermediarios/roleplay-entrevista-comportamental.tsv` |
| Gnarus AI | `roleplay-entrevista-tecnica.sql` | `resultados/intermediarios/roleplay-entrevista-tecnica.tsv` |
| Gnarus AI | `roleplay-defesa-de-case.sql` | `resultados/intermediarios/roleplay-defesa-de-case.tsv` |

As consultas do Gnarus AI devem ser executadas integralmente na mesma conexão, incluindo `BEGIN` e `SET LOCAL`. Configure o BI para encerrar ou descartar a conexão, ou aplicar rollback automático ao fim da execução. Se uma consulta não retornar linhas, mantenha o cabeçalho no arquivo e registre qualquer falha separadamente.

### 3. Gerar a consulta de usuários

No terminal, ainda neste diretório, execute:

```bash
python3 scripts/gerar_consulta_usuarios.py \
  --saida resultados/intermediarios/usuarios-roleplay.sql \
  resultados/intermediarios/roleplay-entrevista-comportamental.tsv \
  resultados/intermediarios/roleplay-entrevista-tecnica.tsv \
  resultados/intermediarios/roleplay-defesa-de-case.tsv
```

O comando substitui `usuarios-roleplay.sql` pela consulta dos IDs encontrados nos três Roleplays.

### 4. Consultar os alunos no Alura

Abra `resultados/intermediarios/usuarios-roleplay.sql`, copie seu conteúdo e execute no banco **Alura** pelo BI. Copie o resultado, incluindo o cabeçalho `user_id`, e cole em:

```text
resultados/intermediarios/usuarios-student.tsv
```

Esse arquivo identifica os usuários com role `STUDENT` no momento da consulta.

### 5. Gerar os resultados finais

```bash
python3 scripts/filtrar_todos_roleplays.py
```

O comando cruza os três Roleplays com a lista de alunos, decodifica os campos e substitui os três arquivos correspondentes em `resultados/finais/`. Se algum filtro falhar durante a preparação, os resultados anteriores são preservados.

### 6. Solicitar a análise

Os cinco arquivos para análise estão em `resultados/finais/`. Peça ao Codex: **“Execute as instruções de [prompt-gerar-relatorio.md](prompt-gerar-relatorio.md)”**. Informe se alguma consulta falhou ou não retornou dados. O prompt usa o [modelo de relatório](modelo-relatorio.md) e salva um novo arquivo em `relatorios/` com a data de hoje.

As extrações são retratos completos e podem repetir tentativas de dias anteriores. Os resultados e relatórios são ignorados pelo Git.
