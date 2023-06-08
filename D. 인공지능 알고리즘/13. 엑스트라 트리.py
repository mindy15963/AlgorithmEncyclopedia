# 엑스트라 트리(Extra Tree)
# 랜덤 포레스트와 마찬가지로 여러 개의 결정 트리를 훈련하지만, 랜덤 포레스트와 다르게 부트스트랩 샘플을 사용하지 않는다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import make_moons
import mglearn as mg

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,stratify=y,random_state=42)

et = ExtraTreesClassifier(n_estimators=5, random_state=2)
et.fit(x_train,y_train)

plt.rcParams['font.family']='Malgun Gothic'
plt.title("엑스트라 트리")
mg.plots.plot_2d_separator(et, x, fill=True, alpha=0.5)
mg.discrete_scatter(x[:,0], x[:,1], y)
plt.show()

print("훈련 세트 정확도 : {:.3f}".format(et.score(x_train,y_train)))
print("테스트 세트 정확도 : {:.3f}".format(et.score(x_test,y_test)))