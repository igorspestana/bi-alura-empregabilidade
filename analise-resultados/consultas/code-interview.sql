-- MySQL: execute no banco de cada tenant desejado.
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
JOIN CodeChallengeSubmission s ON s.attempt_id = a.id
WHERE s.executionResponse IS NOT NULL
ORDER BY s.submittedAt DESC;
