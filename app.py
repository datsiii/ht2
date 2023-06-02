import numpy as np
import cv2
import keras
import tensorflow as tf
import tensorflow
from tensorflow import keras
from glob import glob
import os
import json

#импорт resnet50, распознает объеткы как церковь и тд
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

#обучаем
model = ResNet50(weights='imagenet')

import base64

from flask import Flask, request
from flask import g
import urllib.parse



app = Flask(__name__)

def get_index():
    if 'index' not in g:
        g.index = create_index()

    return g.db

def create_index(labels):
    index = dict()
    with open("sample.json", "r") as infile:
        result = json.load(infile)
        for landmark, value in labels.items():
            for categ, probab in value.items():
                if categ not in index or probab > index[categ][1]:
                    index[categ] = (landmark, probab)
    return index


@app.route('/')
def handle_request():
    return "Successful Connection"


@app.route('/api/recognize', methods=['GET', 'POST'])
def get_file():
    base64_img = request.form["sample"]

    # Get image from POST request
    with open('decoded_image.jpeg', 'wb') as file_to_save:
        # decoded_image_data = base64.decodebytes(base64_img_bytes)
        decoded_image_data = urllib.parse.unquote(base64_img)
        base64_img_bytes = decoded_image_data.encode('utf-8')
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

    # get image labels via ResNet
    img_path = os.path.join("path")
    img = image.load_img(img_path, target_size=(224, 224))
    # превращаем фото в numpy массив для того чтобы подать на вход нейросети
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    _, category, probability = decode_predictions(preds, top=1)[0][0]
    probability = float(probability)
    # preproces_image
    # preds = model.predict(x)


    # find matching landmark
    index = get_index()
    labels = create_index(index)
    # use index to search landmarks
    #answer = create_index(index)
    with open("sample.json", "r") as infile:
        result = json.load(infile)
        for landmark, value in labels.items():
            for categ, probab in value.items():
                if category == categ:
                    response = "landmark: " + str(landmark)
                    return response

    '''
    base64_bytes = base64_message.encode('ascii')
    message_bytes = b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    #text = request.form["sample"]
    #print(text)
    '''
    return "received"


app.run(host="0.0.0.0", port=5000, debug=True)