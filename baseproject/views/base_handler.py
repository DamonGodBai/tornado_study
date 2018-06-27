import tornado.web
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from enum import Enum, unique
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import database_setting


#返回json数据是的常用属性
@unique
class Status(Enum):
    success = 0
    failed = 1
    method = 2
@unique
class Msg(Enum):
    success = 'success'
    failed = 'failed'
    method = 'method error'


class TemplateRendring(object):

    """
    A simple class to hold methods for rendering templates.
    """

    def render_template(self, template_name, **kwargs):
        template_dirs = []
        if self.settings.get('template_path', ''):
            template_dirs.append(self.settings['template_path'])
        env = Environment(loader=FileSystemLoader(template_dirs))

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        content = template.render(kwargs)
        return content

    # 就是重新写 BaseHandler 由jinja2模板渲染


class BaseHandler(tornado.web.RequestHandler, TemplateRendring):
    """
    Tornado RequestHandler subclass.
    """

    def initialize(self):

        #初始化常用数据属性
        self.success_status = Status.success.value
        self.failed_status = Status.failed.value
        self.method_status = Status.method.value

        self.success_msg = Msg.success.value
        self.failed_msg = Msg.failed.value
        self.method_msg = Msg.method.value
        self.data = {}

    @property
    def db(self):
        engine = create_engine(  # 生成连接字符串，有特定的格式
            database_setting['database_type'] +
            '+' +
            database_setting['connector'] +
            '://' +
            database_setting['user_name'] +
            ':' +
            database_setting['password'] +
            '@' +
            database_setting['host_name'] +
            ':' +
            database_setting['port'] +
            '/' +
            database_setting['database_name']
        )

        #获取连接
        db = scoped_session(sessionmaker(bind=engine,autocommit=False, autoflush=True,expire_on_commit=False))
        return db



    def get_current_user(self):
        user = self.get_secure_cookie('user')
        return user if user else None

    def render_html(self, template_name, **kwargs):
        kwargs.update({
            'settings': self.settings,
            'STATIC_URL': self.settings.get('static_url_prefix', '/static/'),
            'request': self.request,
            'current_user': self.current_user,
            'xsrf_token': self.xsrf_token,
            'xsrf_form_html': self.xsrf_form_html,
        })
        content = self.render_template(template_name, **kwargs)
        self.write(content)