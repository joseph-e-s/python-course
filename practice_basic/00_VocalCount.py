'''Crea un programa en Python que:
Pida al usuario una palabra o frase_usuario.
Cuente cuántas vocales tiene (a, e, i, o, u).
Muestre el total de vocales encontradas.'''

print("\n*Total de vocales en una frase*")
print("-" * 46)

while True:
    frase_usuario = input("Escribe tu palabra o frase o (fin) para salir: ")

    if frase_usuario.strip().lower() == "fin":
        print("\nSaliendo del Programa...\n")
        break

    if not frase_usuario.strip():
        print("Error: escribe una frase.\n")
        continue
    
    error = False  

    for letra in frase_usuario:
        if letra != " " and not letra.isalpha():
            print("Error: solo se admiten letras\n")
            error = True  
            break
    
    if not error: 
        print("\n- Analizando...")

        contador = 0

        for letra in frase_usuario:
            if letra.lower() in ["a", "e", "i", "o", "u"]:
                contador += 1 

        if contador == 0:
            print(f"La frase ({frase_usuario}) no contiene vocales.\n")
            print("-" * 46) 
        else:
            print(f"La frase ({frase_usuario}) tiene ({contador}) vocales en total.\n")
            print("-" * 46)

    else:
        continue




