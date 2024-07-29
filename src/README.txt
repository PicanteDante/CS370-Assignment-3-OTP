# OTP and QR Code Generator

## Requirements
- Python 3.x
- Install dependencies: `pip install -r requirements.txt`

## Usage
- Generate QR Code: `./submission --generate-qr <user_id>`
- Generate OTP: `./submission --get-otp <secret>`

## Implementation
- `qr_code_generator.py`: Generates a QR code for Google Authenticator.
- `otp_generator.py`: Generates TOTP based on the current time.
- `main.py`: Main script to handle command-line arguments.

## Assumptions
- The QR code is saved as `<user_id>_qr.png`.
- The secret is printed to the console when generating the QR code.
