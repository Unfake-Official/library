import os
import tensorflow as tf
from model import Classifier
from trainer import Trainer
import matplotlib.pyplot as plt

EPOCHS = 100
BATCH_SIZE = 32
VALIDATION_SPLIT = 0.2

IMG_SIZE = (256, 256)

CHECKPOINT_PATH = 'checkpoints'
METRICS_PATH = 'metrics/metrics.png'
'''
dataset folder with the following structure:
main_directory/
    fake/
        img1
        img2
        ...
    other/
        img1
        img2
        ...
    real/
        img1
        img2
        ...
'''
DATASET_PATH = r'C:\Users\mcsgo\OneDrive\Documentos\Dataset'

model = Classifier()
# if os.path.exists(CHECKPOINT_PATH):
#     model.load_weights(CHECKPOINT_PATH)
# else:
#     os.mkdir(CHECKPOINT_PATH)

train_ds, test_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    label_mode='categorical',
    color_mode='grayscale',
    validation_split=VALIDATION_SPLIT,
    subset='both',
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE)

trainer = Trainer(model=model)
trainer.train(epochs=EPOCHS, train_ds=train_ds, test_ds=test_ds, checkpoint_path=CHECKPOINT_PATH, metrics_path=METRICS_PATH)
