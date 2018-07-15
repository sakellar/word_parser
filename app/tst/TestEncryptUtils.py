import unittest
from mock import patch, Mock, MagicMock, call
from encrypt_utils import CryptoClass


class TestEncryptUtils(unittest.TestCase):
    """TestEncryptUtils"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_encrypt_decrypt(self):
        crypto_object = CryptoClass("This is a key123")
        message = "The answer is no"
        cipher = crypto_object.encrypt_message(message)
        self.assertEquals(crypto_object.decrypt_message(cipher), message)

if __name__ == '__main__':
    unittest.main(buffer=False)
