# 임의 분할 교차 검증 (Shuffle-Split Cross Validation)
# 반복 횟수를 훈련 세트나 테스트 세트의 크기와 독립적으로 조절해야 할 때 유용한 교차 검증 방식이다.

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit

ns=int(input('표본 데이터의 수 입력 : '))
tes=float(input('테스트 세트 비율 입력 : '))
trs=float(input('훈련 세트 비율 입력 : '))
nsp=int(input('반복 분할 횟수 입력 : '))

x,y=make_moons(n_samples=ns,random_state=3)

lr = LogisticRegression()
shuffle_split = ShuffleSplit(test_size = tes, train_size = trs, n_splits=nsp)
scores = cross_val_score(lr,x,y,cv=shuffle_split)

print("교차 검증 점수 : \n", np.round(scores, 3))