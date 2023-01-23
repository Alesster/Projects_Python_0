https://www.youtube.com/watch?v=jawXqaypsJY
Program in Python remove background

First install rembg:
pip install rembg[gpu] - gpu means using graphic card for removing background

During the installation can be Error:
ERROR: Cannot uninstall 'llvmlite'
To solve it do next(https://bobbyhadz.com/blog/python-error-cannot-uninstall-llvmlite):
pip install --ignore-installed llvmlite
and again 
pip install rembg[gpu]

During the test run can appear Error:
/usr/local/lib/python3.7/site-packages/paramiko/transport.py:236: CryptographyDeprecationWarning: Blowfish has been deprecated
"class": algorithms.Blowfish,

To solve it do next(https://github.com/paramiko/paramiko/issues/2038):
pip install fabric
pip uninstall -y cryptography # uninstall 37.0.0
pip install cryptography==36.0.2

To download the models. 
All models are downloaded and saved in the user home folder in the .u2net directory(ex: Users/aless/.u2net):
https://github.com/danielgatis/rembg

file_name = input_path.stem - stem returns file name

If it is necessary Set Up a Virtual Python Environment:
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

