
'''Ejercicio: Validador de palíndromos
Un palíndromo es una palabra o frase que se lee igual al derecho y al revés.
Ejemplo: “reconocer” | “anita lava la tina”
*Requisitos:
-Pedir una frase al usuario
Ignorar:
-Espacios
-Mayúsculas/minúsculas
-Determinar si es palíndromo o no'''



print("*Programa para detectar palindromos*")

while True:
    frase = input("Escriba su frase o (fin) para salir: ")
    
    if not frase:
        print("Error: Digite una palabra o frase\n")
        continue  

    if frase.lower() == 'fin':
        print("Saliendo del programa...\n")
        break
    
    es_valida = True

    for letra in frase:
        if letra != " " and not letra.isalpha():
            print("Error: solo se admiten letras\n")
            es_valida = False
            break  

    if not es_valida:
        continue

    frase_limpia = ''.join(frase.split()).lower()

    palindromo = ""
    
    for letra in frase_limpia:
        palindromo = letra + palindromo

    if palindromo == frase_limpia:
        print(f"La frase ('{frase}') si es palindromo = ('{palindromo}')\n")
    else: 
        print(f"La frase ('{frase}') no es palindromo = ('{palindromo}')\n")






