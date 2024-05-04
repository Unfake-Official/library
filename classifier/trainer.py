import tensorflow as tf
import matplotlib.pyplot as plt

class Trainer:
    def __init__(self, model: tf.keras.Model):
        self.model = model
        self.loss_obj = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        self.optimizer = tf.keras.optimizers.Adam()

        # loss metrics
        self.train_loss = tf.keras.metrics.MeanSquaredError(name='train_loss')
        self.train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')
        self.test_loss = tf.keras.metrics.MeanSquaredError(name='test_loss')
        self.test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')

        # metrics history
        self.train_loss_history = []
        self.train_accuracy_history = []
        self.test_loss_history = []
        self.test_accuracy_history = []


    def plot(self, output):

        plt.figure(figsize=(10,10))
        # n_rows, n_columns, index
        plt.subplot(2, 1, 1)
        plt.plot(self.train_accuracy_history, label='Training Accuracy')
        plt.plot(self.test_accuracy_history, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.ylabel('Accuracy')
        plt.xlabel('Epochs')
        plt.title('Training and Validation Accuracy')

        plt.subplot(2, 1, 1)
        plt.plot(self.train_loss_history, label='Training Loss')
        plt.plot(self.test_loss_history, label='Validation Loss')
        plt.legend(loc='lower right')
        plt.ylabel('Loss')
        plt.xlabel('Epochs')
        plt.title('Training and Validation Loss')

        plt.savefig(output)

    @tf.function
    def train_step(self, images, labels):
        with tf.GradientTape() as tape:
            predictions = self.model(images, training=True)
            loss = self.loss_obj(labels, predictions)
        gradients = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))

        self.train_loss(loss)
        self.train_accuracy(labels, predictions)

    @tf.function
    def test_step(self, images, labels):
        predictions = self.model(images, training=False)
        loss = self.loss_obj(labels, predictions)

        self.test_loss(loss)
        self.test_accuracy(labels, predictions)

    def train(self, epochs: int, train_ds, test_ds, checkpoint_path: str, metrics_path: str):
        for _ in range(epochs):
            self.train_loss.reset_states()
            self.train_accuracy.reset_states()
            self.test_loss.reset_states()
            self.test_accuracy.reset_states()

            for train_images, train_labels in train_ds:
                self.train_step(train_images, train_labels)

            for test_images, test_labels in test_ds:
                self.test_step(test_images, test_labels)

            self.train_loss_history.append(self.train_loss.result())
            self.train_accuracy_history.append(self.train_accuracy.result())

            self.test_loss_history.append(self.test_loss.result())
            self.test_accuracy_history.append(self.test_accuracy.result())

            self.model.save_weights(checkpoint_path)

        self.plot(metrics_path)
