'''Laadt eerst het bestand praktijkcsv in. Daarna kun je 
een lijst met naam, telefoonnummer en adres maken.'''
praktijk = []
def zoekpraktijk(lst):
    for col in lst:
        if col[2] == int('01'):
            praktijk.append(col)

zoekpraktijk(praktijkcsv)

prNr = []
prNa1 = []
prNa2 = []
prTel = []

for item in praktijk:
    prNr.append(item[3])
    prNa1.append(item[4])
    prNa2.append(item[5])
    prTel.append(item[6])

pr = []
def prSamenvoegen(lst1, lst2, lst3, lst4):
    for item in lst1:
        pr.append(item)
    for item in lst2:
        pr.append(item)
    for item in lst3:
        pr.append(item)
    for item in lst4:
        pr.append(item)
        
prSamenvoegen(prNr, prNa1, prNa2, prTel)

prSort = []
def praktijkSort(lst):
    for i in range(len(praktijk)):
        prSort.append(lst[i:len(pr)+i:len(praktijk)])
        
praktijkSort(pr)

for item in prSort:
    if item[2] != '(null)':
        item[1] = item[1] + ' ' + item[2]
    item.remove(item[2])
    
'''Lees het bestand met praktijk adressen in.'''

prakAdres = []

def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'): 
            prakAdres.append(col)

zoekhuisarts(praktijkadrescsv)

'''Voeg het adres toe door middel van het nummer van de praktijk.''' 
def koppeling(lst1, lst2):
    for item in lst1:
        for ding in lst2:
            if item[0] == ding[3]:
                item.append(ding[5])
                item.append(ding[6])
                item.append(ding[7])
                item.append(ding[8])
                item.append(ding[9])
        

koppeling(prSort, prakAdres)

'''Sorteer de lijst zodat een volledig adres per huisarts als list wordt opgeslagen.'''
prakAdressort = []
def adresSort(lijstje):
    for i in range(len(prakData)):
        prakAdressort.append(lijstje[i:len(lijstje)+i:len(prakData)]) 
      
adresSort(prakAdres)

adresCor = []
def adresGeo(lst):
    from time import sleep
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(500)
    for item in lst:
         location = geolocator.geocode(item, timeout=500)
         if location:
             locatieCor = [location.latitude, location.longitude]
             adresCor.append(locatieCor)
             sleep(1)
         else:
             adresCor.append("onbekend")
             sleep(1)
             
'''Method die de adresGeo method gebruikt om de coördinaten van alle adressen 
te vinden'''
adresGeo(prakAdressort[0:len(prakAdressort)])praktijkNamenCoordinaten = []
def prakEnCor(lst1, lst2):
    for item in lst1:
        praktijkNamenCoordinaten.append(item[1])
    for item in lst2:
        praktijkNamenCoordinaten.append(item[0])
    for item in lst2:
        praktijkNamenCoordinaten.append(item[1])

prakEnCor(prSort, adresCor)

'''Het ophalen van de coordinaten en naam toevoegen.'''
gesorteerdeNamenEnCoordinaten = []
def corSort(lijstje):
    for i in range(len(praktijk)):
        gesorteerdeNamenEnCoordinaten.append(lijstje[i:len(lijstje)+i:len(praktijk)])
        
corSort(praktijkNamenCoordinaten)

'''Database'''
import sqlite3

db = sqlite3.connect('specialismen_db.sqlite')

#tabel voor Huisartsen aanmaken
cursor = db.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS Praktijken1(naam TEXT, telnr TEXT, straat TEXT, huisnummer INT, toevoeging TEXT, postcode TEXT, woonplaats TEXT, lat REAL, long REAL, website TEXT)
''')

#data uit haData en adresCor inlezen in tabel Huisartsen
for lst in prSort:
   cursor.execute('''INSERT INTO Praktijken1(naam, telnr, straat, huisnummer, toevoeging, postcode, woonplaats)
                VALUES(?,?,?,?,?,?,?)''', (lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7]))

for lst in gesorteerdeNamenEnCoordinaten:
    if lst[1] != 'o' and lst [2] != 'n':
        sql = "update Praktijken1 set lat = %f, long = %f where naam = %s" % (lst[1], lst[2], lst[0])
        cursor.execute(sql)

#wijzigingen opslaan en connectie met db verbreken
db.commit()
cursor.close()




