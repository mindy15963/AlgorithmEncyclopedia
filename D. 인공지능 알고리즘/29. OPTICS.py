# OPTICS (Ordering Points To Identify the Clustering Structure)
# 밀도 기반의 군집을 탐색하기 위한 알고리즘이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import OPTICS
from sklearn.datasets import make_blobs
import warnings

warnings.filterwarnings('ignore')

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 군집의 수 입력 : '))
ms=int(input('최소 샘플 개수 입력 : '))

x,y=make_blobs(n_samples=ns,centers=ct,cluster_std=1.5,random_state=40)

op = OPTICS(min_samples=ms, xi=0.02, min_cluster_size=0.1)
op.fit(x)

labels = op.labels_

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x[:, 0], x[:, 1], c=labels)
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.title('OPTICS')
plt.show()