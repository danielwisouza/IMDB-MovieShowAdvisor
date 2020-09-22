from xml.dom import minidom
import sqlite3
conn = sqlite3.connect('teste1.db')
cursor = conn.cursor()

#ABRINDO ARQUIVO XML UNICO
xmldoc = minidom.parse('0000301510136952_2016_estendido.xml')
#LOCALIZANDO CAMPO COM AS INFORMACOES NO XML
itemList = xmldoc.getElementsByTagName('TOTAL-PRODUCAO')

#Create table
#c.execute('''CREATE TABLE ANO
#             (ano)''')

# Insert a row of data
for i in range(0,len(itemList)):
        controle = [(int(itemList[i].attributes['ANO-PRODUCAO'].value))]
        if controle = 2014.
        cursor.execute('INSERT INTO ANO VALUES (?)',controle)
        

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()

