# 🎯 Tutas Recommender – AI Tutor Matching System

This project builds a machine learning-based tutor-student recommendation system using synthetic data and Google Cloud Platform tools.

---

## 🚀 Project Goals
- Build an AI recommendation system to match tutors and students based on preferences and feedback
- Train ML models using synthetic data
- Implement an end-to-end ML workflow with BigQuery, SQL, and Vertex AI AutoML
- Serve as a personal portfolio to demonstrate ML & GCP proficiency

---
## 📂 Project Structure

```plaintext
.
├── data/                           # Data generation & preprocessing
│   ├── dataset/
│   │   ├── unprocessed/             # Raw synthetic data (output of main.py)
│   │   │   ├── murid.csv
│   │   │   ├── tutor.csv
│   │   │   └── interaksi.csv
│   │   ├── processed 1/             # BigQuery engineered dataset
│   │   │   └── tutas_recommender_training_features.csv
│   │   └── processed 2/             # Preprocessed splits for ML model
│   │       ├── X_train.csv
│   │       ├── X_test.csv
│   │       ├── y_train.csv
│   │       └── y_test.csv
│   ├── config.py
│   ├── generators.py                # Synthetic data generators (student, tutor, interactions)
│   ├── main.py                      # Entry point to generate unprocessed data
│   ├── utils.py                     # Helper functions
│   └── readme.md                    # Detailed data processing documentation
│
├── docs/                            # Documentation & figures
│   ├── processing_data_in_BigQuery/ # SQL scripts & explanations
│   │   ├── bigquery_sql/
│   │   │   ├── 01_validate_distribution.sql
│   │   │   ├── 02_pernah_gagal_features.sql
│   │   │   ├── 03_training_features_join.sql
│   │   │   └── 04_insight_pairing_failures.sql
│   │   ├── pictures/                # Supporting figures
│   │   │   ├── create_bucket_and_upload_dataset.png
│   │   │   ├── create_table.png
│   │   │   ├── label_distribution.png
│   │   │   ├── feedback_score_distribution.png
│   │   │   ├── anomali_label_check.png
│   │   │   ├── create_pernah_gagal_features.png
│   │   │   └── make_tutas_training_dataset.png
│   │   └── readme.md
│   ├── training_model_in_VertexAI/
│   ├── deploying_model/
│   └── Inference_test_and_Evaluation/
│
├── scripts/
│   └── preprocess.ipynb
│
├── training/
│   └── train.py
│
├── outputs/
│   ├── evaluation/
│   │   └── evaluation.py
│   ├── logs/
│   └── models/
│       └── tutas-v1/
│           ├── saved_model.pb
│           └── variables/
│
├── requirements.txt
├── .gitignore
└── readme.md                        # Main project documentation

---

## 🧱 Tech Stack
- Python (for data generation)
- Google BigQuery (data warehousing & feature engineering)
- Vertex AI AutoML Tabular (model training)
- GitHub & Notion (documentation & presentation)
- Libraries: Faker, Pandas, Jupyter

---

## 📊 Dataset Overview

### 📁 Datasets
- `murid_data`: Student preferences, schedule, learning style
- `tutor_data`: Tutor expertise, ratings, schedule, experience
- `interaksi_data`: Match label, feedback score, joined feature set

### 🧠 Training Features
- `topik_match`, `gaya_match`, `metode_match`, `time_overlap`,  
  `murid_flexible`, `tutor_flexible`, `pernah_gagal`, `rating`, `total_jam_ngajar`

---

## 🔄 ML Workflow (on GCP)
1. Generate synthetic data using Python
2. Upload datasets to BigQuery
3. Feature engineering with SQL (`pernah_gagal`, join tutor info)
4. Train AutoML model using Vertex AI
5. Evaluate & (optionally) deploy the model

---

## 📈 Results & Evaluation
_(To be completed after AutoML training — include screenshots of metrics)_

---

## ✍️ Author
Wayan Raditya Putra – AI Engineering student at ITS  
This project was built as a personal branding portfolio to showcase GCP and ML skills.
