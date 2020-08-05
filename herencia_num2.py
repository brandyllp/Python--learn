name = input("Por favor Ingresar Nombre: ")
age = input ("Por favor Intresar Edad ")
salary = input ("Por favor Ingresar Su Salario: ")
salary = float(salary)
ciclo = 1 
Continuar =""
class persona:
    def nombre(self):                   ##Agrupo valores de Nombre y edad
        print("Su nombre es " + name)
    def edad(self):
        print("Su edad es " + age)
class sueldo:
    def sueldo(self):  
        if salary >= 3000.0:                   # Clase de Salario es igual a salary la variable
            print("Debe pagar impuesto ")
        else:
            print("No debe pagar impuesto ") 

def funcion(obj):       #Valores de Nombre y Edad
    obj.nombre()
    obj.edad()

def funcion_sueldo(obj):        # Valor de Sueldo
    obj.sueldo()
 
nuevo_trabajador = persona()   # Objeto Nuevo Trabajador
funcion(nuevo_trabajador)        
sueldo_trabajador = sueldo()      #Objeto Nuevo sueldo
funcion_sueldo(sueldo_trabajador)

Continuar = input ("Desea Continuar Si o No ")
while ciclo <= 100: 
    if Continuar.upper() == "Si".upper():
      name = input("Por favor Ingresar Nombre: ")
      age = input ("Por favor Intresar Edad ")                    ## Ciclo para repetir la funcionalidad del programa 
      salary = float(input ("Por favor Ingresar Su Salario: "))
      nuevo_trabajador = persona()
      funcion(nuevo_trabajador)
      sueldo_trabajador = sueldo()
      funcion_sueldo(sueldo_trabajador)
    elif Continuar.upper() == "No".upper():
        print("Gracias por usar nuestro Programa")
        break
    Continuar = input ("Desea Continuar Si o No ")
    ciclo +=1