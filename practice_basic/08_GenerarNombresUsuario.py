
'''Ejercicio: Generador de nombres de usuario
Vas a hacer un programa que cree usernames automáticos según datos del usuario.
*Requisitos:
Pedir:
1- Nombre, Apellido y Año de nacimiento
2- Generar un username con esta lógica:
-Primeras 3 letras del nombre
-Primeras 3 letras del apellido
-Últimos 2 dígitos del año'''

print("\n*Creador de nombres de usuario*")
print("-" * 30)

while True:
    nombre = input("Ingrese primer nombre: ").strip().lower()
    if not nombre.isalpha():
        print("Error: ingrese un nombre valido\n")
        continue

    while True:
        apellido = input("Ingrese su primer apellido: ").strip().lower()

        if not apellido.isalpha():
            print("Error: ingrese un apellido valido\n")
            continue

        break

    while True:
        ano_nacimiento = input("Ingrese su año de nacimiento: ")

        if not ano_nacimiento.isnumeric():
            print("Error: ingrese una edad valida\n")
            continue

        ano = int(ano_nacimiento)

        if ano < 1900 or ano > 2026:
            print("Error: ingrese una edad valida\n")
            continue

        break

    username = nombre[:3] + apellido[:3] + ano_nacimiento[2:]

    print("-" * 50)
    print(f"Tu nuevo usuario es: {username} \n")