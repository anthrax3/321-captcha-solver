from io import BytesIO
import os
from os import path, listdir, makedirs
from random import choices
from captcha.image import ImageCaptcha
import config
from tqdm import tqdm

def generate_words(num_generate, charset, length):
    words = []
    for i in range(num_generate):
        s = ''.join(choices(charset, k=length))
        words.append(s)
    return words

def create_captchas(words, outfolder):
    image = ImageCaptcha(width=config.img_width, height=config.img_height)

    for i in tqdm(range(len(words)), desc="Generating captchas"):
        #create a captcha for each string
        captcha_text = words[i]
        image_path = os.path.join(outfolder, str(i)+'_'+captcha_text+'.png')
        image.write(captcha_text, image_path)

def make_captcha(num_generate=24000,outfolder=''):
    if(not path.isdir(outfolder) or not path.exists(outfolder)):
        makedirs(outfolder)
    length = config.captcha_length
    charset = config.charset

    words = generate_words(num_generate, charset, length)
    create_captchas(words, outfolder)

    print("Finished generating %d captchas" % num_generate)

make_captcha(24000, outfolder='captchas')
