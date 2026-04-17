
# Exception Handling 
numberOne = 1
numberTwo = "2"
# print(numberOne + numberTwo) Nos daria error al ejecutar

# Flujo completo de una excepción: try except else finally
# si hay try hay except no puede haber solo uno de los dos
try: # Seria: intenta esto y si funciona ejecuta tambien el else
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: # Si no funciona has esto y para aqui, no ejecuta el else
    print("Se ha producido un error")
else: # Opcional | Este se ejecuta si el try funciona
    print("La ejecucion contiuna correctamente")
finally:  # Opcional | Se ejecuta SIEMPRE, haya error o no.
    print("La ejecución continúa")


# Excepciones por tipo de errores 
try:
    age = int(input("Age: "))    # Me puede generar ValueError si pone un str en ves de un int
    result = 2 / age            # Me puede generar ZeroDivisionError si pone 0,-1,-2...
    print("No se ha producido un error")
    print(result)
except ValueError:  # Con este manejamos el ValueError especificamente
    print("Eso no es un número. Intenta otra vez.")
except ZeroDivisionError: # Con este manejamos ZeroDivisionError especificamente
    print("La edad no puede ser 0 o negativo.")


# Capturar el tipo de error "as nombre_variable" (Captura los datos de cuando la consola falla pero sin fallar)
try:
    age = int(input("Age: "))    # Me puede generar ValueError si pone un str en ves de un int
    result = 2 / age            # Me puede generar ZeroDivisionError si pone 0,-1,-2...
    print("No se ha producido un error")
    print(result)
except ValueError as error:  
    print(error)
    print("Eso no es un número. Intenta otra vez.")
except ZeroDivisionError as error: 
    print(error)
    print("La edad no puede ser 0 o negativo.")
    

