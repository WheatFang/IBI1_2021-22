import numpy as np
import matplotlib.pyplot as plt
scores = [45,36,86,57,53,92,65,45]
print(scores)
plt.boxplot(scores)
plt.title("IBI scores")
plt.axhline(60,color='b',linestyle='--',label='60')
plt.show()
average = np.mean(scores)
if average >= 60:
    print("the average mark is >60%")
else:
    print("the average mark is <60%")
