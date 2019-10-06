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
from urllib.parse import urlencode  # 导入解码库
from requests.exceptions import ConnectionError  # 导入异常处理的库
from pyquery import PyQuery as pq   # 导入PyQuery解析库

base_url = 'https://weixin.sogou.com/weixin?'

headers = {
	'Cookie': 'IPLOC=CN3100; CXID=6C2BC3937A67162051EB788D0F5E30D7; SUID=421DCF8C5018910A000000005D999C98; SUV=1570348185231476; ABTEST=0|1570348187|v1; weixinIndexVisited=1; JSESSIONID=aaantZQI_Xk-9fjAxju1w; PHPSESSID=4e3278kedfmg8rdrhr6kksbm63; usid=FdMM32Bv34eX_zdR; SNUID=6931E3A72B29B8151A87EC192CD567DA; ppinf=5|1570348918|1571558518|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTYlOTclQjYlRTUlODUlODl8Y3J0OjEwOjE1NzAzNDg5MTh8cmVmbmljazoxODolRTYlOTclQjYlRTUlODUlODl8dXNlcmlkOjQ0Om85dDJsdU5fcW52QU41YXE5UjlXMXR3TEgtbVVAd2VpeGluLnNvaHUuY29tfA; pprdig=mMsyZT-j88l6fcORC-3K137kG6pq1xrNGOXTVtoDZvGyZYLSZlQywSrZsZ-9NRDjknD66Zu_KzqpJcZZoVh5XrBKoK89hSLnEkqc5QSZdr71BQVfAkZQz9XOMminU-hzz47kX2XoWF55OIEquIfRIa4tbW4Y14McEq9v_cQE5hc; sgid=14-43608903-AV2Zn3a8VHhfUI16iaXMEo4E; ppmdig=1570348918000000bd84574b72184d4cb10b11c6cedddc67; sct=2',
	'Host': 'weixin.sogou.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36',

}

# 设置全局变量
keyword='风景'
proxy_pool_url='http://127.0.0.1:5000/get'

proxy=None  # 代理初始值
max_count=4 # 最大请求次数


# 获取代理的方法
def get_proxy():
	try:
		response=requests.get(proxy_pool_url)
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
	try:
		response=requests.get(url)
		if response.status_code==200:
			return response.text
		return None
	except ConnectionError:
		return None

def main():
	for page in range(1,101):
		html=get_index(keyword,page)
		if html:
			article_urls=parse_index(html)
			for article_url in article_urls:
				article_html=get_detail(article_url)
				if article_html:
					article_date=parse_detail(article_html)
					print(article_date)



if __name__ == '__main__':
    main()