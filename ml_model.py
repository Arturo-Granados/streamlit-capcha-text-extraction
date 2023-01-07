#Set up 
import numpy as np
import tensorflow as tf
#from tensorflow import keras

#import os
import joblib 
from PIL import Image
import cv2

#Load ml model 
model = tf.keras.models.load_model("result_model.h5")

#Read info store
#importando el dectionario info 
info_path = "info.pkl"
info = joblib.load(info_path)


#Function to clean and preproces images 
def adap_threshold_img(img):
  return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 145, 0)

def closing_img(img):
  return cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((5,2), np.uint8))

def dilatation_img(img):
  return cv2.dilate(img, np.ones((2,2), np.uint8), iterations = 1)

def smooting_img(img):
  return cv2.GaussianBlur(img, (1,1), 0)

def read_image(img_path):
  return cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


def get_demo(img_path):
    
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    
    img = adap_threshold_img(img)
    img = closing_img(img)
    img = dilatation_img(img)
    img = smooting_img(img)
    
    image_list = [img[10:50, 30:50], img[10:50, 50:70], img[10:50, 70:90], img[10:50, 90:110], img[10:50, 110:130]]
    
    
    Xdemo = []
    for i in range(5) :
        Xdemo.append(tf.keras.utils.img_to_array(Image.fromarray(image_list[i])))
    
    Xdemo = np.array(Xdemo)
    Xdemo/= 255.0
    
    ydemo = model.predict(Xdemo)
    ydemo = np.argmax(ydemo, axis = 1)
    
    result = ''
    for res in ydemo :
        result += info[res]
    
    return result


def show_adap_threshold_img(image):
  img = read_image(image)
  return adap_threshold_img(img)


def image_segmantation(image):
  image = cv2.rectangle(image, (30,12), (50,49), 0, 1)
  image = cv2.rectangle(image, (50,12), (70,49), 0, 1)
  image = cv2.rectangle(image, (70,12), (90,49), 0, 1)
  image = cv2.rectangle(image, (90,12), (110,49),0, 1)
  image = cv2.rectangle(image, (110,12),(130,49),0, 1)
  return image