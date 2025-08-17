import pandas as pd
import tensorflow as tf
import numpy as np

# 1) Load data
X_train = pd.read_csv('../data/dataset/processed/X_train.csv')
X_test  = pd.read_csv('../data/dataset/processed/X_test.csv')
y_train = pd.read_csv('../data/dataset/processed/y_train.csv')
y_test  = pd.read_csv('../data/dataset/processed/y_test.csv')

# Pastikan y shape = (N,) dan float32
y_train = y_train.squeeze().astype(np.float32).values
y_test  = y_test.squeeze().astype(np.float32).values

# Pastikan X juga float32 (umumnya aman untuk Keras)
X_train = X_train.astype(np.float32)
X_test  = X_test.astype(np.float32)

# 2) Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3) Train singkat
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)

# 4a) Simpan lokal (format Keras baru)
model.save('./model.keras')          # ✅ artifact utk versi lokal
print("✅ Model (.keras) tersimpan di ./model.keras")

# 4b) Export SavedModel (untuk serving/Vertex AI)
# - ini menghasilkan direktori SavedModel (bukan file tunggal)
model.export('./saved_model')        # ✅ untuk TF Serving / Vertex
print("✅ SavedModel diexport ke ./saved_model")
