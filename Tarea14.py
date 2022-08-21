"""
Crear un vector que almacene 5 nombres proporcionados por el usuario
1.  Crear un menú, con las opciones Modificar, Eliminar, Mostrar y salir
2.  Para modificar, se espera recibir el nombre que desea modificar, al momento de modificar, deberá validar si existe, en caso de existir, recibir el nuevo nombre, caso contrario, mostrar mensaje de error y regresar al menú inicial
3.  Eliminar un dato, dependiendo del nombre que elija el usuario, validar si existe, preguntar al usuario si está seguro y proceder acorde a la elección.
4.  El algoritmo solo finalizara si el usuario así lo decide
5.  Hacer uso de al menos 2 funciones
"""

import os

#Declaracion de variables
nombres = []
opcion = 0
controlModificar = True
datoModificar = ""
controlEliminar = True
datoEliminar = ""
controlPrincipal = True
respuesta = ""

#llenado del vector
print("\n\tLlenado Inicial de su Vector\n")
for i in range(5):
    nombres.append(input(f"Digite el nombre a ingresar [{i+1}]: "))

os.system("pause")
os.system("cls")

def menuPrincipal():
    print("\t\t+---------------------------------------+")
    print("\t\t|\t\tMENU PRINCIPAL\t\t|")
    print("\t\t+---------------------------------------+")
    print("\t\t|\t1. Modificar Registro\t\t|")
    print("\t\t|\t2. Eliminar Registro\t\t|")
    print("\t\t|\t3. Mostrar registros\t\t|")
    print("\t\t|\t4. Salir\t\t\t|")
    print("\t\t+---------------------------------------+")

def funContinuar():
    global respuesta
    respuesta = input("Desea volver al Menu Principal?(SI/NO): ")
    respuesta = respuesta.upper()
            
    if respuesta == "SI":
        controlPrincipal = True
        os.system("cls")
            
    elif respuesta == "NO":
        print("Saliendo del programa...")
        print(quit())
    
    else:
        print("Escriba SI/NO")

#Menu
while controlPrincipal == True:
    menuPrincipal()

    while opcion >= 0:
        opcion = int(input("\t\t\tOPCION(1,2,3,4): "))
        os.system("cls")

        if opcion <= 0 or opcion > 4:
            print("Elija una opcion valida (1-4):\n")
            menuPrincipal()

        elif opcion == 1:
            controlModificar = True
            print("\n\t>> Opcion Modificar Registro <<\n")
            while controlModificar:
                datoModificar = input("Digite el nombre que desea Modificar: ")

                for a in range(len(nombres)):
                    if datoModificar == nombres[a]:
                        nombres[a] = input(f"Valor encontrado en posicion [{a+1}]\n\nDigite el nuevo nombre: ")
                        print("Registro modificado con exito!\n")
                        controlModificar = False
                        break
                    
                    if a == len(nombres)-1:
                        print("Dato no encontrado dentro del registro, ingrese uno valido")
            
            controlPrincipal = False
            funContinuar()
            menuPrincipal()
        
        elif opcion == 2:
            print("\n\t>> Opcion Eliminar Registro <<\n")
            while controlEliminar:
                datoEliminar = input("Digite el nombre que desea Eliminar: ")

                for b in range(len(nombres)):
                    if datoEliminar == nombres[b]:
                        print(f"Nombre *{datoEliminar}* fue encontrado en la posicion [{b+1}], sera eliminado\n")
                        nombres.remove(nombres[b])
                        controlEliminar = False
                        break

                    if b >= len(nombres)-1:
                        print("Dato no encontrado dentro del registro, ingrese uno valido")

            controlPrincipal = False
            funContinuar()
            menuPrincipal()

        elif opcion == 3:
            print("\n\t\t>> Opcion Mostrar Registro <<\n")
            print("\t+-----------------------------------------------+")
            print("\t|\tPosicion\t|\tNombre\t\t|")
        
            for c in range(len(nombres)):
                print("\t+-----------------------------------------------+")
                print(f"\t|\t>> [{c+1}]\t\t|\t{nombres[c]}\t\t|")

            print("\t+-----------------------------------------------+\n")
            controlPrincipal = False
            funContinuar()
            menuPrincipal()

        elif opcion == 4:
            print("Saliendo del programa...")
            print(quit())