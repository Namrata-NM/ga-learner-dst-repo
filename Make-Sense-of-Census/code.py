# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
print(new_record)
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data, new_record),axis=0)
census.shape

#Analysis of age Distribution
age=np.array([census[:,0]])
max_age=np.max(age)
print(max_age)
min_age=np.min(age)
print(min_age)
age_mean=round((np.mean(age)),2)
print(age_mean)
age_std=round((np.std(age)),2)
print(age_std)

#Analysis of Race distribution

race_0=census[census[:,2]==0]
print(race_0)

race_1=census[census[:,2]==1]
print(race_1)

race_2=census[census[:,2]==2]
print(race_0)

race_3=census[census[:,2]==3]
print(race_3)

race_4=census[census[:,2]==4]
print(race_4)


len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)

len_list=[len_0,len_1,len_2,len_3,len_4]
min_len=min(len_list)
minority_race=len_list.index(min_len)
print('Minority_race is race',minority_race)

#New Policy for senior citizens
senior_citizens=census[census[:,0]>60]
working_hours_sum=sum(senior_citizens[:,6])
print('Total Working hours',working_hours_sum)
senior_citizens_len=len(senior_citizens)
print('Total number of senior citizens',senior_citizens_len)
avg_working_hours=round((working_hours_sum/senior_citizens_len),2)
print('Average working hours',avg_working_hours)

#Education and Pay analysis
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=round((np.mean(high[:,7])),2)
print('Average high pay',avg_pay_high)
avg_pay_low=round((np.mean(low[:,7])),2)
print('Average low pay',avg_pay_low)


