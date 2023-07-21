# ROCK (Robust Clustering using Links)
# 이웃 데이터 간의 링크를 이용하여 로버스트하게 군집화하는 알고리즘이다.

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np
from scipy.spatial.distance import cdist

def rock_clustering(data, k, num_iterations, threshold):
    best_labels = None
    best_cost = float('inf')

    for _ in range(num_iterations):
        kmeans = KMeans(n_clusters=k, init='random', n_init=1)
        kmeans.fit(data)
        centers = kmeans.cluster_centers_

        distances = cdist(data, centers)

        labels = np.argmin(distances, axis=1)

        cost = sum(distances[i, labels[i]] for i in range(data.shape[0]))

        if cost < best_cost:
            best_cost = cost
            best_labels = labels

        links = [[] for _ in range(k)]
        for i in range(data.shape[0]):
            links[labels[i]].append(i)

        for i in range(k):
            linked_points = data[links[i]]
            centers[i] = np.mean(linked_points, axis=0)

        if np.max(cdist(kmeans.cluster_centers_, centers)) < threshold:
            break

    return best_labels

ns=int(input('표본 데이터의 수 입력 : '))
k = int(input('군집의 개수 입력 : '))
data, _ = make_blobs(n_samples=ns, centers=k, random_state=42)

num_iterations = int(input('반복 횟수 입력 : '))
threshold = 1e-6

labels = rock_clustering(data, k, num_iterations, threshold)
print("군집화된 라벨 : \n", labels)