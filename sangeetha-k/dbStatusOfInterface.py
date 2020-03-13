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

# to find status of a given interface
interName = input('Enter interface name whose status need to be checked: ')
mycursor.execute("SELECT status FROM interfacedetail WHERE interface = %s", (interName,))
status = mycursor.fetchall()
print(status)

#  to find interface and IP of all interfaces which are up
mycursor.execute("SELECT interface, IP FROM interfacedetail WHERE status = %s", ("up",))
upInterfaces = mycursor.fetchall()
print('Interface and their IP whose status is up')
for row in upInterfaces:
    print('Interface:', row[0])
    print('IP: ', row[1], "\n")

# to count how many ethernet interfaces are there
mycursor.execute("SELECT interface FROM interfacedetail WHERE interface LIKE 'Ethernet%'")
ethernetInterfaces = mycursor.fetchall()
print('Total number of ethernet interfaces: ', len(ethernetInterfaces))

# to add a new entry to above database
newInterface = input('Enter new interface: ')
newIP = input('Enter IP address: ')
newStatus = input('Enter status')
newValues = (newInterface, newIP, newStatus)

mycursor.execute(insertQuery, newValues)
print(mycursor.rowcount, " row inserted")
mydb.commit()