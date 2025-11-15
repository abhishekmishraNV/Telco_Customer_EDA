'''#Handling Missing Values

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Telco_customer_churn.csv')

df.info()

print(df.isnull().sum())

updated_df = df.dropna(axis = 1)  # Deleting the column with a missing values

updated_df.info()

updated_df = df.dropna(axis=0) #Deleting the rows with a missing values

updated_df.info() #None of the process of deletion is good (...test case)...(little bit preferable)

print("----------------------------------------------------------------------")

#Imputation

print(df['Tenure Months'].median())

print(df['Longitude'].mean())

print(df['Churn Reason'].value_counts())
print(df['Churn Reason'].mode())


#Fillna : It fills the null value
#Dropna : It removes the null value

df1 = df.copy()
mode_value = df['Churn Reason'].mode()[0]
df1['Churn Reason'] = df['Churn Reason'].fillna(mode_value)

df1.info() #Median > Mean(if there is a large number of outliers)

#Forward And Backward Filling : Imputation

df = pd.read_csv('Telco_customer_churn.csv')

df.info()

df1 = df
df1['Churn Reason'] = df['Churn Reason'].bfill() # Backward Fill
df1.info()

df1 = df.copy()
df1['Churn Reason'] = df['Churn Reason'].ffill()
df1.info()'''