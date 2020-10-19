"""
File name: 0925.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/9/26 11:41 上午
"""

import pytest
from casedatas import login_data
from common.handle_log import log

class TestLogin:
    @pytest.mark.parametrize('case',login_data.login_data_is_none)
    def test_login_data_is_none(self,login_setup, case):
        login_page,index_page = login_setup
        login_page.reset_login_page()
        # 1登录
        login_page.login(case['phone'], case['pwd'])
        expected = case["expected"]
        # 2获取页面上的错误提示
        res = login_page.get_page_error_info()
        # 3断言是否登录成功
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case',login_data.login_data_wrong)
    def test_login_toast_wrong(self, case,login_setup):
        login_page,index_page = login_setup
        login_page.reset_login_page()
        # 1登录
        login_page.login(case['phone'],case['pwd'])
        expected = case["expected"]
        # 2获取toast弹窗中的错误提示
        res = login_page.get_toast_error_info()
        # 3断言
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case',login_data.login_data_pass)
    def test_login_pass(self, login_setup, case):
        # 登录成功--输入账号--输入密码--点击登录--断言是否登录成功
        login_page, index_page = login_setup
        login_page.reset_login_page()
        login_page.login(case['phone'], case['pwd'])
        # 断言是否登录成功
        res = index_page.is_login()
        try:
            assert res
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))
            index_page.click_quit_login()