# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/6 8:59
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : spider.py
# Description :
# ----------------------------------
'''
Selenium爬取淘宝美食
	淘宝的页面也是通过Ajax来抓取相关数据，但是参数比较复杂，甚至包含加密秘钥。使用selenium来模拟浏览器操作，抓取淘宝商品信息，即可做到可见即可爬。
参考学习链接：https://blog.csdn.net/ynztwlz/article/details/80903678
			 https://blog.csdn.net/sixkery/article/details/81742090
			 https://blog.csdn.net/weixin_43746433/article/details/97623511

爬取流程：
	1.准备工作：安装selenium，pyquery，以及Chrome浏览器并配置ChromeDriver
	2.页面分析
	3.爬取每一页
	4.解析商品列表
	5.保存到MongoDB
	6.查看运行结果
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import re, pymongo

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)#显示等待


def search():
	try:
		browser.get('https://www.taobao.com')
		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
		submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SearchForm > button')))
		input.send_keys('美食')
		submit.click()
		total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
		return total.text
	except TimeoutException:
		return search()

# def next_page(page_number):
# 	#处理翻页的操作
# 	#页面最下方翻页地方输入页码的框出来没有
# 	try:
# 		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span')))
# 		submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_waterfallPagination > div > div > a.pageConfirm')))
# 		input.clear()
# 		input.send_keys(page_number)
# 		submit.click()
# 		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_waterfallPagination > div > div > span.page-cur'), str(page_number)))
# 	except TimeoutException:
# 		next_page(page_number)
#
def get_products():
 	#解析详情列表
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))#看看页面加载出来没有
	html=borwser.page_source#得到网页的源代码
	doc=pq(html)#用pq解析网页源代码
	#得到所有选中的内容
	items=doc('#mainsrp-itemlist .items .item').items()
	for item in items:
		products = {
			'image': item.find('.pic .img').attr('data-src'),
			'price': item.find('.price').text()[3:],
			'deal': item.find('.deal-cnt').text(),
			'title': item.find('.title').text(),
			'shop': item.find('.shop').text(),
			'location': item.find('.location').text()
		}
		print(products)
		save_products(products)

def main():
	total=search()
	total=int(re.compile('(\d*)').search(total).group(1))
	print(total)
	for i in range(2,total+1):
		next_page(i)


if __name__ == '__main__':
	main()
