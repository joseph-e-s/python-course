
# Variables

my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 20
print(my_int_variable)

my_float_variable = 20.5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)


"""Con esto logramos convertir una variable tipo 
int en tipo str aunque siga imprimiendo el 20 
este ahora es tipo str"""
my_int_to_str_variable = str(my_int_variable) # Aqui decimos que el int cambie a str y se llame (my_int_to_str_variable)
print(my_int_to_str_variable) # Al imprimir vemos que sigue dando el numero 20 a pesar de que ahora es tipo str
print(type(my_int_to_str_variable)) 
"""Aqui comprobamos que efectivamente ahora es tipo str con type y muy importante
ya no sirve como numero, osea, no se pueden hacer operaciones con el por que se considera str no int"""

 
# Aqui combinamos para imprimir variables a esto se le llama 'concatenacion de variables'
print(my_string_variable, my_int_to_str_variable, my_bool_variable) # concatenamos variables
print("Este es el valor de: ", my_int_variable) # O tambien concatenamos un str con una variable

#Funcion 'len'
#Esta cuenta la cantidad de caracteres de la variable que le demos (incluye o cuenta espacios)
print(len(my_string_variable))
#No puede contar de tipo numericos eje: 200 -> no daria 3 -> 2-0-0 | porque es numerico

# Distintas Variables en una linea (no es muy buena practica)
name, surname, alias, age = "Joseph", "Elizondo", "Tote", 22
print(name, surname, alias, age)
#Podemos imprimirlas en distinto orden o mezclar str entre ellas
print("Me llamo ", name, surname, "mi apodo es ", alias, "y tengo ", age, "años")
# O usarlas por separado
print(name)

# Input: pide el dato al usuario para usarlo en darle valor a esa variable
first_name = input("Whats your name?: ") #str
date_birthday = input("when is your birthday?: ") #int
print(first_name)
print(date_birthday)