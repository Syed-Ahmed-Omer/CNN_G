from flask import Flask, render_template,request
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
app = Flask(__name__)


#loading the model
model = load_model('models/CNN_G.h5')


@app.route('/')
def home():
    return render_template('home.html') #home page html


@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        img = request.files['image']
        FN = img.filename
        img.save('static/{}.jpg'.format(FN)) #saving the pic
        file_path = 'static/{}.jpg'.format(FN) #path where img will be stored
        img = image.load_img(file_path, target_size=(150, 150)) #loading the image
        # Preprocessing the image
        x = image.img_to_array(img)
        x = np.true_divide(x, 255) #normalization of pixels
        x = np.expand_dims(x, axis=0) #to get shape of (1, 150, 150, 3) as req by model

        #prediction
        prediction = model.predict(x)
        if np.argmax(prediction) == 0:
            return 'Glacoma'
        else:
            return 'NON_Glacoma'


if __name__ == '__main__':
    app.run(debug=True)