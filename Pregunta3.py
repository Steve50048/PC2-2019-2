import os
os.system("cls")

nombres=[]
sex=[]
edades=[]

nombre = input("Escriba su nombre: ")
nombres.append(nombre)
sexo = input("Escriba su sexo entre (Hombre o Mujer): ").lower()
while sexo !="hombre" and sexo != "mujer":
    print("Dato invalido")
    sexo = input("Escriba su sexo: ")
sex.append(sexo)
edad = int(input("Escriba su edad: "))
while edad >= 18 or edad <= 4 :
    print("Dato no valido")
    edad = int(input("Escriba su edad: "))
edades.append(edad)


print(nombres,sex,edades)