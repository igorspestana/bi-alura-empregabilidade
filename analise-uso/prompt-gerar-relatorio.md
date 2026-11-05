# Prompt: gerar relatório de uso

Analise os arquivos em `resultados/finais/` e crie um relatório em `relatorios/` usando `modelo-relatorio.md`. O objetivo é apresentar, para cada feature, a quantidade de alunos únicos, o uso agregado dos alunos por produto válido na consulta.

## Estrutura e preservação

- Preserve o título, as seções, os subtítulos e as colunas das tabelas do modelo. Substitua os textos entre colchetes e acrescente uma linha por produto identificado e, quando necessário, uma linha para cada situação de informação indisponível ou produto não identificado.
- Preencha `Data do relatório` com a data atual no fuso `America/Sao_Paulo`. Essa data não comprova a data em que os dados foram extraídos.
- Salve em `relatorios/AAAA-MM-DD-NN.md`, usando a data atual nesse fuso e um contador por dia, começando em `01` (por exemplo, `2026-11-05-01.md`, depois `2026-11-05-02.md`). Considere os arquivos já existentes na pasta e use um contador maior que todos os já usados para essa data; não reutilize números de arquivos removidos se houver números maiores. Um relatório antigo `AAAA-MM-DD.md` deve ser preservado e não impede o uso de `01`. Após `99`, continue com `100`, `101` e assim por diante.
- Crie o arquivo em modo exclusivo (por exemplo, `open(caminho, "x", encoding="utf-8")` em Python), sem abrir um arquivo existente para escrita. Se outro processo criar o mesmo nome antes da gravação, recalcule o contador e tente novamente. Nunca sobrescreva relatórios.
- Use linguagem direta e informe as limitações na seção correspondente. Não invente valores. Quando uma informação estiver indisponível, escreva `não disponível` e explique o motivo.

## Verificação das fontes

- Confira `resultados/finais/code-interview.tsv`, `system-design.tsv`, `roleplay-entrevista-comportamental-student.tsv`, `roleplay-entrevista-tecnica-student.tsv` e `roleplay-defesa-de-case-student.tsv` no mesmo diretório. Verifique leitura, cabeçalho, separação das colunas, identificadores e contagens numéricas. Identifique IDs duplicados, campos obrigatórios ausentes ou inválidos e possíveis inconsistências antes de calcular métricas; não some linhas duplicadas sem entender sua origem. Registre a limitação e peça os dados corrigidos quando necessário.
- Arquivo somente com cabeçalho representa zero linhas retornadas no escopo consultado, desde que a execução tenha sido confirmada. Diferencie isso de arquivo ausente, vazio, ilegível ou consulta com falha. Se a fonte estiver incompleta, apresente os dados válidos que puder sustentar e marque as conclusões afetadas como indisponíveis.
- As consultas não fornecem datas dos eventos nem um período explícito nas exportações. Não trate a data do relatório como período de uso, não infira evolução temporal e indique o período como não disponível quando não houver evidência.

## Regras de análise

- Para cada feature, conte `user_id` distintos no respectivo arquivo final. Os Roleplays já foram filtrados pela role `STUDENT` no momento da consulta ao Alura. Não use `alunos_unicos_na_feature` dos Roleplays como total de alunos: ela foi calculada antes desse filtro. Os totais por feature não podem ser somados para obter pessoas distintas no conjunto, pois um aluno pode usar mais de uma feature.
- Em cada feature, agrupe os alunos por produto válido na consulta. Conte `user_id` distintos em cada produto e some separadamente as contagens de `tentativas_criadas` e dos demais eventos dos alunos desse grupo. Um aluno com vários produtos integra cada grupo e suas contagens são incluídas integralmente em cada um: não some as linhas de produtos para obter o total da feature. Explique essa sobreposição e evite atribuir o uso exclusivamente a um produto, pois o produto era válido na consulta, não necessariamente durante o uso. Use uma linha separada para alunos sem produto identificado e outra para informação indisponível. Não some tipos de eventos diferentes nem os chame de sessões. Preserve os zeros observados. Se houver divergência entre `tentativas_com_atividade` e `tentativas_criadas`, informe-a nas observações.
- Em Code Interview, mostre tentativas, testes e submissões. Em System Design, mostre tentativas: a consulta atual não extrai testes nem submissões, e os zeros dessas colunas não comprovam ausência desses eventos. Nos Roleplays, mostre tentativas, turnos, finalizações solicitadas e transcrições; finalização solicitada não significa necessariamente conclusão.
- Em Code Interview e System Design, use `produtos_validos_no_momento_da_consulta` para os produtos associados ao aluno no momento da consulta, não necessariamente no momento do uso. Separe produtos apenas quando a concatenação permitir identificá-los com segurança; preserve códigos e nomes, sem deduzir plano, tipo de assinatura ou produto ausente. Se a separação for ambígua ou houver indício de truncamento, marque o agrupamento afetado como indisponível e solicite uma extração corrigida. Se o campo estiver vazio, informe que nenhum produto válido foi identificado pela consulta, sem concluir que o aluno não tem plano.
- Nos arquivos finais de Roleplay, leia `produtos_validos_no_momento_da_consulta` como uma lista JSON de produtos obtidos na consulta de usuários no Alura. Uma lista vazia significa que nenhum produto válido foi identificado por essa consulta; não conclua que o aluno não tem plano. Se a coluna estiver ausente ou a lista for inválida, informe `não disponível` e solicite a geração atualizada. Relações de produtos podem estar incompletas se houver indícios de truncamento ou separação ambígua nas demais fontes.
- Explique o escopo das consultas: os arquivos podem conter histórico acumulado; role e produtos refletem o momento de suas respectivas consultas. As contagens não identificam uso diário e não permitem deduzir outros tipos de atividade não extraídos.

## Entrega

- Inclua apenas tabelas agregadas por produto no relatório, sem identificadores individuais, nomes, e-mails ou outros dados pessoais.
- Na resposta final, informe o caminho do relatório e as limitações relevantes. Peça os dados faltantes necessários quando aplicável.
