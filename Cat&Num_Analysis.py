'''#Categorical and Numerical Data Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns


Data = pd.read_csv('Telco_customer_churn.csv')

# Univariate Analysis

print(Data.info())

print(Data.head().to_string())

# To find what is the characteristics of a people who are likely to churn or who are already got churned
# First we will do the analysis

New_data = Data[['City','Gender','Churn Value']]

print(New_data.head())

for i,predictor in enumerate(New_data.drop(columns=['Churn Value']).columns):
    plt.figure(figsize=(16,6)) # It makes the plot wider
    sns.countplot(data=New_data , x = predictor, hue= 'Churn Value')
    plt.xticks(rotation = 90)  #Rotates x- axis layout
    plt.tight_layout()   #fixes layout overlaps
    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Choose your predictor
predictor = 'City'
N = 10  # Number of top cities to show

# Get top N most common cities
top_cities = New_data[predictor].value_counts().nlargest(N).index

filtered_data = New_data[New_data[predictor].isin(top_cities)]

plt.figure(figsize=(10,6))
sns.countplot(data=filtered_data, x=predictor, hue='Churn Value', order=top_cities)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

Total_Telco_Churn = New_data['Churn Value'].value_counts()
print(Total_Telco_Churn)

Total_Telco_Churn = New_data['Churn Value'].value_counts()/len(New_data)*100
print(Total_Telco_Churn)

#Bivariate Analysis

sns.histplot(x='Gender',hue='City',data=New_data,stat="count",multiple="dodge")
plt.show()

telco_new_data = New_data.loc[New_data['Churn Value']==1] #Selectivity

sns.histplot(x='Gender',hue='City',data=telco_new_data,stat="count",multiple="dodge")
plt.show()

# Numerical Analysis

#Correlation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

Data = pd.read_csv('Telco_customer_churn.csv')
print('===================================================================')
corr_matrix = Data.corr(numeric_only=True)
print(corr_matrix.to_string())

plt.figure(figsize=(20,8))
corrs_matrix = Data.corr(numeric_only=True)['Churn Value'].sort_values(ascending=False).plot(kind='bar')
plt.show()

plt.figure(figsize=(6,6))
sns.heatmap(corr_matrix,cmap='Paired')
plt.show()

Data.head()

Data['Churn Score'].value_counts().sort_index(ascending=True).plot()
plt.show()

New_Data_1 = Data.loc[Data['Churn Value']==1]

New_Data_1['Churn Score'].value_counts().sort(ascending=True).plot()
plt.show()'''



















