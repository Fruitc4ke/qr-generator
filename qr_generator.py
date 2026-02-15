import sys
import qrcode

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print("Please provide a URL")
    sys.exit()

qr = qrcode.make(url)
qr.save("generated_qr.png")

print("QR code saved as generated_qr.png")
