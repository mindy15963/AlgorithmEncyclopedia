# k-겹 교차 검증 (K-fold Cross Validation)
# 데이터를 k개로 분할한 뒤, k-1개를 학습용 데이터 세트로, 1개를 평가용 데이터 세트로 사용하는데, 이 방법을 k번 반복하여 k개의 성능 지표를 얻어내는 방법이다.

from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

ns=int(input('표본 데이터의 수 입력 : '))
c=int(input('겹수 입력 : '))

x,y=make_moons(n_samples=ns,random_state=3)

lr = LogisticRegression()
kfold = KFold(n_splits = c)
reg = LinearRegression()

print("1. 분류 모델 교차 검증 점수 (분할기 사용) : \n", cross_val_score(lr, x, y, cv=kfold))
print("2. 회귀 모델 교차 검증 점수 (분할기 사용) : \n", cross_val_score(reg, x, y, cv=kfold))
print("3. 분류 교차 검증 점수 (정수 사용) : \n", cross_val_score(lr, x, y, cv=5))
print("4. 회귀 교차 검증 점수 (정수 사용) : \n", cross_val_score(reg, x, y, cv=5))