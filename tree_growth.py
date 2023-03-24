import numpy as np


def normalize(nums):
    return nums / np.sum(nums)


class Node:
    def __init__(self):
        pass


def stopping_cond_1(attributes, labels, **kwargs):
    # stop if all have same class label
    return np.all(labels == labels[0])


def stopping_cond_2(attributes, labels, **kwargs):
    # stop if all have same attribute values
    return np.all(attributes == attributes[0])


def stopping_cond_3(attributes, labels, **kwargs):
    # stop if number of records have fallen below some minimum threshold
    threshold = kwargs['threshold']
    return np.sum(labels) <= threshold


def classify(labels):
    # return the label that has the majority number of records
    return np.argmax(labels)


def find_impurity(attributes):


def find_impurity_split(attr, attributes, labels, impurity):
    child_true = attributes[attributes[:, attr] == 0]
    child_false = attributes[attributes[:, attr] == 1]




def find_best_split(attributes, labels, impurity):
    # return the attribute that is best for splitting the records
    # NOTE: only support binary attributes
    impurities = np.array([
        find_impurity_split(attr, attributes, labels, impurity)
        for attr in range(attributes.shape[1])
    ])
    return np.argmax(impurities)

def tree_growth(attributes, labels, stopping_cond):
    if stopping_cond(attributes, labels):
        leaf = Node()
        leaf.label = classify(labels)
        return leaf
    else:
        node = Node()
        node.t


def run():
    records = [1, 2, 3]
