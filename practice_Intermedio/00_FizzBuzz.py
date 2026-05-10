'''
 EL FAMOSO "FIZZ BUZZ"
 1- Escribe un programa que pida al usuario un rango.
(ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
  -Múltiplos de 3 por la palabra "fizz".
  -Múltiplos de 5 por la palabra "buzz".
  -Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def multiplos(i):
  if i % 3 == 0 and i % 5 == 0:
    return "FizzBuzz"
  elif i % 3 == 0:
    return "Fizz"
  elif i % 5 == 0:
    return "Buzz"
  else:
    return str(i)


def pedir_entero(mensaje):
  while True:
    try:
      texto = input(mensaje).strip()
      if texto == "":
        print("Error: no puede estar vacío. Introduce un número entero.\n")
        continue
      return int(texto)
    except ValueError:
      print("Error: debe ser un número entero válido (ej.: 1, -5, 100).\n")


def pedir_rango():
  while True:
    inicio = pedir_entero("Inicio del rango (incluido): ")
    fin = pedir_entero("Fin del rango (incluido): ")
    if inicio > fin:
      print("Error: el inicio no puede ser mayor que el fin. Inténtalo de nuevo.\n")
      continue
    return inicio, fin


def main():
  try:
    inicio, fin = pedir_rango()
  except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario.\n")
    return

  for i in range(inicio, fin + 1):
    print(multiplos(i))


if __name__ == "__main__":
  main()
