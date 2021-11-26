Q4:
import numpy as np
def f(x):
    return x**2*np.sin(x**2)

def deri(x):
    return 2*x*np.sin(x**2)+2*x**3*np.cos(x**2)

data = [10, 100, 1000, 10000]
incr = [10**-9, 10**-12, 10**-15]
for i in range(len(data)):
    for j in range(len(incr)):
        imvalue = complex(data[i], incr[j])
        fvre = f(data[i])
        fvim = f(imvalue)
        result = fvim.imag/incr[j]
        truevalue = deri(data[i])
        error = abs(truevalue-result)/truevalue
        print("value of x is", data[i], "value of increment is", incr[j], "error is", error)

Q5(a)
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

Q5(b)
import matplotlib.pyplot as plt
import numpy as np
A = plt.imread("https://github.com/CambridgeEngineering/PartIA-Computing-Examples-Papers/raw/master/images/southwing.png")
#plt.imshow(A, cmap='gray')
G = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
B = np.zeros(A.shape)
for i in range(1, B.shape[0]-1):
    for j in range(1, B.shape[1]-1):
        for k in range(3):
            for l in range(3):
                B[i, j] += G[k, l]*A[i-1+k, j-1+l]
plt.imshow(B, cmap='gray')
plt.show()