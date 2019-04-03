# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__projrct_ : my126email
__title__  : read_ini
__author__ : chunhua.huang
__time__   : 2019/3/14 14:26

"""
import configparser

class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            # file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
            # file_name = os.path.join(file_path_father + r"\config" + r'\LocalElement.ini')
            file_name = r'D:/F/pyworkspace/my126email/config/locate_element.ini'

        if node == None:
            self.node = 'LoginElement'
        else:
            self.node = None
        self.cf = self.load_ini(file_name)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='UTF-8')
        return cf

    # 获取value值
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value("QRcode_logintab"))
