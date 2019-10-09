# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/9 10:26
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : excel_merge.py
# Description :出版社爬取
# ----------------------------------
import re


# 出版社爬取
import urllib.request  # 导入请求模块
import re  # 导入正则模块

data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
pat = '<div class="name">(.*?)</div>'   # 正则匹配表达式
rst = re.compile(pat).findall(data)     # 正则匹配
fh = open("06_0_chubanshe.txt", "w")
for i in range(0, len(rst)):
	# print(rst[i])
	fh.write(rst[i] + "\n")
fh.close()

