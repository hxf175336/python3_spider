# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/10 9:58
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 06_03_http_request.py
# Description :
# ----------------------------------
'''
自动模拟HTTP请求：
	客户端与服务端需要通过HTTP请求进行通信
	常用的方式：get 和 post
'''

# 1、get请求实战--实现百度信息自动搜索
'''
#	实现单页
import urllib.request,re
keywd="Python"  #关键词
keywd=urllib.request.quote(keywd)  # 中文的关键词需要转码
url='http://www.baidu.com/s?wd='+keywd
data=urllib.request.urlopen(url).read().decode('utf-8')
pat="title:'(.*?)',"
pat2='"title":"(.*?)",'
rst1=re.compile(pat).findall(data)
rst2=re.compile(pat2).findall(data)
print(rst1)
print(rst2)
'''

'''
import urllib.request,re
keywd="Python"  #关键词
keywd=urllib.request.quote(keywd)  # 中文的关键词需要转码
# page=(num-1)*10
for i in range(1,11):
    url="http://www.baidu.com/s?wd="+keywd+"&pn="+str((i-1)*10)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    pat="title:'(.*?)',"
    pat2='"title":"(.*?)",'
    rst1=re.compile(pat).findall(data)
    rst2=re.compile(pat2).findall(data)
    for j in range(0,len(rst1)):#遍历查看结果
        print(rst1[j])
    for z in range(0,len(rst2)):
        print(rst2[z])
'''

# 2、post请求实战
import urllib.request
import urllib.parse

posturl="http://www.iqianyue.com/mypost/"  # 初始posturl
postdata=urllib.parse.urlencode({          # 数据封装
    "name":"ceo@txk7.com",
    "pass":"kjsahgjkashg",
    }).encode("utf-8")
#进行post，就需要使用urllib.request下面的Request(真实post地址,post数据)
req=urllib.request.Request(posturl,postdata) # 封装请求
rst=urllib.request.urlopen(req).read().decode("utf-8") # 打开网页
# print(rst)
fh=open("06_03_post.html","w") # 写入本地文件
fh.write(rst)
fh.close()


