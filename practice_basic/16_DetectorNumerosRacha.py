
'''Ejercicio: Detector de racha más larga
El usuario mete números separados por espacio y tú debes:
Encontrar la racha más larga de números consecutivos iguales
-Ejemplo:
# Entrada
1 1 1 2 2 3 3 3 3 1
# Salida:
La racha más larga es de 4 con el número 3'''


lista_numeros = []

while True:
    numeros_usuario = input("Ingrese un numero a la vez (o 'fin' para calcular y salir): ").strip()

    if not numeros_usuario:
        print("Error: no se puede dejar vacío.\n")
        continue

    if numeros_usuario.lower() == "fin":
        if len(lista_numeros) < 2:
            print("Error: necesitas al menos 2 números para calcular una racha.\n")
            continue
        print("\nCalculando racha...\n")
        break

    if not numeros_usuario.isdigit():
        print(f"Error: '{numeros_usuario}' no es un número válido.\n")
        continue

    lista_numeros.append(int(numeros_usuario))

    print(f"Números guardados: {lista_numeros} (total: {len(lista_numeros)})")

    if len(lista_numeros) < 2:
        print("*Sigue ingresando números (necesitas al menos 2)*\n")


mayor_racha = 1
racha_actual = 1
numero_racha = lista_numeros[0]

for i in range(1, len(lista_numeros)):
    if lista_numeros[i] == lista_numeros[i - 1]:
        racha_actual += 1
    else:
        racha_actual = 1

    if racha_actual > mayor_racha:
        mayor_racha = racha_actual
        numero_racha = lista_numeros[i]
    
if mayor_racha == 1:
    print("No hay repeticiones consecutivas (no existe racha).\n")
else:
    print(f"La racha más larga es de {mayor_racha} apariciones consecutivas por el número {numero_racha}\n")