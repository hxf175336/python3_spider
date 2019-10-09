# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/9 9:14
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 07_python_file.py
# Description :
# ----------------------------------
'''
python的基本语法知识
	文件的操作：
'''
#打开
#open(文件地址,操作形式)

'''
w:写入
r:读取
b:二进制
a:追加
'''

'''
#文件目录：G:\study\A2_python\A3_Spider\学习笔记.txt 注意将\处理成/
fh=open("G:/study/A2_python/A3_Spider/学习笔记.txt","r",encoding='UTF-8')
#文件读取
data_all=fh.read()
print(data_all)
data_line=fh.readline()
print(data_line)
#关闭文件
fh.close()
'''

#文件写入
data="一起学pyhton！"
fh2=open("文本1.txt","w",encoding='UTF-8')
fh2.write(data)
fh2.close()
#追加写入
fh3=open("文本1.txt","a+",encoding='UTF-8')
fh3.write(data)
fh3.close()



