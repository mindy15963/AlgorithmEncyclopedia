# 컨볼루션 LSTM(Convolutional LSTM)
# 2D 공간적인 데이터에서 시간적인 특성을 고려하기 위해 컨볼루션과 LSTM을 결합한 모델로, 시계열 데이터를 처리하는 데 사용되는 인공 신경망 구조이다.

import numpy as np
import tensorflow as tf
from keras.layers import Input, ConvLSTM2D, Flatten, Dense
from keras.models import Model

inputs = np.random.randn(32, 10, 64, 64, 3)

input_shape = inputs.shape[1:]

input_layer = Input(shape=input_shape)
conv_lstm = ConvLSTM2D(filters=16, kernel_size=(3, 3), padding='same', return_sequences=True)(input_layer)
flatten = Flatten()(conv_lstm)
output_layer = Dense(units=1, activation='sigmoid')(flatten)

model = Model(inputs=input_layer, outputs=output_layer)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
ep=int(input('학습 횟수 입력 : '))
model.fit(inputs, np.random.randint(0, 2, size=(32, 1)), epochs=ep, batch_size=16, verbose=1)

test_inputs = np.random.randn(1, 10, 64, 64, 3)
predictions = model.predict(test_inputs)
print("예측 : ", predictions)