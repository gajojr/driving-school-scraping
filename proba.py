import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!!okejhokej",
    database="testdatabase"
)

mycursor = db.cursor()


# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")


# mycursor.execute(
#     "INSERT INTO Person (name, age) VALUES(%s, %s)", ("Miloje", 22))
# db.commit()
# mycursor.execute("SELECT * FROM Person")

# for x in mycursor:
#     print(x)


# mycursor.execute("CREATE TABLE Test (name VARCHAR(50), created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("Milojka", datetime.now(), "O"))
# db.commit()

# mycursor.execute("SELECT id, name FROM Test WHERE gender = 'M' ORDER BY id DESC")
# for x in mycursor:
# 	print(x)

# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
# mycursor.execute("DESCRIBE Test")
# for x in mycursor:
# 	print(x)

# mycursor.execute("ALTER TABLE Test DROP food")
# mycursor.execute("DESCRIBE Test")
# for x in mycursor:
# 	print(x)

# mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")
mycursor.execute("DESCRIBE Test")
for x in mycursor:
	print(x)