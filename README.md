# Loan_Prediction


# software And Tools Requirements


1. [GithubAccount](https://github.com)
2. [vscodeIDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/install/)




# Loan Default Prediction Web Application 🚀
This project is an end-to-end machine learning solution designed to predict the likelihood of a customer defaulting on a loan. It features a high-performance predictive model integrated into a user-friendly Flask web interface.

📌 Project Overview
Financial institutions face significant risks when issuing loans. This project provides a data-driven approach to assess "default risk" by analyzing customer financial history and personal attributes. The model helps lenders make informed decisions to minimize potential losses.

🛠️ Key Features
End-to-End Pipeline: Data cleaning, exploratory data analysis (EDA), feature engineering, and model deployment.

Optimized Preprocessing: Uses Scikit-Learn ColumnTransformer for automated scaling and categorical encoding.

High Accuracy: Achieving 95% accuracy on test data using a fine-tuned XGBoost model.

Web Deployment: A functional UI built with Flask that allows users to input data and get real-time risk predictions.

💻 Tech Stack
Language: Python

Machine Learning: Scikit-Learn, XGBoost, Imbalanced-learn (SMOTE)

Web Framework: Flask, HTML, CSS

Tools: Jupyter Notebook, Git, Joblib

📊 Model Performance
Multiple classification algorithms were evaluated to find the best performer:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Support Vector Machine (SVM)

Champion Model: XGBoost Classifier (95% Accuracy)

🚀 How to Run the App Locally
Clone the Repository:

'''
git clone https://github.com/sandeep21122/Loan_Prediction.git
cd Loan_Prediction
'''
# Create a new Environment for python:
'''
python -m venv venv

source venv/Scripts/activate  # On Windows
'''

# creat a new environment for anaconda 
'''
conda create -p venv python==3.11 -y

conda activate venv/ #on windows
'''
# Install Dependencies:
'''
pip install -r requirements.txt
'''

# Launch the Flask App:
'''
python app.py
'''