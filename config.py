import string
import math

'''CAPTCHA CONFIG'''
#We use numbers and uppercase letters for captcha
numbers = string.digits
uc_alphabet = string.ascii_uppercase
charset = numbers+uc_alphabet
#Length of captchas
captcha_length = 5
#Image sizes
img_width = 150
img_height = 50
datafolder="captchas"

'''DATASET CONFIG'''
num_generated = 24000
train_percentage = 0.75
num_train = int(math.floor(24000 * train_percentage))

'''CNN CONFIG'''
epochs = 64
batch_size=128
weight_file='weights.h5'
model_json='modelconfig.json'
loss_model='categorical_crossentropy'
optimizer='adadelta'
metrics=['accuracy']
