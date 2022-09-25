#查询数据
import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")
#获取游标
c = conn.cursor()

sql = "select id,name,address,salary from company"
#执行sql语句
cursor = c.execute(sql)
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")

#提交数据库操作
conn.commit()
conn.close()
print("查询数据完毕")