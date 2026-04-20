# Listas
my_list = list('Hola') # Datos en lista (separa elementos) = list("hola") -> ['h', 'o', 'l', 'a'] -> 4 elementos
my_other_list = ["Hola"] # Meter un dato como un solo elemento ["hola"] -> ['hola'] -> 1 elemento
print(len(my_list))
print(len(my_other_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

# Podemos mezclar tipos de datos con []
my_other_list = [35, 1.77, "Brais", "Moure"] 
print(len(my_other_list))
# Con list() tambien pero de todas formas usamos [] entonces mejor no usarlo en estos casos
my_other_list = list([35, 1.77, "Brais", "Moure"]) 
print(len(my_other_list))

print(type(my_list))
print(type(my_other_list))


# Acceder a elemento concreto en una lista con []
my_other_list = list([35, 1.77, "Brais", "Moure"]) 
print(my_other_list[0]) # aqui accedemos al elemento en posicion 0 en la variable de my_other_list que seria 1.77
print(my_other_list[1])

print(my_other_list[-1]) # Con el - invertimos la lista de derecha a izquierda por lo que este daria el ultimo elemento
print(my_other_list[-4]) 

print(my_other_list.count("Brais")) # Nos dice cuantas veces aparece lo que le pasemos 

# print(my_other_list[4]) IndexError por que la posicion 4 no esta
# print(my_other_list[-5]) IndexError por que la posicion -5 no esta

print(my_other_list.index("Brais")) # Nos dice en qué posición está el elemento que le indiquemos dentro de la lista

# Aqui asiganmos nombres a las variables de my_other_list para poder accerder a ellas por medio de los mismos
# Se asignan por posicion por lo que age es el primero entonces se le asigna al primero de la lista que es 35 asi con todos
my_other_list = list([35, 1.77, "Brais", "Moure"]) 
age, height, name, surname = my_other_list
print(name)

# Podemos asiganrles su valor siendo nosotros los que indiquemos la posicion a cada uno, no es muy buena practica
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)


# Concatenación
one_list = list([1, 2, 3, 4])
second_list = list([5, 6, 7, 8])
print(one_list + second_list)


# Creación, inserción, actualización y eliminación
my_other_list = list([35, 1.77, "Brais", "Moure"])
my_other_list.append("MoureDev") # Agrega un nuevo elemento a la lista en la ultima posicion
print(my_other_list)

my_other_list.insert(1, "Rojo") # Agrega un nuevo elemento a la lista en la posicion que elijamos 
print(my_other_list)

my_other_list[1] = "Azul" # Reemplaza el elemento de la posicion indicada por el que le pasemos 
print(my_other_list)

my_other_list.remove("Azul") # Elimina el elemnto que le indiquemos de una lista (si hay dos elementos iguales solo quita el primero)
print(my_other_list)

# El pop por defecto elimina el ultimo elemento y nos lo indica por separado como se llamaba
# Perfecto para poder retornar el elemento eliminado 
print(my_other_list.pop()) 
print(my_other_list)
# Tambien podemos indicarle cual posicion quitar pero ya no nos dira por separado el que quito
my_pop_element = my_other_list.pop(2) # Creamos una variable para guardar los pop (elemento que quitamos) esto si queremos
print(my_pop_element) # lo debemos imprimir nosotros manualmente para ver el que se quito
print(my_other_list)

del my_other_list[2] # Aqui eliminas el objeto que indiquemos con la posicion sin mas
print(my_other_list)


# Operaciones con listas
my_list = [35, 24, 62, 52, 30, 30, 17]
my_new_list = my_list.copy() # Copiamos todo de my_list en my_new_list

my_list.clear() # Limpiamos por completo o eliminamos todos los elementos de my_list
print(my_list) # Queda vacia por el clear
print(my_new_list) # Queda con los objetos de my_list porque antes los copiamos 

my_new_list.reverse() # Da la inversa a la lista el ultimo es el primero y asi sucesivamente
print(my_new_list)

# Este ordena | Int de menor a mayor | Str orden alfabetico | Podemos darle parametros personalizados
my_new_list.sort()
print(my_new_list)

my_list = ["h", "o", "l", "a"]
result = "".join(my_list) # join(): une elementos de una lista en un solo string 
print(result)  # hola 


# Sublistas
print(my_new_list[1:3]) # Imprime los elementos de esas posiciones aqui seria el 1 y 2


# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))
