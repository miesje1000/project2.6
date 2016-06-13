#importeer eerst handmatig het bestand met de data, op mijn computer tabelcsv

#filtreer de huisartsen uit het bestand 
haData = []
def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'):
            haData.append(col)

zoekhuisarts(tabelcsv)
        
#Maak lijsten aan om adresgegevens op te slaan en verzamel ze in 1 lijst
haStraat = []
haNummer = []
haPostcode =[]
haWoonplaats = []
haAdres=[]

def adresVerzamelaar(lst):
    for x in lst:
         haStraat.append(x[9])
         haNummer.append(x[10]) 
         haPostcode.append(x[12])
         haWoonplaats.append(x[13])
         
                
adresVerzamelaar(haData)

def lijstmaker(lijst1,lijst2,lijst3,lijst4):
    for i in lijst1,lijst2,lijst3,lijst4:
        for item in i:
            haAdres.append(item)

lijstmaker(haStraat,haNummer,haPostcode,haWoonplaats)

#Sorteer de lijst zodat een volledig adres als list wordt opgeslagen
haAdressort = []
def adresSort(lijstje):
    for i in range(11221):
        haAdressort.append(lijstje[i:len(lijstje)+i:11221]) 
      
adresSort(haAdres)

#Haal de coördinaten op van de adressen als ze bekend zijn
adresCor = []
def adresGeo(lst):
    from time import sleep
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    for item in lst:
         location = geolocator.geocode(item)
         if location:
             locatieCor = [location.latitude, location.longitude]
             adresCor.append(locatieCor)
             sleep(2)
         else:
             adresCor.append("onbekend")
             sleep(1)
             
adresGeo(haAdressort)

#Maak en sorteer een lijst met zowel id als coordinaten
haId = []
for x in haData:
    haId.append(x[3])
    
haIdtest = []
for x in test:
    haIdtest.append(x[3])

adresCorID = []
def idEnCor(lst1, lst2):
    for item in lst1:
        adresCorID.append(item)
    for item in lst2:
        adresCorID.append(item[0])
    for item in lst2:
        adresCorID.append(item[1])

idEnCor(haId, adresCor)

haCorsort = []
def corSort(lijstje):
    for i in range(11221):
        haCorsort.append(lijstje[i:len(lijstje)+i:11221])
        
corSort(adresCorID)

#database aanmaken of openen
import sqlite3

db = sqlite3.connect('specialismen_db.sqlite')

#tabel voor Huisartsen aanmaken
cursor = db.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS Huisartsen(id INTEGER PRIMARY KEY, achternaam TEXT,
                       voorletters TEXT, tussenvoegsel TEXT, telnr TEXT, lat REAL, long REAL)
''')

#data uit haData en adresCor inlezen in tabel Huisartsen
for lst in haData:
   cursor.execute('''INSERT INTO Huisartsen(id, achternaam, voorletters, tussenvoegsel, telnr)
                VALUES(?,?,?,?,?)''', (lst[3], lst[4], lst[5], lst[6], lst[14]))

for lst in haCorsort:
    if lst[1] != 'o' and lst [2] != 'n':
        sql = "update Huisartsen set lat = %f, long = %f where id = %d" % (lst[1], lst[2], lst[0])
        cursor.execute(sql)

#wijzigingen opslaan en connectie met db verbreken
db.commit()
cursor.close()


