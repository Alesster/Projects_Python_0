from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "IMG_Test/3.png", "IMG_test/secret_sms.txt")
secret.save("IMG_test/3_secret.png")