# Generate
import pyqrcode

# Decode
from PIL import Image
from pyzbar.pyzbar import decode


def generate(url, name):
    qr = pyqrcode.create(url, error="H")
    qr.png(name, module_color=(0, 255, 0, 255), background=(0, 0, 0, 255), scale=5)


def decode(image):
    data = decode(Image.open(image))
    print(data)
