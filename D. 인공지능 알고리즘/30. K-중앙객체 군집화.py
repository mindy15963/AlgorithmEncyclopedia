# K-중앙객체 군집화 (K-medoids Clustering)
# 주어진 데이터를 k개의 군집으로 묶는 알고리즘으로, 평균을 구하는 대신에 군집을 대표하는 실제 객체를 선택하는 방식으로 동작한다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn.datasets import make_blobs

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 클러스터의 수 입력 : '))
cstd=float(input('클러스터의 표준 편차 입력 : '))
ec=int(input('실행 횟수 입력 : '))

np.random.seed(8)
x,y=make_blobs(n_samples=ns,centers=ct,cluster_std=cstd)
plt.scatter(x[:,0],x[:,1],marker='.')

k_medoids=KMedoids(n_clusters=ct,random_state=0)
k_medoids.fit(x)

k_medoids_labels=k_medoids.labels_
print(f'레이블 결과 : \n{k_medoids_labels}')

k_medoids_cluster_centers=k_medoids.cluster_centers_
print(f'중심점 값 결과 : \n{k_medoids_cluster_centers}')

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig=plt.figure(figsize=(6,4))

colors=plt.cm.Spectral(np.linspace(0,1,len(set(k_medoids_labels))))

ax=fig.add_subplot(1,1,1)

for k,col in zip(range(ct),colors):
    my_members=(k_medoids_labels==k)
    cluster_center=k_medoids_cluster_centers[k]
    ax.plot(x[my_members,0],x[my_members,1],'w',markerfacecolor=col,marker='.')
    ax.plot(cluster_center[0],cluster_center[1],'o',markerfacecolor=col,markeredgecolor='k',markersize=6)

plt.title('K-중앙객체 군집화')
ax.set_xticks(())
ax.set_yticks(())
plt.show()