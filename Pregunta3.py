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

suma= edades[0]+edades[1]+edades[2]+edades[3]+edades[4]/5

print("El rpomedio de las edades es de ", suma)
print(nombres,sex,edades)