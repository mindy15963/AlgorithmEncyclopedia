# NG 부스트 (NG Boost)
# 확률론적 예측을 위한 자연 그래디언트 부스팅이다.

from sklearn.model_selection import train_test_split
from ngboost import NGBRegressor
from sklearn.datasets import make_moons
from sklearn.metrics import mean_squared_error

dc=int(input('데이터의 개수 입력 : '))
x, y = make_moons(n_samples=dc, noise=0.25, random_state=3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

ngb = NGBRegressor().fit(x_train,y_train)
y_preds = ngb.predict(x_test)
y_dists = ngb.pred_dist(x_test)

test_MSE = mean_squared_error(y_preds, y_test)
print('평균제곱오차 값 : ', test_MSE)

test_NLL = -y_dists.logpdf(y_test).mean()
print('음의 로그우도 값 : ', test_NLL)