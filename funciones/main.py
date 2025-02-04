def funcion_decoradora(funcion_parametros):
    def funcion_interior():
        print("Realizando calculo")
        funcion_parametros()
        print("Calculo finalizado")
    return funcion_interior

@funcion_decoradora
def suma():
    print(10+20)

@funcion_decoradora
def resta():
    print(10-20)

suma()
resta()