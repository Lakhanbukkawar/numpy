import numpy as np
ar1=np.array([1,2,3,4,5,8,6,7])

ar2=np.array([[1,3],
              [5,6]])

# print(ar1.shape)
# a1=np.reshape(ar1,(2,4),order='f')
# print(a1)

# a2=ar1.reshape(4,2)  #array
# print(a2)

a1=np.resize(ar1,(4,2))
print(a1)