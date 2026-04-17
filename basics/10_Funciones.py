
# Funciones
# Una función es un bloque de código que realiza una tarea específica.
# Este bloque lo podemos reutilizar cuantas veces queramos.
def my_function():          # Creamos una función llamada my_function
    print("Esto es una función")      # Lo que hace es hacer este print

# Llamamos a la función
my_function()          # Imprime: Esto es una función


# Las funciones también pueden recibir parámetros desde fuera, no solo lo que ellas contienen internamente.
def sum_two_values(first_value, second_value):
    print(first_value + second_value) # La función recibe first_value y second_value como parámetros para sumarlos

# Ejemplos de uso
sum_two_values(5, 7)                    # first_value = 5, second_value = 7  → 12
sum_two_values(54754, 71231)            # first_value = 54754, second_value = 71231  → 125985
sum_two_values("hola ", "tote")         # Aunque sean strings, también los "suma" (concatena)
sum_two_values(1.2, 1.2)                # Aunque sean float, también funciona  → 2.4
# Osea, esta función recibe cualquier tipo de dato porque no especificamos el tipo.
# Python es de tipado dinámico, así que intenta sumar lo que le pasemos.

# Lo mejor seria indicar el tipo de dato esperado: (Se evitan errores)
# def sum_two_values(first_value: int, second_value: int):
#     print(first_value + second_value)
    

# Función con parámetros y retorno (usando return)
# Con return podemos guardar el resultado de la función en una variable
def sum_two_values_with_return(first_value: int, second_value: int):
    my_sum = first_value + second_value
    return my_sum

# Ejemplo de uso
my_result = sum_two_values_with_return(10, 5)   # Asignamos el resultado a la variable my_result
print(my_result)   # Imprime: 15


# Función con parámetros - Llamada por posición y por clave (keyword arguments)
def print_name(name: str, surname: str):
    print(f"{name} {surname}")  # "f" indica: reemplaza {name} y {surname} por sus valores sino los imprimiria literal

# Llamadas a la función:
# 1. Por posición (el orden importa)
print_name("Tote", "Elizondo")                    # → Tote Elizondo
# 2. Por clave (keyword arguments) - Podemos cambiar el orden
print_name(surname="Elizondo", name="Tote")       # → Tote Elizondo


# Función con parámetros por defecto (default parameters)
def print_name_with_default(name: str, surname: str, alias: str = "Sin alias"):
    print(f"{name} {surname} {alias}")

# Ejemplos de uso:
# 1. Sin pasar el alias → usa el valor por defecto
print_name_with_default("Tote", "Elizondo") # Salida: Tote Elizondo Sin alias
# 2. Pasando el alias → usa el valor que indicamos
print_name_with_default("Tote", "Elizondo", "Guapo") # Salida: Tote Elizondo Guapo


# Función con parámetros arbitrarios. El asterisco (*) permite recibir un número indeterminado de argumentos
def print_upper_texts(*texts):
    for text in texts:
        print(text.upper()) # Convierte todos los textos recibidos a mayúsculas

# Ejemplos de uso:
print_upper_texts("hola", "python", "tote") # Salida: HOLA PYTHON TOTE
print_upper_texts("hola") # Salida: HOLA
print_upper_texts("bienvenido", "a", "python", "es", "genial")
# Puede recibir 2, 5, 10... los argumentos que quieras, es identerminado