from .MySQL import MySQL
from config import mysql

class BaseModels(object):

    def save(self):
        '''
        增加数据操作,只支持int和str
        '''
        #获取表名
        tableName = (self.__class__.__name__).lower()
        fieldsStr = valuesStr='('
        #拼接出sql语句
        #获取实例对象的 key,valus
        for field in self.__dict__:
            fieldsStr += (field + ',')
            if isinstance(self.__dict__[field],str):
                valuesStr += ("'" + self.__dict__[field] + "',")
            else:
                valuesStr += (str(self.__dict__[field]) + ",")
        fieldsStr = fieldsStr[:len(fieldsStr)-1] + ")"
        valuesStr = valuesStr[:len(fieldsStr)-1] + ")"
        sql = 'insert into {} {} values{}'.format(tableName, fieldsStr, valuesStr)
        # print(sql)
        db = MySQL()
        db.to_mql(sql)

    def delete(self):
        pass

    def update(self,**kwargs):
        pass
        # tableName = (self.__class__.__name__).lower()
        # for key, valus in kwargs.items():
        #     print(key, valus)
        #
        # sql = "update {} set {}={} where {}={} and {}={}".format(tableName)

    @classmethod
    def filter(cls,**kwargs):
        '''
        只支持and操作,数据类型为int,str
        Star.filter(name = 'lili', age = 18)
        '''
        tableName = (cls.__name__).lower()
        fieldsStr = ''
        for key, valus in kwargs.items():
            # print(key, valus)
            if isinstance(valus,str):
                fieldsStr += key + '=' + "'" + valus + "'" + ' and '
            else:
                fieldsStr += key + '=' + str(valus) + ' and '
        fieldsStr = fieldsStr.rstrip(' and ')
        # print(fieldsStr)
        sql = "select * from {} where {}".format(tableName, fieldsStr)
        print(sql)

        #进行数据库操作
        db = MySQL()
        db.to_mql(sql=sql)
        results = db.cursor.fetchall()
        print(results)
        # ((1, 'jack', 16), (2, 'mike', 17), (3, 'lili', 18), (4, 'God', 20))
        column_list = BaseModels.column_name(tableName)
        # 处理查询的结果
        results_list = []
        for obj in results:
            results_one = {}
            for i in range(len(column_list)):
                results_one[column_list[i]] = obj[i]
            results_list.append(results_one)
        return results_list

    @classmethod
    def all(cls):
        '''
        获取表中所有的数据.返回信息列表
        [{'age': 16, 'id': 1, 'name': 'jack'}, {'age': 17, 'id': 2, 'name': 'mike'}]
        '''
        tableName = (cls.__name__).lower()
        sql = "select * from {}".format(tableName)
        # print(sql)
        db = MySQL()
        db.to_mql(sql)
        results = db.cursor.fetchall()
        #((1, 'jack', 16), (2, 'mike', 17), (3, 'lili', 18), (4, 'God', 20))
        column_list = BaseModels.column_name(tableName)
        #处理查询的结果
        results_list = []
        for obj in results:
            results_one = {}
            for i in range(len(column_list)):
                results_one[column_list[i]] = obj[i]
            results_list.append(results_one)
        return results_list

    @staticmethod
    def column_name(tableName):
        '''
        获取model的属性,也是数据库属性
        '''

        sql = 'select COLUMN_NAME from information_schema.columns where table_name='+ \
              "'"+ tableName + "'" + "and TABLE_SCHEMA=" +  "'" + mysql['dbname'] +  "'"
        # print(sql)
        db = MySQL()
        db.to_mql(sql)
        column = db.cursor.fetchall()
        column_list = [item[0] for item in column]
        return column_list

