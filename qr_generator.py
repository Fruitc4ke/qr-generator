import qrcode

# Ask user for hyperlink
url = input("Quel lien voulez-vous convertir en QR code ?: ")

if not url.startswith("http"):
    print("! Attention : une URL doit commencer par http ou https !")

# Generate QR code
qr = qrcode.make(url)

# Save image
qr.save("generated_qr.png")

print("QR code saved as generated_qr.png")