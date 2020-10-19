'''
项目结构说明:
    common:存放一些自己封装的公共模块（修改源码的ddt)
    casedatas:存放excel文件的用例数据
    testresult/logs:存放日志文件
    testresult/report:存放测试报告
    testcase:存放测试用例模块
    run.py:项目的启动文件
    conf:里面存放项目的配置文件
    page:存放项目的主要页面操作

'''

import os

# 项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试用例的目录路径
CASE_DIR = os.path.join(BASE_DIR,'testcase')
# 测试报告目录的路径
REPORT_DIR = os.path.join(BASE_DIR,'test_result/reports')
# 日志目录的目录路径
LOG_DIR = os.path.join(BASE_DIR,'test_result/logs')
# 用例数据的目录路径
DATA_DIR = os.path.join(BASE_DIR,'casedatas')
# 配置文件的目录路径
CONF_DIR= os.path.join(BASE_DIR,'conf')
# 错误截图存放的路径
ERROR_IMAGE = os.path.join(BASE_DIR, "test_result/error_images")




