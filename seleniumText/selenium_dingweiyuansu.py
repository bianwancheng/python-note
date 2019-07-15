#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 16:43
# @Author  : Bwcheng
# @Site    : 
# @File    : selenium_dingweiyuansu.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)

# 1、查找元素的方法有很多，通用的是find_element()，还有xpath、id等等
element = driver.find_element(By.XPATH, value='//*[@id="qrcode"]/div/div[2]/p[1]')
element = driver.find_element_by_xpath('//*[@id="qrcode"]/div/div[2]/p[1]')

# 2、等待的方式有三种：1、强制等待；2、隐式等待；3、显示等待；

# 1、强制等待
time.sleep(2)

# 2、隐式等待 implicitly_wait(): 在最大时间内等待整个页面加载完毕，超出时间则会抛出异常
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 3、显示等待 WebDriverWait()

WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
'''
WebDriverWait(driver,timeout,poll_frequency)在单位时间内，检测元素是否存在。返回bool型
:parameter
driver 驱动
timeout等待时间
poll_frequency检测时间间隔
-------------------------------------------------------------------
WebDriverWait()一般由until()或 until_not()方法配合使用
until(method, message=' ')：调用该方法提供的驱动程序作为一个参数，直到返回值为True
until_not(method, message=' ')：调用该方法提供的驱动程序作为一个参数，直到返回值为False
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
presence_of_element_located是判断元素是否存在
ex下还有很多的方法供使用，例如，判断复选是否是勾选等
*****************************************************************
使用时需要注意事项:EX.presence_of_element_located((By.ID,"kw"))
这个方法，要有两个括号，因为参数只能是一个元组
'''
'''
expected_conditions类：

EC.element_located_selection_state_to_be((By.ID,"kw")) #元素的选中状态是否符合预期
EC.element_selection_state_to_be(element) #与上一个用法相同，区别在于一个参数是定位，一个是定位后的元素
EC.alert_is_present() #判断页面上，是否存在Alert弹出框
EC.element_located_to_be_selected((By.ID,"kw")) #某个预期元素是否被选中
EC.element_to_be_selected(element) #与上一个用法相同，区别在于一个参数是定位，一个是定位后的元素
EC.element_to_be_clickable() #判断元素是否可见并且可以点击

EC.frame_to_be_available_and_switch_to_it() #判断该表单是否，可以切换进去，可以返回True，并且Switch进去，否则返回False
EC.invisibility_of_element_located() #判断某元素是否存在于Dom树或不可见
EC.new_window_is_opened() #是否有窗口被打开
EC.presence_of_all_elements_located()
EC.presence_of_element_located() #判读元素是否存在
EC.text_to_be_present_in_element() #判读元素中的Text是否包含了预期字符串
EC.text_to_be_present_in_element_value#判断元素的Value是否包含了预期字符串
EC.title_contains(title) #判读当前页面，标题是否包含预期字符串
EC.title_is(title) #判读当前页面，标题是否为预期

EC.visibility_of_all_elements_located()
EC.visibility_of_element_located((By.ID,"kw")) #判断某元素是否可见
EC.visibility_of(element) #与上个用法相同，区别在于参数是定位后的元素，上一个是传的定位
EC.visibility_of_any_elements_located((By.CLASS_NAME,"a#")) #判断是否至少有一个元素在页面中可见,如果定位到就返回列表

'''

# 封装了一个方法可以用：
'''
def find_element(browser, element, method='xpath'):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((method, element)))
        return browser.find_element(method, element)
    except Exception as e:
        print('no found element')
        raise e
# -----------------------------------------------------------
browser = webdriver.Chrome()
browser.implicitly_wait(10)  # 隐式等待，等待浏览器加载完毕
browser.get('https://www.html5tricks.com/demo/jiaoben1454/index.html#')
element = find_element(browser, '/html/body/div[2]/ul/li[4]/a')

ActionChains(browser).move_to_element(element).perform()  # 鼠标移动到某个元素上
time.sleep(2)
print(browser.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a/i').get_attribute('class'))
browser.close()

'''