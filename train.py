import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image_dataset_from_directory
import os

# ==== PATH TO YOUR IMAGES ====
data_dir = r"C:\Users\Ayushi Rathour\.cursor\Python Model\dataset\PlantVillage"

# ==== LOAD DATA ====
batch_size = 32
img_size = (224, 224)

train_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

val_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

# ✅ FIX: grab class names BEFORE prefetch
class_names = train_ds.class_names

# ==== OPTIMIZE LOADING ====
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

# ==== MODEL ====
base_model = MobileNetV2(input_shape=img_size + (3,), include_top=False, weights='imagenet')
base_model.trainable = False  # freeze base layers

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(len(class_names), activation='softmax')  # ✅ USE FIXED class_names
])

# ==== COMPILE ====
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ==== TRAIN ====
epochs = 10
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)

# ==== SAVE ====
model.save("plant_disease_model.h5")
print("✅ Model saved as plant_disease_model.h5")
