
# Diccionarios
'''Estos son coleccionables de elementos con nombre y dato (clave y valor) | eje: "Nombre":"tote", 
ahi nombre es la clave y tote el valor de ella '''
my_dict = dict() # Se utiliza cuando cuando la clave NO es un numero o NO tiene comillas ("")
my_other_dict = {} # Se utiliza cuando cuando la clave es numero o tiene comillas ("")
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"} # 4 elementos
print(my_other_dict)

# Una misma clave puede tener varios valores como aqui Lenguajes que contiene 3, esto es un set dentro de una clave
my_dict = {
    "Nombre": "Brais", 
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
} # 5 elementos (Recordar que uno de ellos tiene 3 valores en total son 5 claves)
print(my_dict)

print(len(my_other_dict)) # Corroboramos que son 4elementos
print(len(my_dict)) # Corroboramos que son 5 elementos


# Búsqueda | Accede por clave 
print(my_dict[1])
print(my_dict["Nombre"]) 
# Existe esta clave | Nos devuelve un boolean
print("Moure" in my_dict) # false porque a pesar de que esta, es un valor no clave y preguntamos por clave
print("Apellido" in my_dict) # true porque si esta y accedimos por clave

# Insertar nueva clave con elemento al diccionario
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualizar clave con un nuevo valor (reemplaza el anterior)
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminar clave junto a su valor (No son recuperables)
del my_dict["Calle"]
print(my_dict)


# Otras operaciones
print(my_dict.items()) # Nos da un listado de los items que hay, clave y valor
print(my_dict.keys()) # Nos da un listado de las claves nada mas, sin sus valores
print(my_dict.values()) # Nos da un listado de los valores nada mas, sin su claves

''' dict.fromkeys() convierte un coleccionable o elementos especificos que le demos en un diccionario 
con claves sin valor, Luego podemos asiganrles valor es otro tema'''
my_list = ["Nombre", 1, "Piso"]
# Los elementos de my_list serian un diccionario con las claves vacias
my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict)
# Especificamos que elementos quiero que sean un diccionario con claves vacias
my_new_dict = dict.fromkeys(("Altura", 2, "Peso")) 
print((my_new_dict))
# Aqui pasamos un diccionario que ya tenia claves con valores a otro con las mismas claves pero sin valores (Reset de valores)
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
# Obligamos a que todas las claves del my_dict tengan de valor el elemento que le pasemos aqui seria MoureDev
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

#Podemos convertir un diccionario a los otros tipos de coleccionables | Solo agarrarian las claves
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
