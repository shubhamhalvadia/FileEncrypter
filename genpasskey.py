import base64
from cryptography. hazmat. backends import default_backend
from cryptography.hazmat. primitives import hashes 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class genpasskey(object):
    
    @staticmethod
    def passkey(pass_from_user):


        password = pass_from_user.encode()

        mysalt = b'q\xe35\x3c\x19-\x17\xcb\x68\xC6A\xbBj\x64\x85'

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=mysalt, 
            iterations=10000,
            backend=default_backend()
            )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        return key.decode()
