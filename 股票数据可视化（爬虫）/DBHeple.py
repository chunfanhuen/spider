"""
面向对象方法，封装操作数据库类
"""
import pymysql


class MyDBmySQL:
    # 初始化数据库加载
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="baidu123", database="test")
        # 创建游标
        self.cursor = self.conn.cursor()

    #     销毁
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("数据库资源已经关闭")

    #     添加数据
    def add(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print("数据库插入成功")

    #     修改数据
    def update(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print("数据库更新成功")

    #     删除数据
    def delete(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print("数据删除成功")

    #     查询所有数据
    def findAll(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
