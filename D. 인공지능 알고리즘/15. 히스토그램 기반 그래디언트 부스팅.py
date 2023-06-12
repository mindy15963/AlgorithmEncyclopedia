# 히스토그램 기반 그래디언트 부스팅 (Histogram-based Gradient Boosting)
# 앙상블 학습 기법 중 하나로, 여러 개의 결정 트리를 조합하여 예측 모델을 구축하는 알고리즘이다.

from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

hgb = HistGradientBoostingClassifier(random_state=42)
hgb.fit(x_train,y_train)
y_pred=hgb.predict(x_test)

print(f"정확도 : {accuracy_score(y_test,y_pred)}")