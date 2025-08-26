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
│   │   └── tutas_recommender_training_features.csv # This is the result from BigQuerry in Google Cloud Platform
│   │
│   └── processed/           # Preprocessed & split data for ML training
│       ├── X\_train.csv
│       ├── X\_test.csv
│       ├── y\_train.csv
│       └── y\_test.csv
│
├── config.py                # Global configuration (constants, parameters)
├── generators.py            # Functions to generate murid/student, tutor, and interaksi/interaction datasets
├── main.py                  # Main entry point for dataset generation
├── utils.py                 # Helper functions (faker init, random windows, weighted choice, overlap check)
└── readme.md                # Project documentation


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

### 2. Preprocess data for machine learning

Use the provided Jupyter notebook inside `scripts/` to clean and split the data:

```bash
scripts/preprocess.ipynb
```

This notebook takes the raw CSVs from `dataset/unprocessed/` and produces processed files in `dataset/processed/`:
* `X_train.csv`, `X_test.csv`
* `y_train.csv`, `y_test.csv`

---

📌 **Note**: The preprocessing step includes feature engineering and train/test splitting,
which prepares the data for ML model training.

