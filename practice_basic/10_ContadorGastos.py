
'''Contador de gastos del día
Vas a hacer un programa donde el usuario va metiendo gastos y al final le dices cuánto gastó.
*Requisitos:
1-Pedir gastos uno por uno (números)
2-El usuario puede escribir "fin" para terminar
Mostrar:
-Total gastado
-Cantidad de gastos ingresados
-Promedio de gasto'''

print("\n*Contador de gastos diarios*")
print("-" * 50)


lista_gastos = []

while True:
    gastos = input("Ingrese un gasto (o digite fin para salir): ").strip()

    if gastos.lower() == "fin":
        print("Saliendo...\n")
        break

    try:
        gastos = int(gastos)
        if gastos <= 0:
            print("Error: no se pueden digitar numeros sin valor o negativos\n")
            continue
        lista_gastos.append(gastos)
    except ValueError:
        print("Error: ingrese un número válido o 'fin'\n")
        continue


total = sum(lista_gastos)

print("Lista de gastos:", lista_gastos)
print("Total gastado:", total)

elementos_en_lista = len(lista_gastos)

if elementos_en_lista > 0:
    promedio = total / elementos_en_lista
    print("El promedio es:", promedio)
else:
    print("Error: no hay gastos para obtener el promedio")


