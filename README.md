# CSB_P2

Project 2 for CSB 320.

# CSB320 NLP Fake News Classification Experiment

## Project Overview

This project builds Natural Language Processing (NLP) classification pipelines using TF-IDF, sentiment analysis, and Random Forest machine learning models.

Two datasets were used:

1. Fake News Classification
2. Cyberbullying Tweet Classification

The purpose of the project is to explore how NLP techniques can classify different forms of harmful online content.

---

# Environment Setup

## Clone Repository

```bash
git clone <repository-link>
cd CSB320_NLP_Fake_News-
```

## Create Environment

```bash
conda env create -f requirements.yml
```

## Activate Environment

```bash
conda activate csb320-nlp
```

---

# Required Libraries

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* nltk
* textblob
* jupyter

---

# Running the Notebooks

Open Jupyter Notebook or VS Code and run:

* fake_news_analysis.ipynb
* cyberbullying_analysis.ipynb


---

# NLP Pipeline

Both notebooks follow this pipeline:

1. Data Loading and Exploration
2. Text Preprocessing
3. Train/Test Split
4. TF-IDF Feature Extraction
5. Sentiment Analysis using TextBlob
6. Feature Combination
7. Random Forest Training
8. Model Evaluation
9. Cross Validation

---

# Model Performance Summary

## Fake News Dataset

* Accuracy close to 99%
* Strong precision, recall, and F1-score
* TF-IDF worked very effectively due to structured language patterns

## Cyberbullying Dataset

* Accuracy around 85%
* Cyberbullying tweets were harder to classify correctly
* Social media slang and noisy text increased preprocessing difficulty

---

# YouTube Video

Add your unlisted YouTube link here:

(https://youtu.be/kMLW-S9Q-o4)

---

# AI Review

AI-generated feedback and reflection are included in:

 text
ai_review.md


