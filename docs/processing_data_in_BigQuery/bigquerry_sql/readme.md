# 📂 BigQuery SQL Documentation

This folder contains the main SQL logic used in the Tutas Recommender pipeline.

| File                          | Purpose                                      |
|-------------------------------|----------------------------------------------|
| 01_validate_distribution.sql  | Validates the distribution of labels & score |
| 02_pernah_gagal_features.sql | Adds historical failure flag per interaction |
| 03_training_features_join.sql | Combines interaction + tutor stats as ML features |
| 04_insight_pairing_failures.sql | Calculates insights for evaluation/reporting |

Each file is independently runnable in BigQuery.

