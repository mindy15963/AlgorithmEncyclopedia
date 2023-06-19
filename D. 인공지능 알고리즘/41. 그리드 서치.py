# 그리드 서치 (Grid Search)
# 모델의 성능을 가장 높게 하는 최적의 하이퍼파라미터를 찾는 방법이다.

from sklearn.datasets import make_moons
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

ns=int(input('표본 데이터의 수 입력 : '))

x,y=make_moons(n_samples=ns,random_state=3)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)
x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size=0.5, random_state=42)

dt = DecisionTreeClassifier(random_state=42)

params = {'max_depth': [2, 3, 4, 5], 'min_samples_split' : [2,3]}

gs = GridSearchCV(dt, params, n_jobs=-1)
gs.fit(x_train, y_train)
print('점수 : ',gs.score(x_val, y_val))
print('최적의 파라미터 : \n',gs.best_params_)
print('최상의 교차 검증 점수 : ',gs.best_score_)

estimator = gs.best_estimator_
y_pred = estimator.predict(x_val)
print('정확도 : ',accuracy_score(y_val, y_pred))