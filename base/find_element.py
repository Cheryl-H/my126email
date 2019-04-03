# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格

"""
__projrct_ : my126email
__title__  : find_element
__author__ : chunhua.huang
__time__   : 2019/3/14 14:17

"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import traceback
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from util.read_ini import ReadIni

class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        wait = WebDriverWait(self.driver, 5, 0.5)
        try:
            if by == 'id':
                return wait.until(EC.presence_of_element_located((By.ID, value)))
                #return self.driver.find_element_by_id(value)
            elif by == 'name':
                return wait.until(EC.presence_of_element_located((By.NAME, value)))
                #return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                # return self.driver.find_element_by_class_name(value)
            else:
                return wait.until(EC.presence_of_element_located((By.XPATH, value)))
                # return self.driver.find_elements_by_xpath(value)
        except:
            return None

    def iframe(self, key):
        frame = self.get_element(key)
        return self.driver.switch_to.frame(frame)

    def iframe_out(self):
        return self.driver.switch_to.default_content()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://mail.126.com/")
    driver.maximize_window()
    find_element = FindElement(driver)
    find_element.iframe('login_iframe')
    element = find_element.get_element('email_inputbox')
    print(element)

    # element1.send_keys("amaizng_2010@126.com")
    # element2.send_keys("123456")
    # find_element.get_element('login_bt').click()
    # time.sleep(3)
    # ee = find_element.get_element('emailorpw_error')
    # print(ee.text)
    # sleep(3)
    # print(element1.get_attribute("value"))
    driver.close()


