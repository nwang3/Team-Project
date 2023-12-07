import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("Machine Learning/realtor-data.csv")

df.shape
df.head()
df.describe()
df.info()

df.isnull().sum()

df.drop(columns=['prev_sold_date', 'zip_code', 'acre_lot'], inplace=True)

df['bed'].fillna(df['bed'].median(), inplace=True)
df['bath'].fillna(df['bath'].median(), inplace=True)
df['house_size'].fillna(df['house_size'].median(), inplace=True)
df['city'].fillna(df['city'].mode()[0], inplace=True)

df = pd.get_dummies(df, columns=['status', 'city', 'state'], drop_first=True)

df.isnull().sum()

sns.heatmap(df.corr(), annot=True)

