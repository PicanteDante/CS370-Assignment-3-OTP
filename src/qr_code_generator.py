import qrcode
import pyotp


def generate_qr_code(user_id, secret):
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=user_id,
                                                   issuer_name="ConnorOlsen")
    img = qrcode.make(uri)
    img.save(f"{user_id}_qr.png")


if __name__ == "__main__":
    import sys
    user_id = "42"
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
    secret = pyotp.random_base32()
    generate_qr_code(user_id, secret)
    print(f"Secret: {secret}")
