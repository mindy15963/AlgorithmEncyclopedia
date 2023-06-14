# 유사도 전파 군집화 (Affinity Propagation Clustering)
# 데이터 지점 간의 "메시지 전달" 개념을 기반으로 하는 군집화 알고리즘이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from sklearn.datasets import make_blobs
import warnings

warnings.filterwarnings('ignore')

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 군집의 수 입력 : '))

x,y=make_blobs(n_samples=ns,centers=ct,cluster_std=0.6,random_state=0)

ap = AffinityPropagation(random_state=5)
ap.fit(x)

labels = ap.labels_

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x[:, 0], x[:, 1], c=labels, alpha=0.7)
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.title('유사도 전파 군집화')
plt.show()