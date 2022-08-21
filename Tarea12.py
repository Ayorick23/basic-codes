"""
Crear dos vectores que almacenen la temperatura más alta y baja de una cantidad de días 
determinada por el usuario, no menor a 3, el algoritmo deberá:
Mostrar la temperatura media que se obtuvo en cada día
Mostrar cual fue la temperatura media mas alta registrada, junto a su día
Mostrar cual fue la temperatura media más baja registrada, junto a su día
"""

import os

#Declaracion
tempAlta = []
tempBaja = []
tempMedia = []
cantidad = 0
diaMayor = 0
diaMenor = 0

#Llenado de vectores
while cantidad < 3:
    print("Ingrese la cantidad de dias a registrar: ")
    cantidad = int(input(">>"))
    if cantidad < 3:
        print("No puede ingresar menos de 3 dias, intente de nuevo...")

os.system("cls")

for i in range(cantidad):
    print(f"\nDia {i+1}:")
    tempAlta.append(float(input("Mayor temperatura alcanzada: ")))
    tempBaja.append(float(input("Menor temperatura alcanzada: ")))
os.system("pause")

for x in range(cantidad):
    tempMedia.append((tempAlta[x] + tempBaja[x]) / 2)

mayor = tempAlta[0]
for y in range(len(tempAlta)):
    if tempAlta[y] > mayor:
        mayor = tempAlta[y]
        diaMayor = y+1

menor = tempBaja[0]
for z in range(len(tempBaja)):
    if tempBaja[z] < menor:
        menor = tempBaja[z]
        diaMenor = z+1

print()
for a in range(len(tempMedia)):
    print(f"La Media de temperatura del Dia {a+1} es: {tempMedia[a]} grados centigrados")

print()
print(f"El Dia {diaMayor} se registro la temperatura mas alta que fue de: {mayor} grados centigrados")
print(f"El Dia {diaMenor} se registro la temperatura mas baja que fue de: {menor} grados centigrados")