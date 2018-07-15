import json
from collections import Counter, defaultdict
from retrieve_utils import Request, WordParser


class DB:
    pass

class Controller:
    def update_db(self):
        raise NotImplementedError
    def get_statistics(self, url):
        raise NotImplementedError

class WordController(Controller):
    def update_db(self):
        pass

    def transform_to_dict_list(self, most_common_list):
        """Transform most common words to dictionary for the template"""
        my_list = []
        font_size = 200.0
        previous_val = 0
        for list_item in most_common_list:
            try:
                if previous_val != list_item[1]:
                    previous_val = list_item[1]
                    font_size = font_size / 2.0
                word= list_item[0].encode('ascii')
                if not word.isalpha():
                    raise 
                dictionary  = {'word': word,'frequency':list_item[1], 'font':font_size}
                my_list.append(dictionary)
            except:
                #print "ignoring item"
                pass
        return my_list

    def get_statistics(self, url):
        """
            Sents a get request in uri
            parsers request results
            and transofrms them to list for template
        """
        request_obj = Request(url)
        res = request_obj.get_request()
        word_parser = WordParser()
        word_parser.parse_words(res[1])

        return self.transform_to_dict_list(word_parser.most_common)

# module test
url = "http://www.nytimes.com/2009/12/21/us/21storm.html"
wctrl = WordController()
dictionary =  wctrl.get_statistics(url)
