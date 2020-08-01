import numpy as np

height = np.array([1.87,1.87,1.82,1.91,1.90,1.85])
weight = np.array([81.65,97.52,95.52,92.98,86.81,88.45])

bmi=weight/(height**2)
print(bmi)