#!/bin/evn python
#coding:utf8

from selenium import webdriver

"""
    保存网页图片
"""


urls = [
    'http://www.baidu.com',
    'http://www.jd.com',
    'http://www.taobao.com',
    'http://www.sina.com',
    'http://www.sohu.com',
]


web = webdriver.Firefox()
web.set_window_position(0,0)
web.set_window_size(1440,900)
i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage{}.png".format(i))
    i+=1

web.quit()




