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
