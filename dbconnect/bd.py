import sqlite3

miConexion = sqlite3.connect("PrimeraBD")

miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOR (
        CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50),
        PRECIO INTEGER(10),
        SECCION VARCHAR(20)
    )
''')

productos = [
    ("Leche", 1000, "Lácteos"),
    ("Queso", 1500, "Lácteos"),
    ("Pan", 2000, "Panadería"),
    ("Galletas", 500, "Panadería"),
]
miCursor.executemany("INSERT INTO PRODUCTOR VALUES (NULL,?,?,?)", productos)
miConexion.commit()
miConexion.close()