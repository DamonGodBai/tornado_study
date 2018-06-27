from .base_handler import  BaseHandler
from models import Star

class StarHandle(BaseHandler):

    def get(self, *args, **kwargs):
        # star = Star('God',20).save()
        # star = Star.all()
        star = Star.filter(name = 'lili', age = 18)
        # print(star)
        self.data['status'] = self.success_status
        self.data['data'] = star
        self.data['msg'] = self.success_msg

        self.write(self.data)