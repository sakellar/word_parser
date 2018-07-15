import tornado.ioloop
import tornado.web
import mysql.connector
from control_tools import WordController



class FormHandler(tornado.web.RequestHandler):
    pass

class AdminHandler(tornado.web.RequestHandler):
    pass

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../templates/templateForm.html")

    def post(self):
        url = self.get_body_argument("message")
        print url
        config = {
        'user': 'root',
        'password': 'root',
        'host': '0.0.0.0',#db
        'port': '3306',
        'database': 'knights'
        }
        connection = mysql.connector.connect(**config)
        connection.close()

    """
    def post(self):
        try:
            url = self.get_body_argument("message")
            wctrl = WordController()
            items =  wctrl.get_statistics(url)
            self.set_status(200)
            self.render("../templates/template200.html", title="Word frequency url {}".format(url), items = items)
        except Exception as e:
            self.clear()
            self.set_status(500)
            self.render("../templates/template500.html", error=str(e))
    """
application = tornado.web.Application([
   (r"/", MainHandler),
   (r"/myform", FormHandler),
   (r"/admin", AdminHandler),
])
 
if __name__ == "__main__":
   print "hello from tornado"
   application.listen(8888)
   tornado.ioloop.IOLoop.instance().start()
