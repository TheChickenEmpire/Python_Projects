import segno
from pyzbar.pyzbar import decode
from PIL import Image
while True:
    a = input('1 for incoder \n2 for decoder:\n')
    if a == '1':
        code = input("Input content: \n")
        qrcode = segno.make_qr(code)
        qrcode.save(
            "Qr code.png",
            scale=100,
        )
    elif a == '2':
        try:
            an = input('File to qr code:\n')
            decocdeQR = decode(Image.open(an))
            print(decocdeQR[0].data.decode('ascii'))
        except:
            print('File not found')