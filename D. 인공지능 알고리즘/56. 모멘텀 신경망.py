# 모멘텀 신경망(Momentum Neural Network)
# 일반적인 신경망에 모멘텀 최적화 알고리즘을 적용한 모델이다.

import tensorflow as tf
from keras import layers

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)

model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

ep=int(input('학습 횟수 입력 : '))
model.fit(x_train, y_train, epochs=ep, batch_size=32, validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test)
print('테스트 손실도 :', test_loss)
print('테스트 정확도 :', test_acc)