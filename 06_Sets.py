
# Set 
# Es una colección desordenada de elementos únicos (no permite duplicados)
my_set = set() # Datos en set (separa elementos) = set("hola") -> ['a', 'o', 'l', 'h'] -> 4 elementos (Sin orden)
my_other_set = {} # Meter un dato como un solo elemento ["hola"] -> ['hola'] -> 1 elemento
# Con llaves {} vacias es un diccionario si quiero un set vacio es con set()

print(type(my_set)) # Aqui si es type set | con set() puede estar vacio y ser un set
print(type(my_other_set))  # Aqui es type dict | con {} estando vacio sera diccionario hasta que contenga algo

my_other_set = {"Brais", "Moure", 35} 
print(my_other_set) 

print(type(my_other_set)) # Vemos que my_other_set es type set porque contiene cosas
print(len(my_other_set))    


# Inserción
my_other_set.add("MoureDev") # Agrega el elemento que le demos de forma desordenada
print(my_other_set)  

my_other_set.add("MoureDev")  # Un set no admite repetidos por lo que ignora esto (es igual al anterior)
print(my_other_set)


# Búsqueda
'''No podemos acceder por posicion ya que es desordenado, no sabemos en que posisicon estan las cosas
pero si podemos preguntar si lo que le demos esta ahi'''
print("Moure" in my_other_set) # Nos devuelve un boolean true por que si esta
print("Mouri" in my_other_set) # Nos devuelve un boolean false por que no esta


# Eliminación
my_other_set.remove("Moure") # Podemos eliminar el elmento que le demos sin problema
print(my_other_set)

my_other_set.clear() # Al igual que podemos vaciar o limpiar sets sin problemas
print(len(my_other_set))

del my_other_set # Podemos borrarla pero queda indefinida por lo que ahora no podemos usarla 
# print(my_other_set) -> Aqui daria error por que no puedes hacer print a algo que no esta definido


# Transformación
my_set = {"Brais", "Moure", 35}

my_list = list(my_set) # Podemos convertirla en lista pero queda con el ultimo orden del set 
print(type(my_list)) 
print(my_list) # Vemos que no es el orden que le dimos si no el ultimo orden que nos dio el set
print(my_list[0])


# Otras operaciones
my_com_set = {"Brais", "Moure", "Dev"}
my_other_set = {"Kotlin", "Swift", "Python"}

# Con union() unimos my_com_set con my_other_set a este set nuevo lo llamamos my_new_set
my_new_set = my_com_set.union(my_other_set)
print(my_new_set) # El orden es aleatorio 

# Podemos unirlos con cosas que le pasemos 
print(my_new_set.union({"JavaScript", "C#"}))

'''Con difference() decimos que saque la diferencia o lo que no se repite entre una y otra. 
Y por que no sale "JavaScript", "C#" si estos no se repiten? 
Bueno porque estos dos se lo dimos en un print no los almacenamos en my_new_set o en my_com_set
los cuales son los que estamos comparando, ellos no lo poseen por lo que no hay diferncia
'''
print(my_new_set.difference(my_com_set)) 

