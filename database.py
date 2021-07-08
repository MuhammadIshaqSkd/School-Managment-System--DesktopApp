import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="school"
)

mycursor = mydb.cursor()

#------------------Creating Database -------------------------------

# mycursor.execute("CREATE DATABASE school")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

#------------------Creating Table-------------------------------

#___________________student__________________________________

# mycursor.execute("CREATE TABLE student (name VARCHAR(25), age INT ,email  varchar(200),gender VARCHAR(20),rollno INT, Department VARCHAR(20),regular VARCHAR(10),pass  Varchar(30))")

#___________________teacher__________________________________

# mycursor.execute("CREATE TABLE teacher (name VARCHAR(25), age INT ,email  varchar(200),gender VARCHAR(20), Department VARCHAR(20),regular  VARCHAR(10),pass  Varchar(30))")

# ___________________admins__________________________________

# mycursor.execute("CREATE TABLE admins (name VARCHAR(25), age INT ,email  varchar(200),pass Varchar(8))")

#________________ Result ____________________________________

# mycursor.execute("CREATE TABLE result (subjname Varchar(59), rollno INT,AM INT,QM INT,Grade VarChar(10),attd Varchar(5))")

#____________________Records____________________________________________________

# mycursor.execute("CREATE TABLE records (email Varchar(59), rollno INT)")

#____________________Notifications____________________________________________________

# mycursor.execute("CREATE TABLE notifications (notis Varchar(300),dates INT)")


# mycursor.execute("CREATE TABLE staff (notis Varchar(300),dates INT)")

#______________________ TABLES ______________________________________________________

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)


#------------------------Inserting Data into Table----------------------

# sql = "INSERT INTO notifications (notis,dates) VALUES (%s,%s)"
# val = ('Last date of fees submisstion is 22 march 2021',25)
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

#_____Joins____________________________________

# sql="SELECT * FROM result left JOIN student ON result.rollno = student.rollno WHERE student.email = 'ishaq@gmail.com'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#   print(i)

# #__________________________ Show Table Records_______________________

mycursor.execute("Select * from student ")
myresult = mycursor.fetchall()
for i in myresult:
  print(i)


# for x in myresult:
#   if x > 1:
#     print("Increasing")

####_______________Update___________________

# useremail = "Ishaq"
# useract = 2

# query2 = "SELECT email FROM test WHERE email='%s'"%useremail

# query = "UPDATE test SET active = 22 WHERE email = '%s';"%useremail
# val =  (query)
# mycursor.execute(query, val)
# mydb.commit()


#------------------Deleting Table-------------------------------

# mycursor.execute("DROP TABLE notifications")

#-------------------Creating Primary Key Id------------------------------------

# mycursor.execute("ALTER TABLE teacher ADD COLUMN Id INT AUTO_INCREMENT PRIMARY KEY")




#------------Medthod 2------------------------------------

# sql = "INSERT INTO teacher (Id, name, address) VALUES (%s,%s, %s)"
# val = [
#   (2,'Peter', 'Lowstreet 4'),
#   (3,'Amy', 'Apple st 652'),
#   (4,'Hannah', 'Mountain 21'),
#   (5,'Michael', 'Valley 345'),
#   (6,'Sandy', 'Ocean blvd 2'),
#   (7,'Betty', 'Green Grass 1'),
#   (8,'Richard', 'Sky st 331'),
#   (9,'Susan', 'One way 98'),
#   (10,'Vicky', 'Yellow Garden 2')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

#------------------Method 3------------------------------------

# sql = "INSERT INTO admins (name , age  ,email ,gender) VALUES (%s,%s, %s,%s)"
# val = ("Muhammad Ishaq",22, "admin@gmail.com","Male")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)



#__________________To show Specific Attributes_________________

# mycursor.execute("SELECT Id,name FROM teacher")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#__________________Fetch Only One Row________________________

# mycursor.execute("SELECT * FROM teacher")

# myresult = mycursor.fetchone()

# print(myresult)

#***********************Searching Record \ Conditions (WHERE)*****

# sql = "SELECT * FROM teacher WHERE Id =8"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# ************LIKE Condition********************************************

# sql = "SELECT * FROM teacher WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#***********************Escape*********************************************

# sql = "SELECT * FROM teacher WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

###########################ORDER BY #############################

# sql = "SELECT * FROM teacher ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

##################### ORDER BY DEC ##############################

# sql = "SELECT * FROM teacher ORDER BY Id DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# ____________________Delete__________________________________

# sql = "DELETE FROM student WHERE name = "Akmal""

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "records deleted")

#______________________By Escape %s Method ____________________

# sql = "DELETE FROM teacher WHERE Id = %s"
# Ids = (10, )

# mycursor.execute(sql, Ids)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

#_________________UPDATE_________________________________________

# sql = "UPDATE teacher SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

#_________________Limit___________________________________________

# mycursor.execute("SELECT * FROM teacher LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#_________________Offset Limit______________________________________

# mycursor.execute("SELECT * FROM teacher LIMIT 5 OFFSET 3")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# mycursor.execute("SELECT * from teacher ,student where teacher.Department = student.Department order by student.name")
# myresult = mycursor.fetchall()

# for x in myresult:
#       print(x)


mydb.close()


