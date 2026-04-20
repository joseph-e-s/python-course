

'''Haz un programa que:
Reglas:
Pida un número al usuario
Determine si es primo o no
Muestre el resultado

Un número primo:
Solo se dividen  entre 1 y ellos mismos, su division es exacta no sobra nada'''


while True:
    try:
        num_usuario = int(input("Ingrese el numero para determinar si es primo o no: "))
        break
    except ValueError:
        print("Solo se admiten numeros, intentelo de nuevo\n")
        

if num_usuario <= 1:
    print("Es un numero no primo") 
else:
    primo = True
    
    for numero in range(2, num_usuario):
        if num_usuario % numero == 0:
            primo = False
            break
    
    if primo == True:
        print("Es un numero primo")
    else:
        print("Es un numero no primo") 
    