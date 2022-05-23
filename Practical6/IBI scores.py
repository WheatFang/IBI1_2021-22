import numpy as np
import matplotlib.pyplot as plt
scores = [45,36,86,57,53,92,65,45]
print(scores) # Print a sorted list of marks
plt.boxplot(scores) # create a boxplot
plt.title("IBI scores")
plt.axhline(60,color='b',linestyle='--',label='60') # draw the line of "60%"(acceptable score)
plt.xlabel("score")
plt.show()
average = np.mean(scores)
if average >= 60: # judge if the mean scores is acceptable(>60)
    print("the average mark is >60%")
else:
    print("the average mark is <60%")
