
---

# 📊 Model Evaluation & Inference

This section documents how the trained Tutas Recommender model was evaluated and tested after deployment.
--- 

## ⚡ Inference Test on Deployed Model
We first perform an online inference test directly on the deployed endpoint in **Vertex AI** using a JSON request.

```json
{
  "instances": [
    [1, 1, 1, 0, 1, 0, 0.771300, 0.672839, -1.018432, 0]
  ]
}
```

The model returns a prediction probability close to **1.0**, indicating a high likelihood of a successful tutor–student match.
![Inference Test](../docs/Inference_test_and_Evaluation/inference_test_in_model.png)
---

## 📈 Classification Report & Metrics

We then run the evaluation script locally (`evaluation.py`) to compute accuracy, precision, recall, and F1-score on the test set.

```bash
python outputs/evaluation/evaluation.py
```

Results:

* **Accuracy:** 100%
* **Precision, Recall, F1-score:** Perfect across both classes (0 and 1)
* **Confusion Matrix:**

  ```
  [[112   0]
   [  0 291]]
  ```

This shows that the model correctly classified all test samples without error.

![Model Evaluation](../docs/Inference_test_and_Evaluation/model_evaluation.png)

---

## ✅ Summary

* The model achieved **perfect accuracy** on the test dataset.
* Both online inference (Vertex AI endpoint) and offline evaluation (confusion matrix & classification report) confirm that the model generalizes well.
* Next step: monitor in production with real-world data to validate robustness.


