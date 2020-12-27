# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
#probability p(A)for the event that fico credit score is greater than 700
p_a= len(df[df['fico']>700])/len(df['fico'])
print(p_a)
#probabilityp(B) for the event that purpose == 'debt_consolation'
p_b=len(df[df['purpose']=='debt_consolidation'])/len(df['purpose'])
print(p_b)
#probablityp(B|A)
df1=df[df['purpose']=='debt_consolidation']
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
result = (p_a_b == p_a)
print(result)

#conditional probability 
prob_lp = df[df['paid.back.loan']=='Yes'].shape[0]/df.shape[0]
prob_cs=  df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)
bayes=prob_pd_cs*prob_lp/prob_cs
print(bayes)

#Barplot
df['purpose'].value_counts().plot(kind='bar')
df1=df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind='bar')

#Histogram
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
plt.hist(df['installment'])
plt.hist(df['log.annual.inc'])


