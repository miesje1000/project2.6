''' Importeer handmatig de bestanden waarin de zorgverleners staan, 
de praktijken en de koppeling tussen deze twee.'''

'''Importeer de huisartsen uit het bestand met zorgverleners
en maak van voorletters, tussenvoegsel(s) en achternaam één list.'''
haData = []
def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'):
            haData.append(col)

zoekhuisarts(tabelcsv)

for item in haData:
    if item[6] != '(null)':
        item[4] = item[5] + ' ' + item[6] + ' ' + item[4]
        item.remove(item[5])
        item.remove(item[6])
    else:
        item[4] = item[5] + ' ' + item[4]
        item.remove(item[5])
        item.remove(item[6])

'''Importeer de huisartspraktijken uit het bestand met praktijken,
gebruik het nummer, naam deel één en naam deel twee. Maak van de twee
naam delen één list.''' 
praktijk = []
def zoekpraktijk(lst):
    for col in lst:
        if col[2] == int('01'):
            praktijk.append(col)

zoekpraktijk(praktijkcsv)

prNr = []
prNa1 = []
prNa2 = []

for item in praktijk:
    prNr.append(item[3])
    prNa1.append(item[4])
    prNa2.append(item[5])

pr = []
def prSamenvoegen(lst1, lst2, lst3):
    for item in lst1:
        pr.append(item)
    for item in lst2:
        pr.append(item)
    for item in lst3:
        pr.append(item)
        
prSamenvoegen(prNr, prNa1, prNa2)

prSort = []
def praktijkSort(lst):
    for i in range(5429):
        prSort.append(lst[i:16287+i:5429])
        
praktijkSort(pr)

for item in prSort:
    if item[2] != '(null)':
        item[1] = item[1] + ' ' + item[2]
    item.remove(item[2])

'''Zoek de huisartsen uit het bestand met koppelingen.
Maak een lijst met de huisartsen en bijbehorende praktijk(en).'''
koppel = []
def zoekkoppel(lst):
    for col in lst:
        if col[2] == int('01'):
            koppel.append(col)

zoekkoppel(koppelcsv)

kopHa = []
kopPr = []

for item in koppel:
    kopHa.append(item[3])
    kopPr.append(item[4])
    
kopHaPr = []
def haEnPr(lst1, lst2):
    for item in lst1:
        kopHaPr.append(item)
    for item in lst2:
        kopHaPr.append(item)
        
haEnPr(kopHa, kopPr)

koppelSort = []
def kopSort(lst):
    for i in range(12228):
        koppelSort.append(lst[i:24456+i:12228])
        
kopSort(kopHaPr)

'''Vervang in de lijst met koppelingen de nummers van de huisartsen en
praktijken door de namen van de huisartsen en praktijken.'''
def koppeling(lst1, lst2, lst3):
    for item in lst1:
        for obj in lst3:
            if item[0] == obj[2]:
                item[0] = obj[3]
        for ding in lst2:
            if item[1] == ding[0]:
                item[1] = ding[1]
        

koppeling(koppelSort, prSort, haData)

'''Schrijf de gegenereerde data weg naar de specialismendatabase
in een tabel genaamd Huisartsen.'''
import sqlite3

db = sqlite3.connect('specialismen_db.sqlite')

cursor = db.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS Huisartsen(huisarts TEXT, praktijk TEXT)
''')

for lst in koppelSort:
   cursor.execute('''INSERT INTO Huisartsen(huisarts, praktijk)
                VALUES(?,?)''', (lst[0], lst[1]))

db.commit()
cursor.close()




            




            
