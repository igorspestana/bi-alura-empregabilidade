-- PostgreSQL: retorna resultados de todos os tenants acessíveis.
SELECT
    tenant_id,
    user_id,
    id AS attempt_id,
    status,
    started_at,
    completed_at,
    artifact AS report
FROM roleplay_attempts
WHERE roleplay_type = 'technical_interview'
  AND artifact IS NOT NULL
ORDER BY started_at DESC;
