# Prompt: gerar relatório de resultados

Analise os arquivos disponíveis em `resultados/finais/`, usando `modelo-relatorio.md` como estrutura obrigatória, e crie um novo relatório em `relatorios/`.

Use a data de hoje no fuso `America/Sao_Paulo` no nome `AAAA-MM-DD.md`. Se o arquivo já existir, crie outro com um sufixo sequencial, como `AAAA-MM-DD-02.md`, sem sobrescrever relatórios anteriores.

Antes da análise, confira os cinco arquivos esperados: Code Interview, System Design e os três Roleplays filtrados com sufixo `-student`. Identifique arquivos ausentes, vazios, com somente cabeçalho, ilegíveis ou com dados incompletos. Um arquivo apenas com cabeçalho indica que não há linhas salvas, mas não comprova, por si só, que a consulta foi executada com sucesso. Registre essas limitações e solicite a informação necessária se ela impedir uma conclusão; não invente dados nem trate uma falha como zero resultados.

Use exclusivamente os dados disponíveis como evidência. Informe a data de referência, o escopo temporal efetivamente analisado, as fontes, os denominadores e a unidade de cada contagem (tentativas, submissões ou alunos distintos). Para os Roleplays, apresente os valores de decisão observados e suas proporções sobre as tentativas com decisão disponível. Use as avaliações e recomendações para identificar padrões, fundamentando as conclusões; se usar amostra qualitativa, informe seu tamanho e critério. Evite identificar alunos e reproduzir dados pessoais ou trechos de respostas sem necessidade.

As extrações podem conter todo o histórico disponível e repetir registros entre dias. Não apresente totais como uso diário e não some extrações de dias diferentes sem deduplicação. Compare períodos somente quando houver dados anteriores comparáveis e identifique as bases usadas; caso contrário, registre que a comparação não está disponível. O filtro STUDENT reflete a role no momento da consulta ao Alura. As extrações cobrem resultados persistidos e não representam necessariamente todos os usuários que iniciaram cada feature.

Preencha todas as seções aplicáveis do modelo; marque informações indisponíveis de forma explícita. Ao terminar, informe o caminho do relatório criado e as principais limitações encontradas.
