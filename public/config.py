# -*- coding:utf-8 -*-
# @Time   : 2019-10-24
# @Author :

import os

# 主机 (这个地址，是之前测试用的地址)
base_url = 'https://httpbin.org/'

# 获取本文件的上上级路径（这里是获取项目路径）
#获取项目根目录地址
cur_path = os.path.dirname(os.path.abspath('.'))

#设定目录文件地址
test_case_path = os.path.join(cur_path,'test_case')
# form_data_path = os.path.join((os.path.join(cur_path,'data')),'fromaldata')
formal_data_path = os.path.join(cur_path,'formal_data\\')
test_screenshot_path = os.path.join(cur_path,'img\\')
print(test_screenshot_path)
# print(form_data_path)
test_data_path = os.path.join(cur_path,'test_data\\')
# print(test_data_path)
test_report_path = os.path.join(cur_path,'report')
test_log_path = os.path.join(cur_path,'Log')
test_image_path = os.path.join(cur_path,'image\\')

#关联接口参数可以在这里自定义变量存储
accessToken = ''

