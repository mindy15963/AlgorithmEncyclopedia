# 자기조직화 지도(Self-Organizing Map, SOM)
# 대뇌피질의 시각피질의 학습 과정을 모델화한 인공신경망으로써 자율 학습에 의한 클러스터링을 수행하는 알고리즘이다.

from minisom import MiniSom
import numpy as np

data = np.random.rand(100, 5)

som = MiniSom(10, 10, 5)
som.random_weights_init(data)
som.train_random(data, 100)

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 10))
plt.title('자기조직화 지도(SOM) 결과')
plt.pcolor(som.distance_map().T, cmap='bone_r')
plt.colorbar()

for i, x in enumerate(data):
    w = som.winner(x)
    plt.plot(w[0] + 0.5, w[1] + 0.5, 'o', markerfacecolor='None',
             markeredgecolor='red', markersize=8, markeredgewidth=2)

for i in range(som.get_weights().shape[0]):
    for j in range(som.get_weights().shape[1]):
        plt.text(i + 0.5, j + 0.5, f'({i}, {j})',ha='center', va='center', color='black', fontsize=8)

plt.show()