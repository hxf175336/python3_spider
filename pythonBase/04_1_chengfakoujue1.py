# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/9 8:07
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 04_0_chengfakoujue.py
# Description :
# ----------------------------------
'''
	python的基本语法知识
		for循环
'''

'''
乘法口诀逆向输出
	end="" 代表不换行输出
'''
for i in range(9,0,-1):
	for j in range(i,0,-1):
		print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
	print()# 换行
