# 그래디언트 부스팅(Gradient Boosting)
# 이전 학습의 결과에서 나온 오차를 다음 학습에 전달해 이전의 오차(잔여 오차)를 점진적으로 개선하는 부스팅 기법이자 앙상블 기법이다.

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import make_moons

dc=int(input('데이터의 개수 입력 : '))
md=int(input('최대 깊이 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

gb = GradientBoostingClassifier(max_depth=md)
gb.fit(x_train,y_train)

print("훈련 세트 정확도 : {:.3f}".format(gb.score(x_train,y_train)))
print("테스트 세트 정확도 : {:.3f}".format(gb.score(x_test,y_test)))