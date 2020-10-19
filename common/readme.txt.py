"""
File name: readme.txt.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/18 2:47 下午
"""
"""
服务器上怎么运行web自动化

1服务器安装项目运行所需的python环境
    --安装python版本
    --安装项目运行的依赖包(项目中用到的第三方模块)
2.浏览器和对应的驱动版本
    --https://www.cnblogs.com.june-/articles/12553358.html

3.浏览器的无头模式(即没有UI或者显示服务器依赖性)
    --启动浏览器的时候参加参数 --headless:以无头模式运行浏览器，不会显示界面
    
    





"""
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.get('http://www.baidu.com')
driver.quit()

