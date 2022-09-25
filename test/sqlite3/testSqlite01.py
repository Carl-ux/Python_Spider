import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")
#获取游标
c = conn.cursor()

sql = '''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
'''
sql1 = '''
    insert into company(id,name,age,salary)
    values(1,"zhangsan",32,8000)
'''

#执行sql语句
c.execute(sql)
c.execute(sql1)
#提交数据库操作
conn.commit()
conn.close()
print("成功建表")


#Run query快捷键
#Ctrl + shift + Q