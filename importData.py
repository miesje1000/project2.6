import csv
import sqlite3
class Dataimporter(object):
  def __init__(self):
      
      def lijst():
          data = csv.reader(open('C:\\Users\\Maikel\\Documents\\Med.Inf(2.5_2.6)\\SE-project\\vektis_agb_zorgverlener.csv'),delimiter=',',usecols=(2,3,4,14),skiprows=1)
          global huisartsData
          for i in data:
              rij1 = i.next() 
              if rij1[2]=="01":
                  huisartsData = i
         
     
      def overschrijven():     
         conn = sqlite3.connect('huisarts.sqlite3')
         cur = conn.cursor()
         
         for i in huisartsData:
           cur.execute('INSERT INTO Huisarts (achternaam, telefoonnummer) VALUES ( ?, ? )')
             
         conn.commit()
         cur.close()
print("dit is een test")