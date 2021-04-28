import os
from cryptography.fernet import Fernet
from genpasskey import genpasskey

class filedecryptor(object):

    @staticmethod
    def decryptfile(filename,password):

        pkey=genpasskey.passkey(password)
        cipher = Fernet(pkey)

        with open(filename, 'rb') as df: 
            encrypted_data = df.read()

        decrypted_file = cipher.decrypt(encrypted_data)

        os.remove(filename)

        with open(filename, "wb") as df: 
            df.write(decrypted_file)