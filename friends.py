import sqlite3

connection = sqlite3.connect('my_friends.db')
cursor = connection.cursor()
# cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)")

friends = [
    ("Hannah",'Clemmons', 23),
    ('Derek','Smith', 23),
    ('Morgan','Schmit', 23)
]

# insert_query = '''INSERT INTO friends VALUES ('Hannah', 'Clemmons', 23)'''

for friend in friends:
    cursor.execute("INSERT INTO friends VALUES (?,?,?)", friend)
    print("INSERTED!")

connection.commit()
connection.close()