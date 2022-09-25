from bs4 import BeautifulSoup
import re

file = open("test/Bs4/baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")     #html.parser为解析器

#文档的遍历
#Tag的contents 获取所有Tag的子节点 返回一个list
print(bs.head.contents)
print(bs.head.contents[1])
#children  获取Tag的所有子节点 返回一个生成器
for child in bs.body.children:
    print(child)

#文档的搜索
t_list = bs.find_all("a")
print(t_list)

#正则表达式搜索：使用search()方法来匹配内容
tt_list = bs.find_all(re.compile("a"))    #按标签找
print(tt_list)

#方法：传入一个函数，根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")
ttt_list = bs.find_all(name_is_exists)
print(ttt_list)


#2.kwargs    参数
k_list = bs.find_all(class_=True)       #class是python关键字 需要加下划线区分
for item in k_list:
    print(item)

#3.text参数
kk_list = bs.find_all(text = "hao123")
kk_list = bs.find_all(text = ["地图","贴吧"])
#也可以用正则表达式来查找包含特定文本里的内容(标签里的字符串)
kk_list = bs.find_all(text = re.compile("\d"))
print(kk_list)

#4.limit参数
kkk_list = bs.find_all("a",limit=3)
print(kkk_list)

#css选择器
print(bs.select('title'))
print(bs.select('.mnav'))              #通过类名查找
print(bs.select('#u1'))                #通过id来查找
print(bs.select('a[class="bri"]'))     #通过属性查找