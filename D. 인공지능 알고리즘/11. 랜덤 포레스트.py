# 랜덤 포레스트(Random Forest)
# 분류, 회귀 분석 등에 사용되는 앙상블 학습 방법의 일종으로, 훈련 과정에서 구성한 다수의 결정 트리로부터 부류(분류) 또는 평균 예측치(회귀 분석)를 출력함으로써 동작한다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
import mglearn as mg

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,stratify=y,random_state=42)

rf = RandomForestClassifier(n_estimators=10, random_state=0)
rf.fit(x_train,y_train)

plt.rcParams['font.family']='Malgun Gothic'
plt.title("랜덤 포레스트")
mg.plots.plot_2d_separator(rf, x, fill=True, alpha=0.5)
mg.discrete_scatter(x[:,0], x[:,1], y)
plt.show()

print("훈련 세트 정확도 : {:.3f}".format(rf.score(x_train,y_train)))
print("테스트 세트 정확도 : {:.3f}".format(rf.score(x_test,y_test)))