"""
File name: invest_data.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/12 2:35 下午
"""
invest_data_is_pass = [
    {"title": "投资金额小于剩余金额并且是100的倍数", "amount": '1000',"expected": "投标成功！"}
]
invest_data_is_wrong = [
    {'title': "投资金额等于0","amount": "0","expected":"请正确填写投标金额"},
    {'title': "投资金额为负数","amount":'-100',"expected":"请正确填写投标金额"},
    {'title': "投资金额大于剩余金额", "amount": "200000000", "expected": "购买标的金额不能大于标总金额"},
    {'title': "投资金额不是100的倍数","amount": "1080","expected":"投标金额必须为100的倍数"}
]
invest_data_not_10_double =[
    {'title': "投资金额小于100但不是10的倍数","amount":"99", "expected": "请输入10的整数倍"},
    {'title': "投资金额大于100但不是10的倍数","amount":"101","expected": "请输入10的整数倍"}
]