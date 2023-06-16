# 그룹별 교차 검증 (Group K-Fold Cross Validation)
# 데이터 안에 매우 연관된 그룹이 있을 때 사용하는 교차 검증 방식이다.

import matplotlib.pyplot as plt
import mglearn
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold

ns=int(input('표본 데이터의 수 입력 : '))
nsp=int(input('반복 분할 횟수 입력 : '))
groups = list(map(int, input('그룹 입력 : ').split()))

x,y=make_blobs(n_samples=ns, random_state=0)

lr = LogisticRegression()
gkf=GroupKFold(n_splits=nsp)
gkf.get_n_splits(x,y,groups)

for train_index, test_index in gkf.split(x, y, groups):
    print("훈련 :", train_index, "테스트 :", test_index)
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    print(x_train, x_test, y_train, y_test)
    
mglearn.plots.plot_group_kfold()
plt.show()