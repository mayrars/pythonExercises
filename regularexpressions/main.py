import re
cadena = "Vamos a aprender las expresiones regulares en Python. Python es un lenguaje de programación muy potente y con muchas posibilidades."
textoBuscar = "Python"

print(re.findall(textoBuscar,cadena))

print(len(re.findall(textoBuscar,cadena)))
