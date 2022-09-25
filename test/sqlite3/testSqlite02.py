#插入数据
import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")
#获取游标
c = conn.cursor()

sql = '''
    insert into company(id,name,age,address,salary)
    values(2,"lisi",40,"beijing",7200)
'''

#执行sql语句
c.execute(sql)
#提交数据库操作
conn.commit()
conn.close()
print("插入数据完毕")