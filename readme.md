# 🎯 Tutas Recommender – AI Tutor Matching System

This project builds a machine learning-based tutor-student recommendation system using synthetic data and Google Cloud Platform tools.

---

## 🚀 Project Goals
- Build an AI recommendation system to match tutors and students based on preferences and feedback
- Train ML models using synthetic data
- Implement an end-to-end ML workflow with BigQuery, SQL, and Vertex AI AutoML
- Serve as a personal portfolio to demonstrate ML & GCP proficiency

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
