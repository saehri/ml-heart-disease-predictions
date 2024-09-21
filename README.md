# Heart Disease Prediction Using Machine Learning

This project aims to predict the likelihood of heart disease in individuals using Decision Tree algoritm. The model is trained on a dataset of patient medical records, with features such as age, cholesterol level, and blood pressure, among others. The project is a part of my university coursework, demonstrating the use of machine learning in healthcare predictions.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Performance](#performance)
- [Usage](#usage)

## Introduction

Heart disease is one of the leading causes of death worldwide. Early prediction and diagnosis can help in preventing fatal outcomes. In this project, we build a machine learning model using a decision tree algorithm to predict the presence of heart disease based on medical data. The goal is to provide an accurate and interpretable prediction model to assist in the early diagnosis of heart conditions.

## Dataset

The dataset used in this project comes from the UCI Machine Learning Repository. It contains medical information about patients, including:

- Age
- Sex
- Chest pain type
- Resting blood pressure
- Serum cholesterol
- Fasting blood sugar
- Resting electrocardiographic results
- Maximum heart rate achieved
- Exercise-induced angina
- ST depression induced by exercise
- Slope of the peak exercise ST segment
- Number of major vessels (0-3) colored by fluoroscopy
- Thalassemia

## Project Structure

```plaintext
ml-heart-disease-prediction/
│
├── data/
│   └── heart.csv                # The heart disease
notebooks/
│   └── app.ipynb # Jupyter Notebook for exploratory data analysis and model training
model/
│   └── decision_tree_model.joblib   # Trained decision tree model
├── README.md
└── requirements.txt              # Python dependencies
```

## Features

- **Exploratory data analysis**: Univariative and Bivariative data analysis
- **Preprocessing**: Missing data imputation, feature scaling, and encoding categorical variables.
- **Modeling**: Decision Tree Classifier used for building the prediction model.
- **Evaluation**: Accuracy, precision, recall, and F1 score were used to evaluate the model's performance.

## Model Architecture

The model uses a Decision Tree to classify the presence of heart disease based on the 13 input features. The decision tree algorithm was chosen due to its interpretability and ease of use in healthcare-related applications.

## Performance

- **Macro Average Precision**: 0.81
- **Macro Average Recall**: 0.79
- **Macro Average F1 Score**: 0.78
- **Accuracy**: 0.79

These metrics demonstrate that the model is effective in predicting heart disease, though further tuning and experimentation could improve performance.

## Installation

To run this project locally, follow these steps:

1. Clone the repository

```
git clone https://github.com/saehri/ml-heart-disease-predictions.git

cd ml-heart-diseasie-predictions
```

2. Create and activate a virtual environment:

```
python -m venv env

source env/bin/activate   # On Windows: `env\Scripts\activate`
```

3. Install the required dependencies

```
pip install -r requirements.txt
```

4. Go to notebooks/app.py and run the cells

## Usage

- Ensure all dependencies are installed.
- Load the dataset and run the notebook or script.
- Modify the code as needed for further experimentation, such as changing the model or tuning hyperparameters.
- Evaluate the model's performance on the test data.
