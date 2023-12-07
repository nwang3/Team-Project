# import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# load the dataset
df = pd.read_csv('Machine Learning/realtor-data.csv')

# select relevant features and target
features = ['zip_code', 'bed', 'bath', 'acre_lot', 'house_size']
target = 'price'

# handle missing values
df = df[features + [target]].dropna()

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# save the model to a file using pickle
with open('machine_learning_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)


