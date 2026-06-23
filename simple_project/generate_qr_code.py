import qrcode

url = input("Enter the URL: ").strip()
qr_name = input("Name of the QR Code: ").strip()
file_path = f"/Users/mifaniapaolo0012/Desktop/Python/simple_project/qrcodes/{qr_name}.png"


qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")