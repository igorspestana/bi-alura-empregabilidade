# Análise de empregabilidade

Este diretório organiza consultas, resultados extraídos diariamente e relatórios de análise das features de empregabilidade.

```text
alura-empregabilidade/
├── consultas/           # Uma consulta SQL por feature
├── resultados/          # Uma pasta por feature, com arquivos por data
│   ├── code-interview/
│   ├── system-design/
│   ├── roleplay-entrevista-comportamental/
│   ├── roleplay-entrevista-tecnica/
│   └── roleplay-defesa-de-case/
└── relatorios/          # Relatórios de análise por data
```

## Rotina diária

1. Execute cada consulta em `consultas/` no banco correspondente, conforme a tabela abaixo. As consultas retornam todos os resultados disponíveis, sem filtro de data ou de usuário.
2. Exporte o resultado completo de cada consulta, incluindo os nomes das colunas e os campos JSON, em CSV ou JSON. Salve-o na pasta da feature dentro de `resultados/`, com o nome `AAAA-MM-DD.csv` ou `AAAA-MM-DD.json`. Para MySQL, inclua o tenant no nome, por exemplo `2026-11-04-alura.csv` e `2026-11-04-pm3.csv`. Se houver mais de uma extração no mesmo dia, acrescente a hora, como `2026-11-04-1430-alura.csv`.
3. Preserve os arquivos de dias anteriores. Cada arquivo é um retrato completo no momento da consulta; os dados de dias diferentes podem conter as mesmas tentativas.
4. Solicite a análise informando a data e o escopo desejados. Por exemplo: “Analise os resultados de 2026-11-04 de todas as features e compare com 2026-11-03”. Informe também se alguma extração estiver ausente ou tiver falhado, para que ela não seja confundida com um resultado vazio.
5. Salve o relatório em `relatorios/AAAA-MM-DD.md`. Para análises adicionais na mesma data, use um nome descritivo, como `2026-11-04-comparativo.md`.

Use exportação de arquivo pelo cliente de banco para preservar corretamente campos JSON, aspas e quebras de linha. Se não houver linhas, mantenha um arquivo com cabeçalhos em CSV ou um array vazio (`[]`) em JSON, para registrar que a consulta foi executada.

## Consultas

| Feature | Consulta | Banco | Resultado |
| --- | --- | --- | --- |
| Code Interview (Code Challenge) | `consultas/code-interview.sql` | MySQL do serviço de conteúdo | Submissões finais com status, datas e `executionResponse`, que contém os resultados dos testes. Não inclui execuções de testes públicos feitas durante a resolução. |
| System Design | `consultas/system-design.sql` | MySQL do serviço de conteúdo | Tentativas com avaliação final persistida, incluindo classificação, resumo e resultado detalhado em JSON. |
| Roleplay Entrevista comportamental | `consultas/roleplay-entrevista-comportamental.sql` | PostgreSQL do serviço Python | Tentativas `behavioral_interview` com relatório em `artifact`. |
| Roleplay Entrevista Técnica | `consultas/roleplay-entrevista-tecnica.sql` | PostgreSQL do serviço Python | Tentativas `technical_interview` com relatório em `artifact`. |
| Roleplay Defesa de Case | `consultas/roleplay-defesa-de-case.sql` | PostgreSQL do serviço Python | Tentativas `case_interview` com relatório em `artifact`, no formato específico de case. |

Execute as consultas MySQL no banco de cada tenant desejado e identifique o tenant no nome do arquivo: o `user_id` deve ser interpretado nesse contexto. As consultas PostgreSQL retornam os tenants acessíveis à conexão e incluem `tenant_id` em cada linha. As consultas excluem registros sem resultado persistido e ordenam os resultados do mais recente para o mais antigo.

Os arquivos de resultados e relatórios são ignorados pelo Git por poderem conter dados de pessoas usuárias. O `.gitignore` não impede o acesso local aos arquivos; mantenha-os em um local com acesso adequado. As consultas foram elaboradas a partir dos mapeamentos e migrações do projeto e não foram executadas em um banco.
