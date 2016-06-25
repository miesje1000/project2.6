import socket
class adresPraktijkzoeker:
   def __init__(self,haData):
       self.haData = haData
#filtreer de huisartsen uit het bestand 

prakData = []

''' Haalt uit de totale Vektis dataset alle huisartsen. 
Voor huisartsen is de code 01. Makkelijk te vervangen voor nummers van andere soorten
hulpverleners. Wel alle apostroffen in csv bestand weggehaald, geeft 
duidelijkere output.'''
def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'): 
            prakData.append(col)

zoekhuisarts(PraktijkAdrescsv)
        
'''Maak lijsten aan om adresgegevens op te slaan en verzamel ze in 1 lijst'''
prakStraat = []
prakNummer = []
prakToevoeging = []
prakPostcode =[]
prakWoonplaats = []
prakAdres=[]

def adresVerzamelaar(lst):
    for x in lst:
         prakStraat.append(x[5])
         prakNummer.append(x[6]) 
         prakToevoeging.append(x[7])
         prakPostcode.append(x[8])
         prakWoonplaats.append(x[9])     
                
adresVerzamelaar(prakData)

def lijstmaker(lijst1,lijst2,lijst3,lijst4):
    for i in lijst1,lijst2,lijst3,lijst4:
        for item in i:
            prakAdres.append(item)

lijstmaker(prakStraat,prakNummer,prakPostcode,prakWoonplaats)

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
adresGeo(prakAdressort[0:len(prakAdressort)])

praktijkNamenCoordinaten = []
def prakEnCor(lst1, lst2):
    for item in lst1:
        praktijkNamenCoordinaten.append(item)
    for item in lst2:
        praktijkNamenCoordinaten.append(item[0])
    for item in lst2:
        praktijkNamenCoordinaten.append(item[1])

prakEnCor(prakAdressort, adresCor)

gesorteerdeNamenEnCoordinaten = []
def corSort(lijstje):
    for i in range(len(prakData)):
        gesorteerdeNamenEnCoordinaten.append(lijstje[i:len(lijstje)+i:len(prakData)])
        
corSort(praktijkNamenCoordinaten)