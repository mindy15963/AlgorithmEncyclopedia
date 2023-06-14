# 스펙트럴 군집화 (Spectral Clustering)
# 그래프 기반의 군집화 알고리즘이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_blobs

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 군집의 수 입력 : '))

x,y=make_blobs(n_samples=ns,centers=ct,cluster_std=1.5)

sc = SpectralClustering(n_clusters=ct)
sc.fit(x)

labels = sc.labels_

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x[:, 0], x[:, 1], c=labels)
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.title('스펙트럴 군집화')
plt.show()