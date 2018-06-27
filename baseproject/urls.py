import os

import tornado.web
from tornado.web import Application
from views import *
from config import *



class BaseApp(Application):
    def __init__(self):
        handlers = [
            (r"^/index$", IndexHandle),
            # (r"/(?P<page>\d+)", IndexHandle),
            # tornado.web.url(r"/home", HomeHandle, {'name' : 'tom'}, name='home')

            tornado.web.url(r"^/home$", HomeHandle,  name='home'),
            tornado.web.url(r"^/star$", StarHandle, name='star'),
            (r"^/test", Test2),

            #StaticFileHandler放在最下面
            (r"/(.*)$", tornado.web.StaticFileHandler, {'path':os.path.join(settings['static_path'], 'index.html')})
        ]

        super().__init__(handlers, **settings)
