import qrcode
from PIL import Image

data = "https://exemple.fr" #URL 

# Paramètres de génération
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Génération d'image avec couleurs personnalisées
img = qr.make_image(fill_color="#233648", back_color="white").convert("RGB")

# # Ajouter un logo
# logo = Image.open("logo.png").resize((50, 50))
# pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
# img.paste(logo, pos)

# Sauvegarder le QR code
img.save("custom_qrcode.png")
