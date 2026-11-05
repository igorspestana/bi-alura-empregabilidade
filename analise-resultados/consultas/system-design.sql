-- MySQL — Alura: execute no banco de cada tenant desejado.
SELECT
    a.user_id,
    a.id AS attempt_id,
    (s.result IS NOT NULL) AS resultado_disponivel,
    a.status AS attempt_status,
    a.overallClassification,
    a.evaluationSummary,
    a.submittedAt,
    a.completedAt,
    s.status AS evaluation_status,
    s.result AS detailed_result
FROM SystemDesignAttempt a
JOIN `User` u ON u.id = a.user_id AND u.role = 'STUDENT'
LEFT JOIN SystemDesignInterviewStep s
    ON s.attempt_id = a.id
   AND s.type = 'FINAL_EVALUATION'
   AND s.result IS NOT NULL
ORDER BY a.submittedAt DESC;
