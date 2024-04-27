import tensorflow as tf

# CNN model sketch:
def generate_model():
    model = tf.keras.Sequential([
        # image in grayscale (1 color dimension) with 256x256 px resolution
        tf.keras.layers.Rescaling(1./255, input_shape=(256,256,1)),

        tf.keras.layers.Conv2D(16, (16,16), activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

        tf.keras.layers.Conv2D(32, (16,16), activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

        tf.keras.layers.Conv2D(64, (16,16), activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax') # three outputs: true, false or other
    ])

    return model
