# XG 부스트(eXtream Gradient Boosting)
# 최적화된 분산 그래디언트 부스팅 알고리즘을 구현하는 오픈소스 머신러닝 라이브러리이다.

from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

xgb = XGBClassifier(tree_method='hist',random_state=42)
xgb.fit(x_train,y_train)
y_pred=xgb.predict(x_test)

print(f"정확도 : {accuracy_score(y_test,y_pred)}")