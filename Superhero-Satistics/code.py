# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
#Replacing Gender value
data['Gender'].replace('-','Agender',inplace=True)
#Gender distribution
data['Gender'].value_counts().plot(kind='bar')
plt.title('Gender Distribution of Superheros')
#Alignment Distribution
plt.title('Alignment distribution')
plt.pie(data['Alignment'].value_counts(),labels=data['Alignment'].value_counts())
#Best Super Heros
total_high=data['Total'].quantile(0.99)
super_best=data[data['Total'] > total_high]
super_best_names=list(super_best['Name'])
print(super_best_names)
# Code starts here



