import sys
import config
from load_model import load
from load_data import load_one_image, get_max
from config import img_height, img_width, charset, captcha_length

model = load('');
model.compile(loss=config.loss_model,optimizer=config.optimizer, metrics=config.metrics)

def solve(filepath):
    img = load_one_image(filepath)
    cnn_input = img.reshape(img.shape[0], img_height, img_width, 1)
    cnn_input = cnn_input.astype('float32')
    #normalize input
    cnn_input /= 255

    cnn_output = model.predict(cnn_input)

    text = ''
    for i in range(cnn_input.shape[0]):
        true = []
        chars = []
        for j in range(captcha_length):
	        index = get_max(cnn_output[i,len(charset)*j:(j+1)*len(charset)])
	        c = charset[index]
	        chars.append(c)
    text = text.join(chars)
    return text

if len(sys.argv) == 2:
    filename = sys.argv[1]
    text = solve(filename)
    print (text)
else:
    print("Provide a file")
