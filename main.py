import sqlite3

con = sqlite3.connect('ccoo.db')

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS ccoo("+
    "ID INTEGER PRIMARY KEY AUTOINCREMENT, "+
    "NoCO varchar(255), "+
    "Fecha varchar(255), "+
    "Referencia varchar(255), "+
    "Proyecto varchar(255), "+
    "Carpeta varchar(255)"+
")")

con.commit()

con.close()