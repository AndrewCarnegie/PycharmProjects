# _*_ coding:UTF-8 _*_
"""
Template indicates the file operation by Python

"""
__author__ = 'Andrew Carnegie'
__date__ = '20180523'
__purpose__ = 'file operation by Python'

import configparser
from xml.dom.minidom import parse, parseString

# file read by ini configuration file
# def read_file_by_ini_config():
#     def read_file(file_path):
#         with open(file_path, 'r', encoding='UTF-8', errors='ignore') as f:
#             str_line = ''
#             for line in f.readlines():
#                 str_line += line
#             return str_line
#
#     config = configparser.ConfigParser()
#     config.read("C:\\Users\\fenye\\PycharmProjects\\PythonLearning\\Configuration\\ConfigurationFile.ini")
#     f_path = config.get("FilePath", "file_path")
#     print(read_file(f_path))


# file read by xml configuration file
def read_file_by_xml_configuration():
    def read_file(file_path):
        with open(file_path, 'r', encoding='UTF-8', errors='ignore') as f:
            str_line = ''
            for line in f.readlines():
                str_line += line
            return str_line
    Temp_dom = parse("C:\\Users\\fenye\\PycharmProjects\\PythonLearning\\Configuration\\ConfigurationFile.xml")
    config_element = Temp_dom.getElementsByTagName("files")
    print(Temp_dom)
    # print(read_file(config_element))