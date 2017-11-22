import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db",
    charset="utf8"
)

c = db.cursor()

c.execute("INSERT INTO banks (name, address) VALUES (%s, %s);", ('Название', 'адрес'))
db.commit()

c.execute("SELECT *FROM banks;")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()