import sqlite3

miConexion = sqlite3.connect("PrimeraBD")

miCursor = miConexion.cursor()

miCursor.execute('DELETE FROM PRODUCTO WHERE CODIGO=3')

miCursor.execute('SELECT * FROM PRODUCTO')

productos = miCursor.fetchall()
print(productos)

miConexion.commit()
miConexion.close()