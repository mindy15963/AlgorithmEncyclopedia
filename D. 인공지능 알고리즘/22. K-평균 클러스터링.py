# K-평균 클러스터링 (K-means clustering)
# 주어진 데이터를 k개의 클러스터로 묶는 알고리즘으로, 각 클러스터와 거리 차이의 분산을 최소화하는 방식으로 동작한다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 클러스터의 수 입력 : '))
cstd=float(input('클러스터의 표준 편차 입력 : '))
ec=int(input('실행 횟수 입력 : '))

np.random.seed(8)
x,y=make_blobs(n_samples=ns,centers=ct,cluster_std=cstd)
plt.scatter(x[:,0],x[:,1],marker='.')

k_means=KMeans(init="k-means++",n_clusters=ct,n_init=ec)
k_means.fit(x)

k_means_labels=k_means.labels_
print(f'레이블 결과 : \n{k_means_labels}')

k_means_cluster_centers=k_means.cluster_centers_
print(f'중심점 값 결과 : \n{k_means_cluster_centers}')

fig=plt.figure(figsize=(6,4))

colors=plt.cm.Spectral(np.linspace(0,1,len(set(k_means_labels))))

ax=fig.add_subplot(1,1,1)

for k,col in zip(range(4),colors):
    my_members=(k_means_labels==k)
    cluster_center=k_means_cluster_centers[k]
    ax.plot(x[my_members,0],x[my_members,1],'w',markerfacecolor=col,marker='.')
    ax.plot(cluster_center[0],cluster_center[1],'o',markerfacecolor=col,markeredgecolor='k',markersize=6)

ax.set_title('K-Means')
ax.set_xticks(())
ax.set_yticks(())
plt.show()