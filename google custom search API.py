# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:44:56 2016

@author: Bart
"""

import urllib.request
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
    #zoekTerm = '0725061263' + ' ' + 'Dhr. F.P. van Geldern'
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