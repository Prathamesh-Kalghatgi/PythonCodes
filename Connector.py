import mysql.connector

conn = mysql.connector.connect(host="localhost", database="employee", user="root", password="root@1234")
cursor = conn.cursor()
print(conn.is_connected())

mysql = "select * from employees"
cursor.execute(mysql)
rows = cursor.fetchall()
# To print as an sql output use for loop
for data in rows:
    print(data)