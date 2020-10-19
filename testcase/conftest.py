"""
File name: conftest.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/12 11:02 上午
"""
import pytest
from selenium.webdriver import Chrome
from common.handle_config import conf
from page.Index_page import IndexPage
from page.login_page import LoginPage
from page.invest_page import InvestPage
from page.user_page import UserPage
from selenium import webdriver
#读取配置文件中的配置，判断是否是以无头浏览器模式运行
def create_dirver():
    boll = conf.getboolean("run","headless")
    if boll:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    else:
        driver = Chrome()
    return driver

@pytest.fixture(scope="class")
def login_setup():
    driver = create_dirver()
    driver.implicitly_wait(15)
    driver.get(conf.get('env', 'base_url') + conf.get('env', 'url_path'))
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page,index_page
    driver.quit()
@pytest.fixture(scope="class")
def invest_setup():
    driver = create_dirver()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(conf.get('env', 'base_url') + conf.get('env', 'url_path'))
    login_page = LoginPage(driver)
    # 登录
    login_page.login(conf.get("test_data", "phone"), conf.get("test_data", "pwd"))
    # 创建首页对象
    index_page = IndexPage(driver)
    # 点击抢投标
    index_page.click_invest_loan()
    # 进入投资页面
    invest_page = InvestPage(driver)
    user_page = UserPage(driver)
    yield invest_page,user_page
    driver.quit()
