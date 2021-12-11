#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import re
import os

class GetId:
    def __init__(self):
        os.popen('adb devices -l > D:/image/temp.txt')

    #读取出adb devices -l命令中返回的设备名称
    def read_file(self):
        with open('../data/temp.txt','r+',encoding='utf-8') as f:
            data = f.read()
            #使用正则将设备名称找出来，返回一个列表
            list_device = re.findall('(?<=\n).*?\d(?=\s\s)',data)
            return list_device

if __name__ == '__main__':
    GetId().read_file()
