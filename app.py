from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the verified pipeline (preprocessor + selector + model)
model_pipeline = joblib.load('final_loan_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect base inputs from the form
        signup_date = f"{request.form['signup_year']}-01-01"
        
        # Create a dictionary including the exact columns the pipeline is demanding
        input_data = {
            # Standard features
            'income': [float(request.form['income'])],
            'debt_to_income': [float(request.form['debt_to_income'])],
            'savings': [float(request.form['savings'])],
            'credit_score': [float(request.form['credit_score'])],
            'age': [float(request.form['age'])],
            'employment_years': [float(request.form['employment_years'])],
            'has_credit_card': [int(request.form['has_credit_card'])],
            'home_ownership': [request.form['home_ownership']],
            'education': [request.form['education']],
            'signup_date': [signup_date],
            
            # Engineered features identified in your traceback
            # We provide neutral/placeholder values as the 'selector' will likely bypass them
            'signup_year': [int(request.form['signup_year'])],
            'signup_month': [1],
            'day': [1],
            'signup_dayofweek': [0],
            'sin_age': [0.0],  # Placeholder for the sine transformation of age
            
            # Other features required by the initial ColumnTransformer
            'marital_status': ["Single"], 
            'region': ["North"],
            'monthly_expenses': [0.0],
            'loan_amount': [0.0],
            'loan_term_months': [0],
            'recent_default': [0],
            'num_dependents': [0]
        }
        
        df_input = pd.DataFrame(input_data)
        
        # Make the prediction
        prediction = model_pipeline.predict(df_input)[0]
        probability = model_pipeline.predict_proba(df_input)[0][1]
        
        result = "High Risk" if prediction == 1 else "Low Risk"
        return render_template('index.html', 
                               prediction_text=f'Decision: {result}',
                               prob_text=f'Default Probability: {probability:.2%}')
if __name__ == "__main__":
    app.run(debug=True)