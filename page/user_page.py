"""
File name: user_page.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/13 11:30 上午
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from common.base_page import BasePage
import time
class UserPage(BasePage):
    user_locator = (By.XPATH,"//li[@class='color_sub']")
    def get_user_amount(self):
        time.sleep(1)
        ele = self.wait_element_visibility(self.user_locator,"用户页面_剩余金额")
        amount = ele.text
        # amount = self.get_element_text(self.user_locator,"用户页面_剩余金额")
        time.sleep(0.5)
        end_amount = amount.replace('元','')
        return end_amount
