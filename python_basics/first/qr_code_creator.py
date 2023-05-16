import pyqrcode
import png
from pyqrcode import QRcode

address = 'URL'
url = pyqrcode.create(address)
url.png('test_qr.png', scale=8)
