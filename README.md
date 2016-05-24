# project2.6

#importeer eerst handmatig het bestand met de data, op mijn computer tabelcsv

#filtreer de huisartsen uit het bestand 
ha_data = []
def zoekhuisarts(lst):
    for col in lst:
        if col[2] == int('01'):
            ha_data.append(col)

zoekhuisarts(tabelcsv)

#print nummer, naam en telefoon-nummer
def printgegevens(lst):
    for col in lst:
        print(col[3], col[4], col[5], col[6], col[14])

printgegevens(ha_data)
