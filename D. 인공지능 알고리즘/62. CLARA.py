# CLARA (Clustering Large Applications)
# K-평균 군집화를 대규모 데이터에 적용하는 데 사용되는 샘플링 기반 군집화 알고리즘이다.

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np

def clara_clustering(data, k, num_samples, num_iterations):
    best_labels = None
    best_cost = float('inf')

    for _ in range(num_iterations):
        np.random.seed(42)
        subset_indices = np.random.choice(data.shape[0], num_samples, replace=False)
        subset_data = data[subset_indices]

        kmeans = KMeans(n_clusters=k, init='random', n_init=1)
        kmeans.fit(subset_data)

        labels = kmeans.predict(data)

        centers = kmeans.cluster_centers_
        cost = sum(np.linalg.norm(data[i] - centers[labels[i]])**2 for i in range(data.shape[0]))

        if cost < best_cost:
            best_cost = cost
            best_labels = labels

    return best_labels

ns=int(input('표본 데이터의 수 입력 : '))
k = int(input('군집의 개수 입력 : '))
data, _ = make_blobs(n_samples=ns, centers=k, random_state=42)

num_samples = int(input('표본의 개수 입력 : '))
num_iterations = int(input('반복 횟수 입력 : '))

labels = clara_clustering(data, k, num_samples, num_iterations)
print("군집화된 라벨 : \n", labels)