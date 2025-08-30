import tensorflow as tf
import numpy as np
import pandas as pd
import keras

model = tf.keras.models.load_model("../models/models/tutas-v1")

X_test = pd.read_csv("../dataset/processed/X_test.csv").astype("float32")
y_test  = pd.read_csv('../dataset/processed/y_test.csv').squeeze().astype(np.float32).values


loss, acc = model.evaluate(X_test, y_test, verbose=2)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {acc:.4f}")

