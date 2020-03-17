# -*- coding:utf-8 -*-
# @Time   : 2019-10-23
# @Author : Dingjs

import unittest
from ddt import ddt, data
from Interface_python3.public import base
from Interface_python3.public.log import Log

excel_data = base.get_excel_data('test.xlsx', 'test')


@ddt
class TestCase(unittest.TestCase):
    u"""测试"""

    @classmethod
    def setUpClass(cls):
        cls.log = Log('测试').get_logger()

    @data(*excel_data)
    def test_something(self, test_data):
        u"""测试用例"""

        r = base.get_excel_response(test_data)
        base.write_to_excel('test.xlsx', 'test', test_data, r)

        self.log.info("检查点->：" + test_data.get('checkpoint'))
        self.log.info("实际返回结果->：" + r.text)
        if test_data.get('isCheckStatusCode'):
            self.assertEqual(str(r.status_code), test_data.get('checkpoint'), msg='和预期不一样')
        else:
            self.assertTrue(test_data.get('checkpoint') in r.text, msg='和预期不一样')

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
