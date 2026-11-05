# Prompt: gerar relatório de uso

Analise os arquivos em `resultados/finais/` e crie um relatório em `relatorios/` usando `modelo-relatorio.md`. O objetivo é apresentar, para cada feature, a quantidade de alunos únicos, os produtos disponíveis para esses alunos e o uso de cada aluno.

## Estrutura e preservação

- Preserve o título, as seções, os subtítulos e as colunas das tabelas do modelo. Substitua os textos entre colchetes e acrescente às tabelas todas as linhas necessárias para os resultados; não limite a relação de alunos a uma amostra ou ranking.
- Preencha `Data do relatório` com a data atual no fuso `America/Sao_Paulo`. Essa data não comprova a data em que os dados foram extraídos.
- Salve em `relatorios/AAAA-MM-DD.md`, usando a data atual nesse fuso. Se o arquivo existir, use o próximo sufixo disponível, como `AAAA-MM-DD-02.md`; não sobrescreva relatórios.
- Use linguagem direta e informe as limitações na seção correspondente. Não invente valores. Quando uma informação estiver indisponível, escreva `não disponível` e explique o motivo.

## Verificação das fontes

- Confira `resultados/finais/code-interview.tsv`, `system-design.tsv`, `roleplay-entrevista-comportamental-student.tsv`, `roleplay-entrevista-tecnica-student.tsv` e `roleplay-defesa-de-case-student.tsv` no mesmo diretório. Verifique leitura, cabeçalho, separação das colunas, identificadores e contagens numéricas. Identifique IDs duplicados, campos obrigatórios ausentes ou inválidos e possíveis inconsistências antes de calcular métricas; não some linhas duplicadas sem entender sua origem. Registre a limitação e peça os dados corrigidos quando necessário.
- Arquivo somente com cabeçalho representa zero linhas retornadas no escopo consultado, desde que a execução tenha sido confirmada. Diferencie isso de arquivo ausente, vazio, ilegível ou consulta com falha. Se a fonte estiver incompleta, apresente os dados válidos que puder sustentar e marque as conclusões afetadas como indisponíveis.
- As consultas não fornecem datas dos eventos nem um período explícito nas exportações. Não trate a data do relatório como período de uso, não infira evolução temporal e indique o período como não disponível quando não houver evidência.

## Regras de análise

- Para cada feature, conte `user_id` distintos no respectivo arquivo final. Os Roleplays já foram filtrados pela role `STUDENT` no momento da consulta ao Alura. Não use `alunos_unicos_na_feature` dos Roleplays como total de alunos: ela foi calculada antes desse filtro. Os totais por feature não podem ser somados para obter pessoas distintas no conjunto, pois um aluno pode usar mais de uma feature.
- Liste cada aluno por `user_id` nas tabelas de detalhe e apresente suas `tentativas_criadas` como tentativas iniciadas, distinguindo-as dos demais eventos. Apresente também as contagens de eventos disponíveis para a feature; não some tentativas, testes, submissões, turnos, finalizações e transcrições como se fossem a mesma unidade ou sessões. Preserve os zeros observados. Se houver divergência entre `tentativas_com_atividade` e `tentativas_criadas`, informe-a nas observações em vez de presumir equivalência.
- Em Code Interview, mostre tentativas, testes e submissões. Em System Design, mostre tentativas: a consulta atual não extrai testes nem submissões, e os zeros dessas colunas não comprovam ausência desses eventos. Nos Roleplays, mostre tentativas, turnos, finalizações solicitadas e transcrições; finalização solicitada não significa necessariamente conclusão.
- Em Code Interview e System Design, use `produtos_validos_no_momento_da_consulta` para os produtos associados ao aluno no momento da consulta, não necessariamente no momento do uso. Preserve códigos e nomes disponíveis, sem deduzir plano, tipo de assinatura ou produto ausente. Se o campo estiver vazio, informe que nenhum produto válido foi identificado pela consulta, sem concluir que o aluno não tem plano.
- Nos arquivos finais de Roleplay, leia `produtos_validos_no_momento_da_consulta` como uma lista JSON de produtos obtidos na consulta de usuários no Alura. Uma lista vazia significa que nenhum produto válido foi identificado por essa consulta; não conclua que o aluno não tem plano. Se a coluna estiver ausente ou a lista for inválida, informe `não disponível` e solicite a geração atualizada. Relações de produtos podem estar incompletas se houver indícios de truncamento ou separação ambígua nas demais fontes.
- Explique o escopo das consultas: os arquivos podem conter histórico acumulado; role e produtos refletem o momento de suas respectivas consultas. As contagens não identificam uso diário e não permitem deduzir outros tipos de atividade não extraídos.

## Entrega

- Inclua as tabelas completas por aluno no relatório, usando apenas o identificador `user_id` e os dados solicitados; não acrescente nomes, e-mails ou outros dados pessoais.
- Na resposta final, informe o caminho do relatório e as limitações relevantes. Peça os dados faltantes necessários quando aplicável.
