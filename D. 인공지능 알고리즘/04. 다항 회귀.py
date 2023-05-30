# 다항 회귀 (Polynomial Regression)
# 데이터 각 특성의 제곱을 추가하여 확장된 특성을 포함하여 선형 회귀 모델을 훈련 시키는 방법이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

dc=int(input('데이터의 개수 입력 : '))
x = 4 * np.random.rand(dc, 1) - 1
y = 1.5 * x**2 + x + 5 + np.random.rand(dc, 1)

poly = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly.fit_transform(x)

lr = LinearRegression()
lr.fit(x_poly, y)

xx = np.linspace(-1, 3, dc)
xx_poly = poly.transform(xx.reshape(-1, 1))
y_pred = lr.predict(xx_poly)

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.title('다항 회귀')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.scatter(x, y, s=3)
plt.plot(xx, y_pred, 'r-', label = 'pred')
plt.legend()
plt.show()

print(f'회귀 계수 : {lr.coef_}, 절편 : {lr.intercept_}')