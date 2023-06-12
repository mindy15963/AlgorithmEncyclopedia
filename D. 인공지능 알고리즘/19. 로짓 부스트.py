# 로짓 부스트 (LogitBoost)
# 이진 분류 문제에 특화된 그래디언트 부스팅 알고리즘이다.

from sklearn.model_selection import train_test_split
from logitboost import LogitBoost
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

ctb = LogitBoost(n_estimators=200, random_state=0)
ctb.fit(x_train,y_train)
y_pred=ctb.predict(x_test)

print(f"정확도 : {accuracy_score(y_test,y_pred)}")