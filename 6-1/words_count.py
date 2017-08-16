#!/bin/env python
#coding:utf8
from collections import Counter
import re
txt = open('/etc/passwd').read()
content = re.sub("[^a-zA-Z\s]"," ",txt)
c3 = Counter(content.split())
for k,v in c3.items(): print k,":",v
