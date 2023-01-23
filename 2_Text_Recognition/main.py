import pytesseract
from PIL import Image

#img = Image.open('phone_number.png')
img = Image.open('eng_text_long.png')
#img = Image.open('rus_text.png')
# For Windows it is necessary to indicate the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split(".")[0]

# Config is used if result is not exact
#custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='eng', config = custom_config)
print(text)

#with open('phone_number.txt', 'w') as text_file:
with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)