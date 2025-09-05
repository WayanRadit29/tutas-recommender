-- Join tutor metadata to include rating and teaching hours
WITH gagal AS (
  SELECT id_murid, id_tutor
  FROM `tutas_data.interaksi_data`
  WHERE feedback_score < 4
)

SELECT
  i.*,
  t.rating,
  t.total_jam_ngajar,
  IF(g.id_murid IS NOT NULL, TRUE, FALSE) AS pernah_gagal
FROM `tutas_data.interaksi_data` i
LEFT JOIN `tutas_data.tutor_data` t
  ON i.id_tutor = t.id_tutor
LEFT JOIN gagal g
  ON i.id_murid = g.id_murid AND i.id_tutor = g.id_tutor;
