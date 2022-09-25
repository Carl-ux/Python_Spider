#httpbin.org    A simple HTTP Request & Response Service
import urllib.request

# #获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))          #以utf-8编码解析



#获取一个post请求   用于模拟
import urllib.parse
dict = {
        "name":"Carl",
        "key":"123456"
    }
#bytes()函数返回一个新的“bytes"对象，是0<=x<256范围内的不可变整数序列 变为字节文件
#urlencode()函数可以将一个dict字典转换成合法的查询参数
postdata = bytes(urllib.parse.urlencode(dict),encoding = "utf-8")
response = urllib.request.urlopen("https://httpbin.org/post",data = postdata)
print(response.read().decode('utf-8'))


#超时 设定反应时间
try:
    response = urllib.request.urlopen("https://httpbin.org/get",timeout = 0.1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("time out")


#响应报文内容
response = urllib.request.urlopen("https://httpbin.org/get")
print(response.status)            #状态码
print(response.getheaders())      #响应头

