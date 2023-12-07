from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('linear_regression_model.joblib')
preprocessor = joblib.load('preprocessor.joblib')

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        bed = float(request.form['bed'])
        bath = float(request.form['bath'])

        # Use the preprocessor only on the columns used in the model
        input_data = pd.DataFrame({'bed': [bed], 'bath': [bath]})
        predicted_price = model.predict(input_data)[0]

        return render_template('result.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
