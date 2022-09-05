import requests
import re
import sys

def login(rhost):
    s = requests.Session()
    login_url = "http://{}/dvwa/login.php".format(rhost)
    #req = s.get(login_url)
    #match = re.search(r'([a-z,0-9]){32}', req.text)
    #token = match.group(0)
    data = {'username':'admin','password':'password','Login':'Login'}#,'user_token':token}
    login = s.post(url=login_url, data=data)
    if "Welcome" in login.text:
        print("login successful")
        print("admin cookie: {}".format(s.cookies["PHPSESSID"]))
    return s

def main():
    rhost = sys.argv[1]
    sess = login(rhost)
        
if __name__ == "__main__":
    main()
