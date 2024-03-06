"""
1.什么是js逆向
    请求发送的数据，服务器响应的数据是加密数据，一种密文，模拟登录时候需要提交密文，POST数据
2.常见的文件加密类型
    MD5加密     加密数据16或32位数字字母组合  26个字母+0-9 数字
    对称性加密    ASE
    非对称性加密  RSA
3.破解js加密
    1.找到加密的函数，全局搜索相关的函数名。
    2.一般是在js文件中，加密的算法代码，扣出，转换成python语法
    3.python调用js文件中的函数，进行加密 pip install pyExecJS
    4.爬取数据的流程
4.案例实现
    模拟强智教务系统，登录成功以后，爬取个人课表信息
    保存课表信息
"""
import execjs
import requests
from bs4 import BeautifulSoup
import csv


class QiangzhiSpiter:
    # 初始化加载参数
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Host': 'qzjw.peizheng.edu.cn',
            'Origin': 'http://qzjw.peizheng.edu.cn',
            'Referer': 'http://qzjw.peizheng.edu.cn/',
            'vary': 'accept-encoding'
        }
        self.session = requests.session()
        self.username = "20205080910202"
        self.password = "10231561233"
        self.get_encode()
        self.get_pic_code()
        self.soup = BeautifulSoup()

    # 获取加密函数
    def get_encode(self):
        # 加载js文件
        with open('conwork.js', encoding='utf-8')as f:
            # 使用execjs读js文件，转换js对象
            js = execjs.compile(f.read())
            # 调用重写的加密算法，回调函数call
            self.en_code = js.call('encode', self.username, self.password)
        return self.en_code

    #   获取图片验证码
    def get_pic_code(self):
        # 请求发送验证码服务器
        pic_data = self.session.get("http://qzjw.peizheng.edu.cn/jsxsd/verifycode.servlet").content
        with open('pic_code.png', 'wb')as f:
            f.write(pic_data)
        self.randow_code = input("请输入你的验证码")
        return self.randow_code

    #   登录操作
    def login(self):
        # 提交表单数据
        from_data = {
            'RANDOMCODE': self.randow_code,  # 图片验证码
            'encoded': self.en_code
        }
        #         请求登录地址
        self.resp = self.session.post("http://qzjw.peizheng.edu.cn/jsxsd/xk/LoginToXk", data=from_data,
                                      headers=self.headers)
        if self.resp.status_code == 200:  # 是否登录成功
            # 爬取个人课表信息
            html_coures = self.session.get("http://qzjw.peizheng.edu.cn/jsxsd/xskb/xskb_list.do",
                                           headers=self.headers).text
            # print(html_coures)
            # 解析代码 bs4
            soup = BeautifulSoup(html_coures, 'lxml')
            class_list = soup.find_all('div', {'class': 'kbcontent1'})
            print(class_list)
            list = []
            for class_name in class_list:
                list.append(class_name.text)
                print(class_name.text)
            print(list)
            with open('class_name', 'w', encoding='utf-8')as f:
                Writer = csv.writer(f)
                Writer.writerow(list)
            f.close()
        else:
            print("登陆失败")


# 测试
obj = QiangzhiSpiter()
en_code = obj.get_encode()
obj.login()
# print(en_code)
