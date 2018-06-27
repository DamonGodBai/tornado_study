import os

BASE_DIR = os.path.dirname(__file__)


#http接口
options = {
    'port' : 8080,
}

#全局配置
settings = {
    "debug": True,
    "template_path": os.path.join(BASE_DIR, 'templates'),
    "static_path": os.path.join(BASE_DIR, 'static'),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "login_url": "/login",
    "xsrf_cookies": True,
}

# pymql数据库配置
mysql = {
    'host':"192.168.238.133",
    'user':"root",
    'password':'199187',
    'dbname':"tornado",
    'port':3306
}


# SQLAlchemy数据库连接
database_setting = {
    'database_type': 'mysql',  # 数据库类型
    'connector': 'pymysql',  # 数据库连接器
    'user_name': 'root',  # 用户名，根据实际情况修改
    'password': '199187',  # 用户密码，根据实际情况修改
    'host_name': '192.168.238.133',  # 在本机上运行
    'port':'3306',
    'database_name': 'tornado',
    }

