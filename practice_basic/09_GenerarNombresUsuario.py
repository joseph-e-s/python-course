
'''Ejercicio: Generador de nombres de usuario
Vas a hacer un programa que cree usernames automáticos según datos del usuario.
*Requisitos:
Pedir:
-Nombre
-Apellido
-Año de nacimiento
Generar un username con esta lógica:
-Primeras 3 letras del nombre
-Primeras 3 letras del apellido
-Últimos 2 dígitos del año'''

while True:
    username = ""

    nombre = input("Ingrese primer nombre: ").lower()
    apellido = input("Ingrese su primer apellido: ").lower()
    ano_nacimiento = input("Ingrese el año en el que nacio: ")

    if not ano_nacimiento.isnumeric():
        print("Error: el año debe ser un número\n")
        continue

    for elemento in nombre[0:3]:
        username += elemento

    for elemento in apellido[0:3]:
        username += elemento

    for elemento in ano_nacimiento[2:4]:
        username += elemento
    
    print("Tu nuevo usuario es: ", username, '\n')