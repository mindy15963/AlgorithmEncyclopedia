# 엘라스틱넷 회귀 (Elastic Net Regression)
# 릿지 회귀와 라쏘 회귀를 결합한 모델이다.
# 가중치의 절대값의 합과 제곱합을 동시에 제약 조건으로 가지는 모형이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet

dc=int(input('데이터의 개수 입력 : '))
x = 5 * np.random.rand(dc,1)
y = 2 * x +1 + np.random.rand(dc,1)

av=float(input('알파 값 입력 : '))
en = ElasticNet(alpha = av)
en.fit(x,y)
pv1=int(input('예측할 값 1 입력 : '))
pv2=int(input('예측할 값 2 입력 : '))
a = en.predict([[pv1]])
b = en.predict([[pv2]])

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.title('엘라스틱넷 회귀')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.plot(x, y, "b.",label = "데이터")
plt.plot([pv1,pv2],[a[0],b[0]],"r--",label = "예측")
plt.legend()
plt.show()

print(f'회귀 계수 : {en.coef_}, 절편 : {en.intercept_}')