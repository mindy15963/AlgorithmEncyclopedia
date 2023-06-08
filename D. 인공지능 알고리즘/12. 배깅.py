# 배깅(Bagging)
# bootstrap aggregating의 줄임말로 통계적 분류와 회귀 분석에서 사용되는 기계 학습 알고리즘의 안정성과 정확도를 향상시키기 위해 고안된 일종의 앙상블 학습법의 메타 알고리즘이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import *
from sklearn.datasets import make_blobs
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

dc=int(input('데이터의 개수 입력 : '))
x, y = make_blobs(n_samples=dc, centers=4, random_state=2,n_features=2,cluster_std=2)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=22)

bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=1000, max_samples=0.5,bootstrap=True, n_jobs=1)

bagging.fit(x_train, y_train)
y_pred = bagging.predict(x_test)
print(f'정확도 : {accuracy_score(y_test, y_pred)}')