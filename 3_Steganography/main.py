# pip install wheel steganocryptopy
# from stegano import lsb

# secret = lsb.hide("img/1.png", "Your password: hgfdjgfd")
# secret.save("img/1_pass.png")

# result = lsb.reveal("img/1_pass.png")
# print(result)

# from stegano import exifHeader

# secret = exifHeader.hide("img/1.jpg", "img/1_secret.jpg", "I am waiting you")
# result = exifHeader.reveal("img/1_secret.jpg")
# result = result.decode()
# print(result)

from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "img/3.png", "secret_sms.txt")
secret.save("img/3_secret.png")

result = Steganography.decrypt("key.key", "img/3_secret.png")
print(result)
with open(f'img/3_secret.txt', 'w') as text_file:
    text_file.write(result)