import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

real_log = []
imag_log = []
for omega in np.arange(0.1, 1, .01):
    p1 = complex(0, omega)
    p2 = complex(1, 3*omega)
    p3 = complex(1, 4*omega)
    res = 1/(p1*p2*p3)
    real_log.append(res.real)
    imag_log.append(res.imag)
plt.plot(real_log, imag_log)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()