#伪装访问豆瓣
import urllib.parse
import urllib.request

baseurl = "https://www.douban.com"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

req = urllib.request.Request(url=baseurl,headers=headers,method="GET")
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))