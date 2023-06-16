# 반복 교차 검증 (Repeated Cross Validation)
# 데이터셋의 크기가 크지 않을 경우 안정된 검증 점수를 얻기 위해 교차 검증을 반복하여 여러 번 수행하는 교차 검증 방식이다.

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import *

ns=int(input('표본 데이터의 수 입력 : '))

x,y=make_moons(n_samples=ns,random_state=3)
lr = LogisticRegression()

rskfold = RepeatedStratifiedKFold(random_state=42)
scores = cross_val_score(lr, x, y, cv = rskfold)

print("교차 검증 점수 : \n", scores)
print("평균 정확도 : {:.3f}".format(scores.mean()))