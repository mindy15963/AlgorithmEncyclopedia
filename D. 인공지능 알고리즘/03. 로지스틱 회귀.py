# 로지스틱 회귀 (Logistic Regression)
# 수학을 사용하여 두 데이터 요인 간의 관계를 찾는 데이터 분석 기법이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

dc=int(input('데이터의 개수 입력 : '))
x = []
y = []

for i in range(dc):
    for j in range(dc):
        x.append([i, j])

x = np.array(x)
np.random.shuffle(x)

for i in range(pow(dc,2)):
    if x[i, 0] * 2 + x[i, 1] > 150:
        y.append(1)
    else:
        y.append(0)

y = np.array(y)

lr = LogisticRegression().fit(x, y)
test_x = x[:30]
test_y = lr.predict(test_x[:, :])

plt.rcParams['font.family']='Malgun Gothic'
plt.title('로지스틱 회귀')
plt.xlabel('x 값')
plt.ylabel('y 값')

for i in range(30):
    if test_y[i] == 0:
        plt.scatter(test_x[i:i+1, 0], test_x[i:i+1, 1], c='red')
    else:
        plt.scatter(test_x[i:i+1, 0], test_x[i:i+1, 1], c='blue')

print(f'회귀 계수 : {lr.coef_}, 절편 : {lr.intercept_}')
x1, y1 = [-lr.intercept_ / lr.coef_[0][0], (-lr.intercept_ -lr.coef_[0][1]*100) / lr.coef_[0][0]], [0, 100]
plt.plot(x1, y1, color='black')
plt.show()