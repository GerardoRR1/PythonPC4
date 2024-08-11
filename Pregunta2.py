from pyfiglet import Figlet
import random

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()

    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = figlet.getFonts()

    # Solicitar al usuario el nombre de una fuente
    fuente_seleccionada = input("Ingrese el nombre de la fuente (o presione Enter para seleccionar una aleatoria): ")

    # Si no se ingresa ninguna fuente, seleccionar una aleatoriamente
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)

    # Verificar si la fuente seleccionada es válida
    if fuente_seleccionada in fuentes_disponibles:
        figlet.setFont(font=fuente_seleccionada)
    else:
        print("Fuente no válida. Se seleccionará una fuente aleatoria.")
        fuente_seleccionada = random.choice(fuentes_disponibles)
        figlet.setFont(font=fuente_seleccionada)

    # Solicitar al usuario el texto a imprimir
    texto_imprimir = input("Ingrese el texto que desea imprimir: ")

    # Imprimir el texto usando la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

# Ejecutar el programa
if __name__ == "__main__":
    main()
