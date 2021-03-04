peso = float(input("Digita tu peso en Kg: "))
altura = float(input("Digita tu altura en m: "))

icm = peso/altura**2
icm = round(icm,2)
print(f"Tu índice de masa corporal es  {icm} donde  {icm}  es el índice de masa corporal calculado redondeado con dos decimales.")
