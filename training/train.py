import pandas as pd
import tensorflow as tf
import numpy as np

# ========= Konfigurasi =========
GCS_BUCKET = 'tutas-recommender-ml-project'   #cukup ini, sesuai bucket kamu
DATA_PREFIX = 'processed'             #revisi: langsung "processed"
LOG_PREFIX  = 'logs/tutas-v1'
MODEL_PREFIX= 'models/tutas-v1'
FROM_GCS = True

def load_data():
    if FROM_GCS:
        base = f'gs://{GCS_BUCKET}/{DATA_PREFIX}'
        X_train = pd.read_csv(f'{base}/X_train.csv').astype('float32')
        X_test  = pd.read_csv(f'{base}/X_test.csv').astype('float32')
        y_train = pd.read_csv(f'{base}/y_train.csv').squeeze().astype(np.float32).values
        y_test  = pd.read_csv(f'{base}/y_test.csv').squeeze().astype(np.float32).values
    else:
        # fallback lokal (kalau debug di laptop)
        X_train = pd.read_csv('../dataset/processed/X_train.csv')
        X_test  = pd.read_csv('../dataset/processed/X_test.csv')
        y_train = pd.read_csv('../dataset/processed/y_train.csv').squeeze()
        y_test  = pd.read_csv('../dataset/processed/y_test.csv').squeeze()
    return X_train, X_test, y_train, y_test

def build_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def main():
    X_train, X_test, y_train, y_test = load_data()
    model = build_model(X_train.shape[1])

    log_dir = f'gs://{GCS_BUCKET}/{LOG_PREFIX}'
    tb = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    model.fit(X_train, y_train,
              validation_data=(X_test, y_test),
              epochs=10,
              callbacks=[tb])

    export_dir = f'gs://{GCS_BUCKET}/{MODEL_PREFIX}'
    model.export(export_dir)
    print(f"✅ SavedModel exported to {export_dir}")

if __name__ == "__main__":
    main()

