-- Check distribution of label (positive vs negative)
SELECT label, COUNT(*) AS jumlah
FROM `tutas_data.interaksi_data`
GROUP BY label
ORDER BY label;

-- Check distribution of feedback_score
SELECT feedback_score, COUNT(*) AS jumlah
FROM `tutas_data.interaksi_data`
GROUP BY feedback_score
ORDER BY feedback_score;

-- Validate label = 1 only when feedback_score >= 4
SELECT *
FROM `tutas_data.interaksi_data`
WHERE label = 1 AND feedback_score < 4;
