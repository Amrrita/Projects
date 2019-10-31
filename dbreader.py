import sqlite3
conn = sqlite3.connect('videos.db')

c = conn.cursor()

for row in c.execute('SELECT * FROM videos'):
    print(row)

conn.commit()
conn.close()