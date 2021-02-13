# pip3 install pillow
# pip3 install qrcode

import qrcode

img = qrcode.make(input("Enter some data: "))
img.save("qr_code.jpg")
