from .base_handler import  BaseHandler
from models import User

class Test2(BaseHandler):

    def get(self, *args, **kwargs):
        user = self.db.query(User).all()
        self.db.commit()
        data = [{'user_name':i.user_name, 'pass_word':i.pass_word} for i in user]
        self.data['status'] = self.success_status
        self.data['data'] = data
        self.data['msg'] = self.success_msg
        self.write(self.data)