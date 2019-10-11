# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/11 10:10
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 08_02_ip_proxy.py
# Description :
# ----------------------------------
'''
IP代理
	IP代理概述
		IP代理指的是让爬虫使用代理IP去爬取对方网站
	IP代理池构建的第一种方式
	IP代理池构建的第二种方式
'''

'''
# IP代理构建实战
import urllib.request
ip="94.141.244.39:34919"
proxy=urllib.request.ProxyHandler({"http":ip})
# print(proxy)
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url="http://www.baidu.com"
data=urllib.request.urlopen(url).read().decode("gbk","ignore")
print(len(data))
fh=open("data\\rst\\ip_baidu.html","w")
fh.write(data)
fh.close()
'''

'''
# IP代理池构建的第一种方案(适合于代理IP稳定的情况)
import random
import urllib.request

ippools = [
	"94.141.244.39:34919",
	"178.213.13.136:53281",
	"103.226.51.80:8080",
	"154.66.241.27:52004",
]

#自定义函数，选择ip，代理ip池
def ip(ippools):
	thisip=random.choice(ippools)
	# print(thisip)
	proxy = urllib.request.ProxyHandler({"http": thisip})
	print(proxy)
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)

for i in range(0,5):
	try:
		ip(ippools)
		url="http://www.baidu.com"
		data=urllib.request.urlopen(url).read().decode("gbk","ignore")
		print(len(data))
		fh=open("data\\rst\\ip_baidu_"+str(i)+".html","w")
		fh.write(data)
		fh.close()
	except Exception as err:
		print(err)
'''

'''
# IP代理池构建的第二种方案(接口调用法，这种方法更适合于代理IP不稳定的情况)
'''
import urllib.request
def ip():
	thisip=urllib.request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=559126871522487&num=10&foreign=only&filter=on").read().decode("utf-8","ignore")
	print(thisip)
	proxy = urllib.request.ProxyHandler({"http": thisip})
	# print(proxy)
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)

for i in range(0,5):
	try:
		ip()
		url="http://www.baidu.com"
		data=urllib.request.urlopen(url).read().decode("gbk","ignore")
		print(len(data))
		fh=open("data\\rst\\ip_baidu_"+str(i)+".html","w")
		fh.write(data)
		fh.close()
	except Exception as err:
		print(err)