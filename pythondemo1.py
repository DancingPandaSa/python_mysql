import mysql.connector

#
print("建立資料庫連線中")
mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="dbuser",
    password="1234",
    database="world"

)
print("透過連線取得 cursor物件")
dbcursor=cnx.cursor()
print("執行 select name from city")
dbcursor.execute("select name from city")