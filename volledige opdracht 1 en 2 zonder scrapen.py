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
             sleep(1)
         else:
             adresCor.append("onbekend")
             sleep(1)
             
#Gerund per 100 
adresGeo(haAdressort[0:21])
adresGeo(haAdressort[21:41])
adresGeo(haAdressort[41:61])
adresGeo(haAdressort[61:81])
adresGeo(haAdressort[81:101])
adresGeo(haAdressort[101:121])
adresGeo(haAdressort[121:141])
adresGeo(haAdressort[141:161])
adresGeo(haAdressort[161:181])
adresGeo(haAdressort[181:201])
adresGeo(haAdressort[201:221])
adresGeo(haAdressort[221:241])
adresGeo(haAdressort[241:261])
adresGeo(haAdressort[261:281])
adresGeo(haAdressort[281:301])
adresGeo(haAdressort[301:321])
adresGeo(haAdressort[321:341])
adresGeo(haAdressort[341:361])
adresGeo(haAdressort[361:381])
adresGeo(haAdressort[381:401])
adresGeo(haAdressort[401:421])
adresGeo(haAdressort[421:441])
adresGeo(haAdressort[441:461])
adresGeo(haAdressort[461:481])
adresGeo(haAdressort[481:501])
adresGeo(haAdressort[501:521])
adresGeo(haAdressort[521:541])
adresGeo(haAdressort[541:561])
adresGeo(haAdressort[561:581])
adresGeo(haAdressort[581:601])
adresGeo(haAdressort[601:621])
adresGeo(haAdressort[621:641])
adresGeo(haAdressort[641:661])
adresGeo(haAdressort[661:681])
adresGeo(haAdressort[681:701])
adresGeo(haAdressort[701:721])
adresGeo(haAdressort[721:741])
adresGeo(haAdressort[741:761])
adresGeo(haAdressort[761:781])
adresGeo(haAdressort[781:801])
adresGeo(haAdressort[801:821])
adresGeo(haAdressort[821:841])
adresGeo(haAdressort[841:861])
adresGeo(haAdressort[861:881])
adresGeo(haAdressort[881:901])
adresGeo(haAdressort[901:921])
adresGeo(haAdressort[921:941])
adresGeo(haAdressort[941:961])
adresGeo(haAdressort[961:981])
adresGeo(haAdressort[981:1001])
adresGeo(haAdressort[1001:1021])
adresGeo(haAdressort[1021:1041])
adresGeo(haAdressort[1041:1061])
adresGeo(haAdressort[1061:1081])
adresGeo(haAdressort[1081:1101])
adresGeo(haAdressort[1101:1121])
adresGeo(haAdressort[1121:1141])
adresGeo(haAdressort[1141:1161])
adresGeo(haAdressort[1161:1181])
adresGeo(haAdressort[1181:1201])
adresGeo(haAdressort[1201:1221])
adresGeo(haAdressort[1221:1241])
adresGeo(haAdressort[1241:1261])
adresGeo(haAdressort[1261:1281])
adresGeo(haAdressort[1281:1301])
adresGeo(haAdressort[1301:1321])
adresGeo(haAdressort[1321:1341])
adresGeo(haAdressort[1341:1361])
adresGeo(haAdressort[1361:1381])
adresGeo(haAdressort[1381:1401])
adresGeo(haAdressort[1401:1421])
adresGeo(haAdressort[1421:1441])
adresGeo(haAdressort[1441:1461])
adresGeo(haAdressort[1461:1481])
adresGeo(haAdressort[1481:1501])
adresGeo(haAdressort[1501:1521])
adresGeo(haAdressort[1521:1541])
adresGeo(haAdressort[1541:1561])
adresGeo(haAdressort[1561:1581])
adresGeo(haAdressort[1581:1601])
adresGeo(haAdressort[1601:1621])
adresGeo(haAdressort[1621:1641])
adresGeo(haAdressort[1641:1661])
adresGeo(haAdressort[1661:1681])
adresGeo(haAdressort[1681:1701])
adresGeo(haAdressort[1701:1721])
adresGeo(haAdressort[1721:1741])
adresGeo(haAdressort[1741:1761])
adresGeo(haAdressort[1761:1781])
adresGeo(haAdressort[1781:1801])
adresGeo(haAdressort[1801:1821])
adresGeo(haAdressort[1821:1841])
adresGeo(haAdressort[1841:1861])
adresGeo(haAdressort[1861:1881])
adresGeo(haAdressort[1881:1901])
adresGeo(haAdressort[1901:1921])
adresGeo(haAdressort[1921:1941])
adresGeo(haAdressort[1941:1961])
adresGeo(haAdressort[1961:1981])
adresGeo(haAdressort[1981:2001])
adresGeo(haAdressort[2001:2021])
adresGeo(haAdressort[2021:2041])
adresGeo(haAdressort[2041:2061])
adresGeo(haAdressort[2061:2081])
adresGeo(haAdressort[2081:2101])
adresGeo(haAdressort[2101:2121])
adresGeo(haAdressort[2121:2141])
adresGeo(haAdressort[2141:2161])
adresGeo(haAdressort[2161:2181])
adresGeo(haAdressort[2181:2201])
adresGeo(haAdressort[2201:2221])
adresGeo(haAdressort[2221:2241])
adresGeo(haAdressort[2241:2261])
adresGeo(haAdressort[2261:2281])
adresGeo(haAdressort[2281:2301])
adresGeo(haAdressort[2301:2321])
adresGeo(haAdressort[2321:2341])
adresGeo(haAdressort[2341:2361])
adresGeo(haAdressort[2361:2381])
adresGeo(haAdressort[2381:2401])
adresGeo(haAdressort[2401:2421])
adresGeo(haAdressort[2421:2441])
adresGeo(haAdressort[2441:2461])
adresGeo(haAdressort[2461:2481])
adresGeo(haAdressort[2481:2501])
adresGeo(haAdressort[2501:2521])
adresGeo(haAdressort[2521:2541])
adresGeo(haAdressort[2541:2561])
adresGeo(haAdressort[2561:2581])
adresGeo(haAdressort[2581:2601])
adresGeo(haAdressort[2601:2621])
adresGeo(haAdressort[2621:2641])
adresGeo(haAdressort[2641:2661])
adresGeo(haAdressort[2661:2681])
adresGeo(haAdressort[2681:2701])
adresGeo(haAdressort[2701:2721])
adresGeo(haAdressort[2721:2741])
adresGeo(haAdressort[2741:2761])
adresGeo(haAdressort[2761:2781])
adresGeo(haAdressort[2781:2801])
adresGeo(haAdressort[2801:2821])
adresGeo(haAdressort[2821:2841])
adresGeo(haAdressort[2841:2861])
adresGeo(haAdressort[2861:2881])
adresGeo(haAdressort[2881:2901])
adresGeo(haAdressort[2901:2921])
adresGeo(haAdressort[2921:2941])
adresGeo(haAdressort[2941:2961])
adresGeo(haAdressort[2961:2981])
adresGeo(haAdressort[2981:3001])
adresGeo(haAdressort[3001:3021])
adresGeo(haAdressort[3021:3041])
adresGeo(haAdressort[3041:3061])
adresGeo(haAdressort[3061:3081])
adresGeo(haAdressort[3081:3101])
adresGeo(haAdressort[3101:3121])
adresGeo(haAdressort[3121:3141])
adresGeo(haAdressort[3141:3161])
adresGeo(haAdressort[3161:3181])
adresGeo(haAdressort[3181:3201])
adresGeo(haAdressort[3201:3221])
adresGeo(haAdressort[3221:3241])
adresGeo(haAdressort[3241:3261])
adresGeo(haAdressort[3261:3281])
adresGeo(haAdressort[3281:3301])
adresGeo(haAdressort[3301:3321])
adresGeo(haAdressort[3321:3341])
adresGeo(haAdressort[3341:3361])
adresGeo(haAdressort[3361:3381])
adresGeo(haAdressort[3381:3401])
adresGeo(haAdressort[3401:3421])
adresGeo(haAdressort[3421:3441])
adresGeo(haAdressort[3441:3461])
adresGeo(haAdressort[3461:3481])
adresGeo(haAdressort[3481:3501])
adresGeo(haAdressort[3501:3521])
adresGeo(haAdressort[3521:3541])
adresGeo(haAdressort[3541:3561])
adresGeo(haAdressort[3561:3581])
adresGeo(haAdressort[3581:3601])
adresGeo(haAdressort[3601:3621])
adresGeo(haAdressort[3621:3641])
adresGeo(haAdressort[3641:3661])
adresGeo(haAdressort[3661:3681])
adresGeo(haAdressort[3681:3701])
adresGeo(haAdressort[3701:3721])
adresGeo(haAdressort[3721:3741])
adresGeo(haAdressort[3741:3761])
adresGeo(haAdressort[3761:3781])
adresGeo(haAdressort[3781:3801])
adresGeo(haAdressort[3801:3821])
adresGeo(haAdressort[3821:3841])
adresGeo(haAdressort[3841:3861])
adresGeo(haAdressort[3861:3881])
adresGeo(haAdressort[3881:3901])
adresGeo(haAdressort[3901:3921])
adresGeo(haAdressort[3921:3941])
adresGeo(haAdressort[3941:3961])
adresGeo(haAdressort[3961:3981])
adresGeo(haAdressort[3981:4001])
adresGeo(haAdressort[4001:4021])
adresGeo(haAdressort[4021:4041])
adresGeo(haAdressort[4041:4061])
adresGeo(haAdressort[4061:4081])
adresGeo(haAdressort[4081:4101])
adresGeo(haAdressort[4101:4121])
adresGeo(haAdressort[4121:4141])
adresGeo(haAdressort[4141:4161])
adresGeo(haAdressort[4161:4181])
adresGeo(haAdressort[4181:4201])
adresGeo(haAdressort[4201:4221])
adresGeo(haAdressort[4221:4241])
adresGeo(haAdressort[4241:4261])
adresGeo(haAdressort[4261:4281])
adresGeo(haAdressort[4281:4301])
adresGeo(haAdressort[4301:4321])
adresGeo(haAdressort[4321:4341])
adresGeo(haAdressort[4341:4361])
adresGeo(haAdressort[4361:4381])
adresGeo(haAdressort[4381:4401])
adresGeo(haAdressort[4401:4421])
adresGeo(haAdressort[4421:4441])
adresGeo(haAdressort[4441:4461])
adresGeo(haAdressort[4461:4481])
adresGeo(haAdressort[4481:4501])
adresGeo(haAdressort[4501:4521])
adresGeo(haAdressort[4521:4541])
adresGeo(haAdressort[4541:4561])
adresGeo(haAdressort[4561:4581])
adresGeo(haAdressort[4581:4601])
adresGeo(haAdressort[4601:4621])
adresGeo(haAdressort[4621:4641])
adresGeo(haAdressort[4641:4661])
adresGeo(haAdressort[4661:4681])
adresGeo(haAdressort[4681:4701])
adresGeo(haAdressort[4701:4721])
adresGeo(haAdressort[4721:4741])
adresGeo(haAdressort[4741:4761])
adresGeo(haAdressort[4761:4781])
adresGeo(haAdressort[4781:4801])
adresGeo(haAdressort[4801:4821])
adresGeo(haAdressort[4821:4841])
adresGeo(haAdressort[4841:4861])
adresGeo(haAdressort[4861:4881])
adresGeo(haAdressort[4881:4901])
adresGeo(haAdressort[4901:4921])
adresGeo(haAdressort[4921:4941])
adresGeo(haAdressort[4941:4961])
adresGeo(haAdressort[4961:4981])
adresGeo(haAdressort[4981:5001])
adresGeo(haAdressort[5001:5021])
adresGeo(haAdressort[5021:5041])
adresGeo(haAdressort[5041:5061])
adresGeo(haAdressort[5061:5081])
adresGeo(haAdressort[5081:5101])
adresGeo(haAdressort[5101:5121])
adresGeo(haAdressort[5121:5141])
adresGeo(haAdressort[5141:5161])
adresGeo(haAdressort[5161:5181])
adresGeo(haAdressort[5181:5201])
adresGeo(haAdressort[5201:5221])
adresGeo(haAdressort[5221:5241])
adresGeo(haAdressort[5241:5261])
adresGeo(haAdressort[5261:5281])
adresGeo(haAdressort[5281:5301])
adresGeo(haAdressort[5301:5321])
adresGeo(haAdressort[5321:5341])
adresGeo(haAdressort[5341:5361])
adresGeo(haAdressort[5361:5381])
adresGeo(haAdressort[5381:5401])
adresGeo(haAdressort[5401:5421])
adresGeo(haAdressort[5421:5441])
adresGeo(haAdressort[5441:5461])
adresGeo(haAdressort[5461:5481])
adresGeo(haAdressort[5481:5501])
adresGeo(haAdressort[5501:5521])
adresGeo(haAdressort[5521:5541])
adresGeo(haAdressort[5541:5561])
adresGeo(haAdressort[5561:5581])
adresGeo(haAdressort[5581:5601])
adresGeo(haAdressort[5601:5621])
adresGeo(haAdressort[5621:5641])
adresGeo(haAdressort[5641:5661])
adresGeo(haAdressort[5661:5681])
adresGeo(haAdressort[5681:5701])
adresGeo(haAdressort[5701:5721])
adresGeo(haAdressort[5721:5741])
adresGeo(haAdressort[5741:5761])
adresGeo(haAdressort[5761:5781])
adresGeo(haAdressort[5781:5801])
adresGeo(haAdressort[5801:5821])
adresGeo(haAdressort[5821:5841])
adresGeo(haAdressort[5841:5861])
adresGeo(haAdressort[5861:5881])
adresGeo(haAdressort[5881:5901])
adresGeo(haAdressort[5901:5921])
adresGeo(haAdressort[5921:5941])
adresGeo(haAdressort[5941:5961])
adresGeo(haAdressort[5961:5981])
adresGeo(haAdressort[5981:6001])
adresGeo(haAdressort[6001:6021])
adresGeo(haAdressort[6021:6041])
adresGeo(haAdressort[6041:6061])
adresGeo(haAdressort[6061:6081])
adresGeo(haAdressort[6081:6101])
adresGeo(haAdressort[6101:6121])
adresGeo(haAdressort[6121:6141])
adresGeo(haAdressort[6141:6161])
adresGeo(haAdressort[6161:6181])
adresGeo(haAdressort[6181:6201])
adresGeo(haAdressort[6201:6221])
adresGeo(haAdressort[6221:6241])
adresGeo(haAdressort[6241:6261])
adresGeo(haAdressort[6261:6281])
adresGeo(haAdressort[6281:6301])
adresGeo(haAdressort[6301:6321])
adresGeo(haAdressort[6321:6341])
adresGeo(haAdressort[6341:6361])
adresGeo(haAdressort[6361:6381])
adresGeo(haAdressort[6381:6401])
adresGeo(haAdressort[6401:6421])
adresGeo(haAdressort[6421:6441])
adresGeo(haAdressort[6441:6461])
adresGeo(haAdressort[6461:6481])
adresGeo(haAdressort[6481:6501])
adresGeo(haAdressort[6501:6521])
adresGeo(haAdressort[6521:6541])
adresGeo(haAdressort[6541:6561])
adresGeo(haAdressort[6561:6581])
adresGeo(haAdressort[6581:6601])
adresGeo(haAdressort[6601:6621])
adresGeo(haAdressort[6621:6641])
adresGeo(haAdressort[6641:6661])
adresGeo(haAdressort[6661:6681])
adresGeo(haAdressort[6681:6701])
adresGeo(haAdressort[6701:6721])
adresGeo(haAdressort[6721:6741])
adresGeo(haAdressort[6741:6761])
adresGeo(haAdressort[6761:6781])
adresGeo(haAdressort[6781:6801])
adresGeo(haAdressort[6801:6821])
adresGeo(haAdressort[6821:6841])
adresGeo(haAdressort[6841:6861])
adresGeo(haAdressort[6861:6881])
adresGeo(haAdressort[6881:6901])
adresGeo(haAdressort[6901:6921])
adresGeo(haAdressort[6921:6941])
adresGeo(haAdressort[6941:6961])
adresGeo(haAdressort[6961:6981])
adresGeo(haAdressort[6981:7001])
adresGeo(haAdressort[7001:7021])
adresGeo(haAdressort[7021:7041])
adresGeo(haAdressort[7041:7061])
adresGeo(haAdressort[7061:7081])
adresGeo(haAdressort[7081:7101])
adresGeo(haAdressort[7101:7121])
adresGeo(haAdressort[7121:7141])
adresGeo(haAdressort[7141:7161])
adresGeo(haAdressort[7161:7181])
adresGeo(haAdressort[7181:7201])
adresGeo(haAdressort[7201:7221])
adresGeo(haAdressort[7221:7241])
adresGeo(haAdressort[7241:7261])
adresGeo(haAdressort[7261:7281])
adresGeo(haAdressort[7281:7301])
adresGeo(haAdressort[7301:7321])
adresGeo(haAdressort[7321:7341])
adresGeo(haAdressort[7341:7361])
adresGeo(haAdressort[7361:7381])
adresGeo(haAdressort[7381:7401])
adresGeo(haAdressort[7401:7421])
adresGeo(haAdressort[7421:7441])
adresGeo(haAdressort[7441:7461])
adresGeo(haAdressort[7461:7481])
adresGeo(haAdressort[7481:7501])
adresGeo(haAdressort[7501:7521])
adresGeo(haAdressort[7521:7541])
adresGeo(haAdressort[7541:7561])
adresGeo(haAdressort[7561:7581])
adresGeo(haAdressort[7581:7601])
adresGeo(haAdressort[7601:7621])
adresGeo(haAdressort[7621:7641])
adresGeo(haAdressort[7641:7661])
adresGeo(haAdressort[7661:7681])
adresGeo(haAdressort[7681:7701])
adresGeo(haAdressort[7701:7721])
adresGeo(haAdressort[7721:7741])
adresGeo(haAdressort[7741:7761])
adresGeo(haAdressort[7761:7781])
adresGeo(haAdressort[7781:7801])
adresGeo(haAdressort[7801:7821])
adresGeo(haAdressort[7821:7841])
adresGeo(haAdressort[7841:7861])
adresGeo(haAdressort[7861:7881])
adresGeo(haAdressort[7881:7901])
adresGeo(haAdressort[7901:7921])
adresGeo(haAdressort[7921:7941])
adresGeo(haAdressort[7941:7961])
adresGeo(haAdressort[7961:7981])
adresGeo(haAdressort[7981:8001])
adresGeo(haAdressort[8001:8021])
adresGeo(haAdressort[8021:8041])
adresGeo(haAdressort[8041:8061])
adresGeo(haAdressort[8061:8081])
adresGeo(haAdressort[8081:8101])
adresGeo(haAdressort[8101:8121])
adresGeo(haAdressort[8121:8141])
adresGeo(haAdressort[8141:8161])
adresGeo(haAdressort[8161:8181])
adresGeo(haAdressort[8181:8201])
adresGeo(haAdressort[8201:8221])
adresGeo(haAdressort[8221:8241])
adresGeo(haAdressort[8241:8261])
adresGeo(haAdressort[8261:8281])
adresGeo(haAdressort[8281:8301])
adresGeo(haAdressort[8301:8321])
adresGeo(haAdressort[8321:8341])
adresGeo(haAdressort[8341:8361])
adresGeo(haAdressort[8361:8381])
adresGeo(haAdressort[8381:8401])
adresGeo(haAdressort[8401:8421])
adresGeo(haAdressort[8421:8441])
adresGeo(haAdressort[8441:8461])
adresGeo(haAdressort[8461:8481])
adresGeo(haAdressort[8481:8501])
adresGeo(haAdressort[8501:8521])
adresGeo(haAdressort[8521:8541])
adresGeo(haAdressort[8541:8561])
adresGeo(haAdressort[8561:8581])
adresGeo(haAdressort[8581:8601])
adresGeo(haAdressort[8601:8621])
adresGeo(haAdressort[8621:8641])
adresGeo(haAdressort[8641:8661])
adresGeo(haAdressort[8661:8681])
adresGeo(haAdressort[8681:8701])
adresGeo(haAdressort[8701:8721])
adresGeo(haAdressort[8721:8741])
adresGeo(haAdressort[8741:8761])
adresGeo(haAdressort[8761:8781])
adresGeo(haAdressort[8781:8801])
adresGeo(haAdressort[8801:8821])
adresGeo(haAdressort[8821:8841])
adresGeo(haAdressort[8841:8861])
adresGeo(haAdressort[8861:8881])
adresGeo(haAdressort[8881:8901])
adresGeo(haAdressort[8901:8921])
adresGeo(haAdressort[8921:8941])
adresGeo(haAdressort[8941:8961])
adresGeo(haAdressort[8961:8981])
adresGeo(haAdressort[8981:9001])
adresGeo(haAdressort[9001:9021])
adresGeo(haAdressort[9021:9041])
adresGeo(haAdressort[9041:9061])
adresGeo(haAdressort[9061:9081])
adresGeo(haAdressort[9081:9101])
adresGeo(haAdressort[9101:9121])
adresGeo(haAdressort[9121:9141])
adresGeo(haAdressort[9141:9161])
adresGeo(haAdressort[9161:9181])
adresGeo(haAdressort[9181:9201])
adresGeo(haAdressort[9201:9221])
adresGeo(haAdressort[9221:9241])
adresGeo(haAdressort[9241:9261])
adresGeo(haAdressort[9261:9281])
adresGeo(haAdressort[9281:9301])
adresGeo(haAdressort[9301:9321])
adresGeo(haAdressort[9321:9341])
adresGeo(haAdressort[9341:9361])
adresGeo(haAdressort[9361:9381])
adresGeo(haAdressort[9381:9401])
adresGeo(haAdressort[9401:9421])
adresGeo(haAdressort[9421:9441])
adresGeo(haAdressort[9441:9461])
adresGeo(haAdressort[9461:9481])
adresGeo(haAdressort[9481:9501])
adresGeo(haAdressort[9501:9521])
adresGeo(haAdressort[9521:9541])
adresGeo(haAdressort[9541:9561])
adresGeo(haAdressort[9561:9581])
adresGeo(haAdressort[9581:9601])
adresGeo(haAdressort[9601:9621])
adresGeo(haAdressort[9621:9641])
adresGeo(haAdressort[9641:9661])
adresGeo(haAdressort[9661:9681])
adresGeo(haAdressort[9681:9701])
adresGeo(haAdressort[9701:9721])
adresGeo(haAdressort[9721:9741])
adresGeo(haAdressort[9741:9761])
adresGeo(haAdressort[9761:9781])
adresGeo(haAdressort[9781:9801])
adresGeo(haAdressort[9801:9821])
adresGeo(haAdressort[9821:9841])
adresGeo(haAdressort[9841:9861])
adresGeo(haAdressort[9861:9881])
adresGeo(haAdressort[9881:9901])
adresGeo(haAdressort[9901:9921])
adresGeo(haAdressort[9921:9941])
adresGeo(haAdressort[9941:9961])
adresGeo(haAdressort[9961:9981])
adresGeo(haAdressort[9981:10001])
adresGeo(haAdressort[10001:10021])
adresGeo(haAdressort[10021:10041])
adresGeo(haAdressort[10041:10061])
adresGeo(haAdressort[10061:10081])
adresGeo(haAdressort[10081:10101])
adresGeo(haAdressort[10101:10121])
adresGeo(haAdressort[10121:10141])
adresGeo(haAdressort[10141:10161])
adresGeo(haAdressort[10161:10181])
adresGeo(haAdressort[10181:10201])
adresGeo(haAdressort[10201:10221])
adresGeo(haAdressort[10221:10241])
adresGeo(haAdressort[10241:10261])
adresGeo(haAdressort[10261:10281])
adresGeo(haAdressort[10281:10301])
adresGeo(haAdressort[10301:10321])
adresGeo(haAdressort[10321:10341])
adresGeo(haAdressort[10341:10361])
adresGeo(haAdressort[10361:10381])
adresGeo(haAdressort[10381:10401])
adresGeo(haAdressort[10401:10421])
adresGeo(haAdressort[10421:10441])
adresGeo(haAdressort[10441:10461])
adresGeo(haAdressort[10461:10481])
adresGeo(haAdressort[10481:10501])
adresGeo(haAdressort[10501:10521])
adresGeo(haAdressort[10521:10541])
adresGeo(haAdressort[10541:10561])
adresGeo(haAdressort[10561:10581])
adresGeo(haAdressort[10581:10601])
adresGeo(haAdressort[10601:10621])
adresGeo(haAdressort[10621:10641])
adresGeo(haAdressort[10641:10661])
adresGeo(haAdressort[10661:10681])
adresGeo(haAdressort[10681:10701])
adresGeo(haAdressort[10701:10721])
adresGeo(haAdressort[10721:10741])
adresGeo(haAdressort[10741:10761])
adresGeo(haAdressort[10761:10781])
adresGeo(haAdressort[10781:10801])
adresGeo(haAdressort[10801:10821])
adresGeo(haAdressort[10821:10841])
adresGeo(haAdressort[10841:10861])
adresGeo(haAdressort[10861:10881])
adresGeo(haAdressort[10881:10901])
adresGeo(haAdressort[10901:10921])
adresGeo(haAdressort[10921:10941])
adresGeo(haAdressort[10941:10961])
adresGeo(haAdressort[10961:10981])
adresGeo(haAdressort[10981:11001])
adresGeo(haAdressort[11001:11021])
adresGeo(haAdressort[11021:11041])
adresGeo(haAdressort[11041:11061])
adresGeo(haAdressort[11061:11081])
adresGeo(haAdressort[11081:11101])
adresGeo(haAdressort[11101:11121])
adresGeo(haAdressort[11121:11141])
adresGeo(haAdressort[11141:11161])
adresGeo(haAdressort[11161:11181])
adresGeo(haAdressort[11181:11201])
adresGeo(haAdressort[11201:11222])

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


