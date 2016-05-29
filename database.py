#database stuf
import sqlite3

sqlite_file = 'specialismen_db.sqlite'    # name of the sqlite database file
tabel_ha = 'Huisartsen'	# name of the table to be created
ID_kolom = 'ID' # name of the column
field_type = 'TEXT'  # column data type
# Connecting to the database file

conn = sqlite3.connect(specialismen_db.sqlite)
c = conn.cursor()

for row in ha_data:
    c.execute("INSERT INTO Huisartsen VALUES (row[3], row[4], row[5], row[6], row[14])")

for row in c.execute('SELECT * FROM Huisartsen'):
        print(row)
# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
