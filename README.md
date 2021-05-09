# CNN_G
QUICK INTRO THE MODEL:
1. This is a POC for classification of Glaucoma and Non-Glaucoma images of the eyes.
2. This model is built on top of Convolutional Neural Network for feature extraction and then it is then feed 
   to Dense Feed Forward Neural Netwrok.
3. Models takes input as retinal images of the eyes, then pre-process it as required by the the model and gives the prediction.
4. Model is stable and accurate as it has been tested on unseen images and closely examined.
5. Model is built on Google Colab.
6. Model is deployed on local machine using Flask framework.

QUICK GUIDE ABOUT THE FILES:
$ models : folder has the serialized CNN model as CNN_G.h5
$ Static : folder where the uploaded images during testing are saved.
$ templates : folder contain the basic html frontend file as home.html
$ CNN_final.ipynb : main.py file of project.
$ app.py : app.py where the model is buit on top of Flask frmawork.
