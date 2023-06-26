# 순환 신경망 (Convolutional neural network, CNN)
# 순차 데이터나 시계열 데이터를 이용하는 인공신경망이다.

from keras.datasets import imdb

(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)

from sklearn.model_selection import train_test_split

train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)
    
import numpy as np

lengths = np.array([len(x) for x in train_input])

import matplotlib.pyplot as plt

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.hist(lengths)
plt.xlabel('길이')
plt.ylabel('주파수')
plt.show()

from keras_preprocessing.sequence import pad_sequences

train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)

from tensorflow import keras

model = keras.Sequential()

model.add(keras.layers.Embedding(500, 16, input_length=100))
model.add(keras.layers.SimpleRNN(8))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()

ep=int(input('학습 횟수 입력 : '))

rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model.compile(optimizer=rmsprop, loss='binary_crossentropy',metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-embedding-model.h5',save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3,restore_best_weights=True)

history = model.fit(train_seq, train_target, epochs=ep, batch_size=64,validation_data=(val_seq, val_target),callbacks=[checkpoint_cb, early_stopping_cb])

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('학습 횟수')
plt.ylabel('손실도')
plt.legend(['훈련', '검증'])
plt.show()