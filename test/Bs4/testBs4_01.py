#BeautifulSoup4 将复杂HTML文档转换成复杂的树形结构 每个节点都是Python对象
#对象归纳为4种
'''
 - Tag
 - NavigableString
 - BeautifulSoup
 - Comment
'''

from bs4 import BeautifulSoup
file = open("test/Bs4/baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")     #html.parser为解析器

print(bs.title)
print(bs.a)

print(type(bs.head))

#1.Tag   标签及其内容，拿到所找到的第一个内容
print(bs.title.string)
#2.NavigableString 标签里的内容 字符串
print(bs.a.attrs)        #获取属性值
#3.BeautifulSoup
print(bs.attrs)
print(type(bs))
#4.comment 注释
print(bs.a.string)
print(type(bs.a.string))