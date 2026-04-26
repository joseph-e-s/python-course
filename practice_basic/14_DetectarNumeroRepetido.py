
'''Ejercicio: Detector de número más repetido
Vas a hacer un programa que encuentre qué número se repite más en una lista que el usuario ingrese.
*Requisitos:
-Pedir números separados por espacio
-Convertirlos a lista de enteros
Encontrar:
-El número que más se repite'''

numeros_almacenados = []  

while True:
    numeros_usuario = input("Digite números separados por espacio (o 'fin'): ")

    if not numeros_usuario:
        print("Error: no se puede realizar la operacion sin numeros.\n")
        continue

    if numeros_usuario.lower().strip() == "fin":
        if len(numeros_almacenados) < 2:
            print("Error: necesitas al menos 2 números para calcular.\n")
            continue
        print("\nCalculando...")
        break

    numeros_lista = numeros_usuario.split()

    numeros_validos = []
    es_valida = True
    for num_str in numeros_lista:
        if not num_str.isdigit():
            print(f"Error: '{num_str}' no es un número válido.\n")
            es_valida = False
            break
        numeros_validos.append(int(num_str))

    if not es_valida:
        continue

    numeros_almacenados.extend(numeros_validos)
    print(f"Números guardados: {numeros_almacenados} (total: {len(numeros_almacenados)})\n")

    if len(numeros_almacenados) < 2:
        print("Sigue ingresando números (necesitas al menos 2).\n")


numero_ganador = 0
veces_ganador = 0

for num in numeros_almacenados:
    contador = 0

    for n in numeros_almacenados:
        if n == num:
            contador += 1

    if contador > veces_ganador:
        veces_ganador = contador
        numero_ganador = num

print(f"El que mas se repite es el {numero_ganador} se repite {veces_ganador} veces.\n")