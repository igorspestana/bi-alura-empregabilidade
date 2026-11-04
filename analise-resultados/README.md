# Análise de empregabilidade

Este diretório organiza consultas, resultados extraídos diariamente e relatórios de análise das features de empregabilidade.

```text
bi-alura-empregabilidade/analise-resultados/
├── consultas/      # Uma consulta SQL por feature
├── scripts/        # Cruzamento com usuários STUDENT
├── resultados/
│   ├── finais/          # Cinco resultados prontos para análise
│   └── intermediarios/  # Roleplays sem filtro e cruzamento de usuários
└── relatorios/     # Análises por data
```

## Rotina diária

1. Execute cada consulta no banco indicado abaixo. Salve as extrações de Code Interview e System Design em `resultados/finais/`. Salve as três extrações de Roleplay sem filtro em `resultados/intermediarios/`. Use CSV ou TSV com cabeçalhos e inclua a data no nome para preservar o histórico, por exemplo `2026-11-04-roleplay-entrevista-tecnica.tsv`. Identifique o tenant nas extrações MySQL. Preserve os arquivos de dias anteriores: cada extração é um retrato completo e pode repetir tentativas de dias anteriores.
2. Para Roleplay, faça o cruzamento com usuários STUDENT seguindo as instruções abaixo. As consultas MySQL já filtram a role diretamente.
3. Solicite a análise informando a data e eventuais extrações ausentes ou com falha. Salve o relatório em `relatorios/` com a data no nome.

Use exportação pelo cliente de banco que preserve aspas e quebras de linha dentro dos campos. Para registrar um resultado vazio, mantenha um arquivo com os cabeçalhos.

## Consultas

| Feature | Consulta | Banco | Resultado |
| --- | --- | --- | --- |
| Code Interview (Code Challenge) | `consultas/code-interview.sql` | MySQL — Alura | Submissões finais com status, datas e `executionResponse`, que contém os resultados dos testes. Não inclui execuções de testes públicos feitas durante a resolução. |
| System Design | `consultas/system-design.sql` | MySQL — Alura | Tentativas com avaliação final persistida, incluindo classificação, resumo e resultado detalhado em JSON. |
| Roleplay Entrevista comportamental | `consultas/roleplay-entrevista-comportamental.sql` | PostgreSQL — Gnarus AI | Tentativas `behavioral_interview` com decisão, resumo, pontos fortes, pontos a melhorar, competências, pontuação, recomendação e plano de ação. |
| Roleplay Entrevista Técnica | `consultas/roleplay-entrevista-tecnica.sql` | PostgreSQL — Gnarus AI | Tentativas `technical_interview` com decisão, resumo, pontos fortes, pontos a melhorar, competências, pontuação, recomendação e plano de ação. |
| Roleplay Defesa de Case | `consultas/roleplay-defesa-de-case.sql` | PostgreSQL — Gnarus AI | Tentativas `case_interview` com decisão, resultado, competências, melhorias, próxima simulação, recomendação e plano de ação. |

Execute as consultas MySQL no banco Alura de cada tenant desejado e identifique o tenant no nome do arquivo: o `user_id` deve ser interpretado nesse contexto. As consultas PostgreSQL filtram o tenant `96785b22-3302-4c34-ae92-b48425346811` e incluem `tenant_id` em cada linha. As consultas excluem registros sem resultado persistido e ordenam os resultados do mais recente para o mais antigo.

Os arquivos de resultados e relatórios são ignorados pelo Git por poderem conter dados de pessoas usuárias. O `.gitignore` não impede o acesso local aos arquivos; mantenha-os em um local com acesso adequado. As consultas foram elaboradas a partir dos mapeamentos e migrações do projeto e não foram executadas em um banco.

As consultas do Gnarus AI devem ser executadas integralmente, na mesma conexão: `BEGIN READ ONLY` e `SET LOCAL` definem o contexto de tenant exigido pelas políticas de acesso. O bloco termina no `SELECT` para que o cliente mostre as linhas. Configure o cliente para encerrar ou descartar a conexão, ou aplicar rollback automático ao fim da execução, evitando deixar a transação aberta.

## Filtro de alunos nos resultados

Os exemplos abaixo usam os nomes dos arquivos atualmente em `resultados/intermediarios/`. Se você usar nomes com data nas próximas extrações, ajuste os caminhos. Execute os comandos no diretório `analise-resultados/`. A consulta SQL gerada é substituída a cada execução; para os resultados filtrados, escolha nomes de saída que ainda não existam.

As consultas de Code Interview e System Design filtram diretamente `User.role = 'STUDENT'` no MySQL. Para Roleplay, execute as três consultas no Gnarus AI e exporte os resultados originais em CSV ou TSV com cabeçalhos. Em seguida, gere uma consulta contendo somente os IDs distintos presentes nesses arquivos:

```bash
python3 scripts/gerar_consulta_usuarios.py \
  --saida resultados/intermediarios/usuarios-roleplay.sql \
  resultados/intermediarios/roleplay-entrevista-comportamental.tsv \
  resultados/intermediarios/roleplay-entrevista-tecnica.tsv \
  resultados/intermediarios/roleplay-defesa-de-case.tsv
```

Execute o SQL gerado no banco Alura correspondente ao tenant do Gnarus AI. Exporte o resultado em CSV ou TSV com o cabeçalho `user_id`, por exemplo em `resultados/intermediarios/2026-11-04-usuarios-student-alura.csv`. A consulta procura os IDs em grupos de até 1.000 valores, mas é executada como uma única instrução. Se não houver IDs nos arquivos de entrada, ela não retorna usuários.

Para cada arquivo de Roleplay, execute a partir deste diretório:

```bash
python3 scripts/filtrar_roleplay.py \
  resultados/intermediarios/2026-11-04-usuarios-student-alura.csv \
  resultados/intermediarios/roleplay-entrevista-tecnica.tsv \
  resultados/finais/2026-11-04-roleplay-entrevista-tecnica-student.tsv
```

Repita para os arquivos de entrevista comportamental e defesa de case. Os scripts conferem o tenant das linhas de Roleplay. A geração substitui o SQL de saída; o filtro não sobrescreve arquivos existentes. O filtro compara `user_id` com `User.id` e informa quantas linhas foram mantidas e excluídas. Solicite análises usando os arquivos filtrados em `resultados/finais/`; os originais não estão filtrados por role. Use extrações do mesmo dia: o cruzamento considera a role no momento da consulta ao Alura, que pode diferir da role na data da tentativa. Um ID ausente do resultado da consulta ao Alura é excluído.

Os scripts identificam o separador pela extensão: `.tsv` usa tabulação e `.csv` usa vírgula. É possível combinar arquivos CSV e TSV na mesma execução; escolha a extensão da saída filtrada conforme o formato desejado.

Os campos selecionados do JSON podem ser nulos se não estiverem presentes no artefato persistido. As consultas não retornam a conversa completa; ela pode ser consultada separadamente pelo identificador da tentativa.

As consultas de Roleplay codificam os campos de conteúdo em Base64 para permitir a cópia do resultado pelo BI sem tabulações ou quebras de linha dentro das células. O script `filtrar_roleplay.py` decodifica esses campos no arquivo filtrado, preservando o texto original. Os arquivos copiados do BI devem conter o cabeçalho e ser salvos como TSV.
