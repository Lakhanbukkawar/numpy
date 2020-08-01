import numpy as np

ar1=np.array([2,3,4])
ar2=np.array([[2,3],
            [5,6]])
ar3=np.array([[8,9],
               [4,7]])

print(ar1.shape)
print(ar1.ndim)
print(ar2.shape)
print(ar2.ndim)
print(ar1+ar1)
print(ar2+ar2)
print(ar2+ar3)
print(ar3-ar2)
print(ar2*ar3)