
# Tuples 
my_tuple = tuple() # Datos de tuple (separa elementos) = tuple("hola") -> ['h', 'o', 'l', 'a'] -> 4 elementos
my_other_tuple = () # Meter un dato como un solo elemento ["hola", ] -> ['hola', ] -> 1 elemento (siempre poner coma al final)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))


# Acceso a elementos y búsqueda
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
'''Como vemos hasta aqui todo es igual que una lista solo que a diferencia de ellas los tuples no son dinamicos
son datos que no cambian por eso no tienen tantas operaciones, es estatico.
Y a nivel de sistema es mas rapida y usa menos memoria que una lista por la misma razon de antes'''


# Concatenación de tuples
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


# Subtuplas
print(my_sum_tuple[3:6]) # Imprime los elementos de esas posiciones aqui seria el 3, 4 y 5


# Tupla mutable con conversión a lista
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_tuple = list(my_tuple) # Aqui convertimos un tuple a lista y ya nos permite usar operaciones de lista
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple) # Una vez echo los cambios la volvemos a converitr en tuple
print(my_tuple)
print(type(my_tuple))

# Eliminación
# del my_tuple[2] -> No se puede borrar un objeto en un tuple
del my_tuple # Podemos borrarla queda indefinida por lo que ahora no podemos usarla 
# print(my_tuple) -> Aqui daria error por que no puedes hacer print a algo que no esta definido

