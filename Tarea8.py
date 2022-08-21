import os
import getpass

#Declaracion de variables
usuario = ""
contra = ""
opcion = 0

#Usuario admin:       Admin
#Contraseña admin:    Computacionintgrl

#Usuario cliente:     user
#Contraseña cliente:  COMPU1

#Captura de datos
print("BIENVENIDO...")

print("Es usted: \n1. Administrador\n2. Cliente")
opcion = int(input("Elija su opcion (1/2): "))

if opcion == 1:
    usuario = input("Usuario:    >> ")
    usuario = usuario.capitalize()
    contra = getpass.getpass("Contraseña:  >> ")
    contra = contra.capitalize()

    if usuario == "Admin" and contra == "Computacionintgrl":
        print("Bienvenido Administrador!")

    else:
        print("Ingrese credenciales correctas")

elif opcion == 2:
    usuario = input("Usuario:    >> ")
    usuario = usuario.lower()
    contra = getpass.getpass("Contraseña:  >> ")
    contra = contra.upper()

    if usuario == "user" and contra == "COMPU1":
        print("Bienvenido Cliente!")
    
    else:
        print("Ingrese credenciales correctas")

else:
    print("Ingrese una opcion valida (1/2)")

os.system("pause")
