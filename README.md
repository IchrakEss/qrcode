QR Code Generator
This project provides a simple Python script to generate custom QR codes with personalized colors and optional logo integration. The script uses the qrcode library for QR code generation and the Pillow library to customize the output image.

Features
Generate QR codes for any URL.
Customize the QR code with your choice of foreground and background colors.
Optionally add a logo to the center of the QR code (currently commented out in the script).
Requirements
Python 3.x
qrcode library
Pillow library
Installation
Clone this repository:

bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
Install the required dependencies:

bash
pip install -r requirements.txt
Or install the libraries individually:

bash
pip install qrcode[pil] Pillow
Usage
Update the data variable with the URL or information you want to encode in the QR code.

python
data = "https://example.com"
Run the script to generate the QR code:

bash
python generate_qrcode.py
The QR code will be saved as custom_qrcode.png in the same directory.

Optional: Add a Logo
Uncomment the following lines in the script to add a logo in the center of the QR code:

python
# logo = Image.open("logo.png").resize((50, 50))
# pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
# img.paste(logo, pos)
Ensure you have a logo.png file in the same directory as the script.