
''' Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama
 Palabras: Cara - arca. |   Seto - esto.'''
 

def es_anagrama(palabra1: str, palabra2: str):
    if palabra1 == palabra2:
        return False

    return sorted(palabra1) == sorted(palabra2)


print(es_anagrama("roma", "amor"))  # True
print(es_anagrama("cara", "casa"))  # False
print(es_anagrama("hola", "hola"))  # False




