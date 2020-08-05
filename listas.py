user = input("Insert user ")
password = input("Insert password ")
list_for_user = []
words = 1
cycle = 1
element =""
while words <= 5:
     list_for_user.append(input("Insertar Elemento "))
     words += 1

print("Ha ingresado Correctamente los Elementos ")
print("Estos Son Sus Elementos ")
for lista in list_for_user:
 print(lista)
 
 while words <= 100:
     element = input("Desea: Agregar o Eliminar elementos ")
     if element == "agregar":
       list_for_user.append(input("Que elemento desea agregar "))
       for lista in list_for_user:
        print(lista)
     elif element == "eliminar":
       list_for_user.remove(input("Que elemento desea eliminar"))
       for lista in list_for_user:
        print(lista)
     elif element == "no":
       break
     words += 1

print("Gracias Por usar nuestro Sistema " + user)
