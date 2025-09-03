import pandas as pd
import tensorflow as tf
import numpy as np

# ========= Configuration =========
# Google Cloud Storage (GCS) bucket and folder paths
GCS_BUCKET   = 'tutas-recommender-ml-project'   # Change this to your bucket name
DATA_PREFIX  = 'processed'                      # Directory for processed train/test CSV files
LOG_PREFIX   = 'logs/tutas-v1'                  # Directory for TensorBoard logs
MODEL_PREFIX = 'models/tutas-v1'                # Directory to save exported models
FROM_GCS     = True                             # Toggle: True = load from GCS, False = load local

def load_data():
    """
    Load training and testing data.

    If FROM_GCS = True:
        - Load CSV files directly from Google Cloud Storage.
    Else:
        - Load from local dataset folder (for debugging on laptop).

    Returns:
        X_train, X_test (features as float32)
        y_train, y_test (labels as float32 numpy arrays)
    """
    if FROM_GCS:
        base = f'gs://{GCS_BUCKET}/{DATA_PREFIX}'
        X_train = pd.read_csv(f'{base}/X_train.csv').astype('float32')
        X_test  = pd.read_csv(f'{base}/X_test.csv').astype('float32')
        y_train = pd.read_csv(f'{base}/y_train.csv').squeeze().astype(np.float32).values
        y_test  = pd.read_csv(f'{base}/y_test.csv').squeeze().astype(np.float32).values
    else:
        # Local fallback (debug mode)
        X_train = pd.read_csv('../dataset/processed/X_train.csv')
        X_test  = pd.read_csv('../dataset/processed/X_test.csv')
        y_train = pd.read_csv('../dataset/processed/y_train.csv').squeeze()
        y_test  = pd.read_csv('../dataset/processed/y_test.csv').squeeze()
    return X_train, X_test, y_train, y_test


def build_model(input_dim):
    """
    Build a simple feed-forward neural network using Keras.

    Architecture:
        - Dense(64, relu)   → hidden layer with 64 neurons
        - Dense(32, relu)   → hidden layer with 32 neurons
        - Dense(1, sigmoid) → output layer (binary classification)

    Args:
        input_dim (int): Number of features (columns) in training data.

    Returns:
        Compiled Keras Sequential model.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def main():
    """
    Main training pipeline:
        1. Load dataset (from GCS or local).
        2. Build Keras model.
        3. Train model with TensorBoard logging.
        4. Export trained model to GCS in SavedModel format.
    """
    # 1. Load train/test data
    X_train, X_test, y_train, y_test = load_data()

    # 2. Initialize model
    model = build_model(X_train.shape[1])

    # 3. Setup TensorBoard logging (saved to GCS)
    log_dir = f'gs://{GCS_BUCKET}/{LOG_PREFIX}'
    tb = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    # 4. Train model
    model.fit(X_train, y_train,
              validation_data=(X_test, y_test),
              epochs=10,
              callbacks=[tb])

    # 5. Export trained model to GCS in SavedModel format
    export_dir = f'gs://{GCS_BUCKET}/{MODEL_PREFIX}'
    model.export(export_dir)
    print(f"✅ SavedModel exported to {export_dir}")


if __name__ == "__main__":
    main()
