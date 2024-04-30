'''
Building a initial classification layers
'''
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop


# Input -> 150 x 150 x 3 (R, G, B)
image_input = layers.Input(shape=(256, 256, 3))

# 1º Convolution => 16 filters (3x3)
layers = layers.Conv2D(16, 3, activation = 'relu')(image_input)
layers = layers.MaxPooling(2)(layers) # 2x2 window

# 2º Convolution => 32 filters (3x3)
layers = layers.Conv2D(32, 3, activation = 'relu')(layers)
layers = layers.MaxPooling(2)(layers) # 2x2 window

# 3º Convolution => 64 filters (3x3)
layers = layers.Conv2D(64, 3, activation = 'relu')(layers)
layers = layers.MaxPooling(2)(layers) # 2x2 window

# Flatten feature map to 1 dimension tensor
layers = layers.Flatten()(layers)

layers = layers.Dense(512, activatieon = 'relu')(layers)

# Nullifies the contribution of some neurons towards the next layer and leaves unmodified all others
layers = layers.Dropout(0.5)(layers)

output = layers.Dense(3, activation = 'softmax')(layers) # Distribute results between all classes (x + y + z = 100%)

model = Model(image_input, output)
model.summary()

# binary_crossentropy for binary classification
# RMSprop automates learning-rate tuning for us
model.compile(loss = 'binary_crossentropy',
              optimizer = RMSprop(lr = 0.0001),
              metrics = ['acc'])


# All images will be rescaled by 1./255
# + Data augmentation prevents overfitting by rotating, shiffiting, zooming, etc the images => Model will never see the exact same picture twice
train_data_generator = ImageDataGenerator(
                            rescale=1./255,
                            rotation_range=40,
                            width_shift_range=0.2,
                            height_shift_range=0.2,
                            shear_range=0.2,
                            zoom_range=0.2,
                            horizontal_flip=True
                        )

validation_data_generator = ImageDataGenerator(rescale=1./255)

# Flow training images in batches of 20 using validation_data_generator generator
train_generator = train_data_generator.flow_from_directory(
        '',  # Source directory for training images
        target_size = (150, 150),  # All images will be resized to 150x150
        batch_size = 20,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode = 'binary')

# Flow validation images in batches of 20 using val_datagen generator
validation_generator = validation_data_generator.flow_from_directory(
        '',  # Source directory for validation images
        target_size=(150, 150),
        batch_size=20,
        class_mode = 'binary')
