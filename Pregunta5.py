import os

def crear_tabla_multiplicar(n):
    
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, 'w') as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}")

def leer_tabla_multiplicar(n):
    
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as f:
            contenido = f.read()
            print(f"Tabla de multiplicar del {n}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def leer_linea_tabla_multiplicar(n, m):
    """Lee y muestra la línea m de la tabla de multiplicar del número n."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.readlines()
            if 1 <= m <= len(lineas):
                print(f"Línea {m} de la tabla de multiplicar del {n}: {lineas[m-1].strip()}")
            else:
                print(f"El archivo {nombre_archivo} tiene menos de {m} líneas.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Crear y guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar desde archivo")
        print("3. Leer una línea específica de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                crear_tabla_multiplicar(n)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif opcion == '2':
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                leer_tabla_multiplicar(n)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif opcion == '3':
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                m = int(input("Ingrese el número de línea (entre 1 y 10): "))
                if 1 <= m <= 10:
                    leer_linea_tabla_multiplicar(n, m)
                else:
                    print("Número de línea fuera de rango. Debe estar entre 1 y 10.")
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecutar el menú
menu()
