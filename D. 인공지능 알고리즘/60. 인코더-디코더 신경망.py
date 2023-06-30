# 인코더-디코더(Encoder-Decoder) 신경망
# 입력을 압축하고 잠재 표현을 생성하는 인코더와, 잠재 표현을 사용하여 출력을 생성하는 디코더로 구성된 신경망으로 기계 번역, 자연어 생성 등의 작업에 사용된다.

import tensorflow as tf

id=list(map(int, input('입력 데이터 입력 : ').split()))
td=list(map(int, input('대상 데이터 입력 : ').split()))

input_data = [id]
target_data = [td]

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(len(id),), activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(len(id), activation='linear')
])

model.compile(optimizer='adam', loss='mse')
ep=int(input('학습 횟수 입력 : '))
model.fit(input_data, target_data, epochs=ep, verbose=0)

predicted_data = model.predict(input_data)
print("예측 : ", predicted_data)