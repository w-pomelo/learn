#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import json

#读取会员信息
class ReadMemberData:
    def __init__(self):
        pass

    def read_member_data(self,path):
        with open(path,'r',encoding='utf-8') as f:
            data = json.load(f)
            return data['test_case'][0]


if __name__ == '__main__':
    ReadMemberData().read_member_data('../data/member_data.json')


