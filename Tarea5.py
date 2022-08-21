#Declaracion de variables
empleado1 = ""
empleado2 = ""
empleado3 = ""
cargoEmpleado1 = ""
cargoEmpleado2 = ""
cargoEmpleado3 = ""
salarioEmpleado1 = 0
salarioEmpleado2 = 0
salarioEmpleado3 = 0
rentaEmpleado1 = 0
rentaEmpleado2 = 0
rentaEmpleado3 = 0
afpEmpleado1 = 0
afpEmpleado2 = 0
afpEmpleado3 = 0
isssEmpleado1 = 0
isssEmpleado2 = 0
isssEmpleado3 = 0
descuentosEmpleado1 = 0
descuentosEmpleado2 = 0
descuentosEmpleado3 = 0

#Captura de datos
print(">>Datos del empleado 1:")
print("Nombre: ")
empleado1 = input(">>")
print("Cargo: ")
cargoEmpleado1 = input(">>")
print("Salario: ")
salarioEmpleado1 = float(input(">>"))

rentaEmpleado1 = salarioEmpleado1 * 0.1
afpEmpleado1 = salarioEmpleado1 * 0.0725
isssEmpleado1 = salarioEmpleado1 * 0.03
descuentosEmpleado1 = rentaEmpleado1 + afpEmpleado1 + isssEmpleado1

print("\n\n>>Datos del empleado 2:")
print("Nombre: ")
empleado2 = input(">>")
print("Cargo: ")
cargoEmpleado2 = input(">>")
print("Salario: ")
salarioEmpleado2 = float(input(">>"))

rentaEmpleado2 = salarioEmpleado2 * 0.1
afpEmpleado2 = salarioEmpleado2 * 0.0725
isssEmpleado2 = salarioEmpleado2 * 0.03
descuentosEmpleado2 = rentaEmpleado2 + afpEmpleado2 + isssEmpleado2

print("\n\n>>Datos del empleado 3:")
print("Nombre: ")
empleado3 = input(">>")
print("Cargo: ")
cargoEmpleado3 = input(">>")
print("Salario: ")
salarioEmpleado3 = float(input(">>"))

rentaEmpleado3 = salarioEmpleado3 * 0.1
afpEmpleado3 = salarioEmpleado3 * 0.0725
isssEmpleado3 = salarioEmpleado3 * 0.03
descuentosEmpleado3 = rentaEmpleado3 + afpEmpleado3 + isssEmpleado3

#Impresion en pantalla
print("\n+---------------------------------------+")
print("|\t\tEmpleado 1\t\t|")
print("+---------------------------------------+")
print(f"\tNombre: {empleado1}")
print(f"\tCargo: {cargoEmpleado1}")
print("-----------------------------------------")
print(f"\tSalario:       ${salarioEmpleado1}")
print(f"\tRenta:        -${rentaEmpleado1}")
print(f"\tAFP:          -${afpEmpleado1}")
print(f"\tISSS:         -${isssEmpleado1}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioEmpleado1-descuentosEmpleado1}")
print("-----------------------------------------")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 2\t\t|")
print("+---------------------------------------+")
print(f"\n\tNombre: {empleado2}")
print(f"\tCargo: {cargoEmpleado2}")
print("-----------------------------------------")
print(f"\tSalario:       ${salarioEmpleado2}")
print(f"\tRenta:        -${rentaEmpleado2}")
print(f"\tAFP:          -${afpEmpleado2}")
print(f"\tISSS:         -${isssEmpleado2}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioEmpleado2-descuentosEmpleado2}")
print("-----------------------------------------")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 3\t\t|")
print("+---------------------------------------+")
print(f"\n\tNombre: {empleado3}")
print("-----------------------------------------")
print(f"\tSalario:       ${salarioEmpleado3}")
print(f"\tRenta:        -${rentaEmpleado3}")
print(f"\tAFP:          -${afpEmpleado3}")
print(f"\tISSS:         -${isssEmpleado3}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioEmpleado3-descuentosEmpleado3}")
print("-----------------------------------------")
