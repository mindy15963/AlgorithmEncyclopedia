# 게이트 순환 유닛 (Gated Recurrent Unit, GRU)
# 장기 의존성 문제를 해결하기 위해 제안된 순환 신경망(RNN) 구조이다.

import numpy as np
from keras.models import Sequential
from keras.layers import GRU, Dense

data = np.arange(10).reshape((10, 1))

X = data[:-1]
y = data[1:]

model = Sequential()
model.add(GRU(10, input_shape=(1, 1)))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')

ep=int(input('학습 횟수 입력 : '))
model.fit(X, y, epochs=ep, verbose=0)

new_data = np.array([[-1], [10]])
predictions = model.predict(new_data)

print('예측값 : \n',predictions)