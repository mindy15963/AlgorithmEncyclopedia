# 라이트 GBM(LightGBM, LGBM)
# 트리 자료 구조를 기초로 한 그래디언트 부스팅 프레임워크이다.

from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

lgb = LGBMClassifier(random_state=42)
lgb.fit(x_train,y_train)
y_pred=lgb.predict(x_test)

print(f"정확도 : {accuracy_score(y_test,y_pred)}")