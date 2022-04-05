import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/cygwin64/home/Wheat‘s Computer/IBI1_2021-22/Practical7")
covid_data =pd.read_csv("full_data.csv")
#show the first and third columns from rows 10-20
print(covid_data.iloc[10:20,[0,2]])
#get the true/false for each row
task3 = [] 
for i in range(0,len(covid_data)):
    if covid_data.loc[i,"location"] == "Afghanisten":
        task3.append(True)
    else:
        task3.append(False)
total_cases = covid_data.iloc[task3,4]
#compute the mean value of new cases and new death
#firtly we get which rows are China
task4 = []
for i in range(0,len(covid_data)):
    if covid_data.loc[i,"location"] == "China":
        task4.append(True)
    else:
        task4.append(False)
china_new_cases = covid_data.iloc[task4,2]
cases_mean = np.mean(china_new_cases)
china_new_death = covid_data.iloc[task4,3]
death_mean = np.mean(china_new_death)
china_dates = covid_data.iloc[task4,0]
#show the boxplot in china of new cases and new death
plt.subplot(1,2,1)
plt.boxplot(china_new_cases,labels=["new_cases"])
plt.subplot(1,2,2)
plt.boxplot(china_new_death,labels=["new_death"])
plt.title("china_new_data")
plt.show()
#show the plot of new cases nad new death in China  over the time
plt.plot(china_dates,china_new_cases,color='b',label = 'new_cases')
plt.plot(china_dates,china_new_death,color='r',label = 'new death')
plt.xticks(rotation = -90)
plt.legend()
plt.show()
#!!!!code for the question
spain = []
for i in range(0,len(covid_data)):
    if covid_data.loc[i,"location"] == "Spain":
        spain.append(True)
    else:
        spain.append(False)
spain_new_cases = covid_data.iloc[spain,2]
spain_total_cases = covid_data.iloc[spain,4]
spain_dates = covid_data.iloc[spain,0]
plt.plot(spain_dates,spain_new_cases,color='b',label = 'new_cases')
plt.plot(spain_dates,spain_total_cases,color='r',label = 'total cases')
plt.legend()
plt.title = "new cases and total cases in Spain"
plt.xticks(rotation = -90)
plt.show()

