# 결정 트리(Decision Tree)
# 데이터에 있는 규칙을 학습을 통해 자동으로 찾아내 트리 (Tree)기반의 분류 규칙을 만드는 것으로 이 모양이 나무를 닮아 트리 모델이다.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_blobs
from sklearn.tree import export_graphviz
from subprocess import check_call

dc=int(input('데이터의 개수 입력 : '))
x, y = make_blobs(n_samples=dc, centers=4, random_state=2,n_features=2,cluster_std=2)

tree_model = DecisionTreeClassifier(max_depth=3)
tree_model.fit(x,y)

export_graphviz(
    tree_model,
    out_file = './tree_model.dot',
    rounded=True,
    filled=True
)

check_call(['dot','-Tpng','tree_model.dot','-o','OutputFile.png'])

tm=img.imread('OutputFile.png')

plt.rcParams['font.family']='Malgun Gothic'
plt.title('결정 트리')
plt.imshow(tm)
plt.show()