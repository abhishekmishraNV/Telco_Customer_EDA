# Feature Scaling

#pip install -U scikit-learn

'''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Telco_customer_churn.csv')

df.info()

# Applying Standardization and Normalization

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

df.head()

print(df.head().to_string())

print(df.describe().round(2).to_string())

print(df.head().to_string())

new_df = pd.DataFrame(df,columns=['Tenure Months','Monthly Charges'])

print(new_df.head(5))

newest_df = pd.DataFrame(df,columns=['Churn Reason'])

print(newest_df.info())
nx_df = df[['Tenure Months']]
newest_df['Churn Reason'] = newest_df['Churn Reason'].fillna(newest_df['Churn Reason'].mode()[0])
print(newest_df.info())

scalar = MinMaxScaler()
normalized_df = scalar.fit_transform(nx_df)
print(normalized_df)

print("-------------------------------------------------")

x = np.array([[1],[2],[3],[4],[5]])
scalar = MinMaxScaler()
normalized_x = scalar.fit_transform(x)
print(normalized_x)

Y = np.array([[1],[2],[3],[4],[5]])
scaler = StandardScaler()
Standarized_Y = scaler.fit_transform(Y)
print(Standarized_Y)'''