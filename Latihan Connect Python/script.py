db_host = "localhost"
db_name = "postgres"
db_user = "postgres"
db_pass = "postgres"

import psycopg2

conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
cur = conn.cursor()

cur. execute('''CREATE TABLE nilai 
    (NIM SERIAL PRIMARY KEY, 
    Nama VARCHAR,
    Prodi VARCHAR,
    Fakultas VARCHAR,
    Matakuliah VARCHAR, 
    SKS INT, 
    INDEX VARCHAR
    );
    ''')

cur.execute("INSERT INTO nilai (NIM,Name,Prodi,Fakultas,Matakuliah,SKS,Index) VALUES(%d,%s,%)", (120, "Christina", "Ilmu Komunikasi", "Fakultas Komunikasi Bisnis", "Pengantar Komunikasi", 4, "A"))

cur.execute("SELECT * FROM nilai;")
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()