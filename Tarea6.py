import os
#Declaracion de variables
primerTriExa1 = 0
primerTriExa2 = 0
primerTriExa3 = 0
primerTriLab1 = 0
primerTriLab2 = 0
primerTriLab3 = 0
primerTriProyect = 0
primerTriNotas = 0
primerTriLabs = 0
primerTriProyectProm = 0
primerTriProm = 0

segundoTriExa1 = 0
segundoTriExa2 = 0
segundoTriExa3 = 0
segundoTriLab1 = 0
segundoTriLab2 = 0
segundoTriLab3 = 0
segundoTriProyect = 0
segundoTriNotas = 0
segundoTriLabs = 0
segundoTriProyectProm = 0
segundoTriProm = 0

tercerTriExa1 = 0
tercerTriExa2 = 0
tercerTriExa3 = 0
tercerTriLab1 = 0
tercerTriLab2 = 0
tercerTriLab3 = 0
tercerTriProyect = 0
tercerTriNotas = 0
tercerTriLabs = 0
tercerTriProyectProm = 0
tercerTriProm = 0

alumno = ""
promedioTri1 = 0
promedioTri2 = 0
promedioTri3 = 0



promedioFinal = 0

#Captura de datos
print("Ingrese su nombre: ")
alumno = input("::")
print(">>Primer Trismestre")
print("Ingrese la nota del examen 1: ")
primerTriExa1 = float(input("::"))
print("Ingrese la nota del examen 2: ")
primerTriExa2 = float(input("::"))
print("Ingrese la nota del examen 3: ")
primerTriExa3 = float(input("::"))
print("Ingrese la nota del laboratorio 1: ")
primerTriLab1 = float(input("::"))
print("Ingrese la nota del laboratorio 2: ")
primerTriLab2 = float(input("::"))
print("Ingrese la nota del laboratorio 3: ")
primerTriLab3 = float(input("::"))
print("Ingrese la nota del proyecto trimestral: ")
primerTriProyect = float(input("::"))

primerTriNotas = ((primerTriExa1 + primerTriExa2 + primerTriExa3) / 3) * 0.35
primerTriLabs = ((primerTriLab1 + primerTriLab2 + primerTriLab3) / 3) * 0.35
primerTriProyectProm = primerTriProyect * 0.3
primerTriProm = primerTriProyect + primerTriNotas + primerTriLabs

print(">>Segundo Trismestre")
print("Ingrese la nota del examen 1: ")
segundoTriExa1 = float(input("::"))
print("Ingrese la nota del examen 2: ")
segundoTriExa2 = float(input("::"))
print("Ingrese la nota del examen 3: ")
segundoTriExa3 = float(input("::"))
print("Ingrese la nota del laboratorio 1: ")
segundoTriLab1 = float(input("::"))
print("Ingrese la nota del laboratorio 2: ")
segundoTriLab2 = float(input("::"))
print("Ingrese la nota del laboratorio 3: ")
segundoTriLab3 = float(input("::"))
print("Ingrese la nota del proyecto trimestral: ")
segundoTriProyect = float(input("::"))

segundoTriNotas = ((segundoTriExa1 + segundoTriExa2 + segundoTriExa3) / 3) * 0.35
segundoTriLabs = ((segundoTriLab1 + segundoTriLab2 + segundoTriLab3) / 3) * 0.35
segundoTriProyectProm = segundoTriProyect * 0.3
segundoTriProm = segundoTriProyect + segundoTriNotas + segundoTriLabs

print(">>Tercer Trismestre")
print("Ingrese la nota del examen 1: ")
tercerTriExa1 = float(input("::"))
print("Ingrese la nota del examen 2: ")
tercerTriExa2 = float(input("::"))
print("Ingrese la nota del examen 3: ")
tercerTriExa3 = float(input("::"))
print("Ingrese la nota del laboratorio 1: ")
tercerTriLab1 = float(input("::"))
print("Ingrese la nota del laboratorio 2: ")
tercerTriLab2 = float(input("::"))
print("Ingrese la nota del laboratorio 3: ")
tercerTriLab3 = float(input("::"))
print("Ingrese la nota del proyecto trimestral: ")
tercerTriProyect = float(input("::"))

tercerTriNotas = ((tercerTriExa1 + tercerTriExa2 + tercerTriExa3) / 3) * 0.35
tercerTriLabs = ((tercerTriLab1 + tercerTriLab2 + tercerTriLab3) / 3) * 0.35
tercerTriProyectProm = tercerTriProyect * 0.3
tercerTriProm = tercerTriProyect + tercerTriNotas + tercerTriLabs
promedioTri1 = primerTriNotas + primerTriLabs + primerTriProyectProm
promedioTri2 = segundoTriNotas + segundoTriLabs + segundoTriProyectProm
promedioTri3 = tercerTriNotas + tercerTriLabs + tercerTriProyectProm
promedioFinal = (promedioTri1 + promedioTri2 + promedioTri3) / 3

#Impresion en pantalla
print("+---------------------------------------------------------------------------------------+")
print(f"|\t\t\t\tAlumno: {alumno}\t\t\t\t\t|")
print("+---------------------------------------------------------------------------------------+")
print("|\t\t\t\tPrimer Trimestre\t\t\t\t\t|")
print("+---------------------------------------------------------------------------------------+")
print("|\tNotas\t\t|\tN1\t|\tN2\t|\tN3\t|\t%\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tExamenes\t|\t{primerTriExa1}\t|\t{primerTriExa2}\t|\t{primerTriExa3}\t|\t{primerTriNotas}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tLaboratorios\t|\t{primerTriLab1}\t|\t{primerTriLab2}\t|\t{primerTriLab3}\t|\t{primerTriLabs}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tProyecto\t|\t\t\t{primerTriProyect}\t\t\t|\t{primerTriProyectProm}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\t\t\tPromedio Trimestral:\t\t\t\t|\t{promedioTri1}\t|")
print("+---------------------------------------------------------------------------------------+")
print("|\t\t\t\tSegundo Trimestre\t\t\t\t\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tExamenes\t|\t{segundoTriExa1}\t|\t{segundoTriExa2}\t|\t{segundoTriExa3}\t|\t{segundoTriNotas}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tLaboratorios\t|\t{segundoTriLab1}\t|\t{segundoTriLab2}\t|\t{segundoTriLab3}\t|\t{segundoTriLabs}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tProyecto\t|\t\t\t{segundoTriProyect}\t\t\t|\t{segundoTriProyectProm}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\t\t\tPromedio Trimestral:\t\t\t\t|\t{promedioTri2}\t|")
print("+---------------------------------------------------------------------------------------+")
print("|\t\t\t\tTercer Trimestre\t\t\t\t\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tExamenes\t|\t{tercerTriExa1}\t|\t{tercerTriExa2}\t|\t{tercerTriExa3}\t|\t{tercerTriNotas}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tLaboratorios\t|\t{tercerTriLab1}\t|\t{tercerTriLab2}\t|\t{tercerTriLab3}\t|\t{tercerTriLabs}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\tProyecto\t|\t\t\t{tercerTriProyect}\t\t\t|\t{tercerTriProyectProm}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\t\t\tPromedio Trimestral:\t\t\t\t|\t{promedioTri3}\t|")
print("+---------------------------------------------------------------------------------------+")
print(f"|\t\t\t\tPromedio Final:\t\t\t\t|\t{promedioFinal}\t|")
print("+---------------------------------------------------------------------------------------+")
os.system("pause")