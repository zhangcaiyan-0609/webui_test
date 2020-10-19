
"""
File name: Index_page.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/9/27 11:43 上午
"""
from selenium.webdriver.common.by import By
from common.base_page import BasePage
class IndexPage(BasePage):
    quit_login = (By.XPATH,"//a[text()='退出']")
    click_loan = (By.XPATH,'(//a[text()="抢投标"])[1]')
    loc_user_info = (By.XPATH,'//a[contains(text(),"我的帐户")]')

    def is_login(self):
        try:
            self.get_element(self.loc_user_info,"首页_定位我的账户")

        except:
            return False
        else:
            return True

    def click_quit_login(self):
        self.click_element(self.quit_login,"首页_点击退出")

    def click_invest_loan(self):
        # 点击抢投标
        self.click_element(self.click_loan,"首页_点击抢投标")


