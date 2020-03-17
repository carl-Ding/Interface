# -*- coding:utf-8 -*-
# @Time   : 2019-10-23
# @Author : Dingjs


import yaml,os
from Interface_python3.public import config
from Interface_python3.public.base_page import BasePage

class HomePage(BasePage):

    def __init__(self):
        file_path = os.path.join(config.test_data_path,'html_element_data.yaml')
        # file_path = config.test_data_path + '\html_element_data.yaml'
        with open(file_path, 'r', encoding='utf-8') as file:
            # 将yaml格式内容转换成 dict类型
            self.load_data = yaml.load(file)
        super(HomePage, self).__init__(self.load_data.get('baidu').get('url'))

    def search_input(self, text):
        self.clear_type(self.load_data.get('baidu').get('input'), text)

    def send_submit_btn(self):
        self.click(self.load_data.get('baidu').get('submit'))

    def click_news(self):
        self.click(self.load_data.get('baidu').get('news_link'))
        self.sleep(2)
