# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__projrct_ : my126email
__title__  : login_business
__author__ : chunhua.huang
__time__   : 2019/3/18 14:03

"""

from selenium import webdriver
from handle.login_handle import LoginHandle


class LoginBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.lh = LoginHandle(self.driver)

    # ddt调用登录总功能
    def login_function(self, useremail, userpw, assertcode, asserttext):
        self.lh.send_email(useremail)
        self.lh.send_pw(userpw)
        self.lh.click_loginbt()
        if self.lh.get_error_msg(assertcode) == asserttext:
            return True
        else:
            print("实际asserttext：", self.lh.get_error_msg(assertcode))
            return False


    # 密码不正确
    def pw_error(self, useremail, userpw):
        self.lh.send_email(useremail)
        self.lh.send_pw(userpw)
        self.lh.click_loginbt()
        if self.lh.get_error_msg("emailorpw_error") == "帐号或密码错误":
            print("密码不正确验证成功")
            return True
        else:
            print("密码不正确验证失败")
            return False

    # 账号不正确
    def email_error(self, useremail, userpw):
        self.lh.send_email(useremail)
        self.lh.send_pw(userpw)
        self.lh.click_loginbt()
        if self.lh.get_error_msg("emailorpw_error") == "帐号或密码错误":
            print("邮箱不正确验证成功")
            return True
        else:
            print("邮箱不正确验证失败")
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://mail.126.com/")
    driver.maximize_window()
    LB = LoginBusiness(driver)
    LB.pw_error("amazing_2010@126.com", "123456")

