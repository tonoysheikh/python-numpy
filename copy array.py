import numpy as np

a = np.array([1,2,3,4,5])
arr = a.copy();

a[2] = 30

print(arr)
print(a)