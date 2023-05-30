import json
import numpy as np
import cv2
import keras
import tensorflow as tf
import tensorflow
from tensorflow import keras
from glob import glob
import os
from tensorflow.keras.applications.resnet50 import ResNet50
#from keras import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')

with open('sample.json') as json_file:
    data = json.load(json_file)
print(data)
#подали фото из приложения
img_path = 'D:/projects/transfering_learning/images_folder/sources/Tsar Cannon/2-7.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model.predict(x)




'''
for l in label:
    if preds == l:
        print(l)
        exit
print("not found")
'''
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)

# Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]