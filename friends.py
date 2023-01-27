import sqlite3

connection = sqlite3.connect('my_friends.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)")

connection.commit()
connection.close()