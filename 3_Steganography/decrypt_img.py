from steganocryptopy.steganography import Steganography

result = Steganography.decrypt("key.key", "IMG_Test/3_secret.png")
print(result)
with open(f'IMG_Test/3_secret.txt', 'w') as text_file:
    text_file.write(result)