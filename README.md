# Gestor de Tareas en Línea de Comandos

Este proyecto es una aplicación de consola simple y funcional desarrollada en Python para gestionar una lista de tareas pendientes (To-Do List). Permite a los usuarios agregar, ver, marcar como completadas y eliminar tareas, todo desde la terminal.

El objetivo principal de este proyecto es demostrar el dominio de los fundamentos de Python, incluyendo la modularización de código en funciones, el manejo de estructuras de datos (listas y diccionarios), el control del flujo del programa y la interacción básica con el sistema de archivos.

---

## Funcionalidades

El programa ofrece un menú interactivo con las siguientes opciones:

*   **1. Agregar Tarea:** Permite al usuario añadir una nueva tarea a la lista.
*   **2. Ver Tareas:** Muestra todas las tareas actuales, indicando su estado ("Pendiente" o "Completada").
*   **3. Marcar Tarea como Completada:** Cambia el estado de una tarea específica de "Pendiente" a "Completada".
*   **4. Eliminar Tarea:** Borra una tarea de la lista permanentemente.
*   **5. Salir y Guardar:** Termina la ejecución del programa y guarda el estado final de la lista de tareas en un archivo de texto.

---

## Cómo Usarlo

Para ejecutar el programa, sigue estos pasos:

1.  Asegúrate de tener **Python 3** instalado en tu sistema.
2.  Clona o descarga este repositorio en tu máquina local.
3.  Abre una terminal o línea de comandos y navega hasta la carpeta del proyecto.
4.  Ejecuta el siguiente comando:
    ```bash
    python gestor_tareas.py
    ```
5.  El menú interactivo aparecerá en la consola. Sigue las instrucciones y elige una opción numérica para empezar a gestionar tus tareas.

---

## Implementación Técnica y Habilidades Demostradas

Este proyecto fue construido aplicando los siguientes conceptos de Python:

*   **Modularización con Funciones:** El código está organizado en funciones reutilizables (`mostrar_menu`, `agregar_tarea`, `ver_tareas`, etc.), lo que hace que el programa sea más legible, escalable y fácil de depurar.

*   **Estructuras de Datos:**
    *   **Listas:** Se utiliza una lista principal para almacenar todas las tareas. Esto permite mantener un conjunto ordenado y dinámico de elementos.
    *   **Diccionarios:** Cada tarea individual es un diccionario con claves bien definidas (`'descripcion'`, `'completada'`), lo que permite estructurar la información de manera clara y accesible.

*   **Control de Flujo:**
    *   **Bucle `while`:** Un bucle `while True` mantiene el menú interactivo en ejecución hasta que el usuario decide salir.
    *   **Condicionales `if/elif/else`:** Se utilizan para procesar la opción seleccionada por el usuario y dirigir el flujo del programa a la función correspondiente.

*   **Manejo de Errores Básico:**
    *   Se implementan bloques `try-except ValueError` para gestionar de forma segura las entradas del usuario, evitando que el programa se bloquee si se introduce un valor no numérico cuando se espera un número.

*   **Manejo de Archivos (Simplificado):**
    *   Para cumplir con los requisitos específicos de la evaluación, la persistencia de datos se maneja utilizando el módulo `os` y el comando `os.system()`. Al salir, el estado final de las tareas se escribe en un archivo de texto (`tareas_guardadas.txt`) usando el comando `echo` del sistema.
