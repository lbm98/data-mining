import numpy as np

def normalize(nums):
    return nums / np.sum(nums)

def gini(nums):
    p = normalize(nums)
    return 1 - np.sum(p ** 2)

def impurity_children(data, parent, children, impurity):
    x = 0
    for child in children:
        imp = impurity(data[child])
        # Add weight
        imp *= np.sum(data[child]) / np.sum(data[parent])
        x += imp
    return x


data = {}
data[0] = np.array([2, 8])  # Parent
data[1] = np.array([5, 2])  # Child 1
data[2] = np.array([1, 2])  # Child 2
impurity_children(data, parent=0, children=[1, 2], impurity=gini)

print(wa)