#Detection of Outliers

'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

data = pd.read_csv('Telco_customer_churn.csv')

print(type(data))

data.info()

print(data.head().to_string())

#3 sigma Technique (Normal - Distribution)

#Function to detect outliers on a dataset:-

def find_anomalies(data):
    annomaly = [] #Creation of a list to store the annomaly
    random_std = statistics.stdev(data) #calculating the std.dev.
    random_mean = statistics.mean(data) #calculting mean
    annomaly_cutoff = random_std*3 #extreme range decider
    lower_limit = random_mean+annomaly_cutoff # mu + 3rho
    upper_limit = random_mean-annomaly_cutoff #mu-3rho
    for outliers in data:
        if outliers>upper_limit or outliers<lower_limit:
            annomaly.append(outliers)
    return annomaly
print("-------------------------------------------------------------")
print(data['Churn Reason'])

list_1 = find_anomalies(data['Tenure Months'])
print(list_1)
print(len(list_1))

print(len(data))

#if len(list 1) = 462 then the percentage of outlier would br 462/7043 = 6.55970
print('------------')
print(len(list_1))

print(data['Tenure Months'].skew())

import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(data['Tenure Months'])
plt.show()


X = data['Tenure Months']
X = np.log1p(X)              #by typing two times np.log1p you are performing the skew 1+x so that it becomes more symmetrical

print(X.skew())

import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(X) #if the percentage of ouliers is = 0.3 then it's normally distributed
plt.show()
# Anything below 40 and greater then 80 is considered as outliers

#BoxPlot Method

import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(data=data)
plt.show() #anything above 75 and below -35 as outliers

print(data.describe().to_string())
print("------------------------------------------------")
# IQR
import numpy as np

list = [1,2,3,4,5,6,78]
Q1=np.percentile(list,25)
Q3 = np.percentile(list,75)
IQR = Q3-Q1
low = Q1-1.5*IQR
high = Q3+1.5*IQR
for x in list:
    if x<low or x>high:
        print(f"{x} is an outlier")'''




























