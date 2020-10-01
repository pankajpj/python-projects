import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=4,
)
data=("ente your url")
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
