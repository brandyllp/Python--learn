key = "sUpErMaRiO" # Clave predefinida
name = input("Insert User ") # Usuario
tried = 1 #Inicio de numero de intento
key_insert ="" # Clave Vacia
while tried <= 3:                   #Uso del Ciclo While para reptir 3 veces 
    key_insert = input("Insertar Contraseña ")
    if key_insert.upper() == key.upper():
        print("Bienvenido " + name)
        break
    print(tried)
    tried += 1
if key_insert.upper() == key.upper():
    print("Como estuvo su dia? " + name)
else:
    print("Intentas entrar a la cuenta sin permiso, llamare a la policia")      
    print("Llamando a policia")