# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)


#Code starts here

# Step 1 
#Reading the file

#Creating a new variable to store the value counts
property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()

#Plotting bar plot
# Step 2
#Plotting an unstacked bar plot
property_and_loan.plot(kind='bar',stacked=False)




#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label

plt.ylabel('Loan Status')

#Rotating the ticks of X-axis

plt.xticks(rotation=45)

# Step 3
#Plotting a stacked bar plot

education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked=True)



#Changing the x-axis label

plt.xlabel('education_and_loan')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

print(education_and_loan['N'][1] )
print(education_and_loan['Y'][0] )

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
#Subsetting the dataframe based on 'Education' column
#Plotting density plot for 'Graduate'

graduate['LoanAmount'].plot(kind='density',label='Graduate')



#Plotting density plot for 'Not Graduate'

graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#For automatic legend display
plt.legend()

# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(10,5))


#Plotting scatter plot

ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
#Setting the subplot axis title

ax_1.set_title('Applicant Income')
#Plotting scatter plot

ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
#Setting the subplot axis title
ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome']=data['CoapplicantIncome'] + data['ApplicantIncome']

#Plotting scatter plot

ax_3.scatter(data['TotalIncome'],data['LoanAmount'])

#Setting the subplot axis title
ax_3.set_title('Total Income')


