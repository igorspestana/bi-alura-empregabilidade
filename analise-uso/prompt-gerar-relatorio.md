# Prompt: gerar relatório de uso

Analise os arquivos em `resultados/finais/` e crie um novo relatório em `relatorios/`, preenchendo `modelo-relatorio.md`.

## Regra obrigatória de estrutura

- Use o modelo como estrutura literal e obrigatória: preserve o título, todos os títulos e subtítulos, a ordem das seções, os nomes dos campos e as colunas e linhas da tabela de visão geral.
- Substitua os textos entre colchetes por conteúdo. Não mantenha instruções de preenchimento como se fossem resultados.
- Não crie preâmbulo, seção, título, subtítulo, tabela ou campo fora do modelo; não renomeie, remova, reordene ou acrescente elementos estruturais. Coloque a data de referência e eventuais limitações nos campos existentes mais pertinentes, sem adicionar linhas de metadados. Não inclua nomes ou caminhos de arquivos, nem indicações de fonte no relatório.
- Preencha `Data da extração` com a data atual no fuso `America/Sao_Paulo`.
- Preencha todas as seções do modelo. Se uma métrica ou conclusão não estiver disponível, escreva `não disponível` e explique brevemente o motivo no campo correspondente. Não deixe placeholders vazios.

## Nome e preservação de relatórios

- Use a data de hoje no fuso `America/Sao_Paulo` no nome `AAAA-MM-DD.md`.
- Se o nome já existir, crie outro com o próximo sufixo sequencial disponível, como `AAAA-MM-DD-02.md`. Nunca sobrescreva um relatório anterior.

## Verificação das fontes

- Antes de analisar, confira os cinco arquivos esperados: `resultados/finais/code-interview.tsv`, `resultados/finais/system-design.tsv` e `resultados/finais/roleplay-entrevista-comportamental-student.tsv`, `resultados/finais/roleplay-entrevista-tecnica-student.tsv` e `resultados/finais/roleplay-defesa-de-case-student.tsv`. Para cada arquivo, verifique se existe, pode ser lido e interpretado, contém cabeçalho e registros, e se os campos necessários para as métricas informadas estão preenchidos e válidos.
- Um arquivo somente com cabeçalho significa que a consulta foi executada e retornou zero linhas no período e no escopo consultados. Registre que não houve linhas retornadas nesse recorte. Isso não permite concluir que houve zero uso fora do escopo consultado, nem que não existam registros em outros períodos. Não confunda isso com arquivo ausente, vazio, ilegível ou consulta com falha.
- Se a fonte estiver ausente, ilegível ou incompleta a ponto de impedir uma conclusão, marque o resultado como indisponível, diga qual informação falta no relatório e peça essa informação na resposta final. Continue preenchendo o relatório com os dados válidos restantes.

## Análise e evidências

- Escreva para pessoas de produto: use frases curtas, linguagem direta e nomes compreensíveis. Explique o significado de cada métrica e deixe clara sua unidade, como usuários distintos, sessões, tentativas ou eventos, conforme os dados permitirem.
- Use exclusivamente os dados dos arquivos. Não invente nem infira resultados que as fontes não sustentem. Não presuma que linhas de arquivos diferentes possam ser somadas ou comparadas diretamente; verifique períodos, escopos, unidades e possíveis sobreposições.
- Na tabela de visão geral, indique para cada feature o período efetivamente coberto pelos registros válidos, usando as datas da própria fonte. Se não houver registros ou datas válidas, use `—` e explique a limitação no resultado da feature.
- Diferencie contagens de pessoas distintas de contagens de uso, e informe denominadores ao apresentar proporções. Não chame eventos ou tentativas de usuários. Evite identificar pessoas ou reproduzir dados pessoais.
- Considere as limitações de escopo e de definição das consultas. O conteúdo das consultas define quais eventos e usuários foram incluídos; não generalize para todo o uso da feature sem evidência.

## Entrega

- Salve o relatório no caminho definido acima, usando todas e somente as seções do modelo.
- Na resposta final, informe o caminho do arquivo criado e as principais limitações encontradas; peça os dados faltantes necessários quando aplicável.
