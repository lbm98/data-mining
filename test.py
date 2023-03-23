import numpy as np
import matplotlib.pyplot as plt


def normalize(nums):
    return nums / np.sum(nums)


def my_log2(x):
    if x == 0:
        return 0
    else:
        return np.log2(x)


def entropy(nums):
    p = normalize(nums)
    x = 0
    for i in p:
        x += i * my_log2(i)
    return -x


def gini(nums):
    p = normalize(nums)
    return 1 - np.sum(p ** 2)


def classification_error(nums):
    p = normalize(nums)
    return 1 - np.max(p)


def plot(algo, algo_name):
    x = range(100)
    y = []
    for i in x:
        nums = np.array([i, 100 - i])
        y.append(algo(nums))
    ax.plot(x, y, label=algo_name)


fig, ax = plt.subplots()
plot(entropy, 'entropy')
plot(gini, 'gini')
plot(classification_error, 'classification_error')
plt.show()
