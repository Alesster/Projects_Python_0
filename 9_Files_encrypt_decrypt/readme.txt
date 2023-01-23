Simple files Ecryption-Decryption and PDF Ecryption:
https://www.youtube.com/watch?v=4w4sSabOjl0&list=PLqGS6O1-DZLoAADhgzzkvc8ifKsKG4G-T&index=37

For enryption or decryption of files we need the module pyAesCrypt:
pip install pyAesCrypt
then
import pyAesCrypt

PDF files Ecryption:
pip install pypdf2

To generate password use: 
from getpass import getpass


In pyPDF v.3.0.0 many commands are changed with respect to older version:
PdfFileReader => PdfReader
PdfFileWriter => PdfWriter

pdf.numPages => len(pdf.pages)

pass = 123