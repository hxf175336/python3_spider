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
import requests  # 导入requests库
import pymongo   # 导入pymongo
from urllib.parse import urlencode  # 导入解码库

from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError  # 导入异常处理的库
from pyquery import PyQuery as pq   # 导入PyQuery解析库
from config import *
# 声明mongodb信息
client=pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]

base_url = 'https://weixin.sogou.com/weixin?'

headers = {
	'Cookie': 'IPLOC=CN3100; CXID=6C2BC3937A67162051EB788D0F5E30D7; SUID=421DCF8C5018910A000000005D999C98; SUV=1570348185231476; ABTEST=0|1570348187|v1; weixinIndexVisited=1; JSESSIONID=aaantZQI_Xk-9fjAxju1w; PHPSESSID=4e3278kedfmg8rdrhr6kksbm63; usid=FdMM32Bv34eX_zdR; sct=2; SNUID=B9E73576FBFE6EC03B8EBFA6FBCC8C81; ppinf=5|1570359626|1571569226|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTYlOTclQjYlRTUlODUlODl8Y3J0OjEwOjE1NzAzNTk2MjZ8cmVmbmljazoxODolRTYlOTclQjYlRTUlODUlODl8dXNlcmlkOjQ0Om85dDJsdU5fcW52QU41YXE5UjlXMXR3TEgtbVVAd2VpeGluLnNvaHUuY29tfA; pprdig=UuGnb4KSI2XqqHMDA23oVNkUCtnQCTbWpQd67jmgJJHD6s2OlzIPAIrX-Z_NpSVrqwryfUCqbenk5eM8Gi2_JTERa5053PbQq9m1fGap8AkbC_5r_SApkPheORG1-8qSvI7podsFxjLWqk40BXmXCNTzgV45J7RbCoj5UIOpkt8; sgid=14-43608903-AV2ZyUpsb7ZicPrgIQYcl3icI; ppmdig=157035962600000011c0c93fd149b833e5457b6a649aa617',
	'Host': 'weixin.sogou.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36',

}


proxy=None  # 代理初始值
max_count=4 # 最大请求次数


# 获取代理的方法
def get_proxy():
	try:
		response=requests.get(PROXY_POOL_URL)
		if response.status_code==200:
			return response.text
		return None
	except ConnectionError:
		return None

# 请求网页
def get_html(url,count=1):
	print('Crawling',url)
	global proxy  #引入全局变量
	# 加一个请求次数判断
	if count>=max_count:
		print('Tried Too Many Counts')
		return None
	try:
		#添加一个是否有代理的判断
		if proxy:
			proxies={
				'http':'http://'+proxy
			}
			response = requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
		else:
			response = requests.get(url, allow_redirects=False, headers=headers)
		# 状态码判断
		if response.status_code == 200:
			return response.text
		if response.status_code == 302:
			# Need Proxy
			print('302')
			if proxy:  # 如果代理存在的话就一直使用这个代理
				print('Using Proxy',proxy)
				return get_html(url)
			else:
				print('Get Proxy Failed')
				return None
	except ConnectionError as e:
		print('Error Occurred',e.args)
		proxy=get_proxy()
		count+=1
		return get_html(url,count)  # 重新调用

# 获取索引页
def get_index(keyword, page):
	data = {
		'query': keyword,
		'type': 2,
		'page': page
	}
	queries = urlencode(data)  # 进行编码转为get请求参数的格式
	url = base_url + queries  # url拼接
	html = get_html(url)
	return html

#解析索引页
def parse_index(html):
	doc = pq(html)
	items = doc('.new-box .new-list li .txt-box h3 a').items() # 拼接链接
	for item in items:
		yield item.attr('href')

# 抓取详情页
def get_detail(url):
	try:
		response=requests.get(url)
		if response.status_code==200:
			return response.text
		return None
	except ConnectionError:
		return None

# 解析详情页
def parse_detail(url):
	try:
		doc = pq(html)
		title= doc('.rich_media_title').text()
		content=doc('.rich_media_content ').text
		date=doc('#publish_time').text()
		nickname =doc('.rich_media_meta_list .rich_media_meta_nickname')
		wechat = doc('#profileBt').text()
		return {
			'title':title,
			'content':content,
			'date':date,
			'nickname':nickname,
			'wechat':wechat
		}
	except XMLSyntaxError:
		return None

# 保存到数据库
def save_to_mongo(data):
	if db['article'].update({'title':data['title']},{'$set':data},True):
		print('Save to Mongo',data['title'])
	else:
		print('Save to Mongo Failed',data['title'])

def main():
	for page in range(1,101):
		html=get_index(KEYWORD,page)
		if html:
			article_urls=parse_index(html)
			for article_url in article_urls:
				article_html=get_detail(article_url)
				if article_html:
					article_date=parse_detail(article_html)
					print(article_date)
					if article_date:
						save_to_mongo(article_date)

if __name__ == '__main__':
    main()