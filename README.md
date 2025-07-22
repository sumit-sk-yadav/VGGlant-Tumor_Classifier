# VGGlant - Kidney Tumor Classifier(POC)

This project focuses on developing a deep learning model for classifying kidney tumors in medical images using a customized VGG16-based architecture. It addresses challenges such as class imbalance, overfitting, and efficient training on large datasets.

## 🧠 Model Overview

- **Base Model:** VGG16 (pre-trained on ImageNet)
- **Custom Layers:** Added fully connected layers with dropout and L2 regularization to reduce overfitting.
- **Loss Function:** Weighted cross-entropy loss to manage class imbalance.
- **Optimizer:** Adam with learning rate scheduling for better convergence.
- **Regularization:** Dropout and L2 (ridge) regularization.
- **Data Augmentation:** Applied on-the-fly augmentation to enrich training data and improve generalization.

## ⚙️ Training Workflow

1. **Data Preparation:**
   - Applied image preprocessing and augmentation (e.g., rotation, scaling, flipping).
   - Handled class imbalance via weighted loss.

2. **Model Training:**
   - Used transfer learning from VGG16.
   - Fine-tuned top layers while freezing earlier layers initially.
   - Trained with adaptive learning rate scheduling.

3. **Experiment Tracking:**
   - Integrated `mlflow` for logging model parameters, metrics, and artifacts.
   - Versioned datasets to avoid redundant computation and maintain reproducibility.

## 📈 Performance & Evaluation

- Evaluated model on metrics such as accuracy, precision, recall, and F1-score.
- Visualized training curves and confusion matrix via `mlflow` UI.
