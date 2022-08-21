"""
Leer un vector de datos hasta que el usuario decida detenerse, antes de iniciar, 
indicarle al usuario que tipo de datos se espera recibir, a continuación: 
Preguntar al usuario la posición del valor que desea eliminar, 
validar si el numero ingresado está dentro de la longitud del vector.
Antes de eliminar el registro, mostrar el vector con todos los datos y en una línea posterior el dato que se va a eliminar, 
finalmente mostrar el vector sin el registro eliminado
"""

import os

#Declaracion

vector = []
pos = 0
iterador = 0
controlContinue = True
respuesta = ""

#Llenado del vector
print("A continuacion, digite datos numericos de tipo flotante segun corresponda")

while controlContinue == True:
    iterador = iterador + 1
    vector.append(float(input(f"{iterador}.Digite el dato a ingresar: ")))
    print("Dato almacenado")

    while respuesta != "SI" and respuesta != "NO":
        respuesta = input("Desea ingresar un nuevo dato?(SI/NO): ")
        respuesta = respuesta.upper()

    if respuesta == "NO":
        controlContinue = False
    respuesta = ""

os.system("cls")

#Impresion de posiciones para mejor comprension del usuario
print("\n\tPosiciones:")
for z in range(len(vector)):
    print(f"\t::[{z+1}]")

#Validacion de longitud
while pos <= 0:
    pos = int(input("\nQue posicion desea eliminar?: "))

    if pos > len(vector):
        print("Posicion fuera del rango del vector, vuelva a intentar")
        pos = 0

#Impresion del vector integro
print("\n\tVector Integro:")
for j in range(len(vector)):
    print(f"\t\tPosicion [{j+1}]: {vector[j]}")

print(f"\nPosicion encontrada [{pos}]: *{vector[pos-1]}* sera eliminado")

#Eliminacion por posicion
for x in range(len(vector)+1):
    if x == pos:
        vector.remove(vector[x-1])

#Impresion del vector luego de eliminar
print("\n\tVector Modificado:")
for y in range(len(vector)):
    print(f"\t\tPosicion [{y+1}]: {vector[y]}")
