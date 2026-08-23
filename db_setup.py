import sqlite3

con = sqlite3.connect("practice.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS policies (
    policy_id INTEGER,
    holder TEXT,
    premium INTEGER
)
""")

cur.executemany(
    "INSERT INTO policies VALUES (?, ?, ?)",
    [(1, 'Ravi', 12000), (2, 'Meena', 8000), (3, 'Ali', 15000)]
)
con.commit()

for row in cur.execute("SELECT * FROM policies"):
    print(row)

con.close()