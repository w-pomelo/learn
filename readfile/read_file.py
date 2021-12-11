#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import json

#定义一个读取测试数据的类,将测试数据文件地址作为参数传入
class Readdata:
    def __init__(self,path):
        self.path = path

    #定义一个函数进行数据解析
    def read_data(self):
        #读取文件中的内容
        with open(self.path,'r') as f:
            line = f.readline()
            #导入re模块
            import re
            #利用循环一行一行将数据读出来
            while line:
                #利用正则取出中括号之间的字符串，组成一个列表
                list0 = re.findall('(?<=\[).*?(?=\])',line)
                yield list0
                line = f.readline()

    #读取json文件中的数据
    def login_data(self):
        with open(self.path,'r') as f:
            contant = json.load(f)
            for i in contant:
                #进入第二层字典
                input_dict = contant[i][0]
                #取出字典中的值
                username = input_dict["username"]
                password = input_dict["password"]
                captcha = input_dict["captcha"]
                yield [username,password,captcha]


if __name__ == '__main__':
    # r = Readdata('../data/test_data')
    # for data in r.read_data():
    #     print(data)
    r = Readdata('../data/test_login.json')
    for i in r.login_data():
        print(i)


#












