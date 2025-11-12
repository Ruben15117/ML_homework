import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, steps=1000):
        self.lr = lr 
        self.steps = steps 
        self.w = None         
        self.b = None         

    def fit(self, X, y):
        n, m = X.shape
        self.w = np.zeros(m)
        self.b = 0
        y = np.where(y == 0, -1, 1)

        for _ in range(self.steps):
            for xi, target in zip(X, y):
                output = np.dot(xi, self.w) + self.b
                pred = 1 if output >= 0 else -1

                if pred != target:
                    self.w += self.lr * target * xi
                    self.b += self.lr * target

    def predict(self, X):
        out = np.dot(X, self.w) + self.b
        return np.where(out >= 0, 1, 0)
X = np.array([
    [1.4, 0.2],
    [1.3, 0.3],
    [4.7, 1.4],
    [4.5, 1.5]
])

y = np.array([0, 0, 1, 1])

p = Perceptron(lr=0.1, steps=10)
p.fit(X, y)

pred = p.predict(X)

print("pred:", pred)
print("weights:", p.w)
print("bias:", p.b)


import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from collections import Counter

iris = load_iris()
X = iris.data
y = iris.target
names = iris.target_names

kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_
species = {}
for cluster in range(3):
    cluster_specie = y[labels == cluster]
    most_common = Counter(cluster_specie).most_common(1)[0][0]
    species[cluster] = names[most_common]

new_flower = np.array([[5.0, 3.5, 1.4, 0.2]])
cluster = kmeans.predict(new_flower)[0]
pred_species = species[cluster]

print("new flower:", new_flower)
print("pred cluster:", cluster)
print("pred species:", pred_species)