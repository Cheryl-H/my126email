# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__projrct_ : my126email
__title__  : login_page
__author__ : chunhua.huang
__time__   : 2019/3/15 15:36

"""
from base.find_element import FindElement
from selenium import webdriver

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd_el = FindElement(self.driver)
        self.fd_el.iframe('login_iframe')

    def get_email_inputbox(self):
        return self.fd_el.get_element("email_inputbox")

    def get_pw_inputbox(self):
        return self.fd_el.get_element("password_inputbox")

    def get_checkbox(self):
        return self.fd_el.get_element("login_checkbox")

    def get_login_bt(self):
        return self.fd_el.get_element("login_bt")

    def get_register_bt(self):
        return self.fd_el.get_element("register_bt")

    def get_emialorpw_error(self):
        return self.fd_el.get_element("emailorpw_error")

    def get_email_empty_error(self):
        return self.fd_el.get_element("email_empty_msg")

    def get_pw_empty_error(self):
        return self.fd_el.get_element("pw_empty_msg")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://mail.126.com/")
    driver.maximize_window()
    lp = LoginPage(driver)
    ele = lp.get_email_inputbox()
    ele.send_keys("kjgjgjgjg")
    print(ele.get_attribute("value"))
    driver.close()
