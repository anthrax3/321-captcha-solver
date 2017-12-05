import string

#We use numbers and uppercase letters for captcha
numbers = string.digits
uc_alphabet = string.ascii_uppercase

charset = numbers+uc_alphabet

#Length of captchas
captcha_length = 5

#Image sizes
img_width = 150
img_height = 50
