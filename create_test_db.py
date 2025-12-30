# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
c.execute("INSERT INTO users (name) VALUES ('Alice')")
c.execute("INSERT INTO users (name) VALUES ('Bob')")
conn.commit()
conn.close()
print("Created test.db")

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
