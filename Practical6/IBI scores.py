import numpy as np
import matplotlib.pyplot as plt
scores = [45,36,86,57,53,92,65,45]
plt.boxplot(scores,labels=["S"])
plt.title("IBI scores")
plt.show()
