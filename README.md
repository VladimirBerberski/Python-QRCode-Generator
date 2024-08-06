# Python-QRCode-Generator 
# QR Code Generator with Logo

This Python application allows users to generate QR codes with optional embedded logos using a graphical user interface (GUI). The QR codes can be saved as images in PNG format.

## Features

- Generate QR codes from user-provided data.
- Optionally embed a logo at the center of the QR code.
- Save generated QR codes as PNG images.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `qrcode`
  - `PIL` (Pillow)
  - `tkinter` (usually comes pre-installed with Python)

## Installation

1. Install the required libraries using pip:

   pip install qrcode[pil]

2.Make sure Tkinter is installed. On most systems, it comes pre-installed with Python. If not, you can install it as follows:

For Debian-based systems (Ubuntu, etc.):

For Windows:
Tkinter is included in the standard Python distribution.

## Usage
  1.Run the script: python your_script_name.py
  
  2.Enter the data for the QR code in the provided input field.
  
  3.(Optional) Click the "Files" button to select an image file as the logo for the QR code.
  
  4.Click "Generate QR code" to create and display the QR code.
  
  5.The generated QR code will be displayed on the GUI, and you will be prompted to save it as a PNG file.


## GUI Components :
Data: Text input for the data to be encoded in the QR code.
Logo: File path input and button to select an optional logo image.
Generate QR code: Button to generate and display the QR code.
Image Display: Label widget that displays the generated QR code.

## License
This project is open-source and available under the MIT License.
