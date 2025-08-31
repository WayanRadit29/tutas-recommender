import tensorflow as tf
import pandas as pd
import numpy as np

SAVEDMODEL_DIR = r"../models/tutas-v1"
loaded = tf.saved_model.load(SAVEDMODEL_DIR)

infer = loaded.signatures["serving_default"]
print("Output keys:", list(infer.structured_outputs.keys()))

X_test  = pd.read_csv('../../data/dataset/processed/X_test.csv')
y_test  = pd.read_csv('../../data/dataset/processed/y_test.csv').squeeze().astype(np.float32).values

out = infer(tf.constant(X_test.values, dtype=tf.float32))

out_key = list(out.keys())[0]
probs = out[out_key].numpy().ravel()

pred = (probs >= 0.5).astype(np.int32)
acc = (pred == y_test.astype(np.int32)).mean()

print(f"Test Accuracy: {acc:.4f}")
print(f"Example probs[:5]: {probs[:5]}")



