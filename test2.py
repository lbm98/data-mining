import numpy as np

# x = np.array([1, 2, 3,  3])
# y = np.where(x == 1, 5, np.log2(x))
# print(y)

# for i in np.arange(0, 99, 100):
#     print(i)

x = np.array([0, 6, 5, 0])
b = np.count_nonzero(x) == 1

# print(b)

# print(np.array_equal(np.array([1, 2, 3]), np.array([1, 3, 2])))

# q = np.array([[1, 2, 3],
#               [1, 3, 2]])


# print(q.shape[1])

m = np.array([[0, 1, 1],
              [1, 0, 0],
              [1, 0, 1]])

attr = 0

# rows0 = []
# for row in m:
#     if row[attr] == 0:
#           rows0.append(row)

rows0 = m[m[:, attr] == 0]
rows1 = m[m[:, attr] == 1]

print(rows0)
print()
print(rows1)