"""
Diseñe un algoritmo que, dada la división de dos números, muestre en pantalla:
a.  Si la división es exacta
b.  Si se trata de un cociente Par o Impar
c.  Si el cociente es impar, mostrar cual es el residuo
d.  Lea un tercer número y determine cuál de los 3 es mayor
e.  Repetir el proceso para una cantidad de “rondas” determinada por el usuario
"""
import os

#Declaracion de variables
numero1 = 0
numero2 = 0
numero3 = 0
division = 0
residuo = 0
numeroMayor = 0
rondas = 0

#Captura de datos
print("Cuantas divisiones desea realizar?")
rondas = int(input("::"))

for i in range(rondas):
    print("\nDigite el primer numero: ")
    numero1 = float(input("::"))

    print("Digite el segundo numero: ")
    numero2 = float(input("::"))

    while numero2 == 0:
        print("El divisor no puede ser 0")
        print("Digite el segundo numero: ")
        numero2 = float(input("::"))

    division = numero1 / numero2
    residuo = numero1 % numero2

    print(f"\nEl resultado de dividir {numero1} entre {numero2} es: {division}")

    if residuo == 0:
        print("\nLa division es exacta")
    else:
        print("\nLa division no es exacta")

    if division % 2 == 0:
        print("\nEl cociente es PAR")
    else:
        print("\nEl cociente es IMPAR")
        print(f"Su residuo es: {residuo}")

    print("\nIngrese un tercer numero: ")
    numero3 = float(input("::"))

    if numero1 > numero2:
        numeroMayor = numero1
    elif numero2 > numero1: 
        numeroMayor = numero2
    elif numero3 > numero2:
        numeroMayor = numero3
    elif numero2 > numero3:
        numeroMayor = numero2
    elif numero1 > numero3:
        numeroMayor = numero1
    elif numero3 > numero1:
        numeroMayor = numero3
    print(f"\nEl numero mayor es: {numeroMayor}")

os.system("pause")
