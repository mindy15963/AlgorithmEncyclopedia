# 장단기 메모리 (Long Short Term Memory, LSTM)
# 기존의 RNN이 출력과 먼 위치에 있는 정보를 기억할 수 없다는 단점을 보완하여 장/단기 기억을 가능하게 설계한 신경망의 구조이다.

import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

data = np.arange(10).reshape((10, 1))

X = data[:-1]
y = data[1:]

model = Sequential()
model.add(LSTM(10, input_shape=(1, 1)))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')

ep=int(input('학습 횟수 입력 : '))
model.fit(X, y, epochs=ep, verbose=0)

new_data = np.array([[-1], [10]])
predictions = model.predict(new_data)

print('예측값 : \n',predictions)