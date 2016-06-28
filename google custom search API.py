# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:44:56 2016

@author: Bart
"""

import urllib.request, urllib.response
import urllib
import json

def telefoonnummerBewerken(nummer):
    if len(nummer) > 5:
        if nummer[2] == '-':
            nieuwNummer = nummer[0:2] + nummer[3:]
            
        elif nummer[3] == '-':
            nieuwNummer = nummer[0:3] + nummer[4:]
            
        elif nummer[4] == '-':
            nieuwNummer = nummer[0:4] + nummer[5:]
        else:
            nieuwNummer = nummer
    else:
        nieuwNummer = nummer
    return nieuwNummer
         


def zoekHuisarts(nummer, naam):
    
    nummerAangepast = telefoonnummerBewerken(nummer)
    zoekTerm = nummerAangepast + ' ' + naam
    codeerdeTerm = urllib.parse.quote(zoekTerm, safe='') #de zoekterm wordt veranderd zodat google het kan lezen
    
    APIKey = 'AIzaSyCenzxlkgjkItijd8x0AseTh10hYor-L8I'
    APIKey1 = 'AIzaSyADcgIIfqR3_PbpUziTIQBxlKv7BDejkRA'
    cx = '004386439249891552984:kzfpgdjn5uy' #domein zoekmachine, ingesteld op independer.nl
    cx1 = '002435620736733317236:jwtmn7o6xas'
    
    url = 'https://www.googleapis.com/customsearch/v1?key=' + APIKey + '&cx=' + cx + '&q=' + codeerdeTerm
    
    
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"})
    ruweData = urllib.request.urlopen(request).read()
    
    data = json.loads(ruweData.decode('utf-8')) #geeft de zoekpagine terug in een speciale vorm
    
    if data['searchInformation']['totalResults'] == '1':
       
       resultaten = list(data.values())[3] #stukje waarin de resultaten met daarin de links 
       print(resultaten)
       link = resultaten[0]['link'] #haalt eerste link op uit de resultaen  
       return link
    else:
          return 'niet gevonden'
    
    
    
    
    
    
def zoekHuisarts3(query):
    
    api_key = 'AIzaSyC8-TpYB8BnbpdQc1qiCMGtydu40WLseCI'
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 10,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    
    urls = []
    if len(response['itemListElement']) > 0:
        
        for element in response['itemListElement']:
            if 'url' in element['result']:
                urls.append(element['result']['url'])
            if urls == []:
                urls.append('geen url bekend')
    else:
        return 'Onbekend' 
    
    return urls


def naamVullen():   
    
    
    for x in range(1, len(Vektis2csv)):
        achternaam = str(Vektis2csv[x][4])
     
        voorletter = str(Vektis2csv[x][5])
      
        tussenvoegsel = str(Vektis2csv[x][6])
        
        
       
        if voorletter == '(null)' and tussenvoegsel == '(null)' and achternaam != '(null)':
            namen.append(achternaam)
        elif voorletter == '(null)' and tussenvoegsel != '(null)' and achternaam != '(null)':
            namen.append(tussenvoegsel + ' ' + achternaam)
        elif  voorletter != '(null)' and tussenvoegsel == '(null)' and achternaam != '(null)':
            namen.append(voorletter + ' ' + achternaam)
        elif achternaam == '(null)':
            namen.append('')
        else:
            namen.append(voorletter + ' ' + tussenvoegsel + ' ' + achternaam)
 

            
def vullen(plekDataSet, array):
    for x in range(1, len(Vektis2csv)):
        item = str(Vektis2csv[x][plekDataSet])
        if item != '(null)':
            array.append(item)

namen = [0]
telefoonnummers = [0]
plaatsNamen = [0]

vullen(14 ,telefoonnummers)
vullen(13, plaatsNamen)
naamVullen()
websiteHuisartsen = [0] 
 
zoekHuisarts('0725061263', 'van Geldern')

#namen.insert(1, 'van Geldern')
#telefoonnummers.insert(1, '0725061263')


#for x in range(1, 5): #len(dataSet)):      
#   websiteHuisartsen.append(zoekHuisarts(telefoonnummers[x], namen[x]))
#   
#for x in range(1, 20):
#   websiteHuisartsen.append(zoekHuisarts3(namen[x] + ' ' + plaatsNamen[x]))

#zoekHuisarts()