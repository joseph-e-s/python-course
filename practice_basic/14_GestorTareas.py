
'''Ejercicio: Gestor de tareas (To-Do List básico)
Vas a hacer un programa donde el usuario maneje tareas.
🔹 Requisitos:
Mostrar un menú en bucle:
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir

🔹 Funcionalidad:
1️⃣ Agregar tarea
El usuario escribe una tarea
Se guarda en una lista
2️⃣ Ver tareas
Mostrar todas numeradas
Ejemplo:
1. Estudiar Python [Pendiente]
2. Hacer ejercicio [Completada]
3️⃣ Marcar como completada
El usuario elige el número
Cambia su estado
4️⃣ Eliminar tarea
El usuario elige el número
Se borra'''

lista_tareas = []

while True:
    print()
    print("1 → Agregar tarea")
    print("2 → Ver tareas")
    print("3 → Marcar como completada")
    print("4 → Eliminar tarea")
    print("5 → Salir")

    try:
        seleccion_usuario = int(input("| Elije tu opcion: "))
    except ValueError:
        print("-" * 35)
        print("Error: Solo se aceptan numeros\n")
        continue

    if seleccion_usuario < 1 or seleccion_usuario > 5:
        print("-" * 35)
        print("Error: Elija una opcion existente\n")
        continue


    if seleccion_usuario == 1:
        print("-" * 35)

        while True:
            nueva_tarea = input("Ingrese la nueva tarea: ")

            if not nueva_tarea.strip():
                print("Error: No puede estar vacía\n")
                continue

            lista_tareas.append([nueva_tarea, False])
            print(f"- Tarea ({nueva_tarea}) agregada correctamente.\n")

            while True:
                otra_tarea = input("Deseas ingresar otra tarea? (Y/N): ").lower()

                if otra_tarea == "y":
                    break
                elif otra_tarea == "n":
                    break
                else:
                    print("Error: Ingrese Y o N\n")

            if otra_tarea == "n":
                break


    elif seleccion_usuario == 2:
        print("-" * 35)

        if not lista_tareas:
            print("No hay tareas registradas.\n")
            continue

        print("Lista de tareas:")
        for i, tarea in enumerate(lista_tareas, start=1):
            estado = "Pendiente" if not tarea[1] else "Completado"
            print(f"{i}. {tarea[0]} ({estado})")


    elif seleccion_usuario == 3:
        print("-" * 35)

        if not lista_tareas:
            print("No hay tareas para modificar.\n")
            continue

        for i, tarea in enumerate(lista_tareas, start=1):
            estado = "Pendiente" if not tarea[1] else "Completado"
            print(f"{i}. {tarea[0]} ({estado})")

        while True:
            try:
                cambiar_estado = int(input("Digite el numero de tarea a modificar: "))
            except ValueError:
                print("Error: Digite un numero valido.\n")
                continue

            if cambiar_estado < 1 or cambiar_estado > len(lista_tareas):
                print("Error: numero fuera de rango\n")
                continue

            indice = cambiar_estado - 1

            lista_tareas[indice][1] = not lista_tareas[indice][1]

            print("Estado actualizado\n")
            break


    elif seleccion_usuario == 4:
        print("-" * 35)

        if not lista_tareas:
            print("No hay tareas para eliminar.\n")
            continue

        for i, tarea in enumerate(lista_tareas, start=1):
            estado = "Pendiente" if not tarea[1] else "Completado"
            print(f"{i}. {tarea[0]} ({estado})")

        while True:
            try:
                tarea_eliminar = int(input("Digite el numero de tarea a eliminar: "))
            except ValueError:
                print("Error: Digite un numero valido.\n")
                continue

            if tarea_eliminar < 1 or tarea_eliminar > len(lista_tareas):
                print("Error: numero fuera de rango\n")
                continue

            indice = tarea_eliminar - 1
            eliminada = lista_tareas.pop(indice)

            print(f"Tarea eliminada: {eliminada[0]}\n")
            break


    elif seleccion_usuario == 5:
        print("\nSaliendo...\n")
        break

