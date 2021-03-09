#Ejercicio 1
n = int(input("Intoduzca el numero para el triangulo rectangulo: "))
for i in range(n+1):
    print("*"*i)



#Ejercicio 2
n = int(input("Intoduzca el numero para la cuenta regresiva: "))
for i in range(n,-1,-1):
    print(i,end=",")



 #Ejercicio 3
r= True
n = int(input("Intoduzca el numero para comprobar si es primo o no: "))  
d=0
while d<n and r:
    if n%2==0:
        r=False
    d=d+1
if (r):
    print("El numero es primo")
else:
    print("El numero no es primo")