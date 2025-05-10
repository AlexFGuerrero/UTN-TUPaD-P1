#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input( "¿Cuantos años tenes?\n"))

if(edad > 18):
    print("Es mayor de edad")
else:
    pass

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota = int(input("Ingrese su nota: \n"))
if(nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

par = int(input("Ingrese un número: \n"))
#par = par%2
while par % 2 != 0:
    print("Por favor, ingrese un número par")
    par = int(input("Ingrese un número: \n"))

print("Ha ingresado un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad1 = int(input("Ingrese su edad: \n"))
if (edad < 12):
    print("Usted es niño/a")
elif (edad >= 12 and edad < 18):
    print("Usted es adolecente")
elif (edad >= 18 and edad < 30):
    print("Usted es adulto/a joven")
else:
    print("Usted es mayor")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

pass1 = input("ingrese una contraseña: \n")
while not (8 <= len(pass1) <= 14):
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres\n")
    pass1 = input("ingrese una contraseña: \n")

print("Ha ingresado una contraseña correcta")