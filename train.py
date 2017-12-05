#Use GPU
import os
os.environ["THEANO_FLAGS"] = "mode=FAST_RUN,device=cuda*,floatX=float32"

import numpy as np
np.random.seed(0)

from keras.models import Sequential
from keras.utils import np_utils
from keras import backend as K
from load_data import *
import h5py
from keras.callbacks import ModelCheckpoint

import config
from config import captcha_length, img_height, img_width
from load_model import load
from load_data import get_max

#load the dataset
(X_train, Y_train), (X_test, Y_test) = load_data(config.num_generated, config.num_train)

#reshape the datasets
X_train = X_train.reshape(X_train.shape[0], img_height, img_width, 1)
X_test = X_test.reshape(X_test.shape[0], img_height, img_width, 1)
input_shape = (img_height, img_width, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
#normalize the training data
X_train /= 255
X_test /= 255
print("Loaded dataset:")
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

model = load(input_shape)

model.compile(loss=config.loss_model, optimizer=config.optimizer, metrics = config.metrics)
weights = config.weight_file
#Whenever accuracy improves, saved the trained model
checkpoint = ModelCheckpoint(weights, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

model.fit(X_train, Y_train, batch_size=config.batch_size, epochs=config.epochs, verbose=1, validation_data=(X_test,Y_test), callbacks=callbacks_list)

score = model.evaluate(X_test, Y_test, verbose=0)
predict = model.predict(X_test, batch_size=config.batch_size, verbose = 0)


#Test the data
acc = 0
for i in range(X_test.shape[0]):
    true = []
    predictions = []
    for j in range(captcha_length):
        true.append(get_max(Y_test[i,len(charset)*j:(j+1)*len(charset)]))
        predictions.append(get_max(predict[i,len(charset)*j:(j+1)*len(charset)]))
    if true == predictions:
        acc+=1
    if i<20:
        print (i,' true: ',true)
        print (i,' predict: ',predictions)
print('predict correctly: ',acc)
print('total prediction: ',X_test.shape[0])
print('Score: ',score)
