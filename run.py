"""
============================
Author:柠檬班-木森
Time:2020/9/24   20:48
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


"""
import unittest
from unittestreport import TestRunner


def main():
    suite = unittest.defaultTestLoader.discover('/Users/zhangcaiyan/Desktop/py31_1012/testcase')
    runner = TestRunner(suite)
    runner.run()


if __name__ == '__main__':
    main()
"""

import pytest
import os

#1  生成allure测试报告数据

pytest.main(["--alluredir=test_result/reports",
             '--reruns','3',  
             '--reruns-delay', '2' 
             ])
# 2 打开命令终端 运行allure serve test_result/reports

#3 启动allure服务
# os.system(("allure serve test_result/reports"))

