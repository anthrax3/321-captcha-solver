from io import BytesIO
from os import path, listdir, makedirs
from random import randint, choices
from captcha.image import ImageCaptcha
import string
from tqdm import tqdm

def generateCaptchas(amt, outfolder='', minlength=3, maxlength=8):
    assert(minlength <= maxlength)
    if(not path.isdir(outfolder) or not path.exists(outfolder)):
        makedirs(outfolder)

    image = ImageCaptcha()
    strings = []

    for i in range(amt):
        #determine a random length between minlength and maxlength:
        length = randint(minlength,maxlength)
        val = ''.join(choices(string.ascii_uppercase + string.digits, k=length))
        strings.append(val)
    for i in tqdm(range(len(strings)), desc="Generating captchas"):
        #create a captcha for each string
        captcha_text = strings[i]
        captcha_path = outfolder + '/' + captcha_text + '.png'
        if(not path.exists(captcha_path)):
            #write the captcha only if one doesn't exist
            image.write(captcha_text, captcha_path)
    print("Finished generating %d captchas" % amt)

generateCaptchas(10000, outfolder='captchas')
