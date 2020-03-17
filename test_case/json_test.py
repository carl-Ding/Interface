# -*- coding:utf-8 -*-
# @Time   : 2019-10-23
# @Author : Dingjs
'''
测试结果失败，是因为调不通url
'''

import requests

json = {"data": "{\"page\":1,\"limit\":10,\"status\":\"\"}", "action": "app.patterList",
        "sessionId": "b1b42bd0-3361-11e9-b301-2dab4fcab8b0"}

res = requests.post('http://127.0.0.1:6000/action', data=json)
# res = requests.get('http://127.0.0.1:6000/monitor')
print(res.text)
