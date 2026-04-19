
'''Haz un programa que:
Pida un número al usuario
Muestre la tabla de multiplicar de ese número del 1 al 10'''

    
num_multiplicador = 1

while True:
    try:
        num_usuario = int(input("Digite un numero para ver su tabla de multiplicar: "))
        break
    except ValueError:
        print("Solo se admiten numeros, intentalo de nuevo.\n")
        
while num_multiplicador <= 10:
    resultado_multiplicacion = num_usuario * num_multiplicador
    print(num_usuario, "x", num_multiplicador, "=", resultado_multiplicacion)
    num_multiplicador += 1  

