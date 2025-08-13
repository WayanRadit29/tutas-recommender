import pandas as pd
import tensorflow as tf

# 1️⃣ Load data dari folder processed
X_train = pd.read_csv('../data/dataset/processed/X_train.csv')
X_test = pd.read_csv('../data/dataset/processed/X_test.csv')
y_train = pd.read_csv('../data/dataset/processed/y_train.csv')
y_test = pd.read_csv('../data/dataset/processed/y_test.csv')

# 2️⃣ Build model sederhana
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3️⃣ Train model (singkat dulu untuk tes)
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)

# 4️⃣ Save model lokal (nanti kita ubah ke GCS)
model.save('./model')
print("✅ Model tersimpan di ./model")
