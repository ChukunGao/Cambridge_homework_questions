import numpy as np 
import matplotlib.pyplot as plt
def f(x):
    return np.sin(x)+np.cos(10*x)/5
numarray = np.arange(0, 2*np.pi, 2*np.pi/50)
numlist = list(numarray)
numlist.append(2*np.pi)
original = []
for i in range(len(numlist)):
    temp = f(numlist[i])
    original.append(temp)

smoothed = []
for i in range(len(original)):
    if original[i] != original[0] and original[i] != original[-1]:
        temp = (original[i-1]+original[i]+original[i+1])/3
        smoothed.append(temp)

smoothed.insert(0, original[0])
smoothed.append(original[-1])
#print(len(smoothed))
plt.plot(numlist, original, numlist, smoothed)
plt.show()