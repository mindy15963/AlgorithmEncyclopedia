# 가우시안 혼합 모델 (Gaussian Mixture Model, GMM)
# 가우시안 분포가 여러 개 혼합된 군집화 알고리즘이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

ns=int(input('표본 데이터의 수 입력 : '))
ct=int(input('생성할 군집의 수 입력 : '))

x,y=make_blobs(n_samples=ns,centers=ct,cluster_std=0.4,random_state=0)

gmm = GaussianMixture(n_components=ct)
gmm.fit(x)

labels = gmm.predict(x)

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x[:, 0], x[:, 1], c=labels, cmap='viridis')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.title('가우시안 혼합 모델 군집화')
plt.show()