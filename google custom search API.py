# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:44:56 2016

@author: Bart
"""

import urllib.request, urllib.response
import urllib
import json

def telefoonnummerBewerken(nummer):
    if nummer[2] == '-':
        nieuwNummer = nummer[0:2] + nummer[3:]
        
    elif nummer[3] == '-':
        nieuwNummer = nummer[0:3] + nummer[4:]
        
    elif nummer[4] == '-':
        nieuwNummer = nummer[0:4] + nummer[5:]
    else:
        nieuwNummer = nummer
        
    return nieuwNummer
         


def zoekHuisarts(zoekTerm):
    #zoekTerm = '0725061263' + ' ' + 'F.P. van Geldern'
    codeerdeTerm = urllib.parse.quote(zoekTerm, safe='') #de zoekterm wordt veranderd zodat google het kan lezen
    
    APIKey = 'AIzaSyCenzxlkgjkItijd8x0AseTh10hYor-L8I'
    cx = '004386439249891552984:kzfpgdjn5uy' #domein zoekmachine, ingesteld op independer.nl
    
    url = 'https://www.googleapis.com/customsearch/v1?key=' + APIKey + '&cx=' + cx + '&q=' + codeerdeTerm
    
    
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"})
    ruweData = urllib.request.urlopen(request).read()
    
    data = json.loads(ruweData.decode('utf-8')) #geeft de zoekpagine terug in een speciale vorm
    
    resultaten = list(data.values())[0] #stukje waarin de resultaten met daarin de links 
    link = resultaten[0]['link'] #haalt eerste link op uit de resultaen
    
    print(link)
    
    
    
    
def zoekHuisarts2():  
    APIKey = 'AIzaSyC8-TpYB8BnbpdQc1qiCMGtydu40WLseCI'
    zoekTerm = 'huisarts egmond'
    query = urllib.parse.quote(zoekTerm, safe='')
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': APIKey,
    }
    
    url = service_url + '?' + urllib.parse.urlencode(params)
    url = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"})
    
   
    response = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    print (response)
    
    
def zoekHuisarts3():
    
    api_key = 'AIzaSyC8-TpYB8BnbpdQc1qiCMGtydu40WLseCI'
    query = 'Academisch medisch centrum'
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 10,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    print(response) 

zoekHuisarts3()