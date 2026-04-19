''' 
Reto #4
 ÁREA DE UN POLÍGONO
 Dificultad: FÁCIL
 Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, area_cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo. '''
 
 
def calcular_area(poligono, base=0, altura=0, lado=0):
    if poligono == 'cuadrado':
        return  lado * lado
    elif poligono == 'rectangulo':
        return  base * altura
    elif poligono == 'triangulo':
        return  base * altura / 2
    else:
        "No se ha calculado nada"
        

area_cuadrado = (calcular_area(poligono ='cuadrado', lado=4))
print("el area del cuadrado es ", area_cuadrado)
area_rectangulo = (calcular_area(poligono ='rectangulo', base=10, altura=5))
print("el area del rectangulo es ", area_rectangulo)
area_triangulo = (calcular_area(poligono ='triangulo', base=5, altura=10))
print("el area del triangulo es ", area_triangulo)

