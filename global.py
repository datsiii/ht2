import numpy as np
import cv2
import keras
import tensorflow as tf
import tensorflow
from tensorflow import keras
from glob import glob
import os
import json

tf.keras.applications.resnet50.ResNet50(
    include_top=True,
    weights='imagenet',
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    #**kwargs
)

from tensorflow.keras.applications.resnet50 import ResNet50
#from keras import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')

#img_path = 'elephant.1.jpg'
'''
for filename in glob('*.png'):
    process_image(cv2.imread(filename))
'''

path = 'D:/projects/transfering_learning/images_folder/sources'
filelist = set()
for root, dirs, files in os.walk(path):
    for file in files:
        filelist.add(os.path.join(root))

label = dict()
for name in filelist:
    #print(name)
    folderName = os.path.basename(name)
    #print(folderName)
    fds = sorted(os.listdir(name))
    for img in fds:
        if img.endswith(('.jpg', '.png')):
            #print(img)
            #print(os.path.join(path, folderName, img))
            img_path = os.path.join(path,folderName, img)
            img = image.load_img(img_path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            preds = model.predict(x)
            print('Predicted:', decode_predictions(preds, top=3)[0])
            _, category, probability = decode_predictions(preds, top=1)[0][0]
            probability = float(probability)
            label[folderName] = {category:probability}
            break

with open("sample.json", "w") as outfile:
    #json_object = json.dumps(str(label), indent = 4)
    json.dump(label, outfile)
#print(json_object)


def create_index(labels):
    index = dict()
    for landmark, value in labels.items():
        for categ, probab in value.items():
            if categ not in index or probab > index[categ][1]:
                index[categ] = (landmark, probab)
    return index


with open("sample.json", "r") as infile:
    result = json.load(infile)
    print(create_index(result))
