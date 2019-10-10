# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/10 13:45
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 06_04_err_deal.py
# Description :异常处理
# ----------------------------------
'''
异常处理：
	常见状态码及含义
		301 Moved Permanently：重定向到新的URL，永久性
		302 Found：重定向到临时的URL，非永久性
		304 Not Modified：请求的资源未更新
		400 Bad Request：非法请求
		401 Unauthorized：请求未经授权
		403 Forbidden：禁止访问
		404 Not Found：没有找到对应页面
		500 Internal Server Error：服务器内部出现问题
		501 Not Implemented：服务器不支持实现请求所需要的功能
	URLError与HTTPError
		两者都是异常处理的类，HTTPError是URLError的子类
	URLError出现的原因：
		1）连不上服务器
		2）远程url不存在
		3）无网络
		4）触发HTTPError
'''
'''
import urllib.request
import urllib.error # 异常处理模块

try:
	urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.HTTPError as e:
	if hasattr(e,"code"):
		print(e.code)
	if hasattr(e,"reason"):
		print(e.reason)
'''

'''
浏览器伪装技术
	爬取网页出现403错误，是因为对方服务器会对爬虫进行屏蔽，需要伪装成浏览器才能爬取。
	浏览器伪装我们一般通过报头进行。
	实现浏览器模拟：urllib.request.build_opener() 和 urllib.request.Request()下的add_header()
'''
#浏览器伪装技术实战
import urllib.request
url="http://blog.csdn.net"
#头文件格式header=("User-Agent",具体用户代理值)
# headers=("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36")
# opener=urllib.request.build_opener()
# opener.addheaders=[headers]
data=urllib.request.urlopen(url).read()
fh=open("data\\ua.html","wb")
fh.write(data)
fh.close()

#需要研究的问题
#1、(以后会讲，大家先探索)如何将opener安装为全局，让urlopen()访问时也添加对应报头？
#2、研究一下使用Request的方式进行报头添加。（非重点，不讲，自行探索研究）

