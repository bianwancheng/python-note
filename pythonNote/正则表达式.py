#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 17:25
# @Author  : Bwcheng
# @Site    : 
# @File    : 正则表达式.py
# @Software: PyCharm


# 导入用于正则表达式的re模块
import re

str = r'__12df3as561df__??}{'
print(re.findall(r"\d\w{10}", str))
print(re.findall(r"[^__]", str))

string = 'qw.adsf'
print(re.findall(".a", string))

# 取出字符串string8中所有的天气状态
string8 = "{ymd:'2018-01-01',tianqi:'晴',aqiInfo:'轻度污染'},{ymd:'2018-01-02',tianqi:'阴~小雨',aqiInfo:'优'},{ymd:'2018-01-03',tianqi:'小雨~中雨',aqiInfo:'优'},{ymd:'2018-01-04',tianqi:'中雨~小雨',aqiInfo:'优'}"
# 基于正则表达式使用findall函数
print(re.findall("tianqi:'(.*?)'", string8))


# 取出string9中所有含O字母的单词
string9  = 'Together, we discovered that a free market only thrives when there are rules to ensure competition and fair play, Our celebration of initiative and enterprise'
# 先用，或者空格拆分然后匹配(其实还有一个', ',不过不影响)
strList = re.split(r",|\s", string9)
finallyList = []
for str in strList:
    if str == '':
        continue
    elif re.match(r".*o.*", str) is not None:
        str = re.match(r".*o.*", str).group(0)
        finallyList.append(str)
print(finallyList)

# 基于正则表达式使用findall函数
# print(re.match(r'\wo\w*',string9, flags=re.I).group(0))
'''
# 将string10中的标点符号、数字和字母删除
string10 = '据悉，这次发运的4台蒸汽冷凝罐属于国际热核聚变实验堆（ITER）项目的核二级压力设备，先后完成了压力试验、真空试验、氦气检漏试验、千斤顶试验、吊耳载荷试验、叠装试验等验收试验。'
# 基于正则表达式使用sub函数
print(re.sub('[，。、a-zA-Z0-9（）]','',string10))

# 将string11中的每个子部分内容分割开
string11 = '2室2厅 | 101.62平 | 低区/7层 | 朝南 上海未来 - 浦东 - 金杨 - 2005年建'

# 基于正则表达式使用split函数
split = re.split('[-|]', string11)

print(split)
# 分割结果的清洗
split_strip = [i.strip() for i in split]
print(split_strip)

out:
['晴', '阴~小雨', '小雨~中雨', '中雨~小雨']
['Together', 'discovered', 'only', 'to', 'competition', 'Our', 'celebration', 'of']
据悉这次发运的台蒸汽冷凝罐属于国际热核聚变实验堆项目的核二级压力设备先后完成了压力试验真空试验氦气检漏试验千斤顶试验吊耳载荷试验叠装试验等验收试验
['2室2厅 ', ' 101.62平 ', ' 低区/7层 ', ' 朝南 ', ' 上海未来 ', ' 浦东 ', ' 金杨 ', ' 2005年建']

'''