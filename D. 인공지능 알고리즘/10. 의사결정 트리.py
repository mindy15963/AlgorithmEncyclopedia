# 의사결정 트리(Decision Tree)
# 데이터에 있는 규칙을 학습을 통해 자동으로 찾아내 트리 기반의 분류 규칙을 만드는 것으로 이 모양이 나무를 닮아 트리 모델이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import *
from sklearn.datasets import make_blobs

dc=int(input('데이터의 개수 입력 : '))
x, y = make_blobs(n_samples=dc, centers=4, random_state=2,n_features=2,cluster_std=2)

dt = DecisionTreeClassifier(max_depth=3,random_state=42)
dt.fit(x,y)

plt.figure(figsize=(20,15))
plot_tree(dt,filled=True)
plt.show()