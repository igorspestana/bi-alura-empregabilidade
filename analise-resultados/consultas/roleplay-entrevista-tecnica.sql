-- PostgreSQL — Gnarus AI: retorna resultados de todos os usuários do tenant configurado.
BEGIN READ ONLY;

SET LOCAL app.current_tenant_id = '96785b22-3302-4c34-ae92-b48425346811';

SELECT
    tenant_id,
    user_id,
    id AS attempt_id,
    (artifact IS NOT NULL) AS resultado_disponivel,
    status,
    started_at,
    completed_at,
    artifact #>> '{report,decision}' AS decision,
    replace(encode(convert_to((artifact -> 'recommendation')::text, 'UTF8'), 'base64'), E'\n', '') AS recommendation_base64,
    replace(encode(convert_to((artifact -> 'actionPlan')::text, 'UTF8'), 'base64'), E'\n', '') AS action_plan_base64,
    replace(encode(convert_to((artifact #>> '{report,interviewSummary}')::text, 'UTF8'), 'base64'), E'\n', '') AS interview_summary_base64,
    replace(encode(convert_to((artifact #>> '{report,decisionReason}')::text, 'UTF8'), 'base64'), E'\n', '') AS decision_reason_base64,
    replace(encode(convert_to((artifact #> '{report,strengths}')::text, 'UTF8'), 'base64'), E'\n', '') AS strengths_base64,
    replace(encode(convert_to((artifact #> '{report,weaknesses}')::text, 'UTF8'), 'base64'), E'\n', '') AS weaknesses_base64,
    replace(encode(convert_to((artifact -> 'competencyAssessments')::text, 'UTF8'), 'base64'), E'\n', '') AS competency_assessments_base64,
    replace(encode(convert_to((artifact -> 'scoreAggregate')::text, 'UTF8'), 'base64'), E'\n', '') AS score_aggregate_base64
FROM gnarus_ai.roleplay_attempts AS attempt
WHERE attempt.tenant_id = '96785b22-3302-4c34-ae92-b48425346811'::uuid
  AND roleplay_type = 'technical_interview'
ORDER BY started_at DESC;
