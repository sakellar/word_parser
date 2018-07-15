"""module for AES encryption decryption utils"""
from Crypto.Cipher import AES


class CryptoClass(object):
    """
        CryptroClass Constructor Wrapper for AES functions
    """
    def __init__(self, key):
        self.key = key
        self.crypto_obj = None

    def pad_message(self, message):
        """Method to add pad to the message"""
        length = len(message)
        if length%16 !=0:
            modulo = length%16
            message  = message+(modulo*".")
            return message
        return message
            
    def reverse_pad_message(self, message):
        """Method to remove pad from the message"""
        return message.replace(".", "")

    def encrypt_message(self, message):
        """Encrypts a messag using AES.MODE_CBC"""
        message = self.pad_message(message)
        self.crypto_obj = AES.new(self.key, AES.MODE_CBC, 'This is an IV456')
        return self.crypto_obj.encrypt(message)

    def decrypt_message(self, ciphertext):
        """Decrypts a messag using AES.MODE_CBC"""
        decrypt_obj = AES.new(self.key, AES.MODE_CBC, 'This is an IV456')
        return self.reverse_pad_message(decrypt_obj.decrypt(ciphertext))
