#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser

class ConfigFileParser:
    def __init__(self, configFile):
        self.__configFile = configFile
        self.__cf = ConfigParser.ConfigParser()
        self.__cf.read(configFile)

    #获取常量
    def getConst(self, sectionName, optionName):
        return self.__cf.get(sectionName, optionName)

    #获取section中属性名
    def getOptionsOfSection(self, sectionName):
        return self.__cf.options(sectionName)

    #获取配置文件sections
    def getAllSectionsOfConfigFile(self):
        return self.__cf.sections()

    #获取section键值对
    def getItemsOfSection(self, sectionName):
        return self.__cf.items(sectionName)

    #增加常量（成功时返回''；失败时返回错误消息）
    def addConst(self, sectionName, keyName = '', valueName = ''):
        msg = ''
        try:
            self.__cf.add_section(sectionName)

            if keyName != '' and valueName != '':
                self.__cf.set(sectionName, keyName, valueName)

            self.__cf.write(open(self.__configFile, 'w'))
        except Exception as e:
            msg = e

        return msg

cf = ConfigFileParser('test.conf')
print cf.getConst('db', 'db_name')
print cf.getOptionsOfSection('db')
print cf.getAllSectionsOfConfigFile()
print cf.getItemsOfSection('db')
if cf.addConst('newSection', 'key01', 'value01') == '':
    print('add success')
