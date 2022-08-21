#Declaracion de variables
velocidad = 0
tiempo = 0
distancia = 0

#Captura de datos
print(">>Programa para determinar la velocidad")
print("\nDigite la velocidad a la que viaja el auto: ")
velocidad = float(input(">>"))
print("\nDigite el tiempo en el que viajo (en segundos)")
tiempo = float(input(">>"))

#Manejo de datos
distancia = velocidad * tiempo

#Impresion en pantalla
print("\nLa distancia que recorrio el automovil fue:", distancia, "Metros")
print("O")
print(f"La distancia que recorrio el automovil fue: {distancia/1000} Kilometros")
