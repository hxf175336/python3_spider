# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/6 15:59
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : spider.py
# Description :
# ----------------------------------
'''
	用代理爬取微信文章
'''
import requests                     # 导入requests库
from urllib.parse import urlencode

base_url ='https://weixin.sogou.com/weixin?'

def get_index(keyword,page):
	data={
		'query':keyword,
		'type':2,
		'page':page
	}
	queries=urlencode(data)   # 进行编码转为get请求参数的格式
	url =base_url+queries     # url拼接