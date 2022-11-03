import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
c.execute (create_table)

insert_query = "INSERT INTO users VALUES (?, ?, ?)"


users = [
    (1, 'kris', 'admin'),
    (2, 'bob', 'asdf'),
    (3, 'jose', 'asdf')
]

c.executemany (insert_query, users)

select_query = "SELECT * FROM users"
for row in c.execute (select_query):
    print (row)

create_table = "CREATE TABLE items (name text, price real)"
c.execute (create_table)


conn.commit()
conn.close()
