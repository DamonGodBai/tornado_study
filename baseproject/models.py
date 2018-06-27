from mysql_orm import BaseModels
from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey, Float
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
'''
write your template like this:

class ModelName(BaseModels):
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''
#基于mysql_orm的验证表
class Star(BaseModels):
    def __init__(self, name, age):
        self.name = name
        self.age = age



#基于sqlalchemy
class User(Base):
    #注意一定要设置一项为primary_key
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    user_name = Column(VARCHAR(20))
    pass_word = Column(VARCHAR(40))
