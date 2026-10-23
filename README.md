# AI-Based Diabetes Prediction System

## Project Overview

An end-to-end machine learning project that explores
health survey data and predicts diabetes classification
using a trained classification model.

The project includes exploratory data analysis,
data preprocessing, machine learning, model evaluation,
and an interactive Streamlit web application.

**Disclaimer:** This is an educational machine learning
project. It is not a medical diagnostic tool.

## Dataset

Source: Diabetes Health Indicators Dataset
(BRFSS 2015)

The dataset contains survey-based health indicators
including:

- High blood pressure
- High cholesterol
- BMI
- Smoking history
- Physical activity
- General health
- Age category
- Education and income

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Joblib

## Project Workflow

1. Dataset loading and exploration
2. Data cleaning and preprocessing
3. Exploratory data analysis (EDA)
4. Feature and target selection
5. Training and testing split
6. Machine learning model training
7. Model performance evaluation
8. Saving the trained model
9. Building the Streamlit application

## Model Evaluation

The notebook evaluates classification performance
using metrics and visualizations.

Actual performance scores should be taken from
the executed Jupyter Notebook.

## Streamlit Application

The application allows users to:

- Enter health-related information
- Select categorical health indicators
- Generate a model classification
- View the estimated probability for class 1

The displayed probability is a model output,
not a clinically validated diabetes risk score.

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app.py
```

## Project Limitations

- Uses historical BRFSS 2015 survey data
- Model predictions may contain errors
- Survey data may contain reporting bias
- The model has not been clinically validated
- Predictions must not replace medical advice

## Future Improvements

- Compare additional classification algorithms
- Improve probability calibration
- Add explainable AI visualizations
- Improve the Streamlit interface
- Deploy the application online

## Author

Ditya Gupta

Interested in Data Analytics, Python,
Machine Learning, and Data Visualization.
