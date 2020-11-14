import mysql.connector
# from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!!okejhokej",
    database="autoskola"
)

mycursor = db.cursor()

# mycursor.execute("CREATE database autoskola")
# mycursor.execute("CREATE TABLE Questions (question VARCHAR(400), image_address VARCHAR(300), correct_answer VARCHAR(300), questionID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("ALTER TABLE Questions CHANGE pitanje question VARCHAR(400)")

# mycursor.execute("INSERT INTO Questions (question, image_address, correct_answer) VALUES(%s, %s, %s)", ("Ovo je pitanje", "Ovo je adresa slika", "Ovo je tacan odgovor"))
# mycursor.execute("DELETE FROM Questions WHERE questionID = 2")
# db.commit()
# mycursor.execute("SELECT * FROM Questions")

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

# mycursor.execute("DESCRIBE Questions")
# for x in mycursor:
# 	print(x)