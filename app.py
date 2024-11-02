from flask import Flask, request, render_template, send_file
import qrcode
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_qr():
    url = request.form['url']
    if not url:
        return "No URL provided", 400

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img_path = 'static/qrcode.png'
    img.save(img_path)

    # Return to index and show the QR code
    return render_template('index.html', qr_code_url=img_path)


if __name__ == '__main__':
    app.run(debug=True)
