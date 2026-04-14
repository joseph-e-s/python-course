
# Condicionales
# if / elife / else
my_condition = False 
if my_condition: # Para que se ejecuta la condicion siempre debe ser verdadera
    print("Se ejecuta la condición del if") # No ejecuta porque my_condition es falsa
    
my_condition = True
if my_condition:    
    print("Se ejecuta la condición del if") # Aqui si se ejecuta porque my_condition si es verdadera


# Se utiliza para verificar
my_condition = 5 * 5 # my_condition seria = 25
if my_condition == 10: # Aqui decimos si my_condition es igual a 25 has lo siguiente si no, ignora
    print("Se ejecuta la condición del if") # Como my_condition si es igual a 25 lo ejecuta y no lo ignora

# Comprobamos mas cosas (las combinaciones en la comprobaciones son miles)
my_condition = 25
if my_condition > 10 and my_condition < 20: # Aqui pasamos dos condiciones que se deben cumplir para ejecutar la accion
    print("Es mayor que 10 y menor que 30") 
elif my_condition == 25: # Elif es (de lo contrario si...) una condicion especifica que agregamos, pueden ser varias
    print("Es igual a 25")
else: #  Else seria (Y si no has esto) Si no se cumple la condicion se ejecuta este
    print("Es menor o igual que 10 o mayor o igual que 30")


# Condicional con ispección de valor
my_string = "" # Una variable vacia se evalua como false
if not my_string: # Aqui decimos, si no es true has lo siguiente
    print("Mi cadena de texto esta vacía") # como my_string no es true se ejecuta 

if my_string == "Mi cadena de textoooooo": # La variable con datos se evalua como true | Aqui, si es true has esto
    print("Estas cadenas de texto coinciden") # Y lo hace porque es true