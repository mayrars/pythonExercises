import sqlite3

miConexion = sqlite3.connect("PrimeraBD")

miCursor = miConexion.cursor()

variosArticulos = [
    ("Bicicleta", 3000,"DEPORTES"),
    ("Portatil", 2500,"COMPUTADORAS"),
    ("Movil", 500, "TELEFONIA"),
    ("Tablet", 900,"COMPUTADORAS")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?)", variosArticulos)

miConexion.commit()
miConexion.close()