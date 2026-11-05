# Prompt: gerar relatório de resultados

Analise os cinco arquivos em `resultados/finais/`, que reúnem tentativas criadas e resultados disponíveis. Crie um novo relatório em `relatorios/`, preenchendo `modelo-relatorio.md`.

## Regra obrigatória de estrutura

- Use o modelo como estrutura literal e obrigatória: preserve o título, todos os títulos e subtítulos, a ordem das seções, os nomes dos campos e as colunas e linhas da tabela de visão geral.
- Substitua os textos entre colchetes por conteúdo. Não mantenha instruções de preenchimento como se fossem resultados.
- Não crie preâmbulo, seção, título, subtítulo, tabela ou campo fora do modelo; não renomeie, remova, reordene ou acrescente elementos estruturais. Coloque a data de referência e eventuais limitações nos campos existentes mais pertinentes, sem adicionar linhas de metadados. Não inclua nomes ou caminhos de arquivos, nem indicações de fonte no relatório.
- Preencha a linha `Data da extração` com a data atual no fuso `America/Sao_Paulo`.
- Preencha todas as seções do modelo. Se uma métrica ou conclusão não estiver disponível, escreva `não disponível` e explique brevemente o motivo no campo correspondente. Não deixe placeholders vazios.

## Nome e preservação de relatórios

- Salve em `relatorios/AAAA-MM-DD-NN.md`, usando a data atual no fuso `America/Sao_Paulo` e um contador por dia, começando em `01` (por exemplo, `2026-11-05-01.md`, depois `2026-11-05-02.md`). Considere os arquivos já existentes na pasta e use um contador maior que todos os já usados para essa data; não reutilize números de arquivos removidos se houver números maiores. Um relatório antigo `AAAA-MM-DD.md` deve ser preservado e não impede o uso de `01`. Após `99`, continue com `100`, `101` e assim por diante.
- Crie o arquivo em modo exclusivo (por exemplo, `open(caminho, "x", encoding="utf-8")` em Python), sem abrir um arquivo existente para escrita. Se outro processo criar o mesmo nome antes da gravação, recalcule o contador e tente novamente. Nunca sobrescreva relatórios.

## Verificação das fontes

- Antes de analisar, confira os cinco arquivos esperados: Code Interview, System Design e os três Roleplays filtrados com sufixo `-student`.
- Verifique também os identificadores de tentativa e o indicador `resultado_disponivel` em cada arquivo. Aceite os booleanos retornados pelo BI (`1`/`0`, `true`/`false` ou `t`/`f`, sem distinguir maiúsculas). Exportações antigas podem não conter o indicador e excluir tentativas sem resultado: nesse caso, não as use para estimar tentativas criadas; indique `não disponível` e peça uma nova extração. Valores ausentes ou inválidos impedem classificar o registro; explique a limitação e peça uma nova extração.
- Para cada arquivo, verifique se existe, pode ser lido e interpretado, contém cabeçalho e registros, e se os campos necessários estão preenchidos e válidos. Quando necessário, informe a indisponibilidade ou incompletude dos dados junto ao resultado afetado, sem citar nomes de arquivos.
- Um arquivo somente com cabeçalho significa que a consulta foi executada e retornou zero resultados no período e no escopo consultados. Registre que não houve resultados retornados nesse recorte. Isso não permite concluir que houve zero uso ou zero tentativas da feature fora do escopo consultado, nem que não existam resultados em outros períodos ou para usuários excluídos pelos filtros. Não confunda isso com arquivo ausente, vazio, ilegível ou consulta com falha.
- Se a fonte estiver ausente, ilegível ou incompleta a ponto de impedir uma conclusão, marque o resultado como indisponível, diga qual informação falta no relatório e peça essa informação na resposta final. Continue preenchendo o relatório com os dados válidos restantes.

## Análise e evidências

- Escreva para pessoas de produto, sem exigir conhecimento técnico: use frases curtas, linguagem direta e nomes compreensíveis. Apresente `passed` como “aprovada” e `not_passed` como “não aprovada”; explique outros valores sem inventar seus significados. Evite nomes de campos, códigos, detalhes de implementação e jargão. Explique o significado de cada número e use contagens e porcentagens com a base correspondente.

- Use exclusivamente os dados dos arquivos. Não invente nem infira resultados que as fontes não sustentem.
- Preencha a data da extração com a data atual em `America/Sao_Paulo`. Na tabela de visão geral, indique para cada feature o período efetivamente coberto pelos registros válidos, usando os timestamps da própria fonte. Se não houver registros ou datas válidas, use `—` e explique a limitação no resultado da feature.
- Considere limitações de escopo relevantes: as extrações podem conter todo o histórico e repetir registros entre dias; não trate totais como uso diário nem some extrações diferentes sem deduplicar. O filtro `STUDENT` reflete a role no momento da consulta ao Alura. As fontes cobrem resultados persistidos e não necessariamente todos os usuários que iniciaram cada feature.
- Para cada atividade, conte identificadores distintos de tentativa, incluindo registros sem resultado; em Roleplay considere também o tenant. Uma tentativa pode ter várias submissões ou avaliações: não conte linhas como tentativas. Confira identificadores ausentes ou inconsistentes e explique qualquer limitação. Apresente esse total ao lado da quantidade de resultados analisados. Em Code Interview, conte submissões com resultado por identificador distinto; nas demais, conte tentativas distintas com avaliação. Se System Design apresentar mais de uma avaliação para a mesma tentativa, não escolha uma arbitrariamente nem conte classificações duplicadas: sinalize a limitação e peça os dados necessários.
- Analise avaliações, decisões, pontuações e datas somente nas linhas com `resultado_disponivel` verdadeiro; linhas com valor falso representam tentativas sem resultado persistido e não são decisões ausentes. O período da tabela descreve somente os resultados. A criação de uma tentativa não garante conclusão ou avaliação. Se houver tentativas criadas e nenhum resultado retornado, deixe explícito que houve criação de tentativas, mas nenhuma avaliação foi retornada no recorte de resultados. Não calcule taxas de conclusão sem verificar a compatibilidade dos recortes e os identificadores.
- Para cada contagem, deixe clara a unidade: tentativas, submissões ou alunos distintos. Informe numeradores e denominadores de proporções. Para Roleplays, apresente todos os valores de decisão observados, incluindo quaisquer valores inesperados ou ausentes, e calcule as proporções sobre as tentativas com decisão disponível. Nunca use o total de linhas como denominador de decisão se algumas decisões estiverem ausentes.
- Use avaliações e recomendações estruturadas para fundamentar padrões, pontos fortes, dificuldades e recomendações. Identifique a métrica, o tamanho da base e o critério usado. Se analisar apenas uma amostra qualitativa, informe tamanho e critério de seleção; não generalize além dela. Diferencie pontuações médias de contagens e explique o denominador.
- Evite identificar alunos e reproduzir dados pessoais ou trechos de respostas. A decisão de um Roleplay descreve a avaliação daquela tentativa, não resultado de contratação.

## Entrega

- Salve o relatório no caminho definido acima, usando todas e somente as seções do modelo.
- Na resposta final, informe o caminho do arquivo criado e as principais limitações encontradas; peça os dados faltantes necessários quando aplicável.
