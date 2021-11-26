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