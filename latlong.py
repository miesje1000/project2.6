#install geocoder
#import geocoder
class LatLonConverter:
   def __init__(self,haData,haAdres):
       self.haData = haData
       self.haAdres = haAdres
  
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
        
zoekhuisarts(Vektis2csv)

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
#print(haAdres[0],haAdres[11221],haAdres[22442],haAdres[33663])
#print(haAdres[0:len(haAdres):11221]) 
#print(haAdres[1:len(haAdres)+1:11221])
#print(haAdres)

def adresPrinter(lijstje):
    for i in range(11221):
        print(lijstje[i:len(lijstje)+i:11221]) 
        
adresPrinter(haAdres)

#Vanaf hieronder toegevoegd door Michelle
lijstmaker(haStraat,haNummer,haPostcode,haWoonplaats)
haAdressort = []
def adresSort(lijstje):
    for i in range(11221):
        haAdressort.append(lijstje[i:len(lijstje)+i:11221]) 
        
adresSort(haAdres)
adresCor = []
def adresGeo(lst):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    for item in lst:
        location = geolocator.geocode(item)
        locatieCor = [location.latitude, location.longitude]
        adresCor.append(locatieCor)
        
adresGeo(haAdressort)
print(haAdressort[1])

adresCor = []
mini = [haAdressort[0], haAdressort[1], haAdressort[2], haAdressort[3]]
def test(lst):
    for item in lst:
        from geopy.geocoders import Nominatim
        geolocator = Nominatim()
        location = geolocator.geocode(item)
        locatieCor = [location.latitude, location.longitude]
        adresCor.append(locatieCor)
    
test(mini)
        
