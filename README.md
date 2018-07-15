# word_parser

RESTful micro-services application for word counter for url using tornado web server and mysql database

## Uses docker-compose for the different parts of the application

### app
   Uses a Dockerfile to build docker image with python 2.7 and its requirements.txt file.
   Copies src/ code and templates/ to docker application container
   Runs tornado http server
   build: app/ specifies the directory which contains the Dockerfile containing the instructions for building this service
   ports: 8888
   
### db
   Creates a db words_t for creating words_t table.
   build: specifies the directory which contains the Dockerfile containing the instructions for building this service
   ports: 3600

## REST API
I created a RESTful python web application using Tornado web server.
Need to add code for ssl/tls and for running server with multiple threads.

### GET "http://127.0.0.1:8888/"
  I created a python web application using Tornado web server.
  A. The project has a single page with a form (app/templates/templateForm.html).
  B. Form receives a url in string format.
  C. Once the url is submitted, redirects to POST handler for "http://127.0.0.1:8888/".

### POST "http://127.0.0.1:8888/"
  A. POST Handler receives url from GET "http://127.0.0.1:8888/".
  
  B. POST Handler builds a dictionary that contains the frequency of use of each word on that page.
  
  C. POST Handler uses this dictionary to display, on the client’s browser, a “word cloud” of the top 100 words, where
  the font size is largest for the words used most frequently, and gets progressively smaller for
  words used less often. Words with same frequency have same size.
  (using app/templates/template200.html)
  D. POST Handler updates MySQL DB words_t table with the following columns : 
   1) The primary key for the word is a salted hash of the word.
   2) The word itself is saved in a column that has asymmetrical encryption, and you are saving the encrypted version of the word.
   3) The total frequency count of the word.
  E. POST handler in case something is wrong i.e. url submitted sends an error back to the browser using template500.html

### GET "http://127.0.0.1:8888/admin"
  A. Lists all words retrieved from mysql db (using app/templates/template200admin.html), ordered by frequency of usage, visible in decrypted form.
  
## Testing

There is a bash file which runs 4 unit tests  
```
bash run_unit_tests.sh
```

Alternatively you can run explicitily tests (make sure to setup PYTHONPATH firstly to app/src code):
```
python -m unittest TestHashUtils
```
```
python -m unittest TestEncryptUtils
```
```
python -m unittest TestRetrieveUtilsRequest
```

```
python -m unittest TestRetrieveUtilsWordParser
```
