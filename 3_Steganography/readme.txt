Стеганогра́фия (от греч. στεγανός «скрытый» + γράφω «пишу»; букв. «тайнопись») — способ передачи или хранения информации с учётом сохранения в тайне самого факта такой передачи (хранения).

Labrary:
pip install stegano

lsb works with png (jpg does not work), problem wirh cyrillic
from stegano import lsb

secret = lsb.hide("url-input", "text")
secret.save("url-output")

# reveal - to print "text"
result = lsb.reveal("img/1_pass.png")
print(result)

======================================
exifHeader works with jpg
from stegano import exifHeader

secret = exifHeader.hide("url-input", "url-output", "text")

=======================================
Key generation for decryption
pip install wheel steganocryptopy

from steganocryptopy.steganography import Steganography

=======================================
ERROR:
IF used:
secret = lsb.hide("img\a.png", "Your password: grymza")

OSError: [Errno 22] Invalid argument: img\x07.png

First: one need to use slash / instead of backslash \
secret = lsb.hide("img/a.png", "Your password: grymza")

Second: the error x07 => one need to type the URL manually instead of copying it. 