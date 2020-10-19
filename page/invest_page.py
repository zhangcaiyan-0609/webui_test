
"""
File name: invest_page.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/12 3:19 下午
投资功能的实现

前置条件
1.打开浏览器，访问登录页面
2.需要登录
3.选定项目，点击抢头标
执行用例
操作步骤
1。输入投资的金额
2。点击投资（如果输入的不是10的整数倍，点击是没有任何效果）

校验结果
情况一：输入的金额不是10的整数倍，点击按钮上出现提示：校验点按钮上的提示信息是否和预期一致
情况二：输入的金额不符合要求（0，负数，超出最大可投的金额，空），弹框提示对应的错误，校验弹框的提示信息是否
和预期的一致
情况三：投资成功，成功的弹框提示
校验：
1。是否弹出投资成功
2。校验投资之前跟投资之后的余额变化的值是否和投资金额一致
   --投资之前要去获取账户余额
   --投资之后再去获取账户余额（点击成功信息查看按钮，会进入用户页面，获取投资之后的余额）
   --相减，再断言
后置条件
关闭浏览器

分析用例执行过程中涉及到的页面操作
1。登录界面--登录输入账号密码（已封装）
2。主页页面--选中项目，点击抢投标
3。投资项目页面
   --获取账户的可用余额
   --输入投资金额，
   -- 点击投标
    --投资成功，获取投标成功的信息
    --投资成功，点击查看并激活

    --投资失败，获取按钮上的提示信息
    --投资失败，获取弹框的错误信息

4。用户页面
    --获取可用余额
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
from common.base_page import BasePage
class InvestPage(BasePage):
    # 获取可用余额
    data_amount_locator = (By.XPATH,"//input[@data-amount]")
    # 投资金额输入框
    invest_input = (By.XPATH,"//input[@data-amount]")
    # 投资点击按钮
    invest_locator = (By.XPATH,'//button[@class="btn btn-special height_style"]')
    # 投资成功的提示元素
    toast_is_pass_locator = (By.XPATH,"//div[@class='layui-layer-content']//div[text()='投标成功！']")
    # 投资成功，点击查看并激活按钮
    click_success_info = (By.XPATH,"//div[@class='layui-layer-content']//button[text()='查看并激活']")
    # 投资失败，弹窗提示信息
    toast_info_locator = (By.XPATH,"//div[@class='text-center']")
    # 关闭错误弹窗信息，确定按钮
    close_wrong_toast_locator = (By.XPATH,"//a[@class='layui-layer-btn0']")
    # 按钮上的错误信息
    btn_error_locator = (By.XPATH,'//button[@class="btn btn-special height_style"]')
    def get_amount(self):
        # 获取用户投资前的余额,通过属性，获取属性值
        start_amount = self.get_element_attribute(self.data_amount_locator,"data-amount","投资_获取可用余额")
        return start_amount
    def invest(self,amount):
        # 1.投标输入金额
        self.clear_element(self.invest_input,"投资页面_清空输入")
        self.input_text(self.invest_input,amount,"投资_输入投资金额")
    def click_invest(self):
        # 2.点击投标
        self.click_element(self.invest_locator,'投资页面_点击投标')
    # 窗口最大化
    def maxmize_window(self):
        self.driver.maximize_window()
    def get_toast_wrong(self):
        # 获取弹窗的错误信息
        ele = self.wait_element_visibility(self.toast_info_locator,"投资页面_弹窗错误信息")
        res = ele.text
        # res = self.get_element_text(self.toast_info_locator,"投资页面_弹窗错误信息")
        return res
    def close_wrong_toast(self):
        self.click_element(self.close_wrong_toast_locator,"错误窗口_点击确认")
    def get_page_error(self):
        # 获取按钮上的错误信息
        res = self.get_element_text(self.btn_error_locator,"投资页面_按钮上错误信息")
        return res
    def get_toast_pass(self):
        # 获取投资成功的提示信息
        res = self.wait_element_visibility(self.toast_is_pass_locator,"投资页面_投资成功的页面信息").text
        return res
    def click_invest_success(self):
        # 点击投资成功更多信息
        ele = self.wait_element_clickable(self.click_success_info,"投资成功窗口_点击查看并激活")
        ele.click()



