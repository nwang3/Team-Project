# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# from sklearn.preprocessing import MinMaxScaler

# df = pd.read_csv("Machine Learning/realtor-data.csv")

# print(df.describe())

# sns.boxplot(df['price'])

# def outlier_treatment(datacolumn):
#     """function to Remove outlier"""
#     sorted(datacolumn)
#     Q1,Q3 = np.percentile(datacolumn,[40,60])
#     IQR = Q3-Q1
#     lower_range = Q1 - (1.5*IQR)
#     upper_range = Q3 + (1.5*IQR)
#     return lower_range,upper_range

# l,u = outlier_treatment(df['price'])
# l
# u
# df.drop(df[ (df['price'] > u) | (df['price'] < l)].index,inplace=True)

# df.shape

# sns.displot(df['price'],kind='kde')
# plt.title('Housing price distribution')
# plt.xlabel('Price')
# plt.ylabel('Count')
# plt.show()


# X = df.iloc[:,0:6].values
# y = df.iloc[:,6].values

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)
# print((X_train).shape)
# print((X_test).shape)
# print((y_train).shape)
# print((y_test).shape)


# mms = MinMaxScaler()
# X_train_scaled = mms.fit_transform(X_train)
# X_test_scaled = mms.fit_transform(X_test)


# sns.pairplot(df, vars=["bed", "bath", "acre_lot", "house_size", "price"])
# plt.show()


# correlation_matrix = df.corr()
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Correlation Matrix")
# plt.show()


# X = df[["bed", "bath", "acre_lot", "house_size"]]  
# y = df["price"]


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# model = LinearRegression()


# model.fit(X_train, y_train)


# y_pred = model.predict(X_test)


# mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error: {mse}")

# print("Coefficients:", model.coef_)
# print("Intercept:", model.intercept_)
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
df = pd.read_csv("Machine Learning/realtor-data.csv")

# Display the first few rows of the dataset
print(df.head())

# Check the unique states in the dataset
num_states = df['state'].nunique()
print("Number of different states:", num_states)

# Calculate and display mean, median, min, max prices by state
state_stats = df.groupby('state')['price'].agg(['mean', 'median', 'min', 'max'])
print(state_stats)

# Visualize mean prices by state using a bar plot
state_mean_price = df.groupby('state')['price'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
state_mean_price.plot(kind='bar')
plt.xlabel('State')
plt.ylabel('Mean Price')
plt.title('Mean Price by State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Display basic statistics of the dataset
print(df.describe())


duplicated_rows = df.duplicated().sum()
print(f"Number of duplicated rows: {duplicated_rows}")


df.drop_duplicates(inplace=True)


total_missing = df.isna().sum() * 100 / len(df)
print('Percentage Missing Value %')
print(total_missing)


df['bed'].fillna(df['bed'].mode()[0], inplace=True)
df['bath'].fillna(df['bath'].mode()[0], inplace=True)
df['acre_lot'].fillna(df['acre_lot'].mode()[0], inplace=True)
df['house_size'].fillna(df['house_size'].mode()[0], inplace=True)

df = df.dropna(subset=['zip_code', 'city'])

# Drop the 'prev_sold_date' column
df = df.drop('prev_sold_date', axis=1)

df.info()
