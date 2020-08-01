import numpy as np

ar1=np.array([2,3])

ar2=np.array([[1,2],
              [3,4],
              [5,6]])

# for x in np.nditer(ar1):
#     print(x)

for x in np.nditer(ar2):
    print(x)