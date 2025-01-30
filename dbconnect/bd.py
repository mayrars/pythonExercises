import sqlite3

miConexion = sqlite3.connect("PrimeraBD")

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for i in variosProductos:
    print("Nombre del producto: ", i[0], "Secciòn:",i[2], " Precio: ", i[1])

miConexion.commit()
miConexion.close()