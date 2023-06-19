# 반복 교차 검증 (Repeated K-Fold Cross Validation)
# 데이터셋의 크기가 크지 않을 경우 안정된 검증 점수를 얻기 위해 교차 검증을 반복하여 여러 번 수행하는 교차 검증 방식이다.

from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import *

ns=int(input('표본 데이터의 수 입력 : '))

x,y=make_moons(n_samples=ns,random_state=3)
lr = LogisticRegression()

rsfold = RepeatedKFold(random_state=42)
scores = cross_val_score(lr, x, y, cv = rsfold)

print("교차 검증 점수 : \n", scores)
print("평균 점수 : {:.3f}".format(scores.mean()))