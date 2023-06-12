# 에이다 부스트 (AdaBoost)
# 이전 모델이 과소적합했던 학습 샘플의 가중치를 더 높여 다음 모델에서 다시 학습을 시키는 개념으로 새로운 예측기(모델)는 학습하기 어려웠던 데이터(샘플)에 대해 점점 더 잘 맞춰지는 모델로 만들 수 있다.

from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

ab = AdaBoostClassifier(n_estimators=50,learning_rate=1)
ab.fit(x_train,y_train)
y_pred=ab.predict(x_test)

print(f"정확도 : {accuracy_score(y_test,y_pred)}")