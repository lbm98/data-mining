import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass
from collections import Counter


@dataclass
class DataPoint:
    attributes: np.ndarray
    label: str


# Define covariance matrix
cov = np.array([[5, 4], [4, 7]])

# Generate random data using normal multivariate distribution
data = np.random.multivariate_normal(mean=[0, 0], cov=cov, size=100)

print(data)

plt.scatter(data[:, 0], data[:, 1])
plt.show()


# Plot data
# fig, ax = plt.subplots()
# ax.scatter(data[:, 0], data[:, 1])
# ax.set_xlabel("Attribute 1")
# ax.set_ylabel("Attribute 2")
# ax.set_title("Generated Data")
# plt.show()

def knn_classify(k: int, distance, training_dataset: list[DataPoint], test_point: DataPoint):
    distances = []
    for point in training_dataset:
        distances.append(distance(point.attributes, test_point.attributes))

    knn_indices = np.argsort(distances)[:k]
    knn_labels = [point.label for point in training_dataset[knn_indices]]
