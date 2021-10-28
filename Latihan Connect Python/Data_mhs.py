db_host = "localhost"
db_name = "db_akademik"
db_user = "postgres"
db_pass = "postgres"

import psycopg2

conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
cur = conn.cursor()

cur.execute("SELECT * FROM nilai;")
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()