# -*- coding:utf-8 _*-
"""
@function： 配置文件类
"""
import configparser

from common import contants

class ReadConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_conf, encoding='utf-8')
        open = self.config.getboolean('switch', 'open')


        if open:
            self.config.read(contants.test_conf, encoding='utf-8')
        else:
            self.config.read(contants.test2_conf, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)
