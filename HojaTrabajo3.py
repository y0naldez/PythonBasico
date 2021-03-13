
#Ejercicio 1
clave = "contraseña"
contraseña = input("Introduce la contraseña: ")
if clave == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

#Ejercicio 2 
nombre = input("¿Cómo te llamas? ")
genero = input("¿Cuál es tu sexo  -M O H- ? ")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)