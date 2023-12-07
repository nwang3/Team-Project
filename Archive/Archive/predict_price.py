import joblib
import pandas as pd

loaded_preprocessor = joblib.load('preprocessor.joblib')
loaded_model = joblib.load('linear_regression_model.joblib')

status = input("Enter the status (e.g., 'For Sale', 'Sold'): ")
bed = int(input("Enter the number of bedrooms: "))
bath = int(input("Enter the number of bathrooms: "))
acre_lot = float(input("Enter the acre lot size: "))
city = input("Enter the city: ")
state = input("Enter the state: ")
zip_code = int(input("Enter the ZIP code: "))
house_size = int(input("Enter the house size: "))

input_data = pd.DataFrame({
    'status': [status],
    'bed': [bed],
    'bath': [bath],
    'acre_lot': [acre_lot],
    'city': [city],
    'state': [state],
    'zip_code': [zip_code],
    'house_size': [house_size]
})

input_data_encoded = loaded_preprocessor.transform(input_data)
predicted_price = loaded_model.predict(input_data_encoded)
print(f"\nPredicted Price: ${predicted_price[0]:,.2f}")