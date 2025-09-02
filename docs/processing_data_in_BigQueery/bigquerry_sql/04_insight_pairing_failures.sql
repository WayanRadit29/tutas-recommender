-- Calculate how many historical pairings failed
SELECT
  COUNT(*) AS total_interaksi,
  COUNTIF(pernah_gagal) AS jumlah_gagal,
  ROUND(COUNTIF(pernah_gagal)/COUNT(*) * 100, 2) AS persen_gagal
FROM `tutas_data.training_features`;
