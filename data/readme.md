# Tutas Recommender – Synthetic Data Generator

This repository provides a pipeline for generating **synthetic datasets** to train and evaluate a recommender system.  
It creates student profiles, tutor profiles, and labeled interactions, which can be used to prototype and test machine learning models.  
All data is **synthetic** (using Faker + custom logic) and safe for demonstration or educational purposes.

---

## 📂 Project Structure

```
.
├── dataset/
│   ├── unprocessed/         # Raw synthetic data (direct output of main.py)
│   │   ├── murid.csv
│   │   ├── tutor.csv
│   │   ├── interaksi.csv
│   │
│   ├── processed_1/         # Processed dataset from BigQuery (feature-engineered)
│   │   └── tutas_recommender_training_features.csv
│   │
│   └── processed_2/         # Processed dataset from scripts/preprocess.ipynb (train/test split)
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── config.py                # Global configuration (constants, parameters)
├── generators.py            # Functions to generate murid/student, tutor, and interaksi/interaction datasets
├── main.py                  # Main entry point for dataset generation
├── utils.py                 # Helper functions (faker init, random windows, weighted choice, overlap check)
└── readme.md                # Project documentation

```

## 🚀 Usage

### 1. Generate raw synthetic data

Run the main script to create student, tutor, and interaction datasets:
```bash
python main.py
```

The output files will be saved in `dataset/unprocessed/`:

* `murid.csv`
* `tutor.csv`
* `interaksi.csv`
---

### 2. Process data with BigQuery

Upload the raw CSVs from `dataset/unprocessed/` into **Google Cloud BigQuery**.  
Use SQL queries to perform **feature engineering and data transformation**, combining the student, tutor, and interaction datasets into a single training-ready table.

Output:
* `tutas_recommender_training_features.csv` → stored under `dataset/processed_1/`

#### Step 2.1 – Create Bucket and Upload Dataset

Before running any SQL in BigQuery, the raw CSV files need to be stored in **Google Cloud Storage (GCS)**.  
This step creates a dedicated bucket (e.g., `tutas-recommender-bucket`) and uploads the three datasets generated in Step 1:

- `murid.csv` → student profiles  
- `tutor.csv` → tutor profiles  
- `interaksi.csv` → interaction records  

Once uploaded, these files serve as the **source data** that will be imported into BigQuery tables for transformation and feature engineering.

![Create Bucket and Upload Dataset](../docs/processing_data_in_BigQuery/pictures/create_bucket_and_upload_dataset.png)

#### Step 2.2 – Create Tables in BigQuery

After uploading the raw CSV files into **Google Cloud Storage**, the next step is to create tables in **BigQuery**.  
Each CSV file (`murid.csv`, `tutor.csv`, `interaksi.csv`) is imported as a separate BigQuery table inside a dataset (e.g., `tutas_data`).

In this step:
- **Source**: Select *Google Cloud Storage* as the input, and point to the CSV file path (e.g., `tutas-recommender-project/murid.csv`).  
- **Destination**: Define the target project, dataset, and table name inside BigQuery.  
- **Schema**: BigQuery automatically detects schema from the CSV file, but can also be manually adjusted if needed.  

This process is repeated for each dataset to ensure that all raw data is accessible in BigQuery for SQL queries and feature engineering.

![Create Table](../docs/processing_data_in_BigQuery/pictures/create_table.png)

#### Step 2.3 – Run SQL Queries for Feature Engineering

Feature engineering in BigQuery is performed through a series of SQL queries.  
Each query transforms or enriches the raw data into features that will be used for training the recommender model.


### 3. Preprocess data for machine learning

Use the provided Jupyter notebook inside `scripts/` to clean and split the data:

scripts/preprocess.ipynb


This notebook takes the raw CSVs from `dataset/unprocessed/` and produces processed files in `dataset/processed/`:
* `X_train.csv`, `X_test.csv`
* `y_train.csv`, `y_test.csv`

---

📌 **Note**: The preprocessing step includes feature engineering and train/test splitting,
which prepares the data for ML model training.

