import os
import tensorflow as tf
from model import Classifier
from .trainer import Trainer

EPOCHS = 100
BATCH_SIZE = 32
VALIDATION_SPLIT = 0.2

IMG_SIZE = (256, 256)

CHECKPOINT_PATH = 'checkpoints/checkpoint'
METRICS_PATH = 'metrics/metrics.png'
'''
dataset folder with the following structure:
main_directory/
    class_a/
        img1
        img2
        ...
    class_b/
        img1
        img2
        ...
    ...
'''
DATASET_PATH = ''

model = Classifier()
if os.path.exists(CHECKPOINT_PATH):
    model.load_weights(CHECKPOINT_PATH)

train_ds, test_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=VALIDATION_SPLIT,
    subset='both',
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE)

trainer = Trainer(model=model)
trainer.train(epochs=EPOCHS, train_ds=train_ds, test_ds=test_ds, checkpoint_path=CHECKPOINT_PATH, metrics_path=METRICS_PATH)
