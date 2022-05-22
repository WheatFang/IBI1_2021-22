import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/cygwin64/home/Wheat‘s Computer/IBI1_2021-22/Practical7")
# the code for importing the .csv file works
covid_data =pd.read_csv("full_data.csv")
#show the first and third columns from rows 10-20
print("the first and third columns from rows 10-20 are following:","\n",covid_data.iloc[10:21,[0,2]])

#get the true/false for each row
task3 = [] 
for i in range(0,len(covid_data)):
    if covid_data.loc[i,"location"] == "Afghanistan":
        task3.append(True)
    else:
        task3.append(False)
#task3 is the boolean for extracting the total_cases for all rows correspounding to Afghanistem
total_cases = covid_data.iloc[task3,4] # total_cases for all rows corresponding to Afghanistem
print("total_cases for Afghanistem ",total_cases)

#compute the mean value of new cases and new death
#firtly we get which rows are China (boolean)
task4 = []
for i in range(0,len(covid_data)):
    if covid_data.loc[i,"location"] == "China":
        task4.append(True)
    else:
        task4.append(False)
# task4 is the boolean for extracting the rows corresponding to China
china_new_cases = covid_data.iloc[task4,2] # new cases of China
cases_mean = np.mean(china_new_cases) # mean of new cases of China
china_new_death = covid_data.iloc[task4,3] # new death of China
death_mean = np.mean(china_new_death)  # mean of new death of China
china_dates = covid_data.iloc[task4,0]
print("the mean number of new cases in China is", round(cases_mean,2))
print("the mean number of new death in China is", round(death_mean,2))

#show the boxplot in china of new cases and new death
plt.subplot(1,2,1) # makes these two plots shown in one graph
plt.boxplot(china_new_cases,labels=["new_cases in China"])
plt.subplot(1,2,2)
plt.boxplot(china_new_death,labels=["new_death in China"])
plt.show()

#show the plot of new cases nad new death in China  over the time
plt.plot(china_dates,china_new_cases,color='b',label = 'new_cases')
plt.plot(china_dates,china_new_death,color='r',label = 'new death')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation = -90)
plt.legend()
plt.show()

#!!!!code for the question
# how have new cases and total cases developed over time in Spain
spain = []
for i in range(0,len(covid_data)):
    if covid_data.loc[i,"location"] == "Spain":
        spain.append(True)
    else:
        spain.append(False)
# spain is the boolean for extracting the data corresponding to Spain
spain_new_cases = covid_data.iloc[spain,2]
spain_total_cases = covid_data.iloc[spain,4]
spain_dates = covid_data.iloc[spain,0]
plt.plot(spain_dates,spain_new_cases,color='b',label = 'new_cases')
plt.plot(spain_dates,spain_total_cases,color='r',label = 'total cases')
plt.legend()
plt.title = "new cases and total cases in Spain"
plt.xticks(spain_dates.iloc[0:len(spain_dates):4],rotation = -90)
plt.show()

