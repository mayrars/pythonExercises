def funcion_decoradora(funcion_parametros):
    def funcion_interior(*parametros):
        print("Realizando calculo")
        funcion_parametros(*parametros)
        print("Calculo finalizado")
    return funcion_interior

@funcion_decoradora
def suma(num1,num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

suma(10,20)
resta(30,10)