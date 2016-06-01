# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:07:15 2016

@author: Maikel
"""

import sqlite3
import urllib.request
import urllib
import json

haData = []
haTel=[] 
aangepastNummer = []   
zoekterm=[]
haNamen=[]
def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'):
            haData.append(col)
            haTel.append(str(col[14]))
            haNamen.append(col[4]+" "+col[5])
            
zoekhuisarts(Vektis2csv)

def telefoonnummerBewerken(nummer):  
    
    if(len(nummer)>4):
        if nummer[2] == '-':
            nieuwNummer = nummer[0:2] + nummer[3:]
            
        
        elif nummer[3] == '-':
            nieuwNummer = nummer[0:3] + nummer[4:]
        
        elif nummer[4] == '-':
            nieuwNummer = nummer[0:4] + nummer[5:]
        else:
            nieuwNummer = nummer
        
        return nieuwNummer

def telefoonnummerOpvrager(lijst):      
    for nummer in lijst:
        aangepastNummer.append(telefoonnummerBewerken(nummer))


telefoonnummerOpvrager(haTel)
#print(aangepastNummer)

#print nummer, naam en telefoon-nummer
#def printgegevens(lst):
#    for col in lst:
#        print(col[3], col[4], col[5], col[6], col[14])
#
#printgegevens(haData)
#db = sqlite3.connect('specialismen_db.sqlite')
#
##tabel voor Huisartsen aanmaken
#cursor = db.cursor()
#cursor.execute('''
#    CREATE TABLE IF NOT EXISTS Huisartsen(id INTEGER PRIMARY KEY, achternaam TEXT,
#                       voorletters TEXT, tussenvoegsel TEXT, telnr TEXT)
#''')
#
##data uit ha_data inlezen in tabel Huisartsen
#for lst in haData:
#    cursor.execute('''INSERT INTO Huisartsen(id, achternaam, voorletters, tussenvoegsel, telnr)
#                  VALUES(?,?,?,?,?)''', (lst[3], lst[4], lst[5], lst[6], lst[14]))
#
#for row in cursor.execute('SELECT * FROM Huisartsen'):
#        print(row)
#        
##LET OP: dit alleen runnen als je de tabel wilt verwijderen
#cursor.execute('''DROP TABLE Huisartsen''')
#
#db.commit()
##
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
    #print(resultaten)
    link = resultaten[0]['link'] #haalt eerste link op uit de resultaten
    
    print(link)

def zoekTermMaken(lijstNamen, lijstNummers):
   for i in range(50):
       if lijstNamen[i] != 'null':
           naam = lijstNamen[i]
       else:
           naam = ''
           
       if lijstNummers[i] != 'null':  
           nummer = lijstNummers[i]
       else:
           nummer = ''
             
       term = nummer + " "+ naam
       if term:
           zoekterm.append(term)
        
zoekTermMaken(haNamen, aangepastNummer)   
print(zoekHuisarts('KERNEBEEK W 0203449247'))
        
        



