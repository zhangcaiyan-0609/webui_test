
"""
File name: login_data.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/9/27 10:59 上午
"""
login_data_is_none = [
    {"title": "密码为空", "phone": "18684720553", "pwd": "", "expected": "请输入密码"},
    {"title": "手机号为空", "phone": "", "pwd": "python", "expected": "请输入手机号"},

]
login_data_wrong = [
    {"title": "手机号错误", "phone": "17610772806", "pwd": "python", "expected": "帐号或密码错误!"},
    {"title": "密码错误", "phone": "18684720553", "pwd": "python22", "expected": "帐号或密码错误!"}
]

login_data_pass = [
    {"title": "登录成功", "phone": "18684720553", "pwd": "python"}
]