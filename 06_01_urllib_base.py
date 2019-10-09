# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/9 14:34
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 06_01_urllib_base.py
# Description :
# ----------------------------------
'''
urllib基础
	1、urlretrieve(url, filename=None, reporthook=None, data=None)  直接下载网页到本地
	2、urlcleanup():Clean up temporary files from urlretrieve calls 清除缓存
	3、urlopen(url,*)  看网页相应的简介信息info()
	4、getcode()： 返回网页爬取的状态码
	5、geturl()：获取当前访问的网页的url
'''
import urllib.request  # 导入模块

# urlretrieve(网址,本地文件存储地址) 直接下载网页到本地
urllib.request.urlretrieve("http://www.baidu.com","06_01_dld.html")
urllib.request.urlcleanup()
# 看网页相应的简介信息info()
file = urllib.request.urlopen("https://read.douban.com/provider/all")
print(file.info())
# 返回网页爬取的状态码getcode()
print(file.getcode())
# 获取当前访问的网页的url，geturl()
print(file.geturl())

