'''
INVIRTIENDO CADENAS
Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones 
propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloh'''


def invertir_frase(texto):
    invertida = ""

    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]

    return invertida


if __name__ == '__main__':
    print("Invertir frases. Escribe una frase y se mostrará al revés.")
    print("Para salir escribe q, quit o salir.\n")

    while True:
        try:
            frase = input("Frase (q para salir): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nOperación cancelada.")
            break

        if frase.lower() in ('q', 'quit', 'salir'):
            print("Hasta luego.")
            break

        if not frase:
            print("Error: la frase no puede estar vacía.")
            continue

        print(invertir_frase(frase))
