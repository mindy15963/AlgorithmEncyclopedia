# BIRCH (Balanced Iterative Reducing and Clustering using Hierarchies)
# 대규모 데이터셋을 처리하기 위해 개발된 군집화 알고리즘이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import Birch
from sklearn.datasets import make_blobs

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 군집의 수 입력 : '))
bf=int(input('최대 자식 수 입력 : '))
md=float(input('최대 직경 입력 : '))

x,y=make_blobs(n_samples=ns,centers=ct,cluster_std = 0.65, random_state = 0)

brc = Birch(branching_factor = bf, n_clusters = None, threshold = md)
brc.fit(x)

predicted = brc.predict(x)

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x[:, 0], x[:, 1], c=predicted, alpha = 0.8)
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.title('BIRCH')
plt.show()