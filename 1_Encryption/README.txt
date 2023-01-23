Ecryption-Decryption of files:
https://www.youtube.com/watch?v=rJ0RZxxfJ1g&list=PLqGS6O1-DZLoAADhgzzkvc8ifKsKG4G-T

For enryption or decryption of files we need the module pyAesCrypt:
pip install pyAesCrypt
then
import pyAesCrypt
Docs: https://pypi.org/project/pyAesCrypt/

In VSCode the program works only from Terminal with command lines:
python encryption.py

If we work remotely it is better to delete our scripts, for this use 
import sys

os.remove(str(sys.argv[0]))