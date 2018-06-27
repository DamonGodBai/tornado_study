
import tornado.ioloop
from config import options,settings
from urls import BaseApp




if __name__ == "__main__":
    app = BaseApp()
    app.listen(options['port'])
    tornado.ioloop.IOLoop.current().start()