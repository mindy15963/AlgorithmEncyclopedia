# 생성적 적대 신경망(Generative Adversarial Network, GAN)
# 생성자와 식별자가 서로 경쟁하며 데이터를 생성하는 모델이다.

import numpy as np
import tensorflow as tf
import keras
import matplotlib.pyplot as plt

(x_train, _), (_, _) = keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32')
x_train = (x_train - 127.5) / 127.5

latent_dim = 100

generator = keras.Sequential([
    keras.layers.Dense(7 * 7 * 256, input_shape=(latent_dim,), use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.LeakyReLU(),
    keras.layers.Reshape((7, 7, 256)),
    keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.LeakyReLU(),
    keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.LeakyReLU(),
    keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh')
])

discriminator = keras.Sequential([
    keras.layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1]),
    keras.layers.LeakyReLU(),
    keras.layers.Dropout(0.3),
    keras.layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'),
    keras.layers.LeakyReLU(),
    keras.layers.Dropout(0.3),
    keras.layers.Flatten(),
    keras.layers.Dense(1)
])

loss_fn = keras.losses.BinaryCrossentropy(from_logits=True)

def generator_loss(fake_output):
    return loss_fn(tf.ones_like(fake_output), fake_output)

def discriminator_loss(real_output, fake_output):
    real_loss = loss_fn(tf.ones_like(real_output), real_output)
    fake_loss = loss_fn(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

generator_optimizer = keras.optimizers.Adam(1e-4)
discriminator_optimizer = keras.optimizers.Adam(1e-4)

ep=int(input('학습 횟수 입력 : '))
epochs = ep
batch_size = 128
num_batches = x_train.shape[0] // batch_size

for epoch in range(epochs):
    for batch in range(num_batches):

        batch_images = x_train[batch * batch_size: (batch + 1) * batch_size]

        noise = tf.random.normal([batch_size, latent_dim])

        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            generated_images = generator(noise, training=True)

            real_output = discriminator(batch_images, training=True)
            fake_output = discriminator(generated_images, training=True)

            gen_loss = generator_loss(fake_output)
            disc_loss = discriminator_loss(real_output, fake_output)

        gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

        generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
        discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

    if (epoch + 1) % 5 == 0:
        noise = tf.random.normal([10, latent_dim])
        generated_images = generator(noise, training=False)
        generated_images = (generated_images * 127.5 + 127.5).numpy()

        plt.figure(figsize=(10, 1))
        for i in range(10):
            ax = plt.subplot(1, 10, i + 1)
            plt.imshow(generated_images[i, :, :, 0], cmap='gray')
            plt.axis('off')
        plt.show()