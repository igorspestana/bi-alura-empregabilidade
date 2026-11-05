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
| Gnarus AI | Entrevista comportamental | `roleplay-entrevista-comportamental.sql` | `resultados/intermediarios/roleplay-entrevista-comportamental.tsv` |
| Gnarus AI | Entrevista técnica | `roleplay-entrevista-tecnica.sql` | `resultados/intermediarios/roleplay-entrevista-tecnica.tsv` |
| Gnarus AI | Defesa de Case | `roleplay-defesa-de-case.sql` | `resultados/intermediarios/roleplay-defesa-de-case.tsv` |

As consultas do Gnarus AI devem ser executadas integralmente na mesma conexão, incluindo `BEGIN` e `SET LOCAL`. Configure o BI para encerrar ou descartar a conexão, ou aplicar rollback automático ao fim da execução. Se uma consulta não retornar linhas, mantenha o cabeçalho no arquivo e registre qualquer falha separadamente.

### 3. Gerar a consulta dos usuários

No terminal, gere a consulta MySQL com os IDs presentes nas três extrações intermediárias:

```bash
python3 scripts/gerar_consulta_usuarios.py \
  --saida resultados/intermediarios/usuarios-roleplay.sql \
  resultados/intermediarios/roleplay-entrevista-comportamental.tsv \
  resultados/intermediarios/roleplay-entrevista-tecnica.tsv \
  resultados/intermediarios/roleplay-defesa-de-case.tsv
```

O comando substitui `usuarios-roleplay.sql` pela consulta dos IDs encontrados nas extrações. A consulta retorna uma linha por aluno e produto válido; alunos sem produto válido também são retornados. O produto é codificado em Base64 para preservar a separação das colunas na cópia do BI.

### 4. Consultar os alunos no Alura

Abra `resultados/intermediarios/usuarios-roleplay.sql`, copie seu conteúdo e execute no banco **Alura** pelo BI. Copie o resultado, incluindo os cabeçalhos `user_id` e `produto_base64`, e cole em:

```text
resultados/intermediarios/usuarios-student.tsv
```

Esse arquivo identifica os usuários com role `STUDENT` e seus produtos válidos no momento da consulta. Se você já tiver uma exportação anterior contendo apenas `user_id`, execute a consulta atualizada e substitua o arquivo.

### 5. Gerar os resultados finais de Roleplay

```bash
python3 scripts/filtrar_todos_roleplays.py
```

O comando cruza as três extrações intermediárias com a lista de alunos, decodifica e agrupa os produtos de cada usuário em uma lista JSON e grava os resultados em `resultados/finais/` com o sufixo `-student`. Uma lista vazia significa que a consulta não encontrou produto válido para aquele aluno. Se algum filtro falhar durante a preparação, os resultados finais anteriores são preservados.

### 6. Solicitar a análise

Os cinco arquivos para análise estão em `resultados/finais/`: Code Interview, System Design e os três Roleplays filtrados para alunos. Peça ao Codex: **“Execute as instruções de [prompt-gerar-relatorio.md](prompt-gerar-relatorio.md)”**. Informe se alguma consulta falhou ou não retornou dados.

O relatório será salvo em `relatorios/` com a data de hoje e um contador diário, como `AAAA-MM-DD-01.md` e `AAAA-MM-DD-02.md`, sem sobrescrever arquivos existentes. Ele apresentará alunos e eventos agregados por produto válido no momento da consulta. Um aluno com mais de um produto aparece em cada grupo, por isso as linhas não devem ser somadas para obter o total da feature. As extrações e os relatórios são ignorados pelo Git.
