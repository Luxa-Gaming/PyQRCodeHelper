# Generate
import pyqrcode
qr = pyqrcode.create("", error="H")
qr.png("qrcode.png", module_color=(0, 255, 0, 255), background=(0, 0, 0, 255), scale=5)

# Decode
from PIL import Image
from pyzbar.pyzbar import decode

data = decode(Image.open(""))
print(data)
