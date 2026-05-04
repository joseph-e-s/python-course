
'''Haz un programa que:
1- Pida un número al usuario
2- Muestre la tabla de multiplicar de ese número del 1 al 10'''


while True:
    print("-" * 75)
    num_usuario = input("Digite un numero para ver su tabla de multiplicar o (fin) para salir: ").strip()

    if not num_usuario:
        print("Error: solo se permiten numeros o 'fin'.\n")
        continue

    if num_usuario.lower() == "fin":
        print("\nSaliendo...\n")
        break
    
    try:
        num_usuario = int(num_usuario)
    except ValueError:
        print("Error: solo se permiten numeros o 'fin'.\n")
        continue

    for num_multiplicador in range(1, 11):
        resultado = num_usuario * num_multiplicador
        print(num_usuario, "x", num_multiplicador, "=", resultado)

