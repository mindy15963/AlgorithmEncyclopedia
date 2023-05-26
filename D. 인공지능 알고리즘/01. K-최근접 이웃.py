# K-최근접 이웃(K-NN, K-Nearest Neighbor)
# 데이터로부터 거리가 가까운 'k'개의 다른 데이터의 레이블을 참조하여 분류하는 알고리즘이다.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

dc=int(input('데이터의 갯수 입력 : '))
x_arr = [list(map(int, input('x 데이터 값 입력 : ').split())) for _ in range(dc)]
y_arr = list(map(int, input('y 데이터 값 입력 : ').split()))

x_data=np.array(x_arr)
y_data=np.array(y_arr)

labels = ['불일치', '일치']

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=777, stratify=y_data)

model = KNeighborsClassifier()

model.fit(x_train, y_train)

print(f'트레인 데이터 점수 : {model.score(x_train, y_train)}')
print(f'테스트 데이터 점수 : {model.score(x_test, y_test)}')

pv=x_arr = [list(map(int, input('예측할 값 입력 : ').split())) for _ in range(1)]
x_test = np.array(pv)

y_predict = model.predict(x_test)
label = labels[y_predict[0]]
y_predict = model.predict_proba(x_test)
confidence = y_predict[0][y_predict[0].argmax()]

print(f'예측 결과 : {label}\n신뢰도 : {confidence}')