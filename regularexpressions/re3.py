import re

cadena1 = "Danilo Andrusco"
cadena2 = "123456"
cadena3 = "a123789"

if re.match("\d", cadena2):
    print("Match")
else:
    print("No Match")