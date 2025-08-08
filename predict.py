import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

# Load image
img_path = 'test.jpg'  # Make sure the image is in the same folder
img = image.load_img(img_path, target_size=(224, 224))

# Convert to array
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Load model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Predict
preds = model.predict(x)

# Decode results
print("Prediction:", decode_predictions(preds, top=3)[0])
