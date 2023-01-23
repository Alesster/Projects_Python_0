import pyAesCrypt
import os
import sys

# file decryption function
def decryption(file, password):
    # Buffer size
    buffer_size = 512*1024
    
    # Ecryption method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    
    print("[File '" + str(os.path.splitext(file)[0]) + "' decrypted]")
    
    # Deleting source file
    os.remove(file)
    
# dir scanning function
def walking_by_dirs(dir, password):
    # subdir scanning
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # if find file then decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)
        
password = input("Enter your password: ")
walking_by_dirs("./Test_dir", password)
# If we work remotely it is better to delete our scripts:
#os.remove(str(sys.argv[0]))