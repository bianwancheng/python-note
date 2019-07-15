#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 16:02
# @Author  : Bwcheng
# @Site    : 
# @File    : selenium_shubiaodianji.py
# @Software: PyCharm

'''
selenium对鼠标的操作
一、selenium对鼠标的操作是依靠webdriver下的ActionsChains这个类对鼠标进行操作的
创建ActionChains类，构造函数的默认参数为driver

'''
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(10)
element = driver.find_element_by_xpath('//*[@id="u1"]/a[1]')    # 新闻

# 1、鼠标左键单击某元素
# ActionChains(driver).click(element).perform()

# 2、鼠标左键双击某元素
element = driver.find_element_by_xpath('//*[@id="qrcode"]/div/div[2]/p[1]')
ActionChains(driver).double_click(element).perform()    # 可以看到下载百度APP的“百度”被选中

# 3、点击右键
ActionChains(driver).context_click(element).perform()

# 4、点击左键不放
ActionChains(driver).click_and_hold(element).perform() #在此元素上按下左键不放

# 5、鼠标拖拽
ActionChains(driver).drag_and_drop(source,target).perform() #从一个元素的位置，拖至另一个元素位置松开

# 6、以坐标的形式拖拽，x,y
ActionChains(driver).drag_and_drop_by_offset(source,xoffset,yoffset) #以坐标的形式拖拽，x,y

# 7、鼠标移动
ActionChains(driver).move_by_offset(x,y) #移动到（x,y）坐标位置
ActionChains(driver).move_to_element(element) #鼠标移动到某个元素上
ActionChains(driver).move_to_element_with_offset(element,x,y) #移动到某个元素上，然后，在移动到相对坐标（x,y）上

driver.close()