
#Operadores Aritméticos con enteros 
print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicacion
print(10 / 3) # Division exacta, incluye decimas
print(10 // 3) # Division pero aproximandose siempre al numero entero mas cercano, evitamos las decimas

'''Devuleve el residuo de una divion | ideal para saber si un numero es multiplo o no
en este caso 10 entre 3 es 9 es decir nos sobra 1 por lo que ese 1 sera el resultado'''
print(10 % 3) 

#Aqui calculamos exponentes en este caso 2 elevado a 3 (es lo mismo que decir 2x2x2 =8)
print(2 ** 3) 

#Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?") #Es como usar la coma 

'''Solo se pueden operar datos del mismo tipo -> str con str o int con int o etc...
por ende si queremos operar un str con un int debemos convertir uno al tipo del otro como en este ejemplo'''
print("Hola " + str(5)) # Covertimos el int en str y asi quedan una operacion de dos str valida

print("Hola " * 5) # Le decimos que aprezca 5 veces el hola, tambien valido


my_float = 2.5 * 2 # Aqui hacemos un operacion que nos da de resultado 5.0 el cual es float
print("Hola " * int(my_float)) # no podemos operar con floats por lo que lo convertimos a int y alli si deja 
# Importante si el float no es exacto como 5.0 si no que es 5.2 o 5.8 al cambiarlo a int queda en 5 osea a su original


#Operadores Comparativas con enteros 
print(3 > 4) # Mayor que
print(3 < 4) # Menor que
print(3 >= 4) # Mayor o igual que
print(4 <= 4) # Menor o igual que
print(3 == 4) # Igual que
print(3 != 4) # Diferente que
# Estos daran como resultado un boolean (true o false) 


# Operaciones con cadenas de texto. Compara en orden alfabetico 
'''Compara la letra inicial de cada palabra y ahi decide cual es mayor o menor en orden alfabetico, aunque si todo 
es igual pero una palabra es más corta como: hola - holanda | entonces la mas corta es menor y la larga es mayor
Si son exactamente iguales: no es ni mayor ni menor, son iguales
*Importante* Las mayúsculas son “menores” que las minúsculas'''
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
print(len("aaaa") >= len("abaa")) # El len() compara por cantidad caracteres en cada palabra no por lo anterior


# Operadores Lógicos 
print(3 > 4 and "Hola" > "Python") # Es una condicion, se deben cumplir ambos para el true
print(3 > 4 or "Hola" > "Python") # Aqui hay dos opciones, si se cumple A o se cumple B es true
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # Aqui conbinamos ambas y siguen con la misma logica
# not() niega la condicion, aqui 3 es mayor que 4? NO -> false, pero al not negar eso el resultado da true
print(not (3 > 4))  