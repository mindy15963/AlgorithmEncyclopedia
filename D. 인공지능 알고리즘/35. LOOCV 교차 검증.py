# LOOCV 교차 검증 (Leave-One-Out Cross Validation, LOOCV)
# 폴드 하나에 샘플 하나만 들어 있는 k-겹 교차 검증으로 각 반복에서 하나의 데이터 포인트를 선택해 테스트 세트로 사용한다.

from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut

ns=int(input('표본 데이터의 수 입력 : '))

x,y=make_moons(n_samples=ns,random_state=3)

lr = LogisticRegression()
loo = LeaveOneOut()

scores = cross_val_score(lr,x,y,cv=loo)

print("교차 검증 분할 횟수 : ", len(scores))
print("평균 정확도 : {:.2f}".format(scores.mean()))