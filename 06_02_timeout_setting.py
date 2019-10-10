# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/9 14:53
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : 06_02_timeout_setting.py
# Description :超时设置
# ----------------------------------
'''
urlopen(
	url,
	data=None,
	timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
	*,
	cafile=None,
	capath=None,
	cadefault=False,
	context=None
	)

'''
import urllib.request
for i in range(0,100):
    try:
        file=urllib.request.urlopen("http://www.baidu.com",timeout=1)
        print(len(file.read().decode("utf-8")))
    except Exception as err:
        print("出现异常"+str(err))
