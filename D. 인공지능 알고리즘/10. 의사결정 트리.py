# 의사결정 트리 (Decision Tree)
# 데이터에 있는 규칙을 학습을 통해 자동으로 찾아내 트리 기반의 분류 규칙을 만드는 것으로 이 모양이 나무를 닮아 트리 모델이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import *
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

dc=int(input('데이터의 개수 입력 : '))
x, y = make_blobs(n_samples=dc, centers=4, random_state=2,n_features=2,cluster_std=2)

dt = DecisionTreeClassifier(max_depth=3,random_state=42)
dt.fit(x,y)

plt.rcParams['font.family']='Malgun Gothic'
plt.figure(figsize=(20,15))
plot_tree(dt,filled=True)
plt.title("의사결정 트리")
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=22)

y_pred_tree = dt.predict(x_test)
print(f'정확도 : {accuracy_score(y_test, y_pred_tree)}')