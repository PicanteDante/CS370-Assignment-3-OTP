import pyotp
import time


def generate_otp(secret):
    totp = pyotp.TOTP(secret)
    while True:
        print(totp.now())
        time.sleep(30)


if __name__ == "__main__":
    import sys
    secret = sys.argv[1]
    generate_otp(secret)
