import sqlite3
con = sqlite3.connect("practice.db")
cur = con.cursor()

sql = """
select holder,city,premium,rank() over (partition by city order by premium desc) as city_avg from policies

"""

for row in cur.execute(sql):
    print(row)

con.close()
