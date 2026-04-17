'''
# Clases
# Es un molde o plantilla con el cual defines las características(atributos) y comportamientos(métodos) de un objeto
# Las clases se escriben en formato camelcase
class MyEmptyPerson:         # esto es una clase vacia
    pass                     # Es para poder dejar la clase vacía, si el daria error

print(MyEmptyPerson)
print(MyEmptyPerson())


# Clase Clase con constructor y funciones que representa a una persona
class Person:
    # El __init__ es el constructor de la clase.
    # Aquí se definen y reciben TODOS los atributos que el usuario debe proporcionar al crear un objeto.
    def __init__(self, name: str, surname: str, age: int, alias: str):
        self.full_name = f"{name} {surname} ({alias})"  # full_name representa la identidad (nombre + apellido + alias); age no va aquí porque es un dato distinto
        self.age = age  # la edad se guarda aparte porque es otra característica de la persona
        # cada atributo debe guardarse con self.

    def walk(self): # Las acciones(metodos) pueden ser varias y van en funciones normales (no en __init__)
        print(f"está caminando")

# Creamos un objeto(instancia) de la clase Person, lo que permite asignar valores concretos a sus atributos:
# name="Joseph", surname="Elizondo", age=22 y alias="Tote"
my_person = Person("Joseph", "Elizondo", 22, "Tote")

# Usamos los atributos(características) y métodos(acciones) del objeto 
# Accedemos al objeto my_person: usamos full_name (identidad) y age (edad) para armar la frase;
print(f"{my_person.full_name} tiene {my_person.age} años y", end=" ") # end=" " evita el salto de línea 
my_person.walk()  # llamamos al método que imprime la acción, continuando la frase en la misma línea
'''

# Clase con constructor, funciones y propiedades privadas y públicas que representa a una persona
class Person:
    def __init__(self, name: str, surname: str, age: int, alias: str = "Sin alias"):
        # Atributos públicos (pueden ser accedidos y modificados desde fuera) datos que el usuario debe proporcionar
        self.full_name = f"{name} {surname} ({alias})"
        self.age = age
        self.alias = alias

        # Atributos privados(__) __id y __password → Son datos que la clase misma quiere tener internamente pero no
        #quiere que el usuario los tenga que escribir al crear el objeto. Por eso NO van como parámetros en el __init__
        self.__id = 208530555          # Ejemplo: número de identificación interno
        self.__password = 12345      # Ejemplo: contrasena interna
        # Atributos privados (ya definidos por el sistema)
        
    # Método para mostrar información básica
    def introduce(self):
        print(f"Hola, soy {self.full_name} y tengo {self.age} años.")

    # Ejemplo de método que usa dato privado
    def login(self, password_attempt, ID):
        # Compara lo que escribe el usuario con lo que el objeto guarda
        if password_attempt == self.__password and ID == self.__id:
            print("Acceso concedido") # Indica que el login fue correcto
            return True
        else:
            print("Acceso denegado, intentelo nuevamente")  # Indica que falló
            return False
            
myperson = Person("Joseph", "Elizondo", 21)

print("--- LOGIN ---")

# Bucle infinito: repite hasta que el login sea correcto
while True:
    # Usuario intenta ingresar su ID 
    login_id = int(input("Ingrese su ID: "))
    # Usuario intenta ingresar su contraseña
    login_password = int(input("Ingrese su contraseña: "))
    # Se llama al método login y se evalúa los input del usuario coninciden con los datos del sistema
    if myperson.login(login_password, login_id):
        break  # Sale del bucle si el acceso es correcto
    else:
        print(" ")  # Solo separador visual para el siguiente intento


