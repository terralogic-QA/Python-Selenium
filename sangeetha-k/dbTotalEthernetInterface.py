import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="terralogic",
  database="mydatabase"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE interfacedetail (interface varchar(20), IP varchar(20), status varchar(20))")

insertQuery = "INSERT INTO interfacedetail(interface, IP, status) VALUES (%s, %s, %s)"
# val = (("Ethernet0", "1.1.1.1", "up"), ("Ethernet1", "2.2.2.2", "down"), ("Serial0", "3.3.3.3", "up"), ("Serial1", "4.4.4.4", "up"))
# mycursor.executemany(insertQuery, val)
# mydb.commit()
# print(mycursor.rowcount, "rows were inserted.")

# to count how many ethernet interfaces are there
mycursor.execute("SELECT interface FROM interfacedetail WHERE interface LIKE 'Ethernet%'")
ethernetInterfaces = mycursor.fetchall()
print('Total number of ethernet interfaces: ', len(ethernetInterfaces))
