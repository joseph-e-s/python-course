
'''Ejercicio: Analizador de texto básico
Vas a hacer un programa que analice una frase que el usuario escriba.
*Requisitos:
Pedir una frase al usuario
-Mostrar:
-Cantidad total de caracteres (sin contar espacios)
-Cantidad de palabras
-Cuántas veces aparece una letra específica (que el usuario elija)'''

while True:
    frase = input("Escriba su frase: ").lower()
        
    if not frase:
        print("Error: La frase no puede estar vacía\n")
        continue

    error = False  

    for letra in frase:
        if letra != " " and not letra.isalpha():
            print("Error: solo se admiten letras\n")
            error = True  
            break  
    
    if not error: 
        break

cantidad_caracteres = 0

while True:
    letra_especifica = input("Que letra desea ver cuantas veces se repite en la frase: ").lower()
        
    if not letra_especifica:
        print("Error: La letra no puede estar vacía\n")
        continue

    if len(letra_especifica) != 1:
        print("Error: solo puede ingresar una letra\n")
        continue

    error = False  

    for letra in letra_especifica:
        if letra != " " and not letra.isalpha():
            print("Error: solo se admiten letras\n")
            error = True  
            break  
    
    if not error: 
        break


cantidad_letra = 0

for letra in frase:
    if letra != " ":
        cantidad_caracteres += 1
print(f"\nCantidad de caracteres: {cantidad_caracteres}")

cantidad_palabras = len(frase.split())
print(f"Cantidad de palabras: {cantidad_palabras}")

for letra in frase:
    if letra != " " and letra_especifica == letra:
        cantidad_letra += 1
print(f"La letra escogida fue ({letra_especifica}) y aparece {cantidad_letra} veces\n")
    