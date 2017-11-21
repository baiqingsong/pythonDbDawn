# Python中Mysql的操作

* [python的MySQL官网地址](#python的mysql官网地址)
* [MySQL-python](#mysql-python)
* [connection](#connection)
* [cursor](#cursor)

## python的MySQL官网地址
[https://www.python.org/dev/peps/pep-0249/](https://www.python.org/dev/peps/pep-0249/)

## MySQL-python
要使用MySQL需要先下载插件MySQL-python，下载地址  
[http://www.codegood.com/](http://www.codegood.com/)  

## connection
数据库连接：
```
import MySQLdb

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='',
    db='',
    charset='utf8'
)
```
注意Connection实例需要关闭conn.close()  
`host`                MySQL服务器地址  
`port`                MySQL服务器端口号，数字类型  
`user`                用户名  
`passwd`              密码  
`db`                  数据库名称  
`charset`             连接编码  

connection对象支持的方法  
`cursor()`            使用该连接创建并返回游标  
`commit()`            提交当前事务  
`rollback()`          回滚当前事务  
`close()`             关闭连接  

## cursor
cursor对象支持的方法  
`execute(op[,args])`          执行一个数据库查询和命令  
`fetchone()`                  获取结果集的下一行  
`fetchmany(size)`             获取结果集的下几行  
`fetchall()`                  获取结果集中剩下的所有行  
`rowcount`                    最近一次execute返回数据的行数或影响行数  
`close()`                     关闭游标对象  

事务：访问和更新数据库的一个程序执行单元  
1. 原子性：事务中包含的诸多操作要么都做，要么都不做  
2. 一致性：事务必须使数据库从一致性状态到另一个一致性状态  
3. 隔离性：一个事务的执行不能被其他事务干扰  
4. 持久性：事务一旦提交，它对数据库的改变使永久性的  
使用事务：
1. 关闭自动commit,设置conn.autocommit(False)
2. 正常结束事务，conn.commit()
3. 异常结束事务，conn.rollback()

创建表时，设置ENGINE = INNOB，不能设置成MyISAM

查询：
```
import MySQLdb

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='bai910214',
    db='dawn',
    charset='utf8'
)
cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)
rs = cursor.fetchall()
for row in rs:
    print "user_id = %s, username = %s" % row

cursor.close()
conn.close()
```

插入，更新，删除
```
import MySQLdb

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='bai910214',
    db='dawn',
    charset='utf8'
)
cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)
rs = cursor.fetchall()
for row in rs:
    print "user_id = %s, username = %s" % row

sqlInsert = "insert into user(user_id, username) values(5, 'name5')"
sqlUpdate = "update user set username='name001' where user_id=1"
sqlDelete = "delete from user where user_id=11"

try:
    cursor.execute(sqlInsert)
    cursor.execute(sqlUpdate)
    cursor.execute(sqlDelete)
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

sql = "select * from user"
cursor.execute(sql)
rs = cursor.fetchall()
for row in rs:
    print "user_id = %s, username = %s" % row

cursor.close()
conn.close()
```
判断插入，修改，删除是否成功，用cursor.rowcount != 1  
判断查询是否成功，用len(cursor.fetchall()) != 1  
抛出异常raise Exception("异常说明")  
抛出异常后，不要忘了，finally中关闭指针