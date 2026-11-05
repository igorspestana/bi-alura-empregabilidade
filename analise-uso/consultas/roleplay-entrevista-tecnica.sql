-- PostgreSQL — Gnarus AI: execute no tenant configurado.
BEGIN READ ONLY;

SET LOCAL app.current_tenant_id = '96785b22-3302-4c34-ae92-b48425346811';

WITH contexto AS MATERIALIZED (
    SELECT current_setting('app.current_tenant_id') AS tenant_id
),
eventos AS MATERIALIZED (
    SELECT
        r.tenant_id,
        r.user_id,
        r.id AS tentativa_id,
        'tentativa_criada' AS tipo
    FROM contexto
    JOIN gnarus_ai.roleplay_attempts r
      ON r.tenant_id = contexto.tenant_id::uuid
    WHERE r.roleplay_type = 'technical_interview'

    UNION ALL

    SELECT
        r.tenant_id,
        r.user_id,
        r.id AS tentativa_id,
        o.operation_type AS tipo
    FROM contexto
    JOIN gnarus_ai.roleplay_attempt_operations o
      ON o.tenant_id = contexto.tenant_id::uuid
    JOIN gnarus_ai.roleplay_attempts r
      ON r.tenant_id = o.tenant_id
     AND r.id = o.attempt_id
     AND r.user_id = o.user_id
    WHERE r.roleplay_type = 'technical_interview'
      AND o.operation_type IN ('turn', 'finish', 'audio_transcription')
)
SELECT
    user_id,
    COUNT(*) OVER (PARTITION BY tenant_id) AS alunos_unicos_na_feature,
    COUNT(DISTINCT tentativa_id) AS tentativas_com_atividade,
    COUNT(*) FILTER (WHERE tipo = 'tentativa_criada') AS tentativas_criadas,
    COUNT(*) FILTER (WHERE tipo = 'turn') AS turnos,
    COUNT(*) FILTER (WHERE tipo = 'finish') AS finalizacoes_solicitadas,
    COUNT(*) FILTER (WHERE tipo = 'audio_transcription') AS transcricoes
FROM eventos
GROUP BY tenant_id, user_id
ORDER BY user_id;
