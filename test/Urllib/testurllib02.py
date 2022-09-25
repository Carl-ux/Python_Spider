import urllib.parse
import urllib.request

#从爬虫伪装成浏览器
#更改User-Agent
baseurl = "http://httpbin.org/post"
#伪装告知目标网址  来自的操作系统和浏览器等信息
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
postdata = bytes(urllib.parse.urlencode({'name':'Carl'}),encoding="utf-8")

#构建的请求 Request用于请求页面的数据
req = urllib.request.Request(url=baseurl,data=postdata,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))