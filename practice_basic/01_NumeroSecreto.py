
'''Haz un programa que:
1- Genere un número aleatorio entre 1 y 10
2- Le pida al usuario que adivine el número
3- Que le diga diga si: Es muy alto, si es muy bajo o si le atino 
4- Se repita hasta que adivine'''

num_secreto = 38
intentos = 0

while True:
    try:
        num_usuario = int(input("Adivina el numero secreto entre 0-100: "))
        
        if num_usuario < 0 or num_usuario > 100:
            print("El número debe estar entre 0 y 100\n")
            continue
        
        intentos += 1
        if num_usuario > num_secreto:
            print("Ese numero es alto, digita uno mas bajo")
            print("Llevas", intentos, "intentos\n")
        elif num_usuario < num_secreto:
            print("Ese numero es bajo, digita uno mas alto")
            print("Llevas", intentos, "intentos\n")
        else: 
            print("\nFelicidades lo has adivinado era el", num_secreto,)
            print("Lo hiciste en", intentos, "intentos\n")
            break
    except ValueError: 
            print("Solo se pueden digitar numeros\n")

            
            