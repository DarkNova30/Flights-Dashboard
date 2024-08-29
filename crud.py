import mysql.connector

# connect to DataBase server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database = "indigo"
    )
    my_cursor = conn.cursor()
    print("connection established") # returns cursor object

except:
    print("connection error")

# creating a db on the db server
# my_cursor.execute("CREATE DATABASE indigo")
# conn.commit()         ## to commit a change in the server


# # creating an airport table:
# # airport_id | code | city | name |
#
# my_cursor.execute('''
#     CREATE TABLE airport (
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
#     )
# ''')
# conn.commit()   # commit when doing write operation


# # inserting data to table
# my_cursor.execute('''
#     INSERT INTO airport VALUES
#     (1,"DEL","New delhi","IGIA"),
#     (2,"CCU","kolkata","NSCA"),
#     (3,"BOM","bombay","CSMA")
# ''')
# conn.commit()

# SEARCH / RETRIEVE from table

my_cursor.execute('''
    SELECT * from airport WHERE airport_id > 1
''')
data = my_cursor.fetchall()   # fetches all rows returned --> Tuples
print(data)
for i in data:
    print(i[3])  # to get name of airport

# UPDATE
my_cursor.execute('''
    UPDATE airport 
    SET city = "mumbai" 
    WHERE airport_id = 3
''')
conn.commit()

data = my_cursor.fetchall()   # fetches all rows returned --> Tuples
print(data)
for i in data:
    print(i[2])