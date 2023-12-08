import inspect
import pprint
import os

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import joblib


# Load data
df = pd.read_csv("Machine Learning/realtor-data.csv")

# Display the first few rows of the dataframe
df.head()

# Explore unique values in the 'state' column
num_states = df["state"].nunique()
print("Number of different states:", num_states)

# Calculate and display statistics by state
state_stats = df.groupby("state")["price"].agg(["mean", "median", "min", "max"])
print(state_stats)

# Visualize mean prices by state
state_mean_price = df.groupby("state")["price"].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
state_mean_price.plot(kind="bar")
plt.xlabel("State")
plt.ylabel("Mean Price")
plt.title("Mean Price by State")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Data cleaning and preprocessing
df.describe()
df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Handle missing values
df["bed"].fillna(df["bed"].mode()[0], inplace=True)
df["bath"].fillna(df["bath"].mode()[0], inplace=True)
df["acre_lot"].fillna(df["acre_lot"].mode()[0], inplace=True)
df["house_size"].fillna(df["house_size"].mode()[0], inplace=True)
df = df.dropna(subset=["zip_code", "city"])
df = df.drop("prev_sold_date", axis=1)

# Display information about the dataframe
df.info()

# Visualize outliers before removal
column_num = ["bed", "bath", "acre_lot", "house_size", "price"]
fig = px.box(
    df[column_num],
    labels={"variable": "Column", "value": "Value"},
    title="Outlier Before Remove",
)
fig.update_xaxes(tickvals=[1, 2, 3, 4, 5], ticktext=column_num)
fig.show()
print(f"Total Rows with Outliers: {df.shape[0]}")

# Remove outliers based on IQR
Q1 = df[column_num].quantile(0.25)
Q3 = df[column_num].quantile(0.75)
IQR = Q3 - Q1
df = df[
    ~((df[column_num] < (Q1 - 1.5 * IQR)) | (df[column_num] > (Q3 + 1.5 * IQR))).any(
        axis=1
    )
]
print(IQR)

# Visualize outliers after removal
fig = px.box(
    df[column_num].melt(var_name="Column", value_name="Value"),
    x="Column",
    y="Value",
    title="Outlier After Remove",
)
fig.update_xaxes(tickvals=[1, 2, 3, 4, 5], ticktext=column_num)
fig.show()
print(f"Total Rows Without Outliers: {df.shape[0]}")

# Descriptive statistics and correlation analysis
summary_stats = df.describe()
print(summary_stats)

numeric_columns = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr()

# Visualize correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Explore categorical column 'state'
categorical_column = "state"
value_counts = df[categorical_column].value_counts(ascending=False)
print(value_counts)

# Feature engineering
df["price_per_sqft"] = df["price"] / df["house_size"]

# Analyze average price per square foot by state
price_per_sqft_by_state = df.groupby("state")["price_per_sqft"].mean()
print(price_per_sqft_by_state)

# Identify and handle outliers in 'price_per_sqft'
z_scores = (df["price_per_sqft"] - df["price_per_sqft"].mean()) / df[
    "price_per_sqft"
].std()
outlier_threshold = 3
outliers = df[z_scores.abs() > outlier_threshold]
df = df[z_scores.abs() <= outlier_threshold]

# Visualize average price per square foot by state
avg_price_per_sqft_by_state = (
    df.groupby("state")["price_per_sqft"].mean().sort_values(ascending=False)
)
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_price_per_sqft_by_state.index, y=avg_price_per_sqft_by_state.values)
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel("Average Price per Square Foot")
plt.title("Average Price per Square Foot by State")
plt.show()

# Visualize relationship between house size and price per square foot
plt.figure(figsize=(8, 6))
plt.scatter(df["house_size"], df["price_per_sqft"])
plt.xlabel("House Size")
plt.ylabel("Price per Square Foot")
plt.title("Price per Square Foot vs. House Size")
plt.show()

# Display final information about the dataframe
df.info()
