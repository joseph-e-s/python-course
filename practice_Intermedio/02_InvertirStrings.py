
'''
INVIRTIENDO CADENAS
Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloh'''

def invertir_frase(texto):
    invertida = ""
    
    for i in range (len(texto) - 1,-1,-1):
        invertida += texto[i]
        
    return invertida

frase = (invertir_frase("Hola mundo"))
print(frase)
