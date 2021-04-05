import tensorflow as tf
import os
from werkzeug.utils import secure_filename
import flask
import keras
from flask import Flask, render_template,request
from keras.models import load_model
from keras.preprocessing import image
from keras.optimizers import Adam
from keras.preprocessing import image
import cv2
import numpy as np
from keras.models import load_model
app = Flask(__name__)


#loading the model
model = load_model('models/CNN_G.h5')
# model.make_predict_function()

#preprocessing of the input image:


@app.route('/')
def home():
    return render_template('home.html')

COUNT = 0


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # global COUNT
        # Get the file from post request
        img = request.files['image']
        # img.save('static/{}.jpg'.format(COUNT)) #saving the pic
        FN = img.filename
        img.save('static/{}.jpg'.format(FN))
        # COUNT = COUNT + 1
        file_path = 'static/{}.jpg'.format(FN)
        img = image.load_img(file_path, target_size=(150, 150))
        # Preprocessing the image
        x = image.img_to_array(img)
        x = np.true_divide(x, 255)
        x = np.expand_dims(x, axis=0)

        # img_arr = cv2.imread(static/FN)
        # img_arr = cv2.resize(img_arr, (150, 150))
        # img_arr = img_arr / 255.0
        # img_arr = img_arr.reshape(1, 150, 150, 3)
        prediction = model.predict(x)
        if np.argmax(prediction) == 0:
            return 'Glacoma'
        else:
            return 'NON_Glacoma'
pip


if __name__ == '__main__':
    app.run(debug=True)