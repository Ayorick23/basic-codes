#Declaracion de variables
lado = 0
base = 0
altura = 0

area = 0
perimetro = 0

#Captura de datos
print("Digite el lado de su triangulo en centimetros: ")
lado = float(input(">>"))
print("\nDigite la base de su triangulo en centimetros: ")
base = float(input(">>"))
print("\nDigite la altura de su triangulo en centimetros: ")
altura = float(input(">>"))

#Formulas
perimetro = lado * 3
area = (base * altura) / 2

#Impresion en pantalla
print(f"El area de su triangulo es: {area} cm^2")
print(f"El perimetro de su triangulo es: {perimetro} cm")