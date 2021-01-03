# apt-get install libzbar0 libzbar-dev
# pip install zbarlight # you can also use setuptools directly
# pip install pypng zbar pillow qrtools

from PIL import Image
from pyzbar.pyzbar import decode
import base64
import codecs


result = decode(Image.open('qrcode.39907201.png'))
str = codecs.decode(str(base64.b64decode(result[0].data.decode("utf-8"))), 'rot_13')

print (str)