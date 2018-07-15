"""module for retrieving and parsing words from a specific url"""
import requests
from requests import exceptions
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import Counter
from string import punctuation


class WordParser:
    """
       Class which retrieves words from url content/text
    """
    def __init__(self, configuration=None):
        self.lst = {}

    def parse_words(self, text):
        """method parses words from a text"""
        try:
            soup = BeautifulSoup(text, "html.parser")
            text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
            self.lst = text
        except Exception as e:
            raise Exception(str(e))

    @property
    def counter(self):
        """Method returns a collections counter"""
        try:
            c = Counter((x.rstrip(punctuation).lower() for y in self.lst for x in y.split()))
            return c
        except Exception as e:
            raise Exception(str(e))

    @property
    def most_common(self):
        try:
            c = Counter((x.rstrip(punctuation).lower() for y in self.lst for x in y.split()))
            return c.most_common(100)
        except Exception as e:
            raise Exception(str(e))
        

class Request:
    """
        Wrapper Class to parse http request
    """
    def __init__(self, url=""):
        """
            Constructor gets url
        """
        self.url = url
        self.content = None

    def get_request(self, method='GET'):
        """
            Wrapper method on requests get request
        """
        try: 
            response = requests.request(method='GET', url=self.url)
            return (response.status_code, response.text, response.headers)
        except exceptions.RequestException as err:
            raise Exception(str(err))
        except Exception as e:
            raise Exception(str(e))
