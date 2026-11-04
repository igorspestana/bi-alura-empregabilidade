-- MySQL — Alura: execute no banco de cada tenant desejado.
SELECT
    a.user_id,
    a.id AS attempt_id,
    s.id AS submission_id,
    s.status,
    s.submittedAt,
    s.completedAt,
    s.executionEvaluationId,
    s.executionResponse
FROM UserCodeChallengeAttempt a
JOIN `User` u ON u.id = a.user_id AND u.role = 'STUDENT'
JOIN CodeChallengeSubmission s ON s.attempt_id = a.id
WHERE s.executionResponse IS NOT NULL
ORDER BY s.submittedAt DESC;
