def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith('.py'):
            print("El archivo no tiene la extensión .py.")
            return

        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        lineas_codigo = 0

        for linea in lineas:
            # Eliminar espacios en blanco al inicio y al final de la línea
            linea_strip = linea.strip()
            # Contar solo si la línea no está vacía y no es un comentario
            if linea_strip and not linea_strip.startswith('#'):
                lineas_codigo += 1

        print(f"El archivo '{ruta_archivo}' tiene {lineas_codigo} líneas de código efectivas.")
    
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")

def main():
    # Solicitar la ruta del archivo
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    # Llamar a la función para contar líneas de código
    contar_lineas_codigo(ruta_archivo)


main()
