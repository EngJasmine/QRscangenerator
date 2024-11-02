# QRscangenerator
A web application that allows users to easily create QR codes linked to any URL

This tool simplifies the process of generating scannable codes that can be used for various purposes, such as marketing, information sharing, or event management.
- User Input: Users can enter any valid URL into a text field.
- QR Code Generation: Upon submission, the application generates a QR code for the provided URL.
- Download Option: Users can download the generated QR code as a PNG image for offline use.
- Immediate Display: The QR code is displayed on the page after generation, allowing for quick verification.
- Responsive Design: The application is designed to be user-friendly and responsive across different devices and screen sizes.

Technical Details
- Framework: Built using Flask, a lightweight Python web framework that allows for rapid development and easy deployment.
- QR Code Library: Utilizes the qrcode library to generate QR codes dynamically based on user input.
- Front-End: Features an intuitive HTML interface styled with CSS for a clean and modern look.
- Image Handling: The application saves generated QR codes as PNG files in a designated static folder for easy access and downloading.
