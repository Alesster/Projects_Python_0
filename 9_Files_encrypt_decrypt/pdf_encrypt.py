from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass

pdfwriter = PdfWriter()
pdf = PdfReader('Uchebnik_Docker.pdf')

for page in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page])
    
password = getpass(prompt='Enter pass: ')
pdfwriter.encrypt(password)

with open('Uchebnik_Docker_protected.pdf', 'wb') as file:
    pdfwriter.write(file)