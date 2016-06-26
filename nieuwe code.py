''' Importeer handmatig de bestanden waarin de zorgverleners staan, 
de praktijken en de koppeling tussen deze twee.'''

haData = []
def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'):
            haData.append(col)

zoekhuisarts(tabelcsv)

for item in haData:
    if item[6] != '(null)':
        item[4] = item[5] + ' ' + item[6] + ' ' + item[4]
        item.remove(item[5])
        item.remove(item[6])
    else:
        item[4] = item[5] + ' ' + item[4]
        item.remove(item[5])
        item.remove(item[6])

praktijk = []
def zoekpraktijk(lst):
    for col in lst:
        if col[2] == int('01'):
            praktijk.append(col)

zoekpraktijk(praktijkcsv)

koppel = []
def zoekkoppel(lst):
    for col in lst:
        if col[2] == int('01'):
            koppel.append(col)

zoekkoppel(koppelcsv)

kopHa = []
kopPr = []

for item in koppel:
    kopHa.append(item[3])
    kopPr.append(item[4])
    
kopHaPr = []
def haEnPr(lst1, lst2):
    for item in lst1:
        kopHaPr.append(item)
    for item in lst2:
        kopHaPr.append(item)
        
haEnPr(kopHa, kopPr)

koppelSort = []
def kopSort(lst):
    for i in range(12228):
        koppelSort.append(lst[i:24456+i:12228])
        
kopSort(kopHaPr)

prNr = []
prNa1 = []
prNa2 = []

for item in praktijk:
    prNr.append(item[3])
    prNa1.append(item[4])
    prNa2.append(item[5])

pr = []
def prSamenvoegen(lst1, lst2, lst3):
    for item in lst1:
        pr.append(item)
    for item in lst2:
        pr.append(item)
    for item in lst3:
        pr.append(item)
        
prSamenvoegen(prNr, prNa1, prNa2)

prSort = []
def praktijkSort(lst):
    for i in range(5429):
        prSort.append(lst[i:16287+i:5429])
        
praktijkSort(pr)

for item in prSort:
    if item[2] != '(null)':
        item[1] = item[1] + ' ' + item[2]
    item.remove(item[2])
    
haPrNaam = []
def koppeling(lst1, lst2, lst3):
    for item in lst1:
        for obj in lst3:
            if item[0] == obj[2]:
                haPrNaam.append(obj[3])
        for ding in lst2:
            if item[1] == ding[0]:
                haPrNaam.append(ding[1])
        

koppeling(koppelSort, prSort, haData)




            
