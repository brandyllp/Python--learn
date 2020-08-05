operacion = input("Cual es la Operacion Que Quieres Realizar ") #Operacion a Realizar
num1 = input("Ingresa el Primer Numero ") #Primer Numero
num2 = input("Ingresa el Segudo NUmero ") #Segundo Numero
if operacion == "suma" :
    resultado = float(num1) + float(num2) #Operacion Suma
    print("Su resultado es " + str(resultado))
elif operacion == "resta" :
    resultado = float(num1) - float(num2) #Operacion Resta
    print("Su resultado es " + str(resultado))
elif operacion == "multiplicacion" :
    resultado = float(num1) * float(num2) #Operacion Multiplicacion
    print("Su resultado es "+ str(resultado))
elif operacion == "division":
    resultado = float(num1) / float(num2)  #Operacion Division
    print("Su resultado es "+ str(resultado))
else:
    print("Escogio Una Operacion No Valida Para El Programa vuelva a ejecutar")

