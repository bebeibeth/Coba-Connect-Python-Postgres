db_host = "localhost"
db_name = "db_akademik"
db_user = "postgres"
db_pass = "postgres"

import psycopg2

conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
cur = conn.cursor()

# cur. execute = ('''
#     CREATE TABLE nilai(NIM VARCHAR(20)) PRIMARY KEY, 
#     Nama_mahasiswa VARCHAR(20) NOT NULL, 
#     Nama_prodi VARCHAR(20) NOT NULL, 
#     Nama_fakultas VARCHAR(20) NOT NULL, 
#     Nama_matakuliah VARCHAR (20) NOT NULL, 
#     SKS INT NOT NULL, 
#     Index_nilai INT NOT NULL
# ''')
# cur.execute('''
#     INSERT INTO nilai (Nama_mahasiswa) VALUES(%s), ("Mubeth")
# ''')
# cur.execute("INSERT INTO student (name) VALUES(%s)", ("Christina", ))

sql = "INSERT INTO nilai (nim, nama_mahasiswa, nama_prodi, nama_fakultas, nama_matakuliah, sks, index_nilai) VALUES (%s,%s,%s,%s,%s,%s,%s);"
val = ("12021901", "Christina", "Ilmu Komunikasi", "Fakultas Komunikasi", "Pengantar Komunikasi", 4, 10)
cur.execute (sql, val)

cur.execute("SELECT * FROM nilai;")
print(cur.fetchall())

# cur.execute("SELECT * FROM student WHERE id =%s;", (1, ))
# print(cur.fetchone())


conn.commit()

cur.close()
conn.close()