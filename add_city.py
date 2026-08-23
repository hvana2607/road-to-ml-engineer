import sqlite3

con = sqlite3.connect("practice.db")
cur = con.cursor()

cur.execute("ALTER TABLE policies ADD COLUMN city TEXT")

cur.execute("UPDATE policies SET city='Hyderabad' WHERE policy_id IN (1,3)")
cur.execute("UPDATE policies SET city='Mumbai' WHERE policy_id=2")
con.commit()

for row in cur.execute("SELECT * FROM policies"):
    print(row)

con.close()