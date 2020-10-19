"""
File name: test_invest.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/12 3:28 下午
"""
import pytest
from common.handle_config import conf
from common.handle_log import log
from casedatas import invest_data
from page.user_page import UserPage
from decimal import Decimal
import time
class TestInvest:
    # 投资的前置条件-登录成功(默认账号可用金额足够大)-选择项目(默认选择第一个项目)点击抢投标
    # 投资失败，弹窗上出现提示信息的用例
    @pytest.mark.parametrize('case', invest_data.invest_data_is_wrong)
    def test_invest_error(self, case, invest_setup):
        print(case)
        invest_page = invest_setup[0]
        user_page = invest_setup[1]
        # 1.投资
        invest_page.invest(case["amount"])
        time.sleep(1)
        invest_page.maxmize_window()
        # 2.点击投资
        invest_page.click_invest()
        expected = case['expected']
        # 3.获取弹窗提示
        res = invest_page.get_toast_wrong()
        time.sleep(1)
        invest_page.close_wrong_toast()
        # 4 断言
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过".format(case['title']))
    # 投资金额不是10的倍数
    @pytest.mark.parametrize('case', invest_data.invest_data_not_10_double)
    def test_invest_btn_error(self, case, invest_setup):
        invest_page = invest_setup[0]
        user_page = invest_setup[1]
        # 1.投资
        invest_page.invest(case["amount"])
        time.sleep(1)
        expected = case["expected"]
        # 3.获取页面按钮的提示
        res = invest_page.get_page_error()
        # 4.断言
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过".format(case['title']))
    @pytest.mark.parametrize('case',invest_data.invest_data_is_pass)
    def test_invest_pass(self,case,invest_setup):
        invest_page = invest_setup[0]
        user_page = invest_setup[1]
        # 获取投资前的可用余额
        start_amount = invest_page.get_amount()
        # 1.输入投资金额
        invest_page.invest(case["amount"])
        # 2.点击投资
        invest_page.click_invest()
        expected = case["expected"]
        # 3.获取弹窗提示
        res = invest_page.get_toast_pass()
        # 点击查看并激活
        invest_page.click_invest_success()
        # 获取用户的用户余额
        end_amount = user_page.get_user_amount()
        # 4 断言
        try:
            assert res == expected
            assert Decimal(start_amount)-Decimal(end_amount) == Decimal(case["amount"])
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过".format(case['title']))

