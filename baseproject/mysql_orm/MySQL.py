import pymysql
import config


#创建单例对象的装饰器
def out(cls, *args, **kwargs):
    instances = {}
    def inner():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return inner


@out
class MySQL(object):
    def __init__(self):
        host = config.mysql['host']
        user = config.mysql['user']
        password = config.mysql['password']
        dbname = config.mysql['dbname']
        port = config.mysql['port']
        self.conn = pymysql.connect(host=host, port=port, db=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()

    def to_mql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def __del__(self):
        self.conn.close()


