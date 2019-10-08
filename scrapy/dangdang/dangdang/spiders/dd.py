# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem



class DdSpider(scrapy.Spider):
	name = 'dd'
	allowed_domains = ['dangdang.com']
	start_urls = ['http://search.dangdang.com/?key=%C5%AE%D7%B0%CD%E2%CC%D7&act=input']

	# 提取信息
	def parse(self, response):
		item = DangdangItem()  #实例化对象 name="itemlist-review"
		# 信息提取
		item['title'] = response.xpath("//a[@name='itemlist-picture']/@title").extract()
		item['link']= response.xpath("//a[@name='itemlist-picture']/@href").extract()
		item['comment'] = response.xpath("//a[@name='itemlist-review']/text()").extract()
		# print(item['title'])
		# print(item['link'])
		# print(item['comment'])
		yield item # 提交数据到piplines中
		for i in range(2, 81):
			url = 'http://search.dangdang.com/?key=%C5%AE%D7%B0%CD%E2%CC%D7&act=input&page_index=' + str(i)
			yield Request(url, callback=self.parse)


