import pyAesCrypt

password = input('Enter your pass: ')

# Encrypt
pyAesCrypt.encryptFile('readme.txt', 'readme.txt.aes', password)

# Decrypt
#pyAesCrypt.decryptFile('readme.txt.aes', 'readmeout.txt', password)