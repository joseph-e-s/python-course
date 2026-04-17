
# Loops
# While -> "Mientras" sea verdadero, has tal cosa
'''Aqui vemos como my_condition vale 0 como es menor a 10 hace print a my_condition
y luego le suma 1 por lo que en la siguiente ya no vale 0 sino 1, de igual forma es menor a 10
y hace print a my_condition y le vuelve a sumar 1 por lo que en la siguiente ya no vale 1 sino 2
y asi se ira hasta que llegue a 9, la condicion es que sea menor a 10 por eso para alli e imprime el else '''
my_condition = 0
while my_condition < 10: # Dice: mientras my_condition sea menor a 10 
    print(my_condition) # printea my_condition
    my_condition += 1 # y sumale 1 a my_condition
else:  # Si no...
    print("Hasta aqui es menor a 10") # Imprime esto

# Podemos combinar 
my_condition = 0 
while my_condition < 20: # En teoria se ejecuta hasta 19 el cual es meonor a 20
    my_condition += 1 # Vamos sumando de uno en uno
    if my_condition == 15: # Pero con el if decimos que al llegar a 15 haga print y pare, con el break
        print("Se detiene la ejecución")
        break # Detiene el bucle alli
    print(my_condition) # Entonces  mostramos que my_condition quedo en 14



# Ejemplo del while infinito hasta que den el tipo de dato que requerimos
print("Programa para pedir nombre\n")
while True: # Este bucle se repite "para siempre" hasta que yo le diga que pare porque es true
    nombre = input("Por favor ingresa tu nombre: ")
    if nombre.isalpha(): # isalpha() da True si son letras por lo que no admitira otro dato (evitamos errores)
        print(f"¡Perfecto! Bienvenido, {nombre}")
        break # ← Aquí salimos del bucle porque todo está bien nos dio true entonces para
    else: # Sino significa que no nos dio true ya ingreso un dato que no es letra da false osea se repite todo hasta que lo de bien
        print("Error: Solo se permiten letras. No uses números ni símbolos.")
        print("Inténtalo de nuevo.\n")



# For -> "Por cada" lo que sea, has tal cosa
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list: # Por cada lemento en mi lista imprime el elemento
    print(element)
    
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for element in my_tuple: # Por cada elemento en mi tupla imprime el elemento
    print(element)

my_set = {"Brais", "Moure", 35}
for element in my_set: # Por cada elemento en mi set imprime el elemento (lo da desordenado por el set)
    print(element)
    
# En el dict es lo mismo
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
for element in my_dict: # Por cada elemento en mi dict imprime el elemento
    print(element)
    
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
for valor in my_dict.values(): # Por cada elemento en mi dict imprime su valor
    print(valor)
    
    
# Podemos usar el break
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
for element in my_dict: # Por cada lemento en mi dict imprime el elemento
    print(element)
    if element == "Edad": # Si el elemento es edad para ahi | Cuando llegue a edad hara el break no hara mas vueltas
        break
else:
    print("El bucle for para el diccionario ha finalizado")


# continue salta el resto de la vuelta en la que esta y pasa a la siguiente iteración"                        
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
for element in my_dict: # Por cada elemento en mi dict imprime el elemento
    print(element)
    if element == "Edad": # Si el elemento es edad continua osea a todos les da el print de "se ejecuta" menos a edad
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
''' 
El bucle recorre cada clave del diccionario.
- Siempre imprime la clave (primer print).
- Si la clave es "Edad", ejecuta continue, osea: 
  salta el resto del código de esta iteración que seria (el print("Se ejecuta")) 
  y pasa directamente a la siguiente clave.
- Por eso "Edad" solo muestra su nombre, pero no muestra "Se ejecuta".
- Las demás claves (Nombre, Apellido y 1) sí muestran los dos prints.
Como decir una excepcion: A todos los elementos aplícales este código (ambos prints)
excepto a este (edad), a este sáltalo y pasa al siguiente
'''
   