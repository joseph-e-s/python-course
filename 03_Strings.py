#Strings
my_string = "Mi String"
my_other_string = 'Mi otro String'
print(my_string + " " + my_other_string)

# recordar que len() dice la cantidad caracteres de el str 
print(len(my_string))
print(len(my_other_string))


# \n realiza un salto de linea justo cuando el aparece
my_fisrt_line_string = "Este es un String\ncon salto de línea en medio"
print(my_fisrt_line_string)
my_second_line_string = "Este es un String con salto de línea al final\n"
print(my_second_line_string)
my_third_line_string = "\nEste es un String con salto de línea al inicio"
print(my_third_line_string)

# Podemos evitarlo y quedarnos en la misma linea con varios prints gracias a (end=" ")
print("Hola")
print("mundo") # Imprime el "Hola" y "Mundo" en distintas lineas, ya que son dos prints
#Escribimos end=" " para que no baje a la línea de abajo, sino que deje un espacio y continue
print("Hola", end=" ")
print("mundo")  # Imprime: Hola mundo

# \t hace una tabulacion a la linea osea la adelanta un poco
my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# Mezclados
''' Hace ambos pero el que se pone primero se ve interrumpido por el segundo 
por o que aqui hara tabulacion hasta la \n y apartir de alli solo hara el salto de linea sin la tabulacion'''
my_mix_tab_line_string = "\tEste es un String\ncon tabulacion y el salto de linea al final"
print(my_mix_tab_line_string)



# Formateo
'''Aqui el 'f' covierte todo en string dentro del print para que pueda imprimirse 
pero fuera de el sigue siendo un int no lo cambia para siempre solo ahi
Escribir str mezclando int, float, logica o algun otro tipo siempre sera mejor
con el uso del 'f' evita errores, bugs y es mejor interpretado''' 
#Ejemplo:
name, surname, age = "Brais", "Moure", 35
print(f"Mi nombre es {name} {surname} y mi edad es {age}") 
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Este sirve pero es mala practica!


# Desempaqueado de caracteres
'''Aqui lo que hacemos es que asiganamos una variable a cada letra del contenido en este caso Python
asi podemos imprimir la letra que queramos'''
palabra = "python"
a, b, c, d, e, f = palabra
print(a)
print(e)
print(f+e+d+c+b+a) # Podemos imprimir la palabra al reves


# División
'''Aqui extraemos los caracteres por posicion, se empieza desde 0 y el ultimo numero no se imprime, osea:
si en la palabra "Ingles" usamos [1:3] la separa por caracteres y posicion, asi (I-0, N-1, G-2, L-3, E-4, S-5)
siempre inicia desde la primer posicion que es 0 y la ultima que en este caso es 5
como aqui le decimos que imprima [1:3] se imprime "ng" de la palabra "Ingles". Como dato extra importante
no imprimira la posicion 3 ya que es la ultima en el parametro que le dimos sino que imprimira hasta la 2,
de 1 a 3 imprime 1 y 2 y asi con cualquier otro parametro que le demos aqui'''
#Ejemplo:
language = "Ingles"
language_slice = language[1:3]
print(language_slice)

#Aqui es lo mismo pero como no le pasamos un final al parametro imprime desde la posicion 1 hasta que acabe la palabra
language_slice = language[1:]
print(language_slice)

'''Con signo negativo (-) hacemos que la posición se cuente al revés, o sea, 
desde el final de la palabra hacia la izquierda. 
Aquí no es que no exista la posición 0, sino que simplemente empezamos desde -1, que sería la última letra.
Por ejemplo, en la palabra "Ingles", si usamos [-2] nos va a dar el carácter 'e' 
porque es la segunda letra contando desde el final.
En este caso usamos solo una posición, no un rango, por eso no devuelve toda la palabra ni una parte larga 
sino únicamente ese carácter específico. '''
language_slice = language[-2]
print(language_slice)

'''Aqui extraemos los caracteres usando un rango con salto, donde se empieza desde la posicion 0,
se llega hasta la 6 (sin incluirla) y el 2 indica que va agarrando de dos en dos, osea, uno si y uno no.
Si usas 3, entonces avanza 3 posiciones cada vez. O sea: agarra uno y se salta dos 
sucesivamente y asi con cualquier otro parámetro de este tipo'''
language_slice = language[0:6:2]
print(language_slice)

# Para darle la vuelta osea escribir al reves la palabra entera usamo [::-1] 
# Recuerda el final al reves empieza por -1 ya que no existe el -0 solo el 0
reversed_language = language[::-1]
print(reversed_language)


# Funciones del lenguaje
print(language.capitalize()) # Hace que la primer palabra de una cadena de str empiece en mayuscula
print(language.upper()) # Convierte todas las palabras o letras de una cadena de str en mayuscula
print(language.lower())# Convierte todas las palabras o letras de una cadena de str en minusculas
print(language.count("t")) # recorre todo el str contando cuántas veces aparece ese carácter (t != T)
print(language.isnumeric()) # imprime un boolean, dice si es un numero o no 
print(language.isupper()) # imprime un boolean, dice si todas las letras de un str son mayusculas
print(language.startswith("In")) # imprime un boolean, nos dice si la variable empieza con... osea lo que le digamos
print("In" == "in")  # No es lo mismo
