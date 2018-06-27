# import json
from .base_handler import BaseHandler

from tornado.web import StaticFileHandler

class IndexHandle(BaseHandler):
    def get(self, *args, **kwargs):
        data_dict = {
            'name': 'tom',
            'age': '18',

        }
        data_list = ['jackma', 'damen', 'lili', 'david']
        #基于jinja2
        self.set_secure_cookie(name='user',value='1')

        #专门用来设置_xsrf Cookie的接口
        self.xsrf_token

        self.render_html("home.html", data_dict=data_dict, data_list=data_list)
        #反向解析
        # url = self.reverse_url('home')
        # self.redirect(url)

    def post(self, *args, **kwargs):
        message = self.get_body_argument('message')
        print(message)



class HomeHandle(BaseHandler):

    def get(self, *args, **kwargs):
    # def get(self, page, *args, **kwargs):
        data = {
            'name': "Tom",
            'age': '19',
            'height': '170'
        }
        # Content-Type 属性为text/html
        # self.write(json.dumps(data))

        # Content-Type 属性为application/json
        self.write(data)
        # self.redirect('/')




