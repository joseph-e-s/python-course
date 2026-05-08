
'''Ejercicio: Detector de número más repetido
Vas a hacer un programa que encuentre qué número se repite más en una lista que el usuario ingrese.
*Requisitos:
1-Pedir números separados por espacio
2-Convertirlos a lista de enteros
3- Encontrar: El número que más se repite'''

numeros_almacenados = []  

while True:
    print("-" * 60)
    numeros_usuario = input("Ingrese un numero a la vez (o 'fin' para calcular y salir): ")

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
    print(f"Números guardados: {numeros_almacenados} (total: {len(numeros_almacenados)})")

    if len(numeros_almacenados) < 2:
        print("*Sigue ingresando números (necesitas al menos 2)*\n")


numero_mas_repetido = 0
veces_que_se_repite = 0
ya_contados = []

for num in numeros_almacenados:
    if num in ya_contados:
        continue
    contador = 0

    for n in numeros_almacenados:
        if n == num:
            contador += 1

    if contador > veces_que_se_repite:
        veces_que_se_repite = contador
        numero_mas_repetido = num

    ya_contados.append(num)

if veces_que_se_repite == 1:
    print("No hay números repetidos, todos aparecen una sola vez.\n")
else:
    print(f"El numero que mas se repite es el {numero_mas_repetido} este se repite {veces_que_se_repite} veces.\n")