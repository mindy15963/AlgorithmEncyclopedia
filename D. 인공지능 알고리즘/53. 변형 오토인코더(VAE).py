# 변형 오토인코더(Variational Autoencoder, VAE)
# 생성 모델 중 하나로, 데이터의 잠재 표현을 학습하는 동시에 새로운 샘플을 생성하는 능력을 가지고 있다.

import numpy as np
import tensorflow as tf

(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 28 * 28) / 255.0
x_test = x_test.reshape(-1, 28 * 28) / 255.0

latent_dim = 2
input_shape = x_train.shape[1]

encoder_inputs = tf.keras.Input(shape=(input_shape,))
x = tf.keras.layers.Dense(256, activation='relu')(encoder_inputs)
z_mean = tf.keras.layers.Dense(latent_dim)(x)
z_log_var = tf.keras.layers.Dense(latent_dim)(x)

def sampling(args):
    z_mean, z_log_var = args
    epsilon = tf.keras.backend.random_normal(shape=(tf.keras.backend.shape(z_mean)[0], latent_dim))
    return z_mean + tf.keras.backend.exp(0.5 * z_log_var) * epsilon

z = tf.keras.layers.Lambda(sampling)([z_mean, z_log_var])

decoder_inputs = tf.keras.Input(shape=(latent_dim,))
x = tf.keras.layers.Dense(256, activation='relu')(decoder_inputs)
outputs = tf.keras.layers.Dense(input_shape, activation='sigmoid')(x)

encoder = tf.keras.Model(encoder_inputs, [z_mean, z_log_var, z], name='encoder')
decoder = tf.keras.Model(decoder_inputs, outputs, name='decoder')

vae_inputs = encoder_inputs
vae_outputs = decoder(encoder(encoder_inputs)[2])
vae = tf.keras.Model(vae_inputs, vae_outputs, name='vae')

reconstruction_loss = tf.keras.losses.binary_crossentropy(encoder_inputs, vae_outputs)
reconstruction_loss *= input_shape
kl_loss = 1 + z_log_var - tf.keras.backend.square(z_mean) - tf.keras.backend.exp(z_log_var)
kl_loss = tf.keras.backend.sum(kl_loss, axis=-1)
kl_loss *= -0.5
vae_loss = tf.keras.backend.mean(reconstruction_loss + kl_loss)

vae.add_loss(vae_loss)
vae.compile(optimizer='adam')

ep=int(input('학습 횟수 입력 : '))
vae.fit(x_train, epochs=ep, batch_size=128, validation_data=(x_test, None))

_, _, z_samples = encoder.predict(x_test, batch_size=128)

random_samples = np.random.normal(size=(10, latent_dim))
generated_samples = decoder.predict(random_samples)

import matplotlib.pyplot as plt
n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    ax.axis('off')
plt.show()