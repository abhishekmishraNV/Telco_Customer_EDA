'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv('Telco_customer_churn.csv')

print(df.head().to_string())

df.info()

df.drop(columns=['CustomerID','Count'],axis=1,inplace=True)

df.info()

print(df.head().to_string())

print(df.Latitude.min())

print(df.Latitude.max())

Labels = ['32.555828-36','37-39','Above 40 ']
bins = [32.555828,37,40,50]

df['Latitude bins'] = pd.cut(df.Latitude,bins,labels = Labels,include_lowest=True)

print(df['Latitude bins'].head())

print(df.head().to_string())

K = df[['Latitude','Latitude bins']]
print(K)

Z =K.to_csv('test.csv')

print("===================================================")

R = df['Latitude bins'].value_counts()
print(R)


def add_labels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

# Making the bar chart for the data

plt.bar(Labels,R)

# giving the title

plt.title('Latitude Counts')

# Add the labels

add_labels(Labels,R)

#giving x and y label

plt.xlabel('Latitude bins')
plt.ylabel('Latitude Counts')

Visualization

plt.show()'''
























