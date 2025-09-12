import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# Path to the exported TensorFlow SavedModel
SAVEDMODEL_DIR = r"../models/tutas-v1"

# Load the trained model from disk
loaded = tf.saved_model.load(SAVEDMODEL_DIR)

# Access the default inference function from the model
infer = loaded.signatures["serving_default"]
print("Output keys:", list(infer.structured_outputs.keys()))

# Load the test dataset (features and labels)
X_test  = pd.read_csv('../../data/dataset/processed/X_test.csv')
y_test  = pd.read_csv('../../data/dataset/processed/y_test.csv').squeeze().astype(np.float32).values

# Run inference on the test set
out = infer(tf.constant(X_test.values, dtype=tf.float32))

# Extract the output probabilities from the model
out_key = list(out.keys())[0]
probs = out[out_key].numpy().ravel()

# Convert probabilities to binary predictions (threshold = 0.5)
pred = (probs >= 0.5).astype(np.int32)

# Calculate test accuracy
acc = (pred == y_test.astype(np.int32)).mean()
print(f"Test Accuracy: {acc:.4f}")

# Print confusion matrix for detailed error analysis
print(confusion_matrix(y_test, pred))
print()

# Print classification report (precision, recall, f1-score, support)
print(classification_report(y_test, pred))
