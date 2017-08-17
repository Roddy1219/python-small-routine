#!/bin/env python
#coding:utf8
"""
通过ast.literal_eval获取json文件数据
"""


import sys,ast
scores=dict()
with open('test.txt','r') as p:
    filedata = p.read()
    scores = ast.literal_eval(filedata)

for k,v in scores.items():
    print k,v
