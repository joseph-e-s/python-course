
'''Ejercicio: “Detector de contraseña decente”
Vas a hacer un programa que le pida al usuario una contraseña y le diga si es válida o no, según estas reglas:
Reglas:
1- La contraseña debe:
2- Tener al menos 8 caracteres
3- Tener al menos 1 número
4- Tener al menos 1 letra mayúscula
5- Tener al menos 1 carácter especial (como @, #, *, etc.)'''

print("\n*Validar una contrasena*")
print("-" * 25)

while True:
    contrasena_usuario = input("Ingrese su contraseña: ")

    if not contrasena_usuario.strip():
        print("Error: el campo no puede estar vacio\n")
        continue

    tiene_longitud = len(contrasena_usuario) >= 8
    tiene_numero = False
    tiene_mayuscula = False
    tiene_especial = False
    tiene_minuscula = False

    for letra in contrasena_usuario:
        if letra.isdigit():
            tiene_numero = True
        if letra.isupper():
            tiene_mayuscula = True
        if not letra.isalnum():  
            tiene_especial = True
        if letra.islower():
            tiene_minuscula = True

    if (tiene_longitud and tiene_numero and 
        tiene_mayuscula and tiene_minuscula and tiene_especial):
        print("\nCONTRASEÑA VÁLIDA\n")
        break

    if not tiene_longitud:
        print("- Debe tener al menos 8 caracteres")
    if not tiene_numero:
        print("- Debe tener al menos 1 número")
    if not tiene_mayuscula:
        print("- Debe tener al menos 1 letra mayúscula")
    if not tiene_minuscula:
        print("- Debe tener al menos 1 letra minúscula")
    if not tiene_especial:
        print("- Debe tener al menos 1 carácter especial (@, #, *, etc.)\n")


