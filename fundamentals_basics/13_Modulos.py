# MÓDULOS EN PYTHON
# Un módulo es simplemente otro archivo .py del cual puedes importar código.

# Reglas a seguir:
# No se pueden importar archivos que empiezan con números pero sí pueden contener números después de su primera letra

# Ejemplo incorrecto:
# import 08_condicionales -> ERROR (nombre inválido)
# SOLUCIÓN:
# Usa nombres válidos (empiezan con letra o _)


# Archivo: modulo.py hacia este fichero (En este proyecto)
from ModuloEjemplo import sumar, print_value

print(sumar(2, 2, 2))
print_value("Otro ejemplo")


# IDEAS CLAVE
# 1. Un módulo = otro archivo .py
# 2. El nombre del archivo debe ser válido (no empezar con número)
# 3. Puedes:
#    - importar todo → import modulo
#    - importar partes → from modulo import tal funcion
# 4. Es mejor usar return en funciones para reutilizar resultados
# 5. No solo puedes importar tus propios archivos:
#    - Python trae módulos incorporados (ej: math, random, datetime) Que hacen todo tipo de cosas
#    - También puedes usar módulos creados por otras personas (instalados con pip en new terminal) 

