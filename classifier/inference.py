from model import Classifier
import numpy as np
import tensorflow as tf

CHECKPOINT_PATH = 'checkpoints/checkpoint'

model = Classifier()
model.load_weights(CHECKPOINT_PATH)

IMG_PATH = ''
IMG_SIZE = (256, 256)

class_names=['fake', 'other', 'real']

img = tf.keras.utils.load_img(IMG_PATH, target_size=IMG_SIZE)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(f"Your audio is probably '{class_names[np.argmax(score)]}' with {100*np.max(score)}% confidence.")
