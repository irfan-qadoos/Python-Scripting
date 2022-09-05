#!/usr/bin/env python

import mechanize

br = mechanize.Browser()
url = "http://192.168.210.130/dvwa/login.php"
br.open(url)

br.select_form(nr=0)
br.form['username'] = 'admin'
br.form['password'] = 'password'
br.submit()

print(br.title())
print(br.geturl())

