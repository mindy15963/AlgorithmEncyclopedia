# 릿지 회귀 (Ridge Regression)
# 기존 선형 모델에 규제항을 추가한 회귀 모델이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

dc=int(input('데이터의 개수 입력 : '))
x = 5 * np.random.rand(dc,1)
y = 2 * x +1 + np.random.rand(dc,1)

av=float(input('알파 값 입력 : '))
ridge = Ridge(alpha = av)
ridge.fit(x,y)
pv1=int(input('예측할 값 1 입력 : '))
pv2=int(input('예측할 값 2 입력 : '))
a = ridge.predict([[pv1]])
b = ridge.predict([[pv2]])

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.title('릿지 회귀')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.plot(x, y, "b.",label = "데이터")
plt.plot([pv1,pv2],[a[0],b[0]],"r--",label = "예측")
plt.legend()
plt.show()

print(f'회귀 계수 : {ridge.coef_}, 절편 : {ridge.intercept_}')