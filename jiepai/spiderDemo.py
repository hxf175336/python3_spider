# -*- coding: utf-8 -*-
# --------------------------------------
# @Time    : 2019/10/5 13:21
# @Author  : hxf
# @Email   : 1870212598@qq.com
# @File    : spiderDemo.py
# Description :
# ----------------------------------
import requests
from urllib.parse import urlencode
# requests内置的状态码，可判断url响应是否正确
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re


def get_page(offset):
    # 必须的头请求头信息
    headers = {
        'cookie': 'tt_webid=6667396596445660679; csrftoken=3a212e0c06e7821650315a4fecf47ac9; tt_webid=6667396596445660679; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16b846003e03d7-0dd00a2eb5ea11-353166-1fa400-16b846003e1566; CNZZDATA1259612802=2077267981-1561291030-https%253A%252F%252Fwww.baidu.com%252F%7C1561361230; __tasessionId=4vm71cznd1561363013083; sso_uid_tt=47d6f9788277e4e071f3825a3c36a294; toutiao_sso_user=e02fd616c83dff880adda691cd201aaa; login_flag=6859a0b8ffdb01687b00fe96bbeeba6e; sessionid=21f852358a845d783bdbe1236c9b385b; uid_tt=d40499ec45187c2d411cb7bf656330730d8c15a783bb6284da0f73104cd300a2; sid_tt=21f852358a845d783bdbe1236c9b385b; sid_guard="21f852358a845d783bdbe1236c9b385b|1561363028|15552000|Sat\054 21-Dec-2019 07:57:08 GMT"; s_v_web_id=6f40e192e0bdeb62ff50fca2bcdf2944',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    }
    # 获得的真是url必须的参数构造
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    # 真实url的起始url
    base_url = 'https://www.toutiao.com/api/search/content/?'
    # python内置库解码后的真实url
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url, headers=headers)
        # 是正确的响应，即200
        if 200  == resp.status_code:
            return resp.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    # 街拍的总数据
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('title') is None:
                continue
            title = re.sub('[\t]', '', item.get('title'))
            images = item.get('image_list')
            for image in images:
                # 修复了url更改导致了爬取到的部分是小图的问题
                for each in image.get('url'):
                    if each == 'x':
                        origin_image = re.sub("list/190x124", "large", image.get('url'))
                        break
                    else:
                        origin_image = re.sub("list", "large", image.get('url'))
                yield {
                    'image': origin_image,
                    'title': title
                }


def save_image(item):
    # 文件保存的相对路径
    img_path = 'Jie_Pai' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        # 下载真实图片
        resp = requests.get(item.get('image'))
        # 内置状态码，判断响应是否正确
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                # 图片内容的md5值，避免重复
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    # 报错
    except Exception as e:
        print(e)


def main(offset):
    # 以什么倍数来增长
    json = get_page(offset)
    for item in get_images(json):
        save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()