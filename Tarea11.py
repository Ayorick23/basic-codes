"""
Leer 5 pares de numeros ingresados por el usuario, evaluar y mostrar en pantalla cual cuadrante del plano 
cartesiano pertenece, considerar que tambien pueden darse los casos de:
a. Ordenada positiva o negativa
b. Abscisa positiva o negativa
c. Punto origen
"""
import os

#Declaracion de variables
coordenadasX = []
coordenadasY = []

for i in range(5):
    print(f"\n{i+1}.Coordenadas (X,Y)")
    print("Ingrese la coordenada para X: ")
    coordenadasX.append(float(input(">>")))
    print("Ingrese la coordenada para Y: ")
    coordenadasY.append(float(input(">>")))

print()
for j in range(5):
    if coordenadasX[j] == 0 and coordenadasY[j] == 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) es el Punto Origen")

    elif coordenadasX[j] > 0 and coordenadasY[j] > 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) pertenece al 1er Cuadrante")

    elif coordenadasX[j] < 0 and coordenadasY[j] > 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) pertenece al 2do Cuadrante")

    elif coordenadasX[j] < 0 and coordenadasY[j] < 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) pertenece al 3er Cuadrante")

    elif coordenadasX[j] > 0 and coordenadasY[j] < 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) pertenece al 4to Cuadrante")

    elif coordenadasX[j] == 0 and coordenadasY[j] > 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) es una Ordenada Positiva")
    
    elif coordenadasX[j] == 0 and coordenadasY[j] < 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) es una Ordenada Negativa")
    
    elif coordenadasX[j] > 0 and coordenadasY[j] == 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) es una Abscisa Positiva")
    
    elif coordenadasX[j] < 0 and coordenadasY[j] == 0:
        print(f"La coordenada ({coordenadasX[j]},{coordenadasY[j]}) es una Abscisa Negativa")

print()
os.system("pause")
