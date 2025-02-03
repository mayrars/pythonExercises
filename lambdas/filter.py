'''def numeroPar(numero):
    if numero % 2 == 0:
        return True'''

numeros = [17,5,15,23,18,34]

print(list(filter(lambda numeroPar: numeroPar % 2 == 0, numeros)))
