import socket
import csv

praktijk = []
f = open('vektis_agb_praktijk.csv', 'r', encoding = 'UTF-8')
csvreader = csv.reader(f)

def zoekpraktijk(lst):
    for item in lst:
        if '01' in item:
            praktijk.append(item)
            
zoekpraktijk(csvreader)
f.close()

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

zoekhuisarts(PraktijkAdrescsv)

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

'''Maak een tabel aan in de database genaamd Praktijken en voeg de 
naam, het telefoonnummer en het adres toe.'''
import sqlite3

db = sqlite3.connect('specialismen_db.sqlite')

#tabel voor Huisartsen aanmaken
cursor = db.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS Praktijken(id INT PRIMARY KEY, naam TEXT, telnr TEXT, straat TEXT, huisnummer INT, toevoeging TEXT, postcode TEXT, woonplaats TEXT, lat REAL, long REAL, website TEXT)
''')

#data uit haData en adresCor inlezen in tabel Huisartsen
for lst in prSort:
   cursor.execute('''INSERT INTO Praktijken(id, naam, telnr, straat, huisnummer, toevoeging, postcode, woonplaats)
                VALUES(?,?,?,?,?,?,?,?)''', (lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7]))

#wijzigingen opslaan en connectie met db verbreken
db.commit()
cursor.close()

'''Maak lijsten aan om adresgegevens op te slaan en verzamel 
ze in 1 lijst. Met deze lijst kunnen de coordinaten van de praktijken
gezocht worden.'''
prakStraat = []
prakNummer = []
prakToevoeging = []
prakPostcode =[]
prakWoonplaats = []
prAdres=[]

def adresVerzamelaar(lst):
    for x in lst:
         prakStraat.append(x[5])
         prakNummer.append(x[6]) 
         prakToevoeging.append(x[7])
         prakPostcode.append(x[8])
         prakWoonplaats.append(x[9])     
                
adresVerzamelaar(prakAdres)

def lijstmaker(lijst1,lijst2,lijst3,lijst4):
    for i in lijst1,lijst2,lijst3,lijst4:
        for item in i:
            prAdres.append(item)

lijstmaker(prakStraat,prakNummer,prakPostcode,prakWoonplaats)

'''Sorteer de lijst zodat een volledig adres per huisarts als list wordt opgeslagen.'''
prakAdressort = []
def adresSort(lijstje):
    for i in range(len(prakAdres)):
        prakAdressort.append(lijstje[i:len(lijstje)+i:len(prakAdres)]) 
      
adresSort(prAdres)

'''Zoek met behulp van de net gemaakte adreslijst (prakAdressort)
de bijbehorende coordinaten.'''
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
             
adresGeo(prakAdressort[0:len(prakAdressort)])

'''Voeg de nummers van de praktijken aan de coordinaten toe, 
zodat deze gekoppeld kunnen worden aan de juiste praktijken'''
praktijkNamenCoordinaten = []
def prakEnCor(lst1, lst2):
    for item in lst1:
        praktijkNamenCoordinaten.append(item[3])
    for item in lst2:
        praktijkNamenCoordinaten.append(item[0])
    for item in lst2:
        praktijkNamenCoordinaten.append(item[1])

prakEnCor(prakAdres, adresCor)

gesorteerdNummerEnCoordinaten = []
def corSort(lijstje):
    for i in range(len(prakAdres)):
        gesorteerdNummerEnCoordinaten.append(lijstje[i:len(lijstje)+i:len(prakAdres)])
        
corSort(praktijkNamenCoordinaten)

'''Voeg de coordinaten toe aan de praktijken in de database.'''
import sqlite3

db = sqlite3.connect('specialismen_db.sqlite')

#tabel voor Huisartsen aanmaken
cursor = db.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS Praktijken(id INT PRIMARY KEY, naam TEXT, telnr TEXT, straat TEXT, huisnummer INT, toevoeging TEXT, postcode TEXT, woonplaats TEXT, lat REAL, long REAL, website TEXT)
''')

for lst in gesorteerdNummerEnCoordinaten:
    if lst[1] != 'o' and lst [2] != 'n':
        sql = "update Praktijken set lat = %f, long = %f where id = %d" % (lst[1], lst[2], lst[0])
        cursor.execute(sql)

#wijzigingen opslaan en connectie met db verbreken
db.commit()
cursor.close()
