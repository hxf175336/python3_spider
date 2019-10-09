# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/9 9:42
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 08_try.py
# Description :
# ----------------------------------
'''
python的基本语法知识
	异常处理:
		格式：
			try:
				正常程序
			except Exception as 异常名称:
				异常处理部分

'''
try:
	for i in range(1,10):
		print(i)
		if(i==4):
			print(jkl)
	print("hello")
except Exception as err:
	print(err)

#让异常后的程序继续
	for i in range(1,10):
		try:
			print(i)
			if(i==4):
				print(jkl)
		except Exception as err:
			print(err)
print("hello")