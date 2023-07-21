# CURE (Clustering Using Representatives)
# 대표점을 사용하여 군집화를 수행하는 알고리즘이다.

from sklearn.cluster import KMeans
import numpy as np

def cure_clustering(data, k, s):
    np.random.seed(42)
    representatives = data[np.random.choice(data.shape[0], s, replace=False)]

    kmeans = KMeans(n_clusters=k, init=representatives, n_init=1)
    kmeans.fit(data)

    labels = kmeans.predict(data)

    return labels

dc = int(input('데이터의 개수 입력 : '))
data = np.random.randint(10, size=(dc, 2))
k = int(input('군집의 개수 입력 : '))
s = int(input('대표점의 개수 입력 : '))

labels = cure_clustering(data, k, s)
print("군집화된 라벨 : ", labels)