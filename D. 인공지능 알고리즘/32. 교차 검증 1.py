# 교차 검증 (Cross Validation, CV)
# 데이터를 여러 번 반복해서 나누고 여러 모델을 학습하여 성능을 평가하는 방법이다.

from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression

ns=int(input('표본 데이터의 수 입력 : '))
c=int(input('겹수 입력 : '))

x,y=make_blobs(n_samples=ns)

lr = LogisticRegression()

basic_scores= cross_val_score(lr,x,y)
cv_scores= cross_val_score(lr,x,y,cv=c)

print('기본 교차 검증 점수 : ', basic_scores)
print(f'{c}겹 교차 검증 점수 : ', cv_scores)