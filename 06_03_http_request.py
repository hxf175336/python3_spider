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


# 异常处理
'''
URLError出现的原因：
1）连不上服务器
2）远程url不存在
3）无网络
4）触发HTTPError
'''
'''
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
'''
'''
#浏览器伪装
import urllib.request
url="http://blog.csdn.net"
#头文件格式header=("User-Agent",具体用户代理值)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\ua.html","wb")
fh.write(data)
fh.close()
#需要研究的问题
#1、（以后会讲，大家先探索）如何将opener安装为全局，让urlopen()访问时也添加对应报头？
#2、研究一下使用Request的方式进行报头添加。（非重点，不讲，自行探索研究）
'''

# #爬取腾讯新闻首页所有新闻内容
# '''
# 1、爬取新闻首页
# 2、得到各新闻链接
# 3、爬取新闻链接
# 4、寻找有没有frame
# 5、若有，抓取frame下对应网页内容
# 6、若没有，直接抓取当前页面
# '''
# import urllib.request
# import re
# url="http://news.qq.com/"
# data=urllib.request.urlopen(url).read().decode("UTF-8","ignore")
# pat1='<a target="_blank" class="linkto" href="(.*?)"'
# alllink=re.compile(pat1).findall(data)
# for i in range(0,len(alllink)):
#     thislink=alllink[i]
#     thispage=urllib.request.urlopen(thislink).read().decode("gb2312","ignore")
#     pat2="<frame src=(.*?)>"
#     isframe=re.compile(pat2).findall(thispage)
#     if(len(isframe)==0):
#         #直接爬
#         print(i)
#         urllib.request.urlretrieve(thislink,"D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\data\\"+str(i)+".html")
#     else:
#         #得到frame的网址爬
#         flink=isframe[0]
#         urllib.request.urlretrieve(flink,"D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\data\\"+str(i)+".html")
#
