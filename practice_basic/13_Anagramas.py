
'''Ejercicio: Detector de Anagramas
Vas a hacer un programa que diga si dos palabras o frases son anagramas.
Un anagrama es cuando dos palabras o frases tienen exactamente las mismas letras, pero ordenadas diferente.
*Requisitos:
-Pedir dos palabras o frases
Ignorar:
-Espacios
-Mayúsculas/minúsculas
-Determinar si son anagramas 
Ejemplo fácil: amor → roma \ listen → silent \ raton → antro'''

print("\n*Programa para detectar anagramas*")

while True:
    frase_del_usuario = input("Escriba dos palabras o frases y (fin) para ver el resultado: ")

    if not frase_del_usuario:
        print("Error: Digite dos palabras o frases\n")
        continue

    if frase_del_usuario.lower() == "fin":
        print("\nSaliendo...")
        break

    es_valida = True    
    for letra in frase_del_usuario:
        if letra != " " and not letra.isalpha():
            print("Error: solo se admiten letras\n")
            es_valida = False
            break           

    if not es_valida:
        continue  

    comparacion = frase_del_usuario.split()

    if len(comparacion) != 2:
        print("Error: debe ingresar exactamente dos palabras\n")
        continue

    palabra1 = comparacion[0].lower()
    palabra2 = comparacion[1].lower()

    if len(palabra1) != len(palabra2):
        print(f"No son anagramas (distinta longitud)\n")
        continue

    es_anagrama = True

    for letra in palabra1:
        contador_uno = 0
        contador_dos = 0

        for l in palabra1:
            if l == letra:
                contador_uno += 1

        for l in palabra2:
            if l == letra:
                contador_dos += 1

        if contador_uno != contador_dos:
            es_anagrama = False
            break

    if es_anagrama:
        print(f"Las palabras {comparacion[0]} y {comparacion[1]} si son anagramas, tienen las mismas letras y longitud.\n")
    else:
        print(f"Las palabras {comparacion[0]} y {comparacion[1]} no son anagramas, tienen distintas letras.\n")
            









