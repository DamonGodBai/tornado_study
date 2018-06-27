from .base_handler import BaseHandler
from tornado.httpclient import AsyncHTTPClient

class AsyncHandler(BaseHandler):
    def my_res(self, response):
        pass


    def get(self, *args, **kwargs):
        client = AsyncHTTPClient()
        url = ''
        client.fetch(url, callback=self.my_res)
        self.write('ok')