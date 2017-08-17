#!/bin/env python
#coding:utf8

"""
   pip install beautifulsoup4
"""

from bs4 import BeautifulSoup

import requests
import sys,os
from urlparse import urlparse
from urllib import urlopen

url = 'http://cd.qq.com/'
domain = "%s://%s" % (urlparse(url).scheme,urlparse(url).hostname)
html = requests.get(url).text
sp  = BeautifulSoup(html,'html.parser')
alldata = sp.find_all(['IP_content'])
print alldata
