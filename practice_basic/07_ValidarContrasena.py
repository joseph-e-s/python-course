
'''Ejercicio: “Detector de contraseña decente”
Vas a hacer un programa que le pida al usuario una contraseña y le diga si es válida o no, según estas reglas:

Reglas:
La contraseña debe:
Tener al menos 8 caracteres
Tener al menos 1 número
Tener al menos 1 letra mayúscula
Tener al menos 1 carácter especial (como @, #, *, etc.)'''


contrasena_usuario = input("Ingrese su contraseña: ")


tiene_longitud = False
tiene_numero = False
tiene_mayuscula = False
tiene_especial = False


if len(contrasena_usuario) >= 8:
    tiene_longitud = True


for letra in contrasena_usuario:
    if letra.isdigit():
        tiene_numero = True
    elif letra.isupper():
        tiene_mayuscula = True
    elif not letra.isalnum():  
        tiene_especial = True


if tiene_longitud and tiene_numero and tiene_mayuscula and tiene_especial:
    print("CONTRASEÑA VÁLIDA")
else:
    print("CONTRASEÑA INVÁLIDA")
    

if not tiene_longitud:
    print("- Debe tener al menos 8 caracteres")
if not tiene_numero:
    print("- Debe tener al menos 1 número")
if not tiene_mayuscula:
    print("- Debe tener al menos 1 letra mayúscula")
if not tiene_especial:
    print("- Debe tener al menos 1 carácter especial (@, #, *, etc.)")


