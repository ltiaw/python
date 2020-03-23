from memory_pic import *
import os
import base64


def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()

get_pic(cat_ico, 'cat_ico')
# 在这里使用图片 icon.ico
os.remove('cat_ico')
