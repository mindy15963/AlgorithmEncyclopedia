# 전이 학습(Transfer Learning)
# 사전에 학습된 인공 신경망 모델의 가중치를 새로운 문제에 재사용하는 방식이다.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from keras.applications.vgg16 import VGG16
from keras.datasets import cifar10

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

X_train = tf.image.resize(X_train, (224, 224))
X_test = tf.image.resize(X_test, (224, 224))
X_train = tf.keras.applications.vgg16.preprocess_input(X_train)
X_test = tf.keras.applications.vgg16.preprocess_input(X_test)

features_train = base_model.predict(X_train)
features_test = base_model.predict(X_test)

features_train = features_train.reshape(features_train.shape[0], -1)
features_test = features_test.reshape(features_test.shape[0], -1)

scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)

X_train, X_val, y_train, y_val = train_test_split(features_train, y_train, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_val = model.predict(X_val)
y_pred_test = model.predict(features_test)
train_accuracy = accuracy_score(y_train, y_pred_train)
val_accuracy = accuracy_score(y_val, y_pred_val)
test_accuracy = accuracy_score(y_test, y_pred_test)

print("훈련 정확도 : ", train_accuracy)
print("검증 정확도 : ", val_accuracy)
print("테스트 정확도 :", test_accuracy)