'''
Data loading referenced from 
https://github.com/stekhn/tensorflow-captcha-solver/blob/master/solver/captcha_records.py
'''

from tensorflow.python.platform import gfile
import os
from PIL import Image
import numpy as np
from tqdm import tqdm

def create_data_list(captcha_dir):
    if not gfile.Exists(captcha_dir):
        print("Image directory" + captcha_dir + "not found")
        return None
    print("Extracing image data from " + captcha_dir)
    file_list = []
    file_glob = os.path.join(captcha_dir, '*.png')
    file_list.extend(gfile.Glob(file_glob))
    images = []
    labels = []
    for file_name in tqdm(file_list, desc="Loading image data"):
        img=Image.open(file_name, 'r')
        # Convert to grayscale
        img = img.convert('L')

        img_array = np.array(img, dtype='int16')
        img.close()
        label = os.path.basename(file_list[0]).split('_')[0].split(r'.')[0]

        images.append(img_array)
        labels.append(label)
    # create a list of pairs of images (as numpy arrays) and labels
    return zip(images, labels)

data = create_data_list('captchas')
print(next(data))
