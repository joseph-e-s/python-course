
# Clases
# Es un molde o plantilla con el cual defines las características(atributos) y comportamientos(métodos) de un objeto
# Las clases se escriben en formato camelcase
class MyEmptyPerson:         # esto es una clase vacia
    pass                     # Esto es para poder dejar la clase vacía, si el daria error

print(MyEmptyPerson)         # La ejecuta sin error pero no muestra nada esta vacia



# Clase con atributos públicos
class Person:
    # El __init__ es el constructor de la clase.
    # Aquí se definen y reciben TODOS los atributos que el usuario debe proporcionar al crear un objeto.
    def __init__(self, name: str, surname: str, age: int, alias: str):
        self.full_name = f"{name} {surname} ({alias})"  # full_name representa la identidad (name + apellido + alias); age no va aquí porque es un dato distinto
        self.age = age  # la edad se guarda aparte porque es otra característica de la person
        # cada atributo debe guardarse con self.

    def walk(self): # Las acciones(metodos) pueden ser varias y van en funciones normales (no en __init__)
        return "está caminando" # return = darte un papel con la info para usarlo en otro lado


# ---------------- USO DEL OBJETO ----------------

# Creamos un objeto(instancia) de la clase Person, lo que permite asignar valores concretos a sus atributos:
# name="Joseph", surname="Elizondo", age=22 y alias="Tote"
my_person = Person("Joseph", "Elizondo", 22, "Tote")

# Usamos los atributos(características) y métodos(acciones) del objeto 
# Accedemos al objeto my_person: usamos full_name (identidad) y age (edad) para armar la frase;
print(f"{my_person.full_name} tiene {my_person.age} años y {my_person.walk()}")



# Clase con atributos públicos y privados
class Person:
    def __init__(self, name: str, surname: str):
        # Atributo PUBLICO (Se usa desde fuera sin problema)
        self.fullname = f"{name} {surname}"

        # Atributo PRIVADO (NO se usa directamente desde fuera de la clase)
        self.__age = 0

    # Método para ENVIAR el valor privado y usarlo
    def send_age(self):
        return self.__age # Return solo envia(retorna) el valor de la edad -> 0

    # Método para MODIFICAR el valor privado
    def change_age(self, new_age):  # new_age toma el valor que le pasás a change_age() -> 25 | new_age = 25
            self.__age = new_age    # self.__age que tiene 0 ahora sera new_age que tiene 25


# ---------------- USO DEL OBJETO ----------------

my_person = Person("Tote", "Elizondo") # Asignamos valor a fullname
print(my_person.fullname) # Podemos acceder a el desde aqui afuera-> "Tote Elizondo"

# Cambiar la edad usando el método (forma correcta)
my_person.change_age(25) # Le damos el valor 25 a change_age y el se lo dara a new_age
print(f"{my_person.send_age()}") # vemos que cambio a 25

# Mostrarlos juntos
print(f"{my_person.fullname} tiene {my_person.send_age()} años")
