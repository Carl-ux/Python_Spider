#正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re        #regular expression 

#此处的AA是正则表达式 用来验证其它字符串
pat = re.compile("AA")
#被校验的内容          search()方法进行比对查找
m0 = pat.search("CBA")
print(m0)

m1 = pat.search("ABCAA")
print(m1)

m2 = pat.search("ABCAADDCCAAA")
print(m2)

#无模式对象  前字符串是规则(正则表达式)
m3 = re.search("asd","Aasdss")
print(m3)

m4 = re.findall("a","ASDaDFGAa")
print(m4)

m5 = re.findall("[A-Z]","ASDaDFGAa")
print(m5)

m6 = re.findall("[A-Z]+","ASDaDFGAa")
print(m6)

#sub
print(re.sub("a","A","abcdcasd"))        #找到a用A替换