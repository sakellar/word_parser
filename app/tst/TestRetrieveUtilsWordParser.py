import unittest
from mock import patch, Mock, MagicMock, call
from retrieve_utils import WordParser
from collections import Counter


class TestRetrieveUtilsWordParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count_words1(self):
        word_parser = WordParser()
        #import requests
        #r = requests.get("http://www.nytimes.com/2009/12/21/us/21storm.html")
        word_parser.parse_words("<!DOCTYPE html>whatever a the another</html>") #(r.text)
        self.assertEquals(word_parser.counter, Counter())

    def test_count_words2(self):
        word_parser = WordParser()
        content = ""
        with open("tst/html_content", "r") as f:
            content  = f.read()
        word_parser.parse_words(content) 
        self.assertEquals(word_parser.counter, Counter({u'this': 1, u'a': 1, u'is': 1, u'test': 1}))

    def test_most_common_words(self):
        word_parser = WordParser()
        content = ""
        with open("tst/html_content", "r") as f:
            content  = f.read()
        word_parser.parse_words(content) 
        self.assertEquals(word_parser.most_common, [(u'this', 1), (u'a', 1), (u'is', 1), (u'test', 1)])
if __name__ == '__main__':
    unittest.main(buffer=False)
