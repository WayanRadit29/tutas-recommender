-- Identify past failed pairs (feedback < 4)
WITH gagal AS (
  SELECT id_murid, id_tutor
  FROM `tutas_data.interaksi_data`
  WHERE feedback_score < 4
)

-- Join with main data to add 'pernah_gagal' flag
SELECT
  i.*,
  IF(g.id_murid IS NOT NULL, TRUE, FALSE) AS pernah_gagal
FROM
  `tutas_data.interaksi_data` i
LEFT JOIN
  gagal g
ON i.id_murid = g.id_murid AND i.id_tutor = g.id_tutor;
