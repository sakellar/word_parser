"""module for AES encryption decryption utils"""
from Crypto.Cipher import AES


class CryptoClass(object):
    """
        CryptroClass Constructor Wrapper for AES functions
    """
    def __init__(self, key):
        self.key = key
        self.crypto_obj = None

    def encrypt_message(self, message):
        """Encrypts a messag using AES.MODE_CBC"""
        self.crypto_obj = AES.new(self.key, AES.MODE_CBC, 'This is an IV456')
        return self.crypto_obj.encrypt(message)

    def decrypt_message(self, ciphertext):
        """Decrypts a messag using AES.MODE_CBC"""
        decrypt_obj = AES.new(self.key, AES.MODE_CBC, 'This is an IV456')
        return decrypt_obj.decrypt(ciphertext)
