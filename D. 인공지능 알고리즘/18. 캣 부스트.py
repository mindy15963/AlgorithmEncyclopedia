# 캣 부스트 (CatBoost)
# 범주형 특성를 처리하는데 중점을 둔 알고리즘이다.

from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

ctb = CatBoostClassifier(iterations=2,depth=2,learning_rate=2,loss_function='Logloss',verbose=True)
ctb.fit(x_train,y_train)
y_pred=ctb.predict(x_test)

print(f"정확도 : {accuracy_score(y_test,y_pred)}")