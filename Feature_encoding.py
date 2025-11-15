import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv('Telco_customer_churn.csv')

df.info()

print(df.head().to_string())

df.drop(columns=['CustomerID','Count'],axis = 1, inplace = True)

print(df.head().to_string())

df['Churn Reason'].value_counts()


# Handling Missing Values

Mode = df['Churn Reason'].mode()[0]


#df['Churn Reason'].fillna(Mode,inplace=True)
df['Churn Reason'] = df['Churn Reason'].fillna(Mode)

df.info()

print(df['Churn Reason'].value_counts())

# Label Encoding

le = preprocessing.LabelEncoder()
df['Churn Reason Label '] = le.fit_transform(df['Churn Reason'].values)

print(df.head().to_string())

U = df[['Churn Reason','Churn Reason Label ']]
V = U.to_csv('Label Encoder.csv')

print(df['Churn Reason Label '].value_counts())

#One Hot Encoding Technique

one_hot = pd.get_dummies(df,columns=['Churn Reason'],prefix=['Churn_Reason'],dtype=int)
print(df.info())

print(one_hot.head().to_string())

print("==========================================================")

print(df.head().to_string())

one_hot = pd.get_dummies(df,dtype=int)
#print(one_hot.head().to_string())

Y = one_hot.to_csv('One hot Encoded.csv')

# Dummy Encoding ( most preferred or u can use similar on one-hot encoding)
#df_dummies = pd.get_dummies(df, drop_first = True)

# Hashing Encoder

from category_encoders import HashingEncoder
C =df[['Churn Reason']]

ce_hash = HashingEncoder(cols=['Churn Reason'],n_components=8)
O = ce_hash.fit_transform(C)

K = O.to_csv('Hashing.csv')


print(O.head())

#Target encoder

#pip install category_encoders

from category_encoders import TargetEncoder

df1 = pd.read_csv('Telco_customer_churn.csv')

df1.drop(columns=['CustomerID','Count'],axis=1,inplace = True)

Mode = df['Churn Reason'].mode()[0]
df['Churn Reason'] = df['Churn Reason'].fillna(Mode)

df['Churn Reason'].info()

df['Churn Reason'].value_counts()

encoder = TargetEncoder()

df1['Churn Reason Encoded '] = encoder.fit_transform(df1['Churn Reason'],df1['Churn Score'])

print(df1.head().to_string())

J = df1.to_csv("TargetEncoded.csv")

# Target encoding does not increase the size of dimensionality
# It's a good first try method
# The target variable  should be mentioned
# it's prone to overfitting as it depends on the target distribution(as it requires careful validation)











