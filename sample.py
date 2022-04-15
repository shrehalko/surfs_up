import sqlite3

# define connection and cursor. We need these to connect to our database
connection = sqlite3.connect('store_transactions1.sqlite')

#Create acursor to interact with our database through sql commands. This allows to create or modify the tables within our database.

cursor = connection.cursor()

#Create stores table
command1 = """CREATE TABLE IF NOT EXISTS 
STORES(STORES_ID INTEGER PRIMARY KEY, LOCATION TEXT)""" 

cursor.execute(command1)


#Create purchases table

command2 = """create table if not exists 
 purchases(purchase_id integer primary key, store_id integer, total_cost float, 
 foreign key (store_id) references stores(store_id))""" 

cursor.execute(command2)


cursor.execute("insert into stores values(01, 'austin')")
cursor.execute("insert into stores values(02, 'dallas')")
cursor.execute("insert into stores values(03, 'houston')")
cursor.execute("insert into stores values(04, 'round rock')")
cursor.execute("insert into stores values(05, 'plano')")

cursor.execute("insert into purchases values(10,01, 100)")
cursor.execute("insert into purchases values(20,02, 200)")
cursor.execute("insert into purchases values(30,03, 300)")
cursor.execute("insert into purchases values(40,04, 400)")
cursor.execute("insert into purchases values(50,05, 500)")

connection.commit()
connection.close()
# results = cursor.fetchall()
# print(results)