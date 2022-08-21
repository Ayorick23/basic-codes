#Declaracion de variables
num1 = 0
num2 = 0

suma = 0
resta = 0
multi = 0
div = 0

#Captura de datos
num1 = float(input("Digite su primer numero: "))
num2 = float(input("\nDigite su segundo numero: "))

#Formulas
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2

#Impresion en pantalla
print("\n\nRESULTADOS:")
print("\nLa suma de los numeros ingresados es: " + str(suma))
print("\nLa resta de los numeros ingresados es: " + str(resta))
print("\nLa multiplicacion de los numeros ingresados es: " + str(multi))
print("\nLa division de los numeros ingresados es: " + str(div))