# -*- coding:utf-8 -*-
# @Time   : 2019-10-23
# @Author : Dingjs

import logging
import time
import os
from Interface_python3.public import config


class Log(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 拼接日志文件夹，如果不存在则自动创建
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), 'Log')
        if not os.path.exists(log_path):os.mkdir(log_path)

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        # log_name = log_path + rq + '.log'
        log_name = os.path.join(log_path,'%s.log ' %rq)
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)







    # """日志类"""
    #
    # def __init__(self, name=None):
    #     day = time.strftime("%Y%m%d", time.localtime(time.time()))  # 获取当前时间
    #     file = os.path.join(config.test_log_path, (day + '.log'))  # 以当前时间命名日志文件
    #     self.logger = logging.Logger(name)  # 定义日志的名称
    #     self.logger.setLevel(logging.DEBUG)  # 设置日志等级
    #     self.logfile = logging.FileHandler(file, encoding="UTF-8")  # 定义日志输出到文件
    #     self.logfile.setLevel(logging.DEBUG)  # 将INFO级别或更高的日志输出到文件
    #     self.control = logging.StreamHandler()  # 定义日志输出到控制台
    #     self.control.setLevel(logging.DEBUG)  # 将INFO级别或更高的日志输出到控制台
    #     # 定义日志格式:时间、文件名、行号、标记、结果
    #     self.formater = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d : %(message)s')
    #     self.logfile.setFormatter(self.formater)
    #     self.control.setFormatter(self.formater)
    #     self.logger.addHandler(self.logfile)
    #     self.logger.addHandler(self.control)
    #     self.logfile.close()
    #     self.control.close()

    def get_logger(self):
        return self.logger
