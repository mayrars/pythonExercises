import re

listaNombres = ["Ana Lopez", "Pedro Gonzalez", "Maria Martin", "Luis Perez", "Juan Martinez", "Pedro Gomez", "Maria Lopez", "Luis Gonzalez"]


for i in listaNombres:
    if re.findall("[E-K]", i):
        print(i)