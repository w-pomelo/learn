#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import json

#试卷14题，对json文件进行解析
class ReadJson:
    def __init__(self):
        pass

    def read_json(self):
        with open('../data/data15.json','r',encoding='utf-8') as f:
            result = json.load(f)
            for i in result['test_case']:
                yield i

if __name__ == '__main__':
    i = ReadJson().read_json()
    for _ in i:
        print(_)