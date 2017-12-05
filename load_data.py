import os
from PIL import Image
import numpy as np
import random
from config import img_height, img_width, captcha_length, charset, datafolder
from tqdm import tqdm

np.random.seed(0)

def load_grayscale(filename):
    img = Image.open(filename)
    #Grayscale
    img = img.convert('L')
    #Resize to fit our model
    img = img.resize((img_width, img_height), Image.BILINEAR)
    return img

def load_one_image(filename):
    data = np.empty((1,1,img_height,img_width), dtype="float32")
    img = load_grayscale(filename)

    arr = np.asarray(img, dtype="float32")
    data[0,:,:,:] = arr
    return data

def get_max(array):
    max_num = max(array)
    for i in range(len(array)):
        if array[i] == max_num:
            return i

def text2vec(text):
    vector = np.zeros(captcha_length*len(charset))
    for i, c in enumerate(text):
        index = i * len(charset) + charset.index(c)
        vector[index] = 1
    return vector

def load_data(total, training):
    y_len = captcha_length * len(charset)
    #Image data
    data = np.empty((total, 1, img_height, img_width), dtype="float32")
    #Labels
    label = np.empty((total, y_len), dtype="uint8")

    images = os.listdir(datafolder)
    num_images = len(images)
    for i in tqdm(range(num_images), desc="Creating dataset from images"):
        filename = images[i]
        img = load_grayscale(os.path.join(datafolder, filename))
        arr = np.asarray(img, dtype="float32")
        try:
            data[i,:,:,:] = arr
            captcha_text = filename.split('.')[0].split('_')[1]
            label[i] = text2vec(captcha_text)
        except:
            pass
    rand = [i for i in range(total)]
    #shuffle up the images for each epoch
    random.shuffle(rand)
    #split between training and testing data
    x_train = data[rand][:training]
    y_train = label[rand][:training]
    x_test = data[rand][training:]
    y_test = label[rand][training:]

    return (x_train, y_train), (x_test, y_test)
