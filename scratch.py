import numpy as np
import matplotlib.pyplot as plt

# np.linspace(0)

# print(np.arange(1, 11))

def normalize(nums):
    return nums / np.sum(nums)


def entropy(nums):
    p = normalize(nums)
    p = p[p>0]
    return -np.sum(p * np.log2(p))

def plot():
    x = np.arange(1, 11)
    y = np.array([entropy(np.ones(i)) for i in x])
    plt.plot(x, y)

    x = np.arange(10, 24)
    y = np.array([entropy(np.ones(i)) for i in x])
    plt.plot(x, y)

plot()
plt.show()