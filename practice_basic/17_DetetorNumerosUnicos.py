
'''Ejercicio: Detector de números únicos
🔹Objetivo
Hacer un programa que:
-Pida números (uno por uno o varios, tú decides)
-Los guarde en una lista
-Cuando el usuario escriba fin:
-Muestre qué números NO se repiten
Y cuántos son'''

print("\n*Programa para encontrar numeros unicos*\n")
lista_numeros = []

while True:
    numero_usuario = input("Digite un numero o (fin) para salir y calcular: ")

    if not numero_usuario:
        print("Error: Digite un numero.\n")
        continue

    if numero_usuario.lower().strip() == "fin":
        if len(lista_numeros) < 2:
            print("Error: Deben haber 2 numeros al menos para calcular.\n")
            continue
        print("\nCalculando...\n")
        break

    if not numero_usuario.isdigit():
        print(f"Error: ({numero_usuario}) no es un numero valido.\n")
        continue

    lista_numeros.append(int(numero_usuario))

    print(f"Numeros guardados: {lista_numeros} (total: {len(lista_numeros)})")

    if len(lista_numeros) < 2:
        print("Sigue ingresando numeros, necesitas al menos dos.\n")

numeros_unicos = []
ya_contados = []

for numero in lista_numeros: 
    if numero in ya_contados:
        continue
    contador = 0

    for num in lista_numeros:  
        if num == numero:      
            contador += 1

    if contador == 1:         
        numeros_unicos.append(numero)

    ya_contados.append(numero)

cantidad_no_repiten = len(numeros_unicos)

if cantidad_no_repiten == 0:
    print("No hay numeros unicos, todos se repiten.\n")
else:
    print(f"Los numeros unicos son: {numeros_unicos}")
    print(f"Cantidad de numeros unicos: ({cantidad_no_repiten})")