import numpy as np

# a = np.array([7, 1, 7, 7, 1, 5, 7, 2, 3, 2, 6, 2, 3, 0])
# p = np.argpartition(a, 4)[:4]
# print(p)

a = np.array([7, 2, 6, 4])
b = a[[1, 2, 3]]
print(b)