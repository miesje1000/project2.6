class LatLonConverter:
   def __init__(self,haData,haAdres):
       self.haData = haData
       self.haAdres = haAdres

#Maak lijsten aan om adresgegevens op te slaan en verzamel ze in 1 lijst
haData = []
haStraat = []
haNummer = []
haPostcode =[]
haWoonplaats = []
haAdres=[]
def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'):
            haData.append(col)
        
zoekhuisarts(tabelcsv)

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
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    for item in lst:
         location = geolocator.geocode(item)
         if location:
             locatieCor = [location.latitude, location.longitude]
             adresCor.append(locatieCor)
         else:
             adresCor.append("onbekend")

adresGeo(haAdressort)
        
