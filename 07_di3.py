# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/10 16:11
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 07_di3.py
# Description :
# ----------------------------------
'''
#1、CSDN博文爬虫
import urllib.request
import re
import urllib.error

url = "https://www.csdn.net/"  #这里不需要浏览器伪装
# headers=("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36")
# opener=urllib.request.build_opener()#浏览器伪装
# opener.addheaders=[headers]
# urllib.request.install_opener(opener) #安装为全局

data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
pat = '<a href="(.*?)" target="_blank"'
alllink = re.compile(pat).findall(data)
# print(alllink)

for i in range(0, len(alllink)):
	try:
		locaPath = "data\\" + str(i) + ".html"
		thisLink = alllink[i]
		urllib.request.urlretrieve(thisLink, filename=locaPath)
	except urllib.error.URLError as e:
		print("当前文章(第" + str(i) + "篇）爬取失败！")
		print(e.code,e.reason)
	print("当前文章(第" + str(i) + "篇）爬取成功！")

'''

'''
糗事百科段子爬虫
    关键点：(1)浏览器的伪装(2)正则表达式的书写(3)模式修正符的应用
'''

import urllib.request
import re

headers = ("User-Agent",
		   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 安装为全局
urllib.request.install_opener(opener)
for i in range(0, 35):
	thisurl = "http://www.qiushibaike.com/8hr/page/" + str(i + 1) + "/?s=4948859"  # 网址的构造很重要
	data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
	pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
	rst = re.compile(pat, re.S).findall(data)
	for j in range(0, len(rst)):
		print(rst[j])
		print("-------")
