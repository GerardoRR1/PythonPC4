import requests

def obtener_precio_bitcoin():
    try:
        # URL de la API de CoinDesk para obtener el precio actual de Bitcoin
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si hubo algún error en la solicitud
        datos = respuesta.json()  # Convierte la respuesta a un objeto JSON
        precio_usd = datos['bpi']['USD']['rate_float']  # Extrae el precio en USD
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud a la API: {e}")
        return None

def main():
    # Solicitar al usuario la cantidad de Bitcoins
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))

    # Obtener el precio actual del Bitcoin en USD
    precio_usd = obtener_precio_bitcoin()

    if precio_usd is not None:
        # Calcular el valor de 'n' Bitcoins en USD
        valor_total = n * precio_usd
        # Mostrar el resultado con cuatro decimales
        print(f"El costo actual de {n} Bitcoins en USD es: ${valor_total:,.4f}")
    else:
        print("No se pudo obtener el precio de Bitcoin.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
