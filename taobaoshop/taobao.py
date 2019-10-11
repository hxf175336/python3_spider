# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/11 14:13
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : taobao.py
# Description :
# ----------------------------------
'''
爬取淘宝商品
	注意已经用js封装了就爬取不了

'''

import urllib.request
import re
import random

keyname="连衣裙"  # 关键词
key =urllib.request.quote(keyname) # 转码，解析成计算机可以识别的

# 代理池
uapools=[
	" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
	"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36 2345Explorer/10.4.0.19679",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0"
]

#选择代理的函数
def ua(uapools):
	thisua=random.choice(uapools)
	print(thisua)
	headers = ("User-Agent",thisua)
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	# 安装为全局
	urllib.request.install_opener(opener)

for i in range(1,101):
	url = "https://s.taobao.com/search?q="+key+"&s="+str((i-1)*44)

	ua(uapools)
	data = urllib.request.urlopen(url).read().decode("UTF-8", "ignore") # 爬取一页
	# print(len(data))
	pat='"data-src":"//(.*?)"'
	imglist=re.compile(pat).findall(data)
	# print(i)
	for j in range(0,len(imglist)):
		try:
			thisimg=imglist[j]
			thisimgurl="http://"+thisimg
			localfile="data\\rst\\taobao\\"+str(i)+str(j)+".jpg"
			urllib.request.urlretrieve(thisimgurl,filename=localfile)
		except Exception as err:
			print(err)
