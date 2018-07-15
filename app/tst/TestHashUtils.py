import unittest
from mock import patch, Mock, MagicMock, call
from hash_utils import HashUtils
from collections import Counter


class TestHashUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hash_salt1(self):
        hash_result = HashUtils('word')
        hash_result.salt = 1
        expected_result = 4197332404371457004
        self.assertEquals(expected_result, hash(hash_result))

    def test_hash_salt21(self):
        hash_result = HashUtils('word')
        expected_result = 4197332404371457004
        self.assertNotEqual(expected_result, hash(hash_result))

if __name__ == '__main__':
    unittest.main(buffer=False)
