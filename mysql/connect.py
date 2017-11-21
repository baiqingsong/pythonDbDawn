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