
'''Ejercicio: “Simulador de carrito de compras”
Hacé un programa que permita:
Agregar producto a un carrito (nombre + precio).
El usuario puede seguir agregando producto hasta que escriba "fin".
Al final:
Mostrás todos los producto agregados.
Mostrás el total a pagar.
Mostrás el producto más caro.
- Reglas:
Usá listas (mínimo).
Validá que el precio sea número (no seas salvaje).
Nada de interfaces fancy, puro input y print.'''


carrito = []

while True:
    producto = input("Ingrese producto (o 'fin' para terminar): ").strip()
    
    if producto.lower() == "fin":
        break

    while True:
            try:
                precio_str = input(f"Ingrese el precio de '{producto}': ")  
                precio = float(precio_str)  
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue 
                break
            except ValueError:
                print("Ingrese un número válido.")

    carrito.append({"nombre": producto, "precio": precio})


if len(carrito) == 0:
    print("\nNo se agregaron productos.")
else:
    print("\nProductos:")
    total = 0
    producto_mas_caro = carrito[0]

for item in carrito:
    print(f"- {item['nombre']}: {item['precio']}")
    total += item["precio"]


if item["precio"] > producto_mas_caro["precio"]:
    producto_mas_caro = item


print(f"Total: {total}")
print(f"Producto más caro: {producto_mas_caro['nombre']}")