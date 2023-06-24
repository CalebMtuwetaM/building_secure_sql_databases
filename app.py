# import the nessecary modules requiered
import sqlite3

# create the database table
conn = sqlite3.connect("people.db")


# setup the data in the database

cursor = conn.cursor()

# this is to avoid an error since the table is formed every time you run the program and this would bring a problem as the table already exists

cursor.execute("""DROP TABLE IF EXISTS people;""")

cursor.execute("""CREATE TABLE people (
    name VARCHAR(255) NOT NULL,
    job VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    age INT,
    gender CHAR(1));""")

# now lets put some sample data into the database

cursor.execute("""INSERT INTO people (name,job,password,age,gender) VALUES 
('Michael','cooker','mypass123','40','m'),
('Caleb','pooter','mypassword','45','m'),
('hope','presenter','password123','40','f');""")

# lets now commit the sample data
conn.commit()

# now i would like us to make a sort of a login interface where the user will input his or her name and based on his name he will be able to retrieve
#their information

name_input = input("Whats your name: ")

cursor.execute("SELECT * FROM people where name = ?",(name_input,))
rows = cursor.fetchall()

if len(rows) == 0:
    print("Name not found in the database.")
else:
    pass_input = input("Whats your password: ")

    cursor.execute(f"SELECT * FROM people WHERE name = ? AND password = ?", (name_input, pass_input))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("login Failed! ")
    else:
        print(f"Success! Here is the information of {name_input}")
        for row in rows:
            print(row)


