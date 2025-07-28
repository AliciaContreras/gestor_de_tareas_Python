import os
def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir y Guardar")

def agregar_tarea(tareas):
    descripcion = input("Escribe la descripción de la nueva tarea: ")
    nueva_tarea = {
        'descripcion': descripcion,
        'completada': False
    }
    tareas.append(nueva_tarea)
    print(f"¡Tarea '{descripcion}' agregada con éxito!")

def ver_tareas(tareas):
    print("\n--- Lista de Tareas ---")
    if not tareas:
        print("No hay tareas pendientes. ¡Buen trabajo!")
    else:
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - [{estado}]")

def marcar_completada(tareas):
    """Marca una tarea en memoria como completada."""
    ver_tareas(tareas)
    if not tareas:
        return

    try:
        num_tarea_str = input("Ingresa el número de la tarea a marcar como completada: ")
        num_tarea = int(num_tarea_str)
        
        if 1 <= num_tarea <= len(tareas):
            indice = num_tarea - 1
            if tareas[indice]['completada']:
                print("Esta tarea ya estaba marcada como completada.")
            else:
                tareas[indice]['completada'] = True
                print(f"¡Tarea '{tareas[indice]['descripcion']}' marcada como completada!")
        else:
            print("Error: El número de tarea no es válido.")
    except ValueError:
        print("Error: Debes ingresar un número.")

def eliminar_tarea(tareas):
    """Elimina una tarea de la lista en memoria."""
    ver_tareas(tareas)
    if not tareas:
        return

    try:
        num_tarea_str = input("Ingresa el número de la tarea a eliminar: ")
        num_tarea = int(num_tarea_str)

        if 1 <= num_tarea <= len(tareas):
            indice = num_tarea - 1
            tarea_eliminada = tareas.pop(indice)
            print(f"¡Tarea '{tarea_eliminada['descripcion']}' eliminada con éxito!")
        else:
            print("Error: El número de tarea no es válido.")
    except ValueError:
        print("Error: Debes ingresar un número.")

def guardar_al_salir(tareas):
    """
    Convierte la lista de tareas a una cadena de texto y la guarda
    en un archivo usando un comando del sistema.
    """
    print("\nGuardando tareas en el archivo 'tareas_guardadas.txt'...")
    
    nombre_archivo = "tareas_guardadas.txt"

    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)


    for tarea in tareas:
        estado = "Completada" if tarea['completada'] else "Pendiente"
        linea_de_tarea = f"- {tarea['descripcion']} [{estado}]"
        os.system(f'echo "{linea_de_tarea}" >> {nombre_archivo}')
    print("¡Tareas guardadas con éxito!")

def main():  
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            guardar_al_salir(tareas)
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")

if __name__ == "__main__":
    main()