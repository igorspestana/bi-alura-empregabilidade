WITH eventos AS (
    SELECT
        user_id,
        id AS tentativa_id,
        'TENTATIVA_CRIADA' AS tipo
    FROM UserCodeChallengeAttempt

    UNION ALL

    SELECT
        a.user_id,
        a.id AS tentativa_id,
        'TESTE' AS tipo
    FROM CodeChallengeTestRun t
    JOIN UserCodeChallengeAttempt a ON a.id = t.attempt_id

    UNION ALL

    SELECT
        a.user_id,
        a.id AS tentativa_id,
        'SUBMISSAO' AS tipo
    FROM CodeChallengeSubmission s
    JOIN UserCodeChallengeAttempt a ON a.id = s.attempt_id
),
usos AS (
    SELECT
        user_id,
        COUNT(DISTINCT tentativa_id) AS tentativas_com_atividade,
        SUM(tipo = 'TENTATIVA_CRIADA') AS tentativas_criadas,
        SUM(tipo = 'TESTE') AS testes,
        SUM(tipo = 'SUBMISSAO') AS submissoes
    FROM eventos
    GROUP BY user_id
)
SELECT
    u.user_id,
    u.tentativas_com_atividade,
    u.tentativas_criadas,
    u.testes,
    u.submissoes,
    COUNT(*) OVER () AS alunos_unicos_na_feature,
    (
        SELECT GROUP_CONCAT(
            DISTINCT CONCAT(p.code, ' — ', p.name)
            ORDER BY p.code
            SEPARATOR ', '
        )
        FROM Acquirement a
        JOIN Product p ON p.id = a.product_id
        LEFT JOIN BMPayment pagamento ON pagamento.id = a.payment_id
        WHERE a.user_id = u.user_id
          AND a.status IN ('FREE', 'PAID')
          AND p.status = 'ENABLED'
          AND a.startsAt <= NOW()
          AND a.expirationDate >= CURRENT_DATE()
          AND (pagamento.id IS NULL OR pagamento.status <> 'REIMBURSED')
    ) AS produtos_validos_no_momento_da_consulta
FROM usos u
JOIN `User` usuario ON usuario.id = u.user_id
WHERE usuario.role = 'STUDENT'
ORDER BY u.user_id;
