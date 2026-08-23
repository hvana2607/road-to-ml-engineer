import sqlite3

con = sqlite3.connect("practice.db")
cur = con.cursor()

sql = "SELECT holder, city, premium, RANK() OVER (PARTITION BY city ORDER BY premium DESC) FROM policies"

for row in cur.execute(sql):
    print(row)

con.close()