
'''Ejercicio: Simulador de cajero automático (ATM básico)
Vas a hacer un programa que simule un cajero con un saldo inicial.
Requisitos:
- Empieza con un saldo de ₡0
- Muestra un menú en bucle:
1 → Consultar saldo
2 → Depositar dinero
3 → Retirar dinero
4 → Salir
-El programa se repite hasta que el usuario decida salir'''

saldo_inicial = 0 

while True:

    print("1 → Consultar saldo")
    print("2 → Depositar dinero")
    print("3 → Retirar dinero")
    print("4 → Salir")
    
    try:
        seleccion_usuario = int(input("Digite el numero de la operacion a realizar: "))
    except ValueError:
        print("Error: Solo se aceptan numeros\n")
        continue

    if seleccion_usuario <= 0 or seleccion_usuario > 4:
        print("Digito invalido | Seleccione del 1 - 4 segun la operacion\n")
        continue

    if seleccion_usuario == 1:
        print("=" * 50)
        print(f"Tu saldo es de: ₡{saldo_inicial}\n")
        
    elif seleccion_usuario == 2:
        print("=" * 50)
        while True:
            try:
                depositar_dinero = int(input("Deposito | Que cantidad desea ingresar: "))
            except ValueError:
                print("Error: Solo se aceptan numeros\n")
                continue

            if depositar_dinero <= 0:
                print("Cantidad invalida para realizar el deposito\n")
                continue
            else:
                saldo_inicial = saldo_inicial + depositar_dinero
                print(f"Deposito realizado con exito, tu saldo es de: ₡{saldo_inicial}\n")
                break

    elif seleccion_usuario == 3:
        print("=" * 50)
        while True:
            try:
                retirar_dinero = int(input("Retiro | Que cantidad desea retirar: "))
            except ValueError:
                print("Error: Solo se aceptan numeros\n")
                continue

            if retirar_dinero <= 0:
                print("Cantidad invalida para realizar el retiro\n")
                continue
            elif saldo_inicial < retirar_dinero:
                print("Fondos insuficiente para realizar el retiro, intentelo de nuevo\n")
                continue
            else:    
                saldo_inicial = saldo_inicial - retirar_dinero
                print(f"Retiro realizado con exito, tu saldo es de: ₡{saldo_inicial} \n")
                break

    elif seleccion_usuario == 4:
        print("=" * 50)
        print("Saliendo del sistema...\n")
        break
