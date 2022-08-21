"""
Capturar nombre, año de nacimiento, cargo y salario de n empleados:
a.  Calcular el respectivo descuento de renta, AFP e ISSS, 
b.  Mostrar nombre, edad, cargo, descuentos realizados y salario neto
c.  Realizar el ejercicio para una cantidad de empleados desconocida
d.  Mostrar la edad media
e.  Mostrar el dinero neto total, recibido por todos los empleados
"""
import os
#Declaracion de variables
n = 0
nombre0 = ""
nombre1 = ""
nombre2 = ""
nombre3 = ""
nombre4 = ""
nombre5 = ""
nacimiento0 = 0
nacimiento1 = 0
nacimiento2 = 0
nacimiento3 = 0
nacimiento4 = 0
nacimiento5 = 0
cargo0 = ""
cargo1 = ""
cargo2 = ""
cargo3 = ""
cargo4 = ""
cargo5 = ""
salario0 = 0
salario1 = 0
salario2 = 0
salario3 = 0
salario4 = 0
salario5 = 0
renta0 = 0
renta1 = 0
renta2 = 0
renta3 = 0
renta4 = 0
renta5 = 0
afp0 = 0
afp1 = 0
afp2 = 0
afp3 = 0
afp4 = 0
afp5 = 0
isss0 = 0
isss1 = 0
isss2 = 0
isss3 = 0
isss4 = 0
isss5 = 0
edad0 = 0
edad1 = 0
edad2 = 0
edad3 = 0
edad4 = 0
edad5 = 0
salarioNeto0 = 0
salarioNeto1 = 0
salarioNeto2 = 0
salarioNeto3 = 0
salarioNeto4 = 0
salarioNeto5 = 0
edadMedia = 0
salarioGlobal = 0

#Captura de datos
print("Ingrese la cantidad de empleados a ingresar: ")
n = int(input(">>"))

i = 0
while i < n:
    if i == 0:
        print(f"Empleado #{i+1}: ")
        print("\tNombre: ")
        nombre0 = input("\t>>")
        print("\tAño de nacimiento: ")
        nacimiento0 = int(input("\t>>"))
        print("\tCargo: ")
        cargo0 = input("\t>>")
        print("\tSalario (USD): ")
        salario0= float(input("\t>>"))

        edad0 = 2022 - nacimiento0
        renta0 = salario0 * 0.10
        afp0 = salario0 * 0.0725
        isss0 = salario0 * 0.03
        salarioNeto0 = salario0 - (renta0 + afp0 + isss0)

        i+=1
    elif i == 1:
        print(f"Empleado #{i+1}: ")
        print("\tNombre: ")
        nombre1 = input("\t>>")
        print("\tAño de nacimiento: ")
        nacimiento1 = int(input("\t>>"))
        print("\tCargo: ")
        cargo1 = input("\t>>")
        print("\tSalario (USD): ")
        salario1= float(input("\t>>"))

        edad1 = 2022 - nacimiento1
        renta1 = salario1 * 0.10
        afp1 = salario1 * 0.0725
        isss1 = salario1 * 0.03
        salarioNeto1 = salario1 - (renta1 + afp1 + isss1)

        i+=1
    elif i == 2:
        print(f"Empleado #{i+1}: ")
        print("\tNombre: ")
        nombre2 = input("\t>>")
        print("\tAño de nacimiento: ")
        nacimiento2 = int(input("\t>>"))
        print("\tCargo: ")
        cargo2 = input("\t>>")
        print("\tSalario (USD): ")
        salario2= float(input("\t>>"))

        edad2 = 2022 - nacimiento2
        renta2 = salario2 * 0.10
        afp2 = salario2 * 0.0725
        isss2 = salario2 * 0.03
        salarioNeto2 = salario2 - (renta2 + afp2 + isss2)

        i+=1
    elif i == 3:
        print(f"Empleado #{i+1}: ")
        print("\tNombre: ")
        nombre3 = input("\t>>")
        print("\tAño de nacimiento: ")
        nacimiento3 = int(input("\t>>"))
        print("\tCargo: ")
        cargo3 = input("\t>>")
        print("\tSalario (USD): ")
        salario3= float(input("\t>>"))

        edad3 = 2022 - nacimiento3
        renta3 = salario3 * 0.10
        afp3 = salario3 * 0.0725
        isss3 = salario3 * 0.03
        salarioNeto3 = salario3 - (renta3 + afp3 + isss3)

        i+=1
    elif i == 4:
        print(f"Empleado #{i+1}: ")
        print("\tNombre: ")
        nombre4 = input("\t>>")
        print("\tAño de nacimiento: ")
        nacimiento4 = int(input("\t>>"))
        print("\tCargo: ")
        cargo4 = input("\t>>")
        print("\tSalario (USD): ")
        salario4= float(input("\t>>"))

        edad4 = 2022 - nacimiento4
        renta4 = salario4 * 0.10
        afp4 = salario4 * 0.0725
        isss4 = salario4 * 0.03
        salarioNeto4 = salario4 - (renta4 + afp4 + isss4)

        i+=1
    elif i == 5:
        print(f"Empleado #{i+1}: ")
        print("\tNombre: ")
        nombre5 = input("\t>>")
        print("\tAño de nacimiento: ")
        nacimiento5 = int(input("\t>>"))
        print("\tCargo: ")
        cargo5 = input("\t>>")
        print("\tSalario (USD): ")
        salario5= float(input("\t>>"))

        edad5 = 2022 - nacimiento5
        renta5 = salario5 * 0.10
        afp5 = salario5 * 0.0725
        isss5 = salario5 * 0.03
        salarioNeto5 = salario5 - (renta5 + afp5 + isss5)

        i+=1

