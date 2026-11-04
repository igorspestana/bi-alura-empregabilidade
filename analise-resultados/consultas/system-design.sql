-- MySQL: execute no banco de cada tenant desejado.
SELECT
    a.user_id,
    a.id AS attempt_id,
    a.status AS attempt_status,
    a.overallClassification,
    a.evaluationSummary,
    a.submittedAt,
    a.completedAt,
    s.status AS evaluation_status,
    s.result AS detailed_result
FROM SystemDesignAttempt a
JOIN SystemDesignInterviewStep s
    ON s.attempt_id = a.id
   AND s.type = 'FINAL_EVALUATION'
WHERE s.result IS NOT NULL
ORDER BY a.submittedAt DESC;
