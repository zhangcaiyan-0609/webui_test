
"""
File name: login_page.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/9/27 11:05 上午
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_config import conf
from common.base_page import BasePage
class LoginPage(BasePage):
    # 手机号输入框
    input_phone_locator =(By.XPATH,"//input[@name='phone']")
    # 密码输入框
    password_locator =(By.XPATH,"//input[@name='password']")
    # 登陆输入框
    login_btn_locator = (By.XPATH,"//button[text()='登录']")
    # 登陆页面错误提示
    page_error_locator =(By.XPATH,'//div[@class="form-error-info"]')
    # 登陆页面toast提示
    toast_error_info_loactor =(By.XPATH,"//div[@class='layui-layer-content']")
    def __int__(self,driver):
        super.__init__(driver)
        self.driver.get(conf.get("env","base_url")+conf.get("env","url_path"))
        self.driver.implicitly_wait(15)

    def login(self,phone,pwd):
        """
        :param phone:
        :param pwd:
        :return:
        """
        # 1 输入账号
        self.clear_element(self.input_phone_locator,"登录页面_清空账户")
        self.input_text(self.input_phone_locator,phone,"登录页面_输入手机号")
        # 18684720553 python
        # 2 输入密码
        self.clear_element(self.password_locator,"登录页面_清空密码")
        self.input_text(self.password_locator,pwd,"登录页面_输入密码")
        # 3 点击登录
        self.click_element(self.login_btn_locator,"登录页面_点击登录")

    def get_page_error_info(self):
        # 获取页面上的错误提示
        res = self.get_element_text(self.page_error_locator,"登录页面_错误提示")
        return res
    def get_toast_error_info(self):
        # 获取页面toast弹窗
        ele = self.wait_element_visibility(self.toast_error_info_loactor,"登录页面_弹窗错误提示")
        res = ele.text
        return res

    def reset_login_page(self):
        self.driver.get(conf.get('env','base_url')+conf.get('env','url_path'))