os.system("cls")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 1\t\t|")
print("+---------------------------------------+")
print(f"\tNombre: {nombre0}")
print(f"\tEdad: {edad0} años")
print(f"\tCargo: {cargo0}")
print("-----------------------------------------")
print(f"\tSalario:       ${salario0}")
print(f"\tRenta:        -${renta0}")
print(f"\tAFP:          -${afp0}")
print(f"\tISSS:         -${isss0}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioNeto0}")
print("-----------------------------------------")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 2\t\t|")
print("+---------------------------------------+")
print(f"\tNombre: {nombre1}")
print(f"\tEdad: {edad1} años")
print(f"\tCargo: {cargo1}")
print("-----------------------------------------")
print(f"\tSalario:       ${salario1}")
print(f"\tRenta:        -${renta1}")
print(f"\tAFP:          -${afp1}")
print(f"\tISSS:         -${isss1}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioNeto1}")
print("-----------------------------------------")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 3\t\t|")
print("+---------------------------------------+")
print(f"\tNombre: {nombre2}")
print(f"\tEdad: {edad2} años")
print(f"\tCargo: {cargo2}")
print("-----------------------------------------")
print(f"\tSalario:       ${salario2}")
print(f"\tRenta:        -${renta2}")
print(f"\tAFP:          -${afp2}")
print(f"\tISSS:         -${isss2}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioNeto2}")
print("-----------------------------------------")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 4\t\t|")
print("+---------------------------------------+")
print(f"\tNombre: {nombre3}")
print(f"\tEdad: {edad3} años")
print(f"\tCargo: {cargo3}")
print("-----------------------------------------")
print(f"\tSalario:       ${salario3}")
print(f"\tRenta:        -${renta3}")
print(f"\tAFP:          -${afp3}")
print(f"\tISSS:         -${isss3}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioNeto3}")
print("-----------------------------------------")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 5\t\t|")
print("+---------------------------------------+")
print(f"\tNombre: {nombre4}")
print(f"\tEdad: {edad4} años")
print(f"\tCargo: {cargo4}")
print("-----------------------------------------")
print(f"\tSalario:       ${salario4}")
print(f"\tRenta:        -${renta4}")
print(f"\tAFP:          -${afp4}")
print(f"\tISSS:         -${isss4}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioNeto4}")
print("-----------------------------------------")

print("\n+---------------------------------------+")
print("|\t\tEmpleado 6\t\t|")
print("+---------------------------------------+")
print(f"\tNombre: {nombre5}")
print(f"\tEdad: {edad5} años")
print(f"\tCargo: {cargo5}")
print("-----------------------------------------")
print(f"\tSalario:       ${salario5}")
print(f"\tRenta:        -${renta5}")
print(f"\tAFP:          -${afp5}")
print(f"\tISSS:         -${isss5}")
print("-----------------------------------------")
print(f"\tSalario Neto:  ${salarioNeto5}")
print("-----------------------------------------")

edadMedia = (edad0 + edad1 + edad2 + edad3 + edad4 + edad5) / n
salarioGlobal = salarioNeto0 + salarioNeto1 + salarioNeto2 + salarioNeto3 + salarioNeto4 + salarioNeto5

print(f"\nLa edad media de los {n} empleados es: {edadMedia} años")
print(f"El salario neto total de los {n} empleados es: ${salarioGlobal}\n")

os.system("pause")