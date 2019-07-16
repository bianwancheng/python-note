#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 16:43
# @Author  : Bwcheng
# @Site    : 
# @File    : selenium_dingweiyuansu.py
# @Software: PyCharm

'''
excepted_conditions类：
***一般有localed的就是传入元组（locator定位），没有就是web的element***

1、title_is:判断当前页面的title是否完全等于（==）预期字符串，返回是布尔值
2、title_contains 判断当前页面的title是否包含预期字符串，返回布尔值
3、presence_of_element_located:判断某个元素是否被加到了dom树里，并不代表该元素一定可见
4、visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0（参数(By.ID, "kw")）
5、visibility_of :跟上面的方法做一样的事情，只是上面的方法要传入locator（定位(By.ID, "kw")），这个方法直接传定位到的element就好了
6、presence_of_all_elements_located : 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，
那么只要有1个元素存在，这个方法就返回True
7、text_to_be_present_in_element : 判断某个元素中的text是否 包含了预期的字符串
8、frame_to_be_available_and_switch_to_it : 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
9、invisibility_of_element_located : 判断某个元素中是否不存在于dom树或不可见
10、element_to_be_clickable : 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
11、staleness_of :等某个元素从dom树中移除，注意，这个方法也是返回True或False
12、element_to_be_selected:判断某个元素是否被选中了,一般用在下拉列表（传入element对象）
＞* element_selection_state_to_be:判断某个元素的选中状态是否符合预期（element和状态）
13、element_located_selection_state_to_be:跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
14、alert_is_present : 判断页面上是否存在alert
15、new_window_is_opened() #是否有窗口被打开

********************************************************************************
通过封装excepted_conditions来实现查找元素

def find_element(self, locator):  # locator参数是定位方式，如("id", "kw"),把两个参数合并为一个,*号是把两个参数分开传值
    element = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
    print(element)
    return element

********************************************************************************
'''
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
'''
element = driver.find_element(By.XPATH, value='//*[@id="qrcode"]/div/div[2]/p[1]')
element = driver.find_element_by_xpath('//*[@id="qrcode"]/div/div[2]/p[1]')

'''

# 2、等待的方式有三种：1、强制等待；2、隐式等待；3、显示等待；

# 1、强制等待
'''
time.sleep(2)

'''

# 2、隐式等待 implicitly_wait(): 在最大时间内等待整个页面加载完毕，超出时间则会抛出异常
'''
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
'''

# 3、显示等待 WebDriverWait()
'''
WebDriverWait(driver,timeout,poll_frequency)在单位时间内，检测元素是否存在。返回bool型
:parameter
driver 驱动
timeout等待时间
poll_frequency检测时间间隔(每0.5s检测一次)
-------------------------------------------------------------------
WebDriverWait()一般由until()或 until_not()方法配合使用
until(method, message=' ')：一直调用回调函数method，直到返回值为True，返回值为method的返回值
until_not(method, message=' ')：一直调用回调函数method，直到返回值为False，返回值为method的返回值
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
'''


def find_element(driver, locator):  # locator参数是定位方式，如("id", "kw"),传入元组但是*号是把两个参数分开传值
    print(*locator)
    element = WebDriverWait(driver, 20, 0.5).until(lambda x: x.find_element(*locator)) #find_element()里面的参数是分开
    # find_element()里面的参数是分开传的并不是一个元组  def find_element(self, by=By.ID, value=None):
    print(element)
    return element


wait = WebDriverWait(driver, 5, 0.5)
try:
    wait.until(EC.presence_of_element_located((By.ID, "kw")))
    wait.until(EC.title_is('百度一下，你就知道'))
    print(wait.until(EC.title_contains('百度一下')))
    print(wait.until(EC.presence_of_element_located((By.ID, "kw"))))
    print(wait.until(EC.visibility_of_element_located((By.ID, "kw"))))
    print(find_element(driver, ('id', 'kw')))

except Exception as e:
    raise e
finally:
    driver.close()


'''
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐式等待，等待浏览器加载完毕
driver.get('https://www.html5tricks.com/demo/jiaoben1454/index.html#')
element = find_element(driver, '/html/body/div[2]/ul/li[4]/a')

ActionChains(driver).move_to_element(element).perform()  # 鼠标移动到某个元素上
time.sleep(2)
print(driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a/i').get_attribute('class'))
driver.close()

'''



