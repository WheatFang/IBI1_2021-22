import numpy as np
import matplotlib.pyplot as plt
age = [30,35,40,45,50,55,60,65,70,75]
chd = [1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
age_chd={}
for i in range(10):
    age_chd[age[i]] = chd[i]   # restore the data in a directory to get easily
print(age_chd)
plt.scatter(age,chd,marker='o')
plt.title("effect of paternal age")
plt.xlabel('Paternal_age')
plt.ylabel('chd')
plt.show()

m = 35 # a variable for age that can be modified
corresponding_chd = age_chd[m]
print(corresponding_chd)
print("the the probability is %s for %d years old"% (corresponding_chd,m))