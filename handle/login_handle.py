# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__projrct_ : my126email
__title__  : login_handle
__author__ : chunhua.huang
__time__   : 2019/3/18 13:49

"""

from page.login_page import LoginPage
from selenium import webdriver


class LoginHandle(object):
    def __init__(self, driver):
        self.lp = LoginPage(driver)

    def send_email(self, useremail):
        self.lp.get_email_inputbox().send_keys(useremail)

    def send_pw(self,userpw):
        self.lp.get_pw_inputbox().send_keys(userpw)

    def click_loginbt(self):
        self.lp.get_login_bt().click()

    def get_error_msg(self, info):
        try:
            if info == "emailorpw_error":
                msg = self.lp.get_emialorpw_error().text
            elif info == "email_empty_error":
                msg = self.lp.get_email_empty_error().text
            else:
                msg = self.lp.get_pw_empty_error().text
        except:
            msg = None
        return msg

    # 用来验证是否登录成功
    def get_login_bt_text(self):
        text = self.lp.get_login_bt().text
        return text


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://mail.126.com/")
    driver.maximize_window()
    lh = LoginHandle(driver)
    print(lh.get_login_bt_text())
