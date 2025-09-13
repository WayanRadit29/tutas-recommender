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

.
├── data/                           # Data generation & preprocessing
│   ├── dataset/
│   │   ├── unprocessed/             # Raw synthetic data (output of main.py)
│   │   │   ├── murid.csv
│   │   │   ├── tutor.csv
│   │   │   └── interaksi.csv
│   │   ├── processed 1/             # BigQuery engineered dataset
│   │   │   └── tutas\_recommender\_training\_features.csv
│   │   └── processed 2/             # Preprocessed splits for ML model
│   │       ├── X\_train.csv
│   │       ├── X\_test.csv
│   │       ├── y\_train.csv
│   │       └── y\_test.csv
│   ├── config.py
│   ├── generators.py                # Synthetic data generators (student, tutor, interactions)
│   ├── main.py                      # Entry point to generate unprocessed data
│   ├── utils.py                     # Helper functions
│   └── readme.md                    # Detailed data processing documentation
│
├── docs/                            # Documentation & figures
│   ├── processing\_data\_in\_BigQuery/ # SQL scripts & explanations
│   │   ├── bigquery\_sql/
│   │   │   ├── 01\_validate\_distribution.sql
│   │   │   ├── 02\_pernah\_gagal\_features.sql
│   │   │   ├── 03\_training\_features\_join.sql
│   │   │   └── 04\_insight\_pairing\_failures.sql
│   │   ├── pictures/                # Supporting figures
│   │   │   ├── create\_bucket\_and\_upload\_dataset.png
│   │   │   ├── create\_table.png
│   │   │   ├── label\_distribution.png
│   │   │   ├── feedback\_score\_distribution.png
│   │   │   ├── anomali\_label\_check.png
│   │   │   ├── create\_pernah\_gagal\_features.png
│   │   │   └── make\_tutas\_training\_dataset.png
│   │   └── readme.md
│   ├── training\_model\_in\_VertexAI/  # Vertex AI training setup & screenshots
│   ├── deploying\_model/             # Deployment process & screenshots
│   └── Inference\_test\_and\_Evaluation/ # Inference & evaluation figures
│
├── scripts/
│   └── preprocess.ipynb             # Notebook for scaling & splitting data
│
├── training/
│   └── train.py                     # Model training script (Keras/TensorFlow)
│
├── outputs/
│   ├── evaluation/                  # Evaluation scripts
│   │   └── evaluation.py
│   ├── logs/                        # TensorBoard logs
│   └── models/                      # Saved model checkpoints
│       └── tutas-v1/
│           ├── saved\_model.pb
│           └── variables/
│
├── requirements.txt                 # Python dependencies
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
