"""
File name: base_page.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/14 3:12 下午
"""

# 1.显示等待(元素被加载，元素可见，元素可点击)
# 2.获取元素的文本
# 3.点击元素
# 4.获取元素的属性
# 5.输入文本
# 6.窗口拖动
# 7.滑动到元素可见
# 8.执行js代码
# 9.获取元素


# 如果元素定位出错了，要不要日志输出？
    # 日志输出可以封装到basepage的基础操作中
    # 如果元素定位出错了，页面错误截图
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from common.handle_log import log
import time
from common.handle_path import ERROR_IMAGE
import os
class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    # 把页面一些常见的公共操作全部封装到这里

    def wait_element_visibility(self,locator,img_info,timeout=15,poll_frequency=0.5):
        # 等待元素可见
        # 元素等待之前获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver,timeout,poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            # 输出日志
            log.error("元素--{}--等待可见超时".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(start_time,img_info)
            file_path = os.path.join(ERROR_IMAGE,file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误页面截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            # 元素等待之后获取时间
            end_time = time.time()
            log.info("元素--{}--等待成功,等待时间是{}秒".format(locator,end_time-start_time))
            return ele

    def wait_element_clickable(self,locator,img_info,timeout=15,poll_frequency=0.5):
        # 等待元素可点击
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver,timeout,poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            # 输出日志
            log.error("元素--{}--等待可点击超时".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(start_time, img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误页面截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            # 元素等待之后获取时间
            end_time = time.time()
            log.info("元素--{}--等待成功,等待时间是{}秒".format(locator, end_time - start_time))
            return ele

    def wait_element_presence(self,locator,img_info,timeout=15,poll_frequency=0.5):
        start_time = time.time()
        try:
            # 等待元素被加载
            ele = WebDriverWait(self.driver,timeout,poll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            # 输出日志
            log.error("元素--{}--等待可见超时".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(start_time, img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误页面截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            # 元素等待之后获取时间
            end_time = time.time()
            log.info("元素--{}--等待成功,等待时间是{}秒".format(locator, end_time - start_time))
            return ele

    def get_element_text(self,locator,img_info):
        # "获取元素的文本"
        start_time = time.time()
        try:
            text = self.driver.find_element(*locator).text
        except Exception as e:
            # 输出日志
            log.error("元素--{}--获取文本失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(start_time, img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误页面截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:

            log.info("元素--{}--获取文本成功".format(locator))
            return text

    def get_element_attribute(self, locator,attr_name, img_info):
        # "获取元素的文本"
        try:
            ele = self.driver.find_element(*locator)
            attr_value = ele.get_attribute(attr_name)
        except Exception as e:
            # 输出日志
            log.error("元素--{}--获取属性失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误属性截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            log.info("元素--{}--获取属性成功".format(locator))
            return attr_value

    def click_element(self,locator,img_info):
        try:
            self.driver.find_element(*locator).click()
        except Exception as e:
            # 输出日志
            log.error("元素--{}--点击元素失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误属性截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            log.info("元素--{}--元素点击成功,".format(locator))

    def input_text(self,locator,text_value,img_info):
        # 文本内容输入
        try:
            self.driver.find_element(*locator).send_keys(text_value)
        except Exception as e:
            # 输出日志
            log.error("输入文本-{}--失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误属性截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            log.info("输入文本内容--{}--成功,".format(locator))

    def get_element(self,locator,img_info):
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            # 输出日志
            log.error("获取元素-{}--失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误属性截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            log.info("获取元素--{}--成功,".format(locator))

    def save_screen_image(self,img_info):
        file_name = "{}_{}.png".format(img_info)
        file_path = os.path.join(ERROR_IMAGE, file_name)
        self.driver.save_screenshot(file_path)
        log.info("错误属性截图成功，图片保存的路径:{}".format(file_path))
    def clear_element(self,locator,img_info):
        try:
            self.driver.find_element(*locator).clear()
        except Exception as e:
            # 输出日志
            log.error("清空文本-{}--失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图,格式：时间_页面_操作.png
            file_name = "{}_{}.png".format(img_info)
            file_path = os.path.join(ERROR_IMAGE, file_name)
            self.driver.save_screenshot(file_path)
            log.info("错误属性截图成功，图片保存的路径:{}".format(file_path))
            raise e
        else:
            log.info("清空文本内容--{}--成功,".format(locator))

