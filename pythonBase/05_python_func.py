# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/9 8:27
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 05_python_func.py
# Description :
# ----------------------------------
'''
	python的基本语法知识
		funcation 函数 局部变量与全局变量
		变量就是有生效范围的，即作用域
'''

'''
# 1、作用域
i=10
def func():
	j=10
	print(j)
print(i)
func()
print(j)
'''
'''
输出结果：
	10
	10
	Traceback (most recent call last):
  	File "F:/Projects/Python/python3_spider/pythonBase/05_python_func.py", line 22, in <module>
    	print(j)
	NameError: name 'j' is not defined
	
'''

'''
2、函数定义的格式：
	def 函数名(参数):
		函数体
'''
def abc():
	print("abc")
	print("456")
#3、调用函数：函数名(参数)
abc()
#4、参数：与外界的接口，分为形参与实参，一般在函数定义时使用的是形参，函数调用时是实参
def func2(a,b):
	if(a>b):
		print(str(a)+"比"+str(b)+"大")
	else:
		print(str(b)+"比"+str(a)+"大或者"+str(b)+"与"+str(a)+"一样大")

func2(4,5)










