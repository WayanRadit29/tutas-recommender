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

```

---

## 📚 Detailed Documentation

For a full walkthrough of **data preprocessing** and **feature engineering** (synthetic data → BigQuery → processed datasets), check the dedicated documentation here:

👉 [Data Processing & Feature Engineering](data/readme.md)
👉 [Training Model in Vertex AI](training/readme.md)
👉 [Deploying model in Vertex AI](outputs/Readme.md)
👉 [Inference and Evaluation of Model](outputs//evaluation/readme.md)

---

## 🧱 Tech Stack
- Python (for data generation)
- Google BigQuery (data warehousing & feature engineering)
- Vertex AI AutoML Tabular (model training)
- GitHub & Notion (documentation & presentation)
- Libraries: Faker, Pandas, Jupyter

---
## 🚀 Usage

Here’s the end-to-end workflow to run the **Tutas Recommender – AI Tutor Matching System**:

1. **📦 Generate Synthetic Data**
   ```bash
   python main.py
   ```

This creates raw synthetic datasets (`murid.csv`, `tutor.csv`, `interaksi.csv`) inside [`data/dataset/unprocessed/`](data/dataset/unprocessed/).

2. **🗄️ Data Processing & Feature Engineering**

   * Upload datasets to **Google BigQuery**.
   * Run SQL scripts to validate, join, and create features like `pernah_gagal`.
   * See detailed steps in:
     👉 [`data/readme.md`](data/readme.md)
     👉 [`docs/processing_data_in_BigQuery/readme.md`](docs/processing_data_in_BigQuery/readme.md)

3. **⚙️ Preprocessing for ML**

   * Split into train/test sets.
   * Outputs stored in [`data/dataset/processed 2/`](data/dataset/processed%202/).
     Example:

     ```
     X_train.csv | X_test.csv | y_train.csv | y_test.csv
     ```

4. **🤖 Train the Model (Vertex AI Workbench)**

   ```bash
   python training/train.py
   ```

   * Uses TensorFlow backend.
   * Logs and checkpoints saved in `outputs/logs/`.
   * Trained model exported to `models/tutas-v1/`.

5. **🌐 Deploy & Inference (Vertex AI)**

   * Deploy model to an endpoint via **Vertex AI**.
   * Test with JSON requests:

     ```json
     {
       "instances": [[1, 1, 1, 0, 1, 0, 0.771300, 0.672839, -1.018432, 0]]
     }
     ```
   * Deployment steps: 👉 [`docs/deploying_model/`](docs/deploying_model/)

6. **📈 Evaluate the Model**

   ```bash
   python outputs/evaluation/evaluation.py
   ```

   * Generates classification report & confusion matrix.
   * See details: 👉 [`docs/Inference_test_and_Evaluation/`](docs/Inference_test_and_Evaluation/)



---

## 🔄 ML Workflow (on GCP)
1. Generate synthetic data using Python
2. Upload datasets to BigQuery
3. Feature engineering with SQL (`pernah_gagal`, join tutor info)
4. Train AutoML model using Vertex AI
5. Evaluate & (optionally) deploy the model
---

## ✍️ Author
Wayan Raditya Putra – AI Engineering student at ITS  
This project was built as a personal branding portfolio to showcase GCP and ML skills.
