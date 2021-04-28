import os
import re
from cryptography.fernet import Fernet
from genpasskey import genpasskey

class filencryptor(object):

    @staticmethod
    def encryptfile(filename,password):   
        #textpass = password.text()
        pkey=genpasskey.passkey(password)

        cipher = Fernet(pkey)

        with open(filename,'rb')as f: 
            e_file = f.read()
            encrypted_file = cipher.encrypt(e_file)
        
        os.remove(filename)

        with open(filename, "wb") as ef: 
            ef.write(encrypted_file)