# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

#Categorical Variable
categorical_var = bank_data.select_dtypes(include = 'object')
#print(categorical_var)
#Numerical Variable
numerical_var=bank_data.select_dtypes(include='number')
#print(numerical_var)
bank_data.columns
#Drop columns
bank_data.drop('Loan_ID',axis=1,inplace=True)
banks=bank_data
#Null values check
banks.isnull().sum()
#Mode
bank_mode=banks.mode().iloc[0]
#Fillna
banks.fillna(bank_mode,inplace=True)
#null values check
print(banks.isnull().sum())
#Pivot table
avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
#Percentage of loan approved
loan_approved_se=len(banks[(banks['Self_Employed'] == 'Yes' ) & (banks['Loan_Status']== 'Y')])

loan_approved_nse=len(banks[(banks['Self_Employed'] == 'No' ) & (banks['Loan_Status']== 'Y')])

Loan_Status=614

percentage_se=round(loan_approved_se*100/Loan_Status,2)
percentage_nse=round(loan_approved_nse*100/Loan_Status,2)

print(percentage_se)
print(percentage_nse)
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

#Average Income of an applicant
loan_groupby=banks.groupby(banks['Loan_Status'])
loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=round(loan_groupby.mean(),2)
print(mean_values)


