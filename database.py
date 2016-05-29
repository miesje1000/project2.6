#database aanmaken of openen
import sqlite3

db = sqlite3.connect('specialismen_db.sqlite')

#tabel voor Huisartsen aanmaken
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Huisartsen(id INTEGER PRIMARY KEY, achternaam TEXT,
                       voorletters TEXT, tussenvoegsel TEXT, telnr TEXT)
''')

#data uit ha_data inlezen in tabel Huisartsen
for lst in ha_data:
    cursor.execute('''INSERT INTO Huisartsen(id, achternaam, voorletters, tussenvoegsel, telnr)
                  VALUES(?,?,?,?,?)''', (lst[3], lst[4], lst[5], lst[6], lst[14]))
cursor.execute('''INSERT INTO Huisartsen(id, achternaam, voorletters, tussenvoegsel, telnr)
                  VALUES(?,?,?,?,?)''', (ha2[3], ha2[4], ha2[5], ha2[6], ha2[14]))

for row in cursor.execute('SELECT * FROM Huisartsen'):
        print(row)
        
#LET OP: dit alleen runnen als je de tabel wilt verwijderen
cursor.execute('''DROP TABLE Huisartsen''')

db.commit()
