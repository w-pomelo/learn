#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import requests

class GetSession:
    def __init__(self):
        self.base_url = "http://192.168.88.128:8080/WoniuBoss2.5/"
        self.session = requests.session()

    #调用该方法可获取session
    def get_session(self):
        login_url = 'log/userLogin'
        login_data = {'userName':'WNCD000','userPass':'Woniu123','checkcode':'0000'}
        response = self.session.post(url=self.base_url+login_url,data=login_data)
        return self.session

if __name__ == '__main__':
    test = GetSession()
    test.get_session()
