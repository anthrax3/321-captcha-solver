import os.path
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import model_from_json
from config import weight_file, model_json, captcha_length, charset
num_filters1 = 32
num_filters2 = 64
num_filters3 = 64

pool_size = (2,2)
kernel_size=(3,3)

def load(input_shape):
    model = Sequential()
    if os.path.exists(weight_file):
        print("Loading a trained model")
        model = model_from_json(open(model_json).read())
        model.load_weights(weight_file)
    else:
        #Construct a new model and save it
        #Layer 1
        model.add(Conv2D(num_filters1, (kernel_size[0], kernel_size[1]), padding='valid', input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=pool_size))
        model.add(Dropout(0.25))
        #Layer 2
        model.add(Conv2D(num_filters2, (kernel_size[0], kernel_size[1])))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=pool_size))
        model.add(Dropout(0.25))
        #Layer 3
        model.add(Conv2D(num_filters3, (kernel_size[0], kernel_size[1])))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=pool_size))
        model.add(Dropout(0.25))

        # Fully connected layer
        model.add(Flatten())
        model.add(Dense(1024*captcha_length))
        model.add(Dense(512*captcha_length))
        model.add(Activation('relu'))
        model.add(Dropout(0.25))
        model.add(Dense(captcha_length*len(charset)))
        model.add(Activation('softmax'))

        #Save the model
        json_string = model.to_json()
        open("my_model.json","w").write(json_string)

    return model
