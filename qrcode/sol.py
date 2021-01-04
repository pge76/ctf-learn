from PIL import Image
from pyzbar.pyzbar import decode
import base64
import codecs


result = decode(Image.open('qrcode.39907201.png'))
str = codecs.decode(str(base64.b64decode(result[0].data.decode("utf-8"))), 'rot_13')

print (str)
