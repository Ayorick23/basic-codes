#Declaracion de variables
VALOR_PI = 3.1416

radio = 0
altura = 0
volumen = 0

#Captura de datos
print("Digite el valor del radio del cilindro: ")
radio = float(input(">>"))
print("Digite el valor de la altura del cilindro: ")
altura = float(input(">>"))

#Formula
volumen = VALOR_PI * (radio)**2 * altura

#Impresion en pantalla
print("\n\nRESULTADO...")
print(f"El volumen del cilindro con radio {radio} cm y altura {altura} cm, es: {volumen} cm^3")
