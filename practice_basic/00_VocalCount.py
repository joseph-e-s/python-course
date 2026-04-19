'''Crea un programa en Python que:
Pida al usuario una palabra o frase.
Cuente cuántas vocales tiene (a, e, i, o, u).
Muestre el total de vocales encontradas.'''

frase = input("Escribe tu palabra o frase: ")
contador = 0

for letra in frase:
    if letra.lower() in ["a", "e", "i", "o", "u"]:
        contador += 1     
    
print("Contiene", contador, "vocales.")
