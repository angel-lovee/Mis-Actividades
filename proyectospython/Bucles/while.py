#Bucle While
import math
numero=int(input("Escriba un numero: "))

while numero<0:
    print("Por favor ingrese un numero positivo")
    numero= int(input("Vuelva a ingresar un numero positivo: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f}")


