# DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
# 특정 데이터를 중심으로 밀도가 높은 곳에 포함된 데이터에는 군집를 할당하고 밀도가 낮으면 그 데이터를 노이즈로 취급하는 알고리즘이다.

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 군집의 수 입력 : '))

x,y=make_blobs(n_samples=ns,centers=ct,cluster_std=0.4,random_state=0)
X = StandardScaler().fit_transform(x)

epsilon = float(input('반지름 길이 입력 : '))
minimumSamples = int(input('최소 요소 값 입력 : '))
db = DBSCAN(eps=epsilon, min_samples=minimumSamples).fit(X)
labels = db.labels_

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)
print('군집 개수 : ', n_clusters_)
print('노이즈 개수 : ', n_noise)
print('동질성 : %0.3f' % metrics.homogeneity_score(y, labels))
print("완전성 : %0.3f" % metrics.completeness_score(y, labels))

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.title('DBSCAN')

unique_labels = set(labels)

colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for k, col in zip(unique_labels, colors):
    if k == -1:
        col = 'k'

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1], s=50, c=[col], marker=u'o', alpha=0.5)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1], s=50, c=[col], marker=u'o', alpha=0.5)

plt.show()