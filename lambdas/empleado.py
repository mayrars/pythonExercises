class Empleado:
    def __init__(self,nombre,cargo,sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
    def __str__(self):
        return "{} trabaja como {} y gana {} ".format(self.nombre,self.cargo,self.sueldo)

listaEmpleado = [
    Empleado("Juan","Programador",5000),
    Empleado("Ana","Analista",6000),
    Empleado("Luis","Diseñador",7000),
    Empleado("Maria","Gerente",8000),
    Empleado("Pedro","Contador",9000),
    Empleado("Sofia","Secretaria",4000),
]

sueldoAltos = filter(lambda empleado: empleado.sueldo > 6000,listaEmpleado)

for empleado in sueldoAltos:
    print(empleado)