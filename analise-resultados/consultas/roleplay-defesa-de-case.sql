-- PostgreSQL — Gnarus AI: retorna resultados de todos os usuários do tenant configurado.
BEGIN READ ONLY;

SET LOCAL app.current_tenant_id = '96785b22-3302-4c34-ae92-b48425346811';

SELECT
    tenant_id,
    user_id,
    id AS attempt_id,
    status,
    started_at,
    completed_at,
    artifact #>> '{report,decision}' AS decision,
    replace(encode(convert_to((artifact -> 'recommendation')::text, 'UTF8'), 'base64'), E'\n', '') AS recommendation_base64,
    replace(encode(convert_to((artifact -> 'actionPlan')::text, 'UTF8'), 'base64'), E'\n', '') AS action_plan_base64,
    replace(encode(convert_to((artifact #> '{report,result}')::text, 'UTF8'), 'base64'), E'\n', '') AS result_base64,
    replace(encode(convert_to((artifact -> 'competencyReviews')::text, 'UTF8'), 'base64'), E'\n', '') AS competency_reviews_base64,
    replace(encode(convert_to((artifact #> '{report,improvementMap}')::text, 'UTF8'), 'base64'), E'\n', '') AS improvement_map_base64,
    replace(encode(convert_to((artifact #> '{report,nextSimulation}')::text, 'UTF8'), 'base64'), E'\n', '') AS next_simulation_base64
FROM gnarus_ai.roleplay_attempts AS attempt
WHERE attempt.tenant_id = '96785b22-3302-4c34-ae92-b48425346811'::uuid
  AND roleplay_type = 'case_interview'
  AND artifact IS NOT NULL
ORDER BY started_at DESC;
