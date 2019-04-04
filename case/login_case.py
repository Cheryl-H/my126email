# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__projrct_ : my126email
__title__  : login_case
__author__ : chunhua.huang
__time__   : 2019/3/18 14:36

"""

import ddt
import unittest
from business.login_business import LoginBusiness
from selenium import webdriver
from HTMLTestRunner_PY3 import HTMLTestRunner

@ddt.ddt
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.126.com/")
        self.driver.maximize_window()
        self.login = LoginBusiness(self.driver)

    def tearDown(self):
        self.driver.close()

    @ddt.data(["amazing_2010@126.com", "123456", "emailorpw_error", "帐号或密码错误"],
              ["amazing_2011@126.com", "123456", "emailorpw_error", "帐号或密码错误"],
              ["amazing_2010@126.com", "", "pw_empty_error", "请输入密码"],
              ["", "123456", "email_empty_error", "请输入帐号"]
              )

    @ddt.unpack
    def test_login(self,useremail, pw, assertcode, asserttext):
        email_e = self.login.login_function(useremail, pw, assertcode, asserttext)
        self.assertTrue(email_e, "测试通过")

    # def test_email_error(self, useremail, pw):
    #     '''邮箱错误'''
    #     email_e = self.login.email_error(useremail, pw)
    #     self.assertTrue(email_e, "test_email_error测试通过")
    #
    # def test_pw_error(self, useremail, pw):
    #     '''密码错误'''
    #     pw_e = self.login.pw_error(useremail, pw)
    #     self.assertTrue(pw_e, "test_pw_error测试通过")


if __name__ == "__main__":
    # 创建测试用例集
    suite = unittest.TestSuite()
    # 添加测试用例，方法一
    suite.addTest(unittest.makeSuite(LoginCase))

    # 添加测试用例，方法二
    # suite.addTest(LoginCase('test_pw_error'))
    # suite.addTest(LoginCase('test_email_error'))

    # 执行测试用例，方法一
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 执行测试用例，方法二
    filepath = "D:\F\pyworkspace\my126email\\report\\login_case.html"
    f = open(filepath, 'wb')  # 以读写模式打开
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='LoginCaseTestReport',
                            description=u'20190318第一轮测试报告')
    runner.run(suite)
    f.close()









