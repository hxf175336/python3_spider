# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/11 9:37
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 08_01_user_agent_pool.py
# Description :
# ----------------------------------
'''
用户代理池
	用户代理池概述
		将不同的用户代理组建成为一个池子，随后随机调用
	用户代理池构建实战
'''
# 用户代理池的构建
import urllib.request
import re
import random
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

for i in range(0, 35):
	ua(uapools)
	thisurl = "http://www.qiushibaike.com/8hr/page/" + str(i + 1) + "/?s=4948859"  # 网址的构造很重要
	data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
	pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
	rst = re.compile(pat, re.S).findall(data)
	for j in range(0, len(rst)):
		print(rst[j])
		print("-------")